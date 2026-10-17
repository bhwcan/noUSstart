#!/usr/bin/env python

import sys
from snsave import SNSave
from noUStrucks import trucksInWarehouse, customColors

upgradesGiverData = {
  "level_us_01_01": {
      "US_01_01_UPGRADE_FLEESTAR_ALLWHEELS": 2,
      "US_01_01_UPGRADE_G_SCOUT_OFFROAD": 2,
      "US_01_01_UPGRADE_CK_SUSPENSION": 2,
      "US_01_01_UPGRADE_SCOUT_OLD_ENGINE": 2,
      "US_01_01_UPGRADE_FLEESTAR_SUSP_HIGHT": 2,
      "US_01_01_UPGRADE_TRUCK_OLD_ENGINE": 2,
      "US_01_01_UPGRADE_GMC_SUSP_HIGHT": 2
  },
  "level_us_01_02": {
      "US_01_02_UPGRADE_TRUCK_ENG_4070": 2,
      "US_01_02_UPGRADE_CHEVY_DIFF_LOCK": 2,
      "US_01_02_UPGRADE_TRUCK_ENG": 2,
      "US_01_02_UPGRADE_WHITE_ALLWHEELS": 2,
      "US_01_02_UPGRADE_GMC_DIFF_LOCK": 2,
      "US_01_02_UPGRADE_INTERN_SCOUT_SUSP_HIGH": 2,
      "US_01_02_UPGRADE_WHITE_SUSP_HIGH": 2,
      "US_01_02_UPGRADE_G_SCOUT_HIGHWAY": 2
  },
  "level_us_01_03": {
      "US_01_03_UPG_3": 2,
      "US_01_03_UPG_6": 2,
      "US_01_03_UPG_2": 2,
      "US_01_03_UPG_4": 2
  },
  "level_us_01_04_new": {
      "US_01_04_UPG_1": 2,
      "US_01_04_UPG_3": 2
  },
  "level_us_02_01": {
      "US_02_01_UPG_02": 2,
      "US_02_01_UPG_09": 2,
      "US_02_01_UPG_05": 2,
      "US_02_01_UPG_06": 2,
      "US_02_01_UPG_04": 2,
      "US_02_01_UPG_07": 2,
      "US_02_01_UPG_08": 2,
      "US_02_01_UPG_01": 2
  },
  "level_us_02_02_new": {
      "US_02_02_UPG_05": 2,
      "US_02_02_UPG_01": 2,
      "US_02_02_UPG_02": 2,
      "US_02_02_UPG_04": 2,
      "US_02_02_UPG_06": 2
  },
  "level_us_02_03_new": {
      "US_02_03_UPG_01": 2,
      "US_02_03_UPG_02": 2,
      "US_02_03_UPG_04": 2,
      "US_02_03_UPG_06": 2,
      "US_02_03_UPG_05": 2,
      "US_02_03_UPG_07": 2
  },
  "level_us_02_04_new": {
      "US_02_04_UPG_3": 2,
      "US_02_04_UPG_2": 2,
      "US_02_04_UPG_1": 2,
      "US_02_04_UPG_5": 2
  }
}

def setRank(save, srank):

    rank = int(srank)
    if rank < 1 or rank > 30:
        sys.exit("Invalid rank " + srank + " must be between 1 and 30")

    ranks = [ 0, 0, 700, 1700, 2900, 4100, 5400, 6900, 8500, 10100, 11800,
              12700, 15700, 17800, 20100, 22500, 25000, 27500, 30100, 32700,
              35500, 38300, 41300, 44300, 47500, 50700, 54100, 57500, 61100,
              64900, 69000 ]
    pd = save.data[save.name]['SslValue']['persistentProfileData']

    #print("current       rank: ", pd['rank'])
    #print("current experience: ", pd['experience'], "\n")
        
    rp = pd['experience'] - ranks[pd['rank']]
    np = ranks[rank] + rp
    if rank < 30 and np >= ranks[rank+1]:
        np = ranks[rank]
    #print(rank, ranks[rank], rp, np)
        
    print("    new       rank: ", rank)
    print("    new experience: ", np)
    #pprint.pprint(pd)

    pd['experience'] = np
    pd['rank'] = rank

def usage():
    print("Usage:")
    print("    noUSstart CompleteSave.dat")
     
# MAIN
if __name__ == "__main__":

    # command line arguments
    argc = len(sys.argv)
    #print(f"Arguments count: {argc}")
    if argc <= 1:
        usage()
        sys.exit(0)

    # open Save file
    fd = SNSave()
    fd.openSaveFile(sys.argv[1])
    if fd.isCreated():
        print("Save file not found:", sys.argv[1])
        sys.exit(10)

    # add Canada Red and White
    if fd.data[fd.name]['SslValue']['persistentProfileData']['customColors']:
        fd.data[fd.name]['SslValue']['persistentProfileData']['customColors'].append(customColors['color900'])
    else:
        fd.data[fd.name]['SslValue']['persistentProfileData']['customColors'] = customColors

    # adding US_01 and US_02 trucks
    print("\nAdding trucks from Michigan and Alaska")
    for t in trucksInWarehouse:
        print ("\t", t['type'])

    fd.data[fd.name]['SslValue']['persistentProfileData']['trucksInWarehouse'] = trucksInWarehouse
    
    # Adding US_01 and US_02 upgrades
    print("\nAdding upgrades from Michigan and Alaska")
    fd.data[fd.name]['SslValue']['upgradesGiverData'] = upgradesGiverData

    # set rank to 21
    print("\nAdding a reasonable rank of 21 if played Michigan and Alaska")
    setRank(fd, 21)


    print("\nAdding a reasonable amount of money $300,000 if played Michigan and Alaska")
    fd.data[fd.name]['SslValue']['persistentProfileData']['money'] = 300000


    print("\nLet's start in Taymyr")
    if "ru_02" not in fd.data[fd.name]['SslValue']['persistentProfileData']['knownRegions']:
        fd.data[fd.name]['SslValue']['persistentProfileData']['knownRegions'].append("ru_02")
    fd.data[fd.name]['SslValue']['lastLoadedLevel'] = "level_ru_02_02"

    fd.writeSaveFile()
    sys.exit(10)

    
 

