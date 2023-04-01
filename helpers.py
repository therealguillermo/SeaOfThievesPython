
import math
import json
import logging
import win32gui
import pyglet
from pyglet.graphics import Batch, Group
from pyglet.text import Label

# True=Enabled & False=Disabled for each of the config items
CONFIG = {
    "WORLD_PLAYERS_ENABLED": True,
    "SHIPS_ENABLED": True,
    "EVENTS_ENABLED": True,
    "SEALOOT_ENABLED": True,
    "PLAYERS_ENABLED": True,
    "CHESTS_ENABLED": True,
    "CRATES_ENABLED": True,
    "FLAGS_ENABLED": True,
    "KEYS_ENABLED": True,
    "MERCHANTCRATES_ENABLED": True,
    "SKULLS_ENABLED": True,
    "STATUES_ENABLED": True,
    "TOMES_ENABLED": True,
    "TREASURE_ENABLED": True,
    "PlayerName": "VirtualTomcat74",
}

version = "1.0.0"

# Config specification for logging file
logging.basicConfig(filename='DougsESP.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s', filemode="w")
logger = logging.getLogger()

# Offset values for the text labels from the circles we draw to the screen
TEXT_OFFSET_X = 13
TEXT_OFFSET_Y = -5

# Information on SoT height and width. Used here and in main.py to display
# data to the screen. May need to manually override if wonky
try:
    window = win32gui.FindWindow(None, "Sea of Thieves")
    SOT_WINDOW = win32gui.GetWindowRect(window)  # (x1, y1, x2, y2)
    SOT_WINDOW_H = SOT_WINDOW[3] - SOT_WINDOW[1]
    SOT_WINDOW_W = SOT_WINDOW[2] - SOT_WINDOW[0]
except Exception as e:
    logger.error("Unable to find Sea of Thieves window; exiting.")
    exit(-1)

# Creates a pyglet "Batch" that we draw our information to. Effectively serves
# as a piece of paper, so we save render cost because its 2D
main_batch = Batch()

# Load our offset json file
with open("offsets.json") as infile:
    OFFSETS = json.load(infile)


def dot(array_1: tuple, array_2: tuple) -> float:
    """
    Python-converted version of Gummy's External SoT v2 vMatrix Dot method (No
    Longer Avail). Takes two lists and multiplies the same index across both
    lists, and adds them together. (Need Source)
    :param tuple array_1: Presumably some array about our player position
    :param tuple array_2: Presumably some array about the dest actor position
    :rtype: float
    :return: The result of a math equation between those two arrays
    """
    if array_2[0] == 0 and array_2[1] == 0 and array_2[2] == 0:
        return 0.0

    return array_1[0] * array_2[0] + array_1[1] \
           * array_2[1] + array_1[2] * array_2[2]


def object_to_screen(player: dict, actor: dict) -> tuple:
    """
    Using the player and an actors coordinates, determine where on the screen
    an object should be displayed. Assumes your screen is 2560x1440

    Python-converted version of Gummy's External SoT v2 WorldToScreen method:
    (No Longer Avail; Need Source)

    :param player: The player coordinate dictionary
    :param actor: An actor coordinate dictionary
    :rtype: tuple
    :return: tuple of x and y screen coordinates to display where the actor is
    on screen
    """
    try:
        player_camera = (player.get("cam_x"), player.get("cam_y"),
                         player.get("cam_z"))
        temp = make_v_matrix(player_camera)

        v_axis_x = (temp[0][0], temp[0][1], temp[0][2])
        v_axis_y = (temp[1][0], temp[1][1], temp[1][2])
        v_axis_z = (temp[2][0], temp[2][1], temp[2][2])

        v_delta = (actor.get("x") - player.get("x"),
                   actor.get("y") - player.get("y"),
                   actor.get("z") - player.get("z"))
        v_transformed = [dot(v_delta, v_axis_y),
                         dot(v_delta, v_axis_z),
                         dot(v_delta, v_axis_x)]

        if v_transformed[2] < 1.0:
            v_transformed[2] = 1.0

        fov = player.get("fov")
        screen_center_x = SOT_WINDOW_W / 2
        screen_center_y = SOT_WINDOW_H / 2

        tmp_fov = math.tan(fov * math.pi / 360)

        x = screen_center_x + v_transformed[0] * (screen_center_x / tmp_fov) \
            / v_transformed[2]
        if x > SOT_WINDOW_W or x < 0:
            return False
        y = screen_center_y - v_transformed[1] * \
            (screen_center_x / math.tan(fov * math.pi / 360)) \
            / v_transformed[2]
        if y > SOT_WINDOW_H or y < 0:
            return False

        return int(x), int(SOT_WINDOW_H - y)
    except Exception as e:
        logger.error(f"Couldn't generate screen coordinates for entity: {e}")


