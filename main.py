from time import sleep
import adb_control as ac
import binary_control as BIN
import screen_control as scr

BIN.launchLiveLogDisplayer()
BIN.launchMemu()

sleep(2)
ac.ADB_KillServer()
ac.ADB_startServer()
sleep(5)
ac.ADB_listDevices()
ac.ADB_connectMemu()

ac.ADB_startGame()
ac.ADB_screencap()
ac.ADB_pull("/storage/emulated/0/Project_X/sc/screenshot.png","Images\screenshot\\")



