import datetime
import csv

class HappyLogger:
    def __init__(mainSelf, Path="log\CommandsLog.txt"):
        mainSelf.file = open(Path,'a')
        mainSelf.writer= csv.writer(mainSelf.file)
        mainSelf.AddLog("HappyLogger Class-instance Created",1,1)

    def AddLog(self, information="No Information", LOGlevel=1 ,CMDtype = 1): 
        CurrentTime = datetime.datetime.now().strftime("%H:%M:%S")      
        row = [CurrentTime,CMDtype,LOGlevel,information[0:60]]

        for i in range(0,4):
            self.file.write(str(row[i]))
            if(i == 3):
                break
            self.file.write(',')
        self.file.write("\n")
        self.file.flush()

BigDataLogger = HappyLogger()




