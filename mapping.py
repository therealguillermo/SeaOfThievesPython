

ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },
    "BP_MediumShipTemplate_C": {
        "Name": "Brig (Near)",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },
    "BP_LargeShipTemplate_C": {
        "Name": "Galleon (Near)",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },
    "BP_AISmallShipTemplate_C": {
        "Name": "Ghost Sloop (Near)",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Ghost Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Ghost Galleon (Near)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Ghost Galleon",
    },
    "BP_AggressiveGhostShip_C": {
        "Name": "Flameheart Galleon",
    },
}


ship_keys = set(ships.keys())

events = {
    "BP_AshenLord_SkullCloud_C": {
        "Name": "Ashen Lord Event",
    },
    "BP_GhostShips_Signal_Flameheart_NetProxy_C": {
        "Name": "Flameheart Event",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "Fort Event",
    },
    "BP_SkellyFort_RitualSkullCloud_C": {
        "Name": "Fort of the Damned Event",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "Fort of Fortune",
    },
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "Ship Event",
    },
    "BP_Shipwreck_01_a_NetProxy_C": {
        "Name": "Shipwreck"
    },
    "BP_Storm_C": {
        "Name": "Storm Eye"
    },
}
event_keys = set(events.keys())

seaLoot = {
    "BP_Seagulls_Barrels_C": {
        "Name": "Barrels"
    },
    "BP_Seagull01_8POI_C": {
        "Name": "Shipwreck Quest Area"
    },
    "BP_Seagull01_8POI_LostShipments_C": {
        "Name": "Small Treasure Quest Area"
    },
    "BP_Seagull01_32POI_Circling_Shipwreck_C": {
        "Name": "Large Seagull Area"
    },
}

seaLoot_keys = set(seaLoot.keys())

statues = {
    "BP_SunkenCurseArtefact_Ruby_C": {
        "Name": "Ruby Statue"
    },
    "BP_SunkenCurseArtefact_Emerald_C": {
        "Name": "Emerald Statue"
    },
    "BP_SunkenCurseArtefact_Sapphire_C": {
        "Name":  "Sapphire Statue"
    },
    "BP_MermaidGem_ItemInfo_Ruby_C": {
        "Name": "Ruby Mermaid Gem"
    },
    "BP_MermaidGem_ItemInfo_Emerald_C": {
        "Name": "Emerald Mermaid Gem"
    },
    "BP_MermaidGem_ItemInfo_Sapphire_C": {
        "Name": "Sapphire Mermaid Gem"
    },
}

statues_keys = set(statues.keys())

skulls = {
    "BP_BountyRewardSkull_UncommonPirateLegend_C": {
        "Name": "Legendary Athena Skull"
    },
    "BP_BountyRewardSkull_PirateLegend_C": {
        "Name": "Athena Skull"
    },
    "BP_AshenWindsSkull_ItemInfo_C": {
        "Name": "Ashen Winds Skull"
    },
    "BP_BountyRewardSkullItemInfo_Fort_C": {
        "Name": "Stronghold Skull"
    },
    "BP_BountyRewardSkullItemInfo_Ghost_Captain_C": {
        "Name": "Captain Skull of the Damned"
    },
    "BP_BountyRewardSkullItemInfo_Ghost_Common_C": {
        "Name": "Skull of the Damned"
    },
    "BP_BountyRewardSkullItemInfo_AIShip_C": {
        "Name": "Skeleton Captain Skull"
    },
    "BP_BountyRewardSkullItemInfo_Mythical_DVR_C": {
        "Name": "Ashen Villainous Skull"
    },
    "BP_BountyRewardSkullItemInfo_Mythical_C": {
        "Name": "Villainous Skull"
    },
    "BP_BountyRewardSkullItemInfo_Legendary_C": {
        "Name": "Hateful Skull"
    },
    "BP_BountyRewardSkullItemInfo_Legendary_DVR_C": {
        "Name": "Ashen Hateful Skull"
    },
    "BP_BountyRewardSkullItemInfo_Rare_C": {
        "Name": "Disgraced Skull"
    },
    "BP_BountyRewardSkullItemInfo_Rare_DVR_C": {
        "Name": "Ashen Disgraced Skull"
    },
    "BP_BountyRewardSkullItemInfo_Common_C": {
        "Name": "Foul Skull"
    },
    "BP_Ritual_Skull_ItemInfo_C": {
        "Name": "Ritual Skull"
    },

}

