from argparse import Namespace
import adb_control as adb
import happyLogger as HL
from time import sleep

def scr_recenter():
    sleep(1.5)
    HL.BigDataLogger.AddLog("Recentering screen",1,2)
    for x in range(2):
        adb.ADB_runBashScript("zoomOut.sh")
    for x in range (4):
        adb.ADB_swipe(200,500,400,750,100)
    HL.BigDataLogger.AddLog("Recentered screen",1,2)

