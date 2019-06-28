## Advanced Text Manipulation (AdvText)

import time
try:
    from Notify import Main as NotifyMain
    Notify = NotifyMain()
    Notify.SetMode("A")
except(ImportError):
    print("[ATX] Failed to import Notify. Aborting.")
    exit()

Notify.Info("TEST")


class Main:
    def __init__(self):
        self.AvailForeColours = ["RED","GREEN","CYAN","YELLOW","BLUE","MAGENTA","WHITE"]
        self.AvailBackColours = ["BLACK","RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE"]
        self.AvailStyles = ["DIM","BRIGHT","NORMAL"]

    def LoadingEllipsis(self, Text, Delay, Count, CompletionMessage, BackColour, ForeColour):
        Notify.SetForeColour(ForeColour)
        Notify.SetBackColour(BackColour)
        print(Text,end='')
        for count in range(0,Count):
            print(".",end='')
            time.sleep(Delay)
        print(CompletionMessage)
        Notify.ClearColour()


ex = Main()

ex.LoadingEllipsis("System Init",0.25,5,"OK","NONE","MAGENTA")
#Notify.SetForeColour("RED")
