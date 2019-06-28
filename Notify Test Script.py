## Notify Test Script
import os
try:
    from Notify import Main as NotifyMain
    Notify = NotifyMain()
    Notify.SetMode("A")
except(ImportError):
    print("[!] Failed to import Notify. Aborting.")
    exit()

print("Beginning test...")

Notify.Test()

print("#####")

Notify.Red()
print("RED")
Notify.Green()
print("GREEN")
Notify.Yellow()
print("YELLOW")
Notify.Blue()
print("BLUE")
Notify.Magenta()
print("MAGENTA")
Notify.Cyan()
print("CYAN")
Notify.White()
print("WHITE")
Notify.ClearColour()

print("###########")

Notify.BackBlack()
print("TEST")
Notify.BackBlue()
print("TEST")
Notify.BackCyan()
print("TEST")
Notify.BackGreen()
print("TEST")
Notify.BackRed()
print("TEST")
Notify.BackMagenta()
print("TEST")
Notify.BackWhite()
print("TEST")
Notify.BackYellow()
print("TEST")

input()