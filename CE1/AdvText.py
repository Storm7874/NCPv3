## Advanced Text Manipulation (AdvText)

import time
import random
import os
try:
    from Notify import Main as NotifyMain
    Notify = NotifyMain()
    Notify.SetMode("A")
except(ImportError):
    print("[ATX] Failed to import Notify. Aborting.")
    exit()

class Main:
    def __init__(self):
        self.AvailForeColours = ["RED","GREEN","CYAN","YELLOW","BLUE","MAGENTA","WHITE"]
        self.AvailBackColours = ["BLACK","RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE"]
        self.AvailStyles = ["DIM","BRIGHT","NORMAL"]

    def LoadingEllipsis(self, Text, Delay, Count, CompletionMessage):
        print(Text,end='')
        for count in range(0,Count):
            print(".",end='')
            time.sleep(Delay)
        print(CompletionMessage)

    def LoadingEllipsisColour(self, Text, Delay, Count, CompletionMessage, BackColour, ForeColour):
        Notify.SetForeColour(ForeColour)
        Notify.SetBackColour(BackColour)
        print(Text,end='')
        for count in range(0,Count):
            print(".",end='')
            time.sleep(Delay)
        print(CompletionMessage)
        Notify.ClearColour()

    def Example(self):
        phrases = ["SYSTEM SELF TEST","RESERVE POWER GRID","MAIN POWER GRID","AUX ELECTRICAL SUBSYSTEMS","ENGINE DIAGNOSTICS CORE",
                   "ICC SUBSYSTEM A","ICC SUBSYSTEM B","ICC SUBSYSTEM C","MAIN SHIP DIAGNOSTICS","SHIELD SUBSYSTEM","MAIN ENGINE CONTROL",
                   "FLIGHT CONTROL RESERVE","FLIGHT CONTROL MAIN","A,B AND C WEAPON BUSSES","TARGETTING AND CONTROL COMPUTER","GUIDANCE",
                   "NAVIGATION","LIFE SUPPORT","OXYGEN GENERATION","MEP","DCS","IRRRV"]

        for count in range(0,len(phrases)):
            self.LoadingEllipsis(phrases[count],0.25,random.randint(3,7),"OK")
        print()
        print("Ship initialization complete.")

        time.sleep(5)

        os.system("clear")

        input()


ex = Main()


ex.Example()

input()