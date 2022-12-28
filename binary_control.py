from subprocess import Popen
from pathlib import Path
import os
import happyLogger as HL


def launchLiveLogDisplayer():
    Log_Dir = str(Path().resolve())+"\\log\\"
    command = Log_Dir+"Log_File_Displayer.exe"
    cwd = os.getcwd()

    os.chdir(Log_Dir)
    Popen(["start","/wait","cmd","/k",command],shell=True)
    os.chdir(cwd)

    HL.BigDataLogger.AddLog("Live Log Displayer Launched",3,2)

def launchMemu():
    memu_Dir = "E:\MyPrograms\Emulator\Memu\Microvirt\MEmu\MEmu.exe"
    Popen(["start","/wait",memu_Dir],shell=True)
    HL.BigDataLogger.AddLog("Memu Has been Launched through consol",3,2)
