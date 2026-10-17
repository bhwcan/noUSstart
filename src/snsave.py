#!/usr/bin/env python

import json

class SNSave:
  def __init__(self):
        self.filename = ""
        self.name = ""
        self.data = {}
        
  def openSaveFile(self, filename):

    #print(filename)
    
    # JSON file
    try:
        f = open(filename, 'r', encoding="utf-8", errors='ignore')
    except FileNotFoundError:
        self.createSaveFile(filename)
        return
    rd = f.read()
    #print(rd[-1], rd[-10:])
    if rd[-1] == '\x00':
        data = json.loads(rd[:-1])
    else:
        data = json.loads(rd)
    f.close()

    for name in data:
        if name[:12] == "CompleteSave":
            self.name = name

    if self.name != "":
      self.filename = filename
      self.data = data
    return

  def isCreated(self):
    if "objVersion" in self.data[self.name]['SslValue']:
      return False
    else:
      return True

  def createSaveFile(self, filename):

    self.name = 'CompleteSave'
    self.filename = filename
    self.data = { 'CompleteSave':
                  { 'SslValue':
                    { 'persistentProfileData':
                    { 'trucksInWarehouse': [],
                      'ownedTrucks': {}
                    }
                  }
                }
              }

  def writeSaveFile(self):
    f = open(self.filename, "w", encoding="utf-8")
    json.dump(self.data, f, separators=(',', ':'))
    f.write('\00')
    f.close()

# MAIN
if __name__ == "__main__":
  import sys
  argc = len(sys.argv)
  #print(f"Arguments count: {argc}")
  if argc <= 1:
    exit(0)
  fd = SNSave()
  fd.openSaveFile(sys.argv[1])
  print(fd.filename, fd.name)
    
 