skulls_keys = set(skulls.keys())

keys = {
    "BP_MA_CabinDoorKey_ItemInfo_C": {
        "Name": "Captain's Key"
    },
    "BP_FotD_StrongholdKey_ItemInfo_C": {
        "Name": "FOTD Key"
    },
    "BP_LegendaryFort_StrongholdKey_ItemInfo_C": {
        "Name": "Fort of Fortune Key"
    },
    "BP_StrongholdKey_ItemInfo_C": {
        "Name": "Stronghold Key"
    },
    "BP_MA_CabinDoorKey_Wieldable_C": {
        "Name": "Captain's' Key"
    },
    "BP_Totem_GoldShark_ItemInfo_C": {
        "Name": "Krakens Fall Gold Key"
    },
    "BP_Medallion_Sun_ItemInfo_C": {
        "Name": "Medallion"
    },
    "BP_Totem_GoldBoar_ItemInfo_C": {
        "Name": "Devils Ridge Gold Key"
    },
    "BP_Totem_SilverBoar_ItemInfo_C": {
        "Name": "Devils Ridge Silver Key"
    },
    "BP_Totem_GoldMoon_ItemInfo_C": {
        "Name": "Cresent Isle Gold Key"
    },
    "BP_Totem_GoldSnake_ItemInfo_C": {
        "Name": "Mermaids Hideaway Gold Key"
    },
    "BP_Totem_GoldScarab_ItemInfo_C": {
        "Name": "Crooks Hollow Gold Key"
    },
    "BP_Totem_GoldCrab_ItemInfo_C": {
        "Name": "N-13 Gold Key"
    },
    "BP_Totem_GoldEagle_ItemInfo_C": {
        "Name": "Fletchers Rest Gold Key"
    },
    "BP_Totem_GoldSun_ItemInfo_C": {
        "Name": "Ashen Reaches Gold Key"
    },
}

keys_keys = set(keys.keys())

chests = {
    "BP_FortReapersChest_ItemInfo_C": {
        "Name": "Reapers Chest"
    },
    "BP_CollectorsChest_ItemInfo_C": {
        "Name": "Collectors Chest"
    },
    "BP_AshenChestCollectorsChest_ItemInfo_C": {
        "Name": "Ashen Collectors Chest"
    },
    "BP_AshenChestCollectorsChest_Unlocked_ItemInfo_C": {
        "Name": "Ashen Collectors Chest (Open)"
    },
    "BP_TreasureChest_ItemInfo_Fort_C": {
        "Name": "Stronghold Chest"
    },
    "BP_TreasureChest_Vault_ItemInfo_C": {
        "Name": "Chest of Ancient Tributes"
    },
    "BP_TreasureChest_ItemInfo_ChestOfRage_C": {
        "Name": "Chest of Rage"
    },
    "BP_TreasureChest_ItemInfo_Ghost_C": {
        "Name": "Chest of the Damned"
    },
    "BP_TreasureChest_ItemInfo_AIShip_C": {
        "Name": "Skeleton Captain Chest"
    },
    "BP_TreasureChest_ItemInfo_Mythical_DVR_C": {
        "Name": "Ashen Captain Chest"
    },
    "BP_TreasureChest_Vault_Mythical_ItemInfo_C": {
        "Name": "Vault Captain Chest"
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Mythical_C": {
        "Name": "Shipwrecked Captain Chest"
    },
    "BP_TreasureChest_ItemInfo_Mythical_C": {
        "Name": "Captain Chest"
    },
    "BP_TreasureChest_ItemInfo_Drunken_C": {
        "Name": "Grog Chest"
    },
    "BP_TreasureChest_ItemInfo_Legendary_DVR_C": {
        "Name": "Ashen Marauder Chest"
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Legendary_C": {
        "Name": "Shipwrecked Marauder Chest"
    },
    "BP_TreasureChest_Vault_Legendary_ItemInfo_C": {
        "Name": "Vault Marauder Chest"
    },
    "BP_TreasureChest_ItemInfo_Legendary_C": {
        "Name": "Marauder Chest"
    },
    "BP_TreasureChest_ItemInfo_Rare_DVR_C": {
        "Name": "Ashen Seafarer Chest"
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Rare_C": {
        "Name": "Shipwrecked Seafarer Chest"
    },
    "BP_TreasureChest_Vault_Rare_ItemInfo_C": {
        "Name": "Vault Seafarer Chest"
    },
    "BP_TreasureChest_ItemInfo_Rare_C": {
        "Name": "Seafarer Chest"
    },
    "BP_TreasureChest_ItemInfo_Common_DVR_C": {
        "Name": "Ashen Castaway Chest"
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Common_C": {
        "Name": "Shipwrecked Castaway Chest"
    },
    "BP_TreasureChest_Vault_Common_ItemInfo_C": {
        "Name": "Vault Castaway Chest"
    },
    "BP_TreasureChest_ItemInfo_Common_C": {
        "Name": "Castaway Chest"
    },
    "BP_MerchantCrate_CommonPirateLegend_ItemInfo_C": {
        "Name": "Athena's Crate"
    },
}

