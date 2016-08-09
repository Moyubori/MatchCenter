import sys
import os

config = {}

def LoadFile():
    file = open('config.conf', 'r')
    temp = file.read().splitlines()
    for i in range(len(temp)):
        temp[i] = temp[i].split(" ", 1)
    for i in temp:
        config[i[0]] = i[1]

def SaveFile():
    file = open('config.conf', 'w')
    for key in config:
        file.write(key + " " + config[key] + '\n')

def SetConf(i, x): # i - numer argumentu dla ktorego dokonuje zmiany
        config[x] = sys.argv[i + 1]
        if config[x] < '0':
            config[x] = '0'

LoadFile()
i = 1
while i < len(sys.argv):
    SetConf(i, sys.argv[i])
    i += 2
SaveFile()
os.system('dispatch.py')
