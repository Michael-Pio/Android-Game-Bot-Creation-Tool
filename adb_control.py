from re import sub
import subprocess
import happyLogger as HL

def ADB_startServer():
    command = r"adb start-server"
    HL.BigDataLogger.AddLog("Starting ADB server",5,2)
    res = subprocess.run(command,capture_output=False,shell=True)

def ADB_KillServer():
    command = r"adb kill-server"
    HL.BigDataLogger.AddLog("Killing ADB server",5,2)
    res = subprocess.run(command,capture_output=False,shell=True)
    
def ADB_connectMemu():
    command = r"adb connect localhost:21503"
    HL.BigDataLogger.AddLog("Attempting to establish connection",5,2)
    res = subprocess.run(command,capture_output=True,shell=True)
    HL.BigDataLogger.AddLog(res.stdout,5,1)

def ADB_anonymousCommand(command):
    res = subprocess.run(command,capture_output=True)
    HL.BigDataLogger.AddLog("Anonymous cmd :" + str(res.stdout),1,1)
    print("Anonymous cmd :" + str(res.stdout))

def ADB_listDevices():
    command = r"adb devices"
    HL.BigDataLogger.AddLog("Attempting to See attached Devices",5,2)
    res = subprocess.run(command,capture_output=True,shell=True)
    datum = str(res.stdout).split('\n')
    datum.pop(0)
    for device in datum:
        HL.BigDataLogger.AddLog(device,1,1)
    else:
        HL.BigDataLogger.AddLog("No Device Found",6,1)

def ADB_startGame():
    command = r"adb shell am start com.supercell.hayday/com.supercell.hayday.GameApp"
    HL.BigDataLogger.AddLog("Launching Hayday Game")
    res = subprocess.run(command,capture_output=True,shell = True)
    HL.BigDataLogger.AddLog(res.stdout,1,1)

def ADB_tap(x,y):
    command = f"adb shell input tap {x} {y}"
    res = subprocess.run(command,capture_output=False,shell=True)
    HL.BigDataLogger.AddLog(f"Action ->Tap {x} {y}",1,1)

def ADB_swipe(x1,y1,x2,y2,timePeriod):
    command = f"adb shell input touchscreen swipe {x1} {y1} {x2} {y2} {timePeriod}"
    res = subprocess.run(command,capture_output=False,shell=True)
    HL.BigDataLogger.AddLog(f"Action ->swipe {x1} {y1} {x2} {y2} {timePeriod}",1,1)

def ADB_longPress(x,y,timePeriod = 150):
    command = f"adb shell input touchscreen swipe {x} {y} {x} {y} {timePeriod}"
    res = subprocess.run(command,capture_output=False,shell=True)
    HL.BigDataLogger.AddLog(f"Action ->LongPress {x} {y} for {timePeriod}",1,1)

def ADB_push(pathOfFile,pathOnDevice = "/storage/emulated/0/Project_X/"):
    command = f"adb push {pathOfFile} {pathOnDevice}"
    res = subprocess.run(command,capture_output=True,shell=True)
    HL.BigDataLogger.AddLog(res.stdout,1,1)

def ADB_pull(pathOfFileOnDevice,StoragePath):
    command = f"adb pull {pathOfFileOnDevice} {StoragePath}"
    res = subprocess.run(command,capture_output=True,shell=True)
    HL.BigDataLogger.AddLog(res.stdout,1,1)

def ADB_screencap(Filename = "screenshot",pathOnDevice = "/storage/emulated/0/Project_X/screenCapture/"):
    command = f"adb shell screencap -p {pathOnDevice}{Filename}.png"
    res = subprocess.run(command,capture_output=True,shell=True)
    HL.BigDataLogger.AddLog("Screen Captured on Device")
    
def ADB_runBashScript(nameOfTheScript = "",pathOnDevice = "/data/MyBashScripts/"):
    command = f"adb shell {pathOnDevice+nameOfTheScript}"
    res = subprocess.run(command,shell=True,capture_output=True)
    HL.BigDataLogger.AddLog(f"Executing {nameOfTheScript}",1,1)
    HL.BigDataLogger.AddLog(res.stdout)

def ADB_pressBack():
    ADB_ShellInputKeyevent(4)
    HL.BigDataLogger.AddLog("Back Button Pressed",1,1)

def ADB_pressHome():
    ADB_ShellInputKeyevent(3)
    HL.BigDataLogger.AddLog("Home Button Pressed",1,1)

def ADB_ShellInputKeyevent(eventNumber):
    command = f"adb shell input keyevent {eventNumber}"
    res = subprocess.run(command,shell=True,capture_output=True)
    HL.BigDataLogger.AddLog(f"input Keyevent sent {eventNumber}",1,1)