def make_v_matrix(rot: tuple) -> list:
    """
    Builds data around how the camera is currently rotated.

    Python-converted version of Gummy's External SoT v2 Matrix method:
    (No Longer Avail; Need Source)

    :param rot: The player objects camera rotation information
    :rtype: list
    :return: A list of lists containing data about the rotation of our actor
    """
    rad_pitch = (rot[0] * math.pi / 180)
    rad_yaw = (rot[1] * math.pi / 180)
    rad_roll = (rot[2] * math.pi / 180)

    sin_pitch = math.sin(rad_pitch)
    cos_pitch = math.cos(rad_pitch)
    sin_yaw = math.sin(rad_yaw)
    cos_yaw = math.cos(rad_yaw)
    sin_roll = math.sin(rad_roll)
    cos_roll = math.cos(rad_roll)

    matrix = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    matrix[0][0] = cos_pitch * cos_yaw
    matrix[0][1] = cos_pitch * sin_yaw
    matrix[0][2] = sin_pitch

    matrix[1][0] = sin_roll * sin_pitch * cos_yaw - cos_roll * sin_yaw
    matrix[1][1] = sin_roll * sin_pitch * sin_yaw + cos_roll * cos_yaw
    matrix[1][2] = -sin_roll * cos_pitch

    matrix[2][0] = -(cos_roll * sin_pitch * cos_yaw + sin_roll * sin_yaw)
    matrix[2][1] = cos_yaw * sin_roll - cos_roll * sin_pitch * sin_yaw
    matrix[2][2] = cos_roll * cos_pitch
    return matrix


def calculate_distance(obj_to: dict, obj_from: dict) -> int:
    """
    Determines the distances From one object To another in meters, rounding
    to whatever degree of precision you request
    (**2 == ^2)

    Note: Can convert the int() to a round() if you want more precision

    :param obj_to: A coordinate dict for the destination object
    :param obj_from: A coordinate dict for the origin object
    :rtype: int
    :return: the distance in meters from obj_from to obj_to
    """
    return int(math.sqrt((obj_to.get("x") - obj_from.get("x")) ** 2 +
                         (obj_to.get("y") - obj_from.get("y")) ** 2 +
                         (obj_to.get("z") - obj_from.get("z")) ** 2))


def getRGB(boolean):
    if boolean:
        return 0, 255, 0, 255
    else:
        return 255, 0, 0, 255


def reverse(boolean):
    if boolean:
        return False
    return True


