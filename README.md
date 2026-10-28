# noUSstart
Snowrunner edit save file to skip starting in the US maps of Michigan and Alaska. It will give you one copy of the trucks found in Michigan and Alaska however it does not discover the trucks. It will give you all the upgrades found in Michigan and Alaska. It sets the rank at 21, gives you an additional 300,000 in money, and starts the game in Taymur. 

## WARNING Backup up save files before running. It will remove trucks from storage and upgrades found after Alaska. Start with a newly created save file.

### Instructions
1. Create a new save in Snowrunner
2. Open a Command Prompt
3. Run "path to exe"\noUSstart "path to save files"\CompleteSave.dat
4. Play Snowrunner and have fun

### Command Line
```
Usage:
    noUSstart CompleteSave.dat <args>

  /base        - add Taymyr trucks and upgrades, to start on DLC map
  /DLC         - do not remove trucks from storage, keep DLC trucks
  /money:value - value of money to add, default is 300000
  /rank:value  - value for rank, 0 does not change your rank, default is 21

```
### Example
```
C:\Users\myhome>D:\projects\noUSstart\dist\noUSstart \
"C:\Users\myhome\Documents\My Games\SnowRunner\base\storage\deadbeefdeadbeefdeadbeefdeadbeef\CompleteSave.dat"

Deleting all trucks currently in storage

Adding trucks from Michigan and Alaska
         ank_mk38
         derry_longhorn_3194
         cat_745c
         hummer_h2
         pacific_p16
         ws_6900xd_twin
         ws_4964_white
         international_transtar_4070a
         chevrolet_ck1500
         international_scout_800
         chevrolet_kodiakc70
         gmc_9500
         international_fleetstar_f2070a
         royal_bm17

Adding upgrades from Michigan and Alaska
level_us_01_01
level_us_01_02
level_us_01_03
level_us_01_04_new
level_us_02_01
level_us_02_02_new
level_us_02_03_new
level_us_02_04_new

Setting a rank of 21
    new       rank:  21
    new experience:  38450

Adding a reasonable amount of money 300000 if played Michigan and Alaska
money: 303850

Let's start in Taymyr

```


