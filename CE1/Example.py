from CE1 import AdvText

from CE1 import Notify
Notify = Notify.Main()
Notify.SetMode("A")

Adv = AdvText.Main()


def InitialLoadingScreen():
    phrases = ["SHIP RESERVE POWER","ENGINE DIAGNOSTICS"]
    for count in range(0,len(phrases)):
        Adv.LoadingEllipsis(phrases[count],1,5,"OK")

    Adv.LoadingEllipsis("MAIN PROPULSION",3,5,"FAULT")
    Notify.Error("PROPULSION FAULT DETECTED. RUNNING DIAGNOSTICS...")
    Adv.LoadingEllipsis("Beginning diagnostics",10,5,"done")
    