class Menu(object):
    def __init__(self):
        self.config = CONFIG
        self.display = False
        self.group = Group()
        y_offset_constant = -20
        y_constant = SOT_WINDOW_H * .65

        self.seaLootLabel = Label("Shipwrecks and Sealoot Label - '`'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                  color=getRGB(self.config.get('SEALOOT_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.shipLabel = Label("Ships Label - '1'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                               color=getRGB(self.config.get('SHIPS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.eventLabel = Label("Event Label - '2'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                color=getRGB(self.config.get('EVENTS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.playerLabel = Label("Player ESP - '3'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                 color=getRGB(self.config.get('PLAYERS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.chestLabel = Label("Chest ESP - '4'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                color=getRGB(self.config.get('CHESTS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.skullsLabel = Label("Skull ESP - '5'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                 color=getRGB(self.config.get('SKULLS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.merchantCrateLabel = Label("Merchant Crate ESP - '6'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                        color=getRGB(self.config.get('MERCHANTCRATES_ENABLED')), batch=main_batch,
                                        group=self.group)
        y_constant += y_offset_constant
        self.treasureLabel = Label("Treasure ESP - '7'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                   color=getRGB(self.config.get('TREASURE_ENABLED')), batch=main_batch,
                                   group=self.group)
        y_constant += y_offset_constant
        self.crateLabel = Label("Storage Crate ESP - '8'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                color=getRGB(self.config.get('CRATES_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.flagLabel = Label("Flag ESP - '9'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                               color=getRGB(self.config.get('FLAGS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.keysLabel = Label("Keys ESP - '0'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                               color=getRGB(self.config.get('KEYS_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.statuesLabel = Label("Statues ESP - '['", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                  color=getRGB(self.config.get('STATUES_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant
        self.tomesLabel = Label("Tomes ESP - '='", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                color=getRGB(self.config.get('TOMES_ENABLED')), batch=main_batch, group=self.group)
        y_constant += y_offset_constant * 1.5
        self.closeLabel = Label("to close press '-'", x=SOT_WINDOW_W * 0.10, y=y_constant,
                                color=(255, 0, 0, 255), batch=main_batch, group=self.group)
        self.group.visible = False

    def setShow(self):
        if self.display:
            self.display = False
            self.group.visible = False
        else:
            self.display = True
            self.group.visible = True

    def setSettings(self, symbol):
        if symbol == 96:  # '
            self.config['SEALOOT_ENABLED'] = reverse(self.config['SEALOOT_ENABLED'])
            self.seaLootLabel.color = getRGB(self.config['SEALOOT_ENABLED'])
        elif symbol == 49:  # 1
            self.config['SHIPS_ENABLED'] = reverse(self.config['SHIPS_ENABLED'])
            self.shipLabel.color = getRGB(self.config['SHIPS_ENABLED'])
        elif symbol == 50:  # 2
            self.config['EVENTS_ENABLED'] = reverse(self.config['EVENTS_ENABLED'])
            self.eventLabel.color = getRGB(self.config['EVENTS_ENABLED'])
        elif symbol == 51:  # 3
            self.config['PLAYERS_ENABLED'] = reverse(self.config['PLAYERS_ENABLED'])
            self.playerLabel.color = getRGB(self.config['PLAYERS_ENABLED'])
        elif symbol == 52:  # 4
            self.config['CHESTS_ENABLED'] = reverse(self.config['CHESTS_ENABLED'])
            self.chestLabel.color = getRGB(self.config['CHESTS_ENABLED'])
        elif symbol == 53:  # 5
            self.config['SKULLS_ENABLED'] = reverse(self.config['SKULLS_ENABLED'])
            self.skullsLabel.color = getRGB(self.config['SKULLS_ENABLED'])
        elif symbol == 54:  # 6
            self.config['MERCHANTCRATES_ENABLED'] = reverse(self.config['MERCHANTCRATES_ENABLED'])
            self.merchantCrateLabel.color = getRGB(self.config['MERCHANTCRATES_ENABLED'])
        elif symbol == 55:  # 7
            self.config['TREASURE_ENABLED'] = reverse(self.config['TREASURE_ENABLED'])
            self.treasureLabel.color = getRGB(self.config['TREASURE_ENABLED'])
        elif symbol == 56:  # 8
            self.config['CRATES_ENABLED'] = reverse(self.config['CRATES_ENABLED'])
            self.crateLabel.color = getRGB(self.config['CRATES_ENABLED'])
        elif symbol == 57:  # 9
            self.config['FLAGS_ENABLED'] = reverse(self.config['FLAGS_ENABLED'])
            self.flagLabel.color = getRGB(self.config['FLAGS_ENABLED'])
        elif symbol == 48:  # 0
            self.config['KEYS_ENABLED'] = reverse(self.config['KEYS_ENABLED'])
            self.keysLabel.color = getRGB(self.config['KEYS_ENABLED'])
        elif symbol == 91:  # [
            self.config['STATUES_ENABLED'] = reverse(self.config['STATUES_ENABLED'])
            self.statuesLabel.color = getRGB(self.config['STATUES_ENABLED'])
        elif symbol == 61:  # =
            self.config['TOMES_ENABLED'] = reverse(self.config['TOMES_ENABLED'])
            self.tomesLabel.color = getRGB(self.config['TOMES_ENABLED'])
        else:
            return