chests_keys = set(chests.keys())

crates = {
    "BP_MerchantCrate_AIShipAnyItemCrate_ItemInfo_C": {
        "Name":  "Storage Crate"
    },
    "BP_MerchantCrate_GhostResourceCrate_ItemInfo_C": {
        "Name": "Ghost Storage Crate"
    },
    "BP_MerchantCrate_GhostCannonballCrate_ItemInfo_C": {
        "Name": "Ghost Cannonball Crate"
    },
    "BP_PortableAmmoCrate_ItemInfo_C": {
        "Name": "Ammo Chest"
    },
    "BP_MerchantCrate_WoodCrate_FullyStocked_ItemInfo_C": {
        "Name": "Plank Crate"
    },
    "BP_MerchantCrate_CannonballCrate_FullyStocked_ItemInfo_C": {
        "Name": "Cannonball Crate"
    },
    "BP_MerchantCrate_BananaCrate_FullyStocked_ItemInfo_C": {
        "Name": "Food Crate"
    },
    "BP_MerchantCrate_FirebombCrate_ItemInfo_C": {
        "Name": "Firebomb Crate"
    },
    "BP_MerchantCrate_AnyItemCrate_ItemInfo_C": {
        "Name": "Storage Crate"
    },
}

crates_keys = set(crates.keys())

merchantCrate = {
    "BP_MerchantManifest_01a_ItemInfo_C": {
        "Name": "Prosperous Manifest"
    },
    "BP_MerchantManifest_01b_ItemInfo_C": {
        "Name": "Esteemed Manifest"
    },
    "BP_MerchantManifest_01c_ItemInfo_C": {
        "Name": "Eminent Manifest"
    },
    "BP_MerchantManifest_01d_ItemInfo_C": {
        "Name": "Revered Merchant Manifest"
    },
    "BP_MerchantCrate_Commodity_Fort_ItemInfo_C": {
        "Name": "Ancient Bone Dust"
    },
    "BP_MerchantCrate_Commodity_Gemstones_ItemInfo_C": {
        "Name": "Crate of Precious Gemstones"
    },
    "BP_MerchantCrate_Commodity_Minerals_ItemInfo_C": {
        "Name": "Crate of Minerals"
    },
    "BP_MerchantCrate_Commodity_SpiceCrate_ItemInfo_C": {
        "Name": "Exotic Spice Crate"
    },
    "BP_MerchantCrate_Commodity_Ore_ItemInfo_C": {
        "Name": "Crate of Fine Ore"
    },
    "BP_MerchantCrate_Commodity_SilkCrate_ItemInfo_C": {
        "Name": "Silk Crate"
    },
    "BP_MerchantCrate_Commodity_VolcanicStone_ItemInfo_C": {
        "Name": "Volcanic Stone"
    },
    "BP_MerchantCrate_Commodity_TeaCrate_ItemInfo_C": {
        "Name": "Tea Crate"
    },
    "BP_MerchantCrate_Commodity_SugarCrate_ItemInfo_C": {
        "Name": "Sugar Crate"
    },
}

