#!/usr/bin/env python

import sys
from snsave import SNSave
from UStrucks import USupgradesGiverData, UStrucksInWarehouse, CAcustomColors
from RUtrucks import RUupgradesGiverData, RUtrucksInWarehouse

def setRank(save, srank):

    try:
        rank = int(srank)
    except ValueError:
        rank = 0
    pd = save.data[save.name]['SslValue']['persistentProfileData']

    if (rank < 1 or rank > 30) or (pd['rank'] == 30 and rank == 30):
        print("current       rank: ", pd['rank'])
        print("current experience: ", pd['experience'], "\n")
        return

    ranks = [ 0, 0, 700, 1700, 2900, 4100, 5400, 6900, 8500, 10100, 11800,
              12700, 15700, 17800, 20100, 22500, 25000, 27500, 30100, 32700,
              35500, 38300, 41300, 44300, 47500, 50700, 54100, 57500, 61100,
              64900, 69000 ]

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
    print("    noUSstart CompleteSave.dat <args>\n")
    print("  /base        - add Taymyr trucks and upgrades, to start on DLC map")
    print("  /DLC         - do not remove trucks from storage, keep DLC trucks")
    print("  /money:value - value of money to add, default is 300000")
    print("  /rank:value  - value for rank, 0 does not change your rank, default is 21")
    print("\n")

def getarguments():
    # use windows style arguments
    switches = ['DLC', "base", "rank", "money"]
    arguments = {}
    for arg in sys.argv[2:]: # Skip script name and file name
        if arg.startswith('/'):
            arg = arg[1:]
            if ':' in arg:
                key, value = arg.split(':', 1)
            else:
                key, value = arg, "0"
            
            if key in switches:
                arguments[key] = value

    return arguments

# defaults
money = 300000
rank = 21

# MAIN
if __name__ == "__main__":

    # command line arguments
    argc = len(sys.argv)
    #print(f"Arguments count: {argc}")
    if argc <= 1:
        usage()
        sys.exit(1)
    arguments = getarguments()
    for a in arguments:
        print(a, arguments[a])

    # open Save file
    fd = SNSave()
    fd.openSaveFile(sys.argv[1])
    if fd.isCreated():
        print("Save file not found:", sys.argv[1])
        sys.exit(10)

    # add Canada Red and White
    if "customColors" not in fd.data[fd.name]['SslValue']['persistentProfileData']:
        fd.data[fd.name]['SslValue']['persistentProfileData']['customColors'] = {}
    fd.data[fd.name]['SslValue']['persistentProfileData']['customColors']['color900'] = CAcustomColors['color900']

    if "DLC" not in arguments:
        print("\nDeleting all trucks currently in storage")
        # deleting trucks in warehouse
        fd.data[fd.name]['SslValue']['persistentProfileData']['trucksInWarehouse'] = []

    # adding US_01 and US_02 trucks
    print("\nAdding trucks from Michigan and Alaska")
    for t in UStrucksInWarehouse:
        fd.data[fd.name]['SslValue']['persistentProfileData']['trucksInWarehouse'].append(t)
        print ("\t", t['type'])
    
    # Adding US_01 and US_02 upgrades
    print("\nAdding upgrades from Michigan and Alaska")
    for u in USupgradesGiverData:
        print(u)
        fd.data[fd.name]['SslValue']['upgradesGiverData'][u] = USupgradesGiverData[u]

    # if requested adding RU_02 trucks
    if "base" in arguments:
        print("\nAdding trucks from Taymyr plus the \"Azov 73210\" which you would have needed")
        for t in RUtrucksInWarehouse:
            fd.data[fd.name]['SslValue']['persistentProfileData']['trucksInWarehouse'].append(t)
            print ("\t", t['type'])
        
        # Adding US_01 and US_02 upgrades
        print("\nAdding upgrades from Taymyr")
        for u in RUupgradesGiverData:
            print(u)
            fd.data[fd.name]['SslValue']['upgradesGiverData'][u] = RUupgradesGiverData[u]

    # set rank
    if "rank" in arguments:
        rank = arguments["rank"]
    print("\nSetting a rank of", rank)
    setRank(fd, rank)

    if "money" in arguments:
        try:
            money = int(arguments["money"])
        except ValueError:
            money = 0
    print("\nAdding a reasonable amount of money", money, "if played Michigan and Alaska")
    fd.data[fd.name]['SslValue']['persistentProfileData']['money'] += money
    print("money:", fd.data[fd.name]['SslValue']['persistentProfileData']['money'])

    print("\nLet's start in Taymyr")
    if "ru_02" not in fd.data[fd.name]['SslValue']['persistentProfileData']['knownRegions']:
        fd.data[fd.name]['SslValue']['persistentProfileData']['knownRegions'].append("ru_02")
    fd.data[fd.name]['SslValue']['lastLoadedLevel'] = "level_ru_02_02"

    fd.writeSaveFile()
    sys.exit(0)

    
 

