import struct
import logging
from memory_helper import ReadMemory
from mapping import ship_keys, event_keys, seaLoot_keys, chests_keys, crates_keys, flags_keys, keys_keys, \
    merchantCrate_keys, skulls_keys, statues_keys, tomes_keys, treasure_keys
from helpers import OFFSETS, logger
from Modules.ship import Ship
from Modules.event import Event
from Modules.seaLoot import SeaLoot
from Modules.chests import Chest
from Modules.crates import Crate
from Modules.flags import Flag
from Modules.keys import Key
from Modules.merchantCrate import MerchantCrate
from Modules.skulls import Skull
from Modules.statues import Statue
from Modules.tomes import Tome
from Modules.treasure import Treasure
from Modules.players import Player
from Modules.debugOBJ import debugOBJ

STEAM_VERSION = False


class SoTMemoryReader:
    """
    Wrapper class to handle reading data from the game, parsing what is
    important, and returning it to be shown by pyglet
    """

    def __init__(self):
        """
        Upon initialization of this object, we want to find the base address
        for the SoTGame.exe, then begin to load in the static addresses for the
        uWorld, gName, gObject, and uLevel objects.

        We also poll the local_player object to get a first round of coords.
        When running read_actors, we update the local players coordinates
        using the camera-manager object

        Also initialize a number of class variables which help us cache some
        basic information
        """
        self.rm = ReadMemory("SoTGame.exe")
        base_address = self.rm.base_address
        logging.info(f"Process ID: {self.rm.pid}")

        u_world_offset = self.rm.read_ulong(
            base_address + self.rm.u_world_base + 3
        )
        u_world = base_address + self.rm.u_world_base + u_world_offset + 7
        self.world_address = self.rm.read_ptr(u_world)

        g_name_offset = self.rm.read_ulong(
            base_address + self.rm.g_name_base + 3
        )
        g_name = base_address + self.rm.g_name_base + g_name_offset + 7
        logging.info(f"SoT gName Address: {hex(g_name)}")
        self.g_name = self.rm.read_ptr(g_name)

        g_objects_offset = self.rm.read_ulong(
            base_address + self.rm.g_object_base + 2
        )
        g_objects = base_address + self.rm.g_object_base + g_objects_offset + 22
        logging.info(f"SoT gObject Address: {hex(g_objects)}")
        self.g_objects = self.rm.read_ptr(g_objects)

        self.u_level = self.rm.read_ptr(self.world_address +
                                        OFFSETS.get('UWorld.PersistentLevel'))

        self.u_local_player = self._load_local_player()
        self.player_controller = self.rm.read_ptr(
            self.u_local_player + OFFSETS.get('ULocalPlayer.PlayerController')
        )

        self.my_coords = self._coord_builder(self.u_local_player)
        self.my_coords['fov'] = 90

        self.config = {}

        self.actor_name_map = {}
        self.server_players = []
        self.display_objects = []
        self.crewDict = {}

        self.read_actors()

    def _load_local_player(self) -> int:
        """
        Returns the local player object out of uWorld.UGameInstance.
        Used to get the players coordinates before reading any actors
        :rtype: int
        :return: Memory address of the local player object
        """
        game_instance = self.rm.read_ptr(
            self.world_address + OFFSETS.get('UWorld.OwningGameInstance')
        )
        local_player = self.rm.read_ptr(
            game_instance + OFFSETS.get('UGameInstance.LocalPlayers')
        )
        return self.rm.read_ptr(local_player)

    def update_my_coords(self):
        """
        Function to update the players coordinates and camera information
        storing that new info back into the my_coords field. Necessary as
        we dont always run a full scan and we need a way to update ourselves
        """
        manager = self.rm.read_ptr(
            self.player_controller + OFFSETS.get('APlayerController.CameraManager')
        )
        self.my_coords = self._coord_builder(
            manager,
            OFFSETS.get('APlayerCameraManager.CameraCache')
            + OFFSETS.get('FCameraCacheEntry.FMinimalViewInfo'),
            fov=True)

    def _coord_builder(self, actor_address: int, offset=0x78, camera=True,
                       fov=False) -> dict:
        """
        Given a specific actor, loads the coordinates for that actor given
        a number of parameters to define the output
        :param int actor_address: Actors base memory address
        :param int offset: Offset from actor address to beginning of coords
        :param bool camera: If you want the camera info as well
        :param bool fov: If you want the FoV info as well
        :rtype: dict
        :return: A dictionary containing the coordinate information
        for a specific actor
        """
        if fov:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 44)
            unpacked = struct.unpack("<ffffff16pf", actor_bytes)
        else:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 24)
            unpacked = struct.unpack("<ffffff", actor_bytes)

        coordinate_dict = {"x": unpacked[0] / 100, "y": unpacked[1] / 100,
                           "z": unpacked[2] / 100}
        if camera:
            coordinate_dict["cam_x"] = unpacked[3]
            coordinate_dict["cam_y"] = unpacked[4]
            coordinate_dict["cam_z"] = unpacked[5]
        if fov:
            coordinate_dict['fov'] = unpacked[7]

        return coordinate_dict

    def _read_name(self, actor_id: int) -> str:
        name_ptr = self.rm.read_ptr(self.g_name + int(actor_id / 0x4000) * 0x8)
        name = self.rm.read_ptr(name_ptr + 0x8 * int(actor_id % 0x4000))
        return self.rm.read_string(name + 0x10, 64)

    def read_actors(self):
        printacc = []
        for display_ob in self.display_objects:
            try:
                display_ob.text_render.delete()
            except:
                continue
        self.display_objects = []
        self.update_my_coords()

        actor_raw = self.rm.read_bytes(self.u_level + 0xa0, 0xC)
        actor_data = struct.unpack("<Qi", actor_raw)

        self.server_players = []
        for x in range(0, actor_data[1]):
            raw_name = ""
            actor_address = self.rm.read_ptr(actor_data[0] + (x * 0x8))
            actor_id = self.rm.read_int(actor_address + OFFSETS.get('AActor.actorId'))
            if actor_id not in self.actor_name_map and actor_id != 0:
                try:
                    raw_name = self._read_name(actor_id)
                    self.actor_name_map[actor_id] = raw_name
                except Exception as e:
                    logger.error(f"Unable to find actor name: {e}")
            if actor_id in self.actor_name_map:
                raw_name = self.actor_name_map.get(actor_id)
            if not raw_name:
                continue

            #print(self.actor_name_map)

            if "CrewService" == raw_name:
                self.crewDict = {}
                TArrayData = self.rm.read_TArray(actor_address + OFFSETS.get('ACrewService.Crews'))
                for i in range(0, TArrayData[1]):
                    nextFCrew = 0x0090*i
                    crewid = self.rm.read_CrewID(TArrayData[0] + nextFCrew)
                    PlayerData = self.rm.read_TArray(TArrayData[0] + nextFCrew + 0x0020)
                    crewNames = []
                    for j in range(0, PlayerData[1]):
                        playerptr = self.rm.read_ptr(PlayerData[0] + (0x0008*j))
                        player_name_location = self.rm.read_ptr(playerptr + 0x03D8)
                        crewNames.append(self.rm.read_name_string(player_name_location))
                    if crewNames is not None:
                        self.crewDict[crewid] = crewNames
                #print(self.crewDict)

            if "MapTable_C" in raw_name:
                PinArrayData = self.rm.read_TArray(actor_address + 0x04E0)
                print("Pins: {}".format(PinArrayData))
                ShipArrayData = self.rm.read_TArray(actor_address + 1232)
                print("shipdata = {}".format(ShipArrayData))

            if self.config.get('SHIPS_ENABLED') and raw_name in ship_keys:
                ship = Ship(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(ship)

            if self.config.get('EVENTS_ENABLED') and raw_name in event_keys:
                event = Event(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(event)

            if self.config.get('SEALOOT_ENABLED') and raw_name in seaLoot_keys:
                seaLoot = SeaLoot(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(seaLoot)

            if self.config.get('CHESTS_ENABLED') and raw_name in chests_keys:
                chest = Chest(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(chest)

            if self.config.get('CRATES_ENABLED') and raw_name in crates_keys:
                crate = Crate(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(crate)

            if self.config.get('FLAGS_ENABLED') and raw_name in flags_keys:
                flag = Flag(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(flag)

            if self.config.get('KEYS_ENABLED') and raw_name in keys_keys:
                key = Key(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(key)

            if self.config.get('MERCHANTCRATES_ENABLED') and raw_name in merchantCrate_keys:
                merchantCrate = MerchantCrate(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(merchantCrate)

            if self.config.get('SKULLS_ENABLED') and raw_name in skulls_keys:
                skull = Skull(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(skull)

            if self.config.get('STATUES_ENABLED') and raw_name in statues_keys:
                statue = Statue(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(statue)

            if self.config.get('TOMES_ENABLED') and raw_name in tomes_keys:
                tome = Tome(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(tome)

            if self.config.get('TREASURE_ENABLED') and raw_name in treasure_keys:
                treasure = Treasure(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(treasure)

            if self.config.get('PLAYERS_ENABLED') and "AthenaPlayerState" in raw_name:
                self.read_world_players(actor_address)
                player = Player(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(player)


    def read_actors_debug(self):
        """
        Represents a full scan of every actor within our render distance.
        Will create an object for each type of object we are interested in,
        and store it in a class variable (display_objects).
        Then our main game loop updates those objects
        """
        # On a full run, start by cleaning up all the existing text renders
        for display_ob in self.display_objects:
            try:
                display_ob.text_render.delete()
            except:
                continue
        self.display_objects = []
        self.update_my_coords()

        actor_raw = self.rm.read_bytes(self.u_level + 0xa0, 0xC)
        actor_data = struct.unpack("<Qi", actor_raw)

        self.server_players = []
        for x in range(0, actor_data[1]):
            # We start by getting the ActorID for a given actor, and comparing
            # that ID to a list of "known" id's we cache in self.actor_name_map
            raw_name = ""
            actor_address = self.rm.read_ptr(actor_data[0] + (x * 0x8))
            actor_id = self.rm.read_int(actor_address + OFFSETS.get('AActor.actorId'))
            # We save a mapping of actor id to actor name for the sake of
            # saving memory calls
            if actor_id not in self.actor_name_map and actor_id != 0:
                try:
                    raw_name = self._read_name(actor_id)
                    self.actor_name_map[actor_id] = raw_name
                except Exception as e:
                    logger.error(f"Unable to find actor name: {e}")
            elif actor_id in self.actor_name_map:
                raw_name = self.actor_name_map.get(actor_id)

            if raw_name.find("BP") != -1:
                debug = debugOBJ(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(debug)

            if self.config.get('PLAYERS_ENABLED') and "AthenaPlayerState" in raw_name:
                self.read_world_players(actor_address)
                player = Player(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(player)

    def read_world_players(self, actor_address):
        """
        Reads information about an AthenaPlayerState actor (a server-level
        player object), to obtain into on who is on the server. Append the user
        to the list of players on the server for a given run
        :param actor_address: The memory address which the actor begins at
        """
        player_name_location = self.rm.read_ptr(
            actor_address + OFFSETS.get('APlayerState.PlayerName')
        )
        player_name = self.rm.read_name_string(player_name_location)
        if player_name and player_name not in self.server_players:
            self.server_players.append(player_name)

    def read_crew_players(self, actor_address):
        crews = self.rm.read_TArray(
            actor_address + OFFSETS.get('ACrewService.Crews')
        )
        return crews

    def set_config(self, cfg):
        self.config = cfg