merchantCrate_keys = set(merchantCrate.keys())

treasure = {
    "BP_TreasureArtifact_ItemInfo_piratelegend_goblet_02_a_C": {
        "Name": "Athena Goblet"
    },
    "BP_TreasureArtifact_ItemInfo_piratelegendimpressive_03_a_C": {
        "Name": "Athena Peculiar Relic"
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Mythical_C": {
        "Name": "Magma Grail"
    },
    "BP_TreasureArtifact_ItemInfo_impressive_02_a_C": {
        "Name": "Adorned Receptacle"
    },
    "BP_TreasureArtifact_Vault_impressive_01_a_ItemInfo_C": {
        "Name": "Opulent Curio"
    },
    "BP_TreasureArtifact_ItemInfo_vase_03_a_C": {
        "Name": "Ornate Carafe"
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Legendary_C": {
        "Name": "Devils Peculiar Relic"
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Rare_C": {
        "Name": "Brimstone Casket"
    },
    "BP_TreasureArtifact_Vault_box_03_a_ItemInfo_C": {
        "Name": "Golden Reliquary"
    },
    "BP_TreasureArtifact_ItemInfo_goblet_03_a_C": {
        "Name": "Guilded Chalice"
    },
    "BP_TreasureArtifact_Vault_goblet_03_a_ItemInfo_C": {
        "Name": "Vault Guilded Chalice"
    },
    "BP_TreasureArtifact_Vault_impressive_02_a_ItemInfo_C": {
        "Name": "Vault Adorned Receptical"
    },
    "BP_TreasureArtifact_Vault_impressive_03_a_ItemInfo_C": {
        "Name": "Vault Peculiar Relic"
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Common_C": {
        "Name": "Roaring Goblet"
    },
    "BP_TreasureArtifact_Vault_box_01_a_ItemInfo_C": {
        "Name": "Decorative Coffer"
    },
    "BP_TreasureArtifact_ItemInfo_goblet_02_a_C": {
        "Name": "Silvered Cup"
    },
    "BP_TreasureArtifact_Vault_goblet_02_a_ItemInfo_C": {
        "Name": "Vault Silvered Cup"
    },
    "BP_TreasureArtifact_ItemInfo_impressive_03_a_C": {
        "Name": "Peculiar Relic"
    },
    "BP_TreasureArtifact_ItemInfo_vase_02_a_C": {
        "Name": "Elaborate Flagon"
    },
    "BP_TreasureArtifact_ItemInfo_box_02_a_C": {
        "Name": "Bronze Secret-Keeper"
    },
    "BP_TreasureArtifact_ItemInfo_vase_01_a_C": {
        "Name": "Mysterious Vessel"
    },
    "BP_TreasureArtifact_ItemInfo_goblet_01_a_C": {
        "Name": "Ancient Goblet"
    },
    "BP_TreasureArtifact_Vault_goblet_01_a_ItemInfo_C": {
        "Name": "Vault Ancient Goblet"
    },
}

treasure_keys = set(treasure.keys())

flags = {
    "BP_EmissaryFlotsam_OrderOfSouls_Rank5_ItemInfo_C": {
        "Name": "OOS Flag Lvl5"
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank4_ItemInfo_C": {
        "Name": "OOS Flag Lvl4"
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank3_ItemInfo_C": {
        "Name": "OOS Flag Lvl3"
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank2_ItemInfo_C": {
        "Name": "OOS Flag Lvl2"
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank1_ItemInfo_C": {
        "Name": "OOS Flag Lvl1"
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank5_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl5"
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank4_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl4"
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank3_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl3"
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank2_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl2"
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank1_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl1"
    },
    "BP_EmissaryFlotsam_Reapers_Rank5_ItemInfo_C": {
        "Name": "Reapers Flag Lvl5"
    },
    "BP_EmissaryFlotsam_Reapers_Rank4_ItemInfo_C": {
        "Name": "Reapers Flag Lvl4"
    },
    "BP_EmissaryFlotsam_Reapers_Rank3_ItemInfo_C": {
        "Name": "Reapers Flag Lvl3"
    },
    "BP_EmissaryFlotsam_Reapers_Rank2_ItemInfo_C": {
        "Name": "Reapers Flag Lvl2"
    },
    "BP_EmissaryFlotsam_Reapers_Rank1_ItemInfo_C": {
        "Name": "Reapers Flag Lvl1"
    },
}

flags_keys = set(flags.keys())

tomes = {
    "BP_AshenTomeVol2_05_ItemInfo_C": {
        "Name": "Ashen Tome Vol 2-5"
    },
    "BP_AshenTomeVol4_05_ItemInfo_C": {
        "Name": "Ashen Tome Vol 4-5"
    },
    "BP_AshenTomeVol4_01_ItemInfo_C": {
        "Name": "Tome of Resurrection 1"
    },
    "BP_AshenTomeVol4_02_ItemInfo_C": {
        "Name": "Tome of Resurrection 2"
    },
    "BP_AshenTomeVol4_03_ItemInfo_C": {
        "Name": "Tome of Resurrection 3"
    },
    "BP_AshenTomeVol4_04_ItemInfo_C": {
        "Name": "Tome of Resurrection 4"
    },
    "BP_AshenTomeVol1_01_ItemInfo_C": {
        "Name": "Tome of Curses 1"
    },
    "BP_AshenTomeVol1_02_ItemInfo_C": {
        "Name": "Tome of Curses 2"
    },
    "BP_AshenTomeVol1_03_ItemInfo_C": {
        "Name": "Tome of Curses 3"
    },
    "BP_AshenTomeVol1_04_ItemInfo_C": {
        "Name": "Tome of Curses 4"
    },
    "BP_AshenTomeVol2_01_ItemInfo_C": {
        "Name": "Tome of Power 1"
    },
    "BP_AshenTomeVol2_02_ItemInfo_C": {
        "Name": "Tome of Power 2"
    },
    "BP_AshenTomeVol2_03_ItemInfo_C": {
        "Name": "Tome of Power 3"
    },
    "BP_AshenTomeVol2_04_ItemInfo_C": {
        "Name": "Tome of Power 4"
    },
}

tomes_keys = set(tomes.keys())

#   "Humble Gift": "BP_LowValueGift_ItemInfo_C"
#   "Skeleton": "BP_SkeletonPawnBase_C",
# #   "Meg": "BP_TinyShark_C",
# #   "Meg Zone": "BP_TinySharkExperience_C",
# #   "Shark": "BP_Shark_C",
# #   "Mermaid": "BP_Mermaid_C",
# #   "Harpoon Rowboat": "BP_RowboatHarpoonLauncher_C",
# #   "Rowboat": "BP_Rowboat_C",
# #   "Cannonball": "BP_Projectile_CannonBall_C",
# #   "Reapers Bounty": "BP_ReapersBounty_ItemInfo_C",
# #   "FOTD Reapers Bounty": "BP_FortReapersBountyChest_ItemInfo_C",
# #   "Athena Gunpowder": "BP_MerchantCrate_PirateLegendBigGunpowderBarrel_ItemInfo_C",
# #   "Stronghold Gunpowder": "BP_MerchantCrate_BigGunpowderBarrel_ItemInfo_C",
# #   "Gunpowder": "BP_MerchantCrate_GunpowderBarrel_ItemInfo_C",