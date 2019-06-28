## For handling of colour-based warning and error messages

try:
    from Colorama import *
    #print(Fore.GREEN + "[N] Imported Colorama" + Style.RESET_ALL)
except ImportError:
    print("[N] Failed to import Colorama.")

# Notify.Warning("Error Message Here")

class Main():
    def __init__(self):
        self.mode = "A"
        self.initial = True

    def SetMode(self, mode):
        self.mode = mode
        self.initial = True

    def Warning(self, msg):
        if self.initial == True:
            if self.mode not in ["A","B","C","D"]:
                self.mode = "A"
                self.Error("Invalid Mode Selected.")
        if self.mode == "A":
            print(Fore.YELLOW + "[!] " + Style.RESET_ALL + msg)
        elif self.mode == "B":
            print(Fore.YELLOW +"[!] " + msg + Style.RESET_ALL)
        elif self.mode == "C":
            print(Fore.YELLOW + "(!) " + Style.RESET_ALL + msg)
        elif self.mode == "D":
            print(Fore.YELLOW +"(!) " + msg + Style.RESET_ALL)

    def Error(self, msg):
        if self.initial == True:
            if self.mode not in ["A","B","C","D"]:
                self.mode = "A"
                self.Error("Invalid Mode Selected.")
        if self.mode == "A":
            print(Fore.RED + "[!] " + Style.RESET_ALL + msg)
        elif self.mode == "B":
            print(Fore.RED + "[!] " + msg + Style.RESET_ALL)
        elif self.mode == "C":
            print(Fore.RED + "(!) " + Style.RESET_ALL + msg)
        elif self.mode == "D":
            print(Fore.RED +"(!) " + msg + Style.RESET_ALL)

    def Info(self, msg):
        if self.initial == True:
            if self.mode not in ["A","B","C","D"]:
                self.mode = "A"
                self.Error("Invalid Mode Selected.")
        if self.mode == "A":
            print(Fore.CYAN + "[-] " + Style.RESET_ALL + msg)
        elif self.mode == "B":
            print(Fore.CYAN + "[-]" + msg + Style.RESET_ALL)
        elif self.mode == "C":
            print(Fore.CYAN + "(-) " + Style.RESET_ALL + msg)
        elif self.mode == "D":
            print(Fore.CYAN +"(-) " + msg + Style.RESET_ALL)

    def Success(self, msg):
        if self.initial == True:
            if self.mode not in ["A","B","C","D"]:
                self.mode = "A"
                self.Error("Invalid Mode Selected.")
        if self.mode == "A":
            print(Fore.GREEN + "[+] " + Style.RESET_ALL + msg)
        elif self.mode == "B":
            print(Fore.GREEN + "[+] " + msg + Style.RESET_ALL)
        elif self.mode == "C":
            print(Fore.GREEN + "(+) " + Style.RESET_ALL + msg)
        elif self.mode == "D":
            print(Fore.GREEN +"(+) " + msg + Style.RESET_ALL)

    def Test(self):
        modes = ["A","B","C","D"]
        for count in range(0,len(modes)):
            self.Error("This is an error.")
            self.Info("This is an information")
            self.Warning("This is a warning")
            self.Success("This is a success")
            self.mode = modes[count]

    def Red(self):
        print(Fore.RED)

    def Green(self):
        print(Fore.GREEN)

    def Cyan(self):
        print(Fore.CYAN)

    def Yellow(self):
        print(Fore.YELLOW)

    def Blue(self):
        print(Fore.BLUE)

    def Magenta(self):
        print(Fore.MAGENTA)

    def White(self):
        print(Fore.WHITE)

    def SetForeColour(self, Colour):
        if Colour == "RED":
            self.Red()
        elif Colour == "GREEN":
            self.Green()
        elif Colour == "CYAN":
            self.Cyan()
        elif Colour == "YELLOW":
            self.Yellow()
        elif Colour == "BLUE":
            self.Blue()
        elif Colour == "MAGENTA":
            self.Magenta()
        elif Colour == "WHITE":
            self.White()
        elif Colour == "NONE":
            pass

    def ftt(self):
        print("FTT")

    ## Backs

    def SetBackColour(self, Colour):
        if Colour == "BLACK":
            self.BackBlack()
        elif Colour == "RED":
            self.BackRed()
        elif Colour == "GREEN":
            self.BackGreen()
        elif Colour == "YELLOW":
            self.BackYellow()
        elif Colour == "BLUE":
            self.BackBlue()
        elif Colour == "MAGENTA":
            self.BackMagenta()
        elif Colour == "CYAN":
            self.BackCyan()
        elif Colour == "WHITE":
            self.BackWhite()
        elif Colour == "NONE":
            pass
        else:
            self.Error("Invalid Colour!")

    def BackBlack(self):
        print(Back.BLACK)

    def BackRed(self):
        print(Back.RED)

    def BackGreen(self):
        print(Back.GREEN)

    def BackYellow(self):
        print(Back.YELLOW)

    def BackBlue(self):
        print(Back.BLUE)

    def BackMagenta(self):
        print(Back.MAGENTA)

    def BackCyan(self):
        print(Back.CYAN)

    def BackWhite(self):
        print(Back.WHITE)

    ## Styles

    def StyleDim(self):
        print(Style.DIM)

    def StyleNormal(self):
        print(Style.NORMAL)

    def StyleBright(self):
        print(Style.BRIGHT)

    def ClearColour(self):
        print(Style.RESET_ALL)



#def Warning(msg):
#    print(Fore.YELLOW + "[!] " + Style.RESET_ALL + msg)
#
#def Error(msg):
#    print(Fore.RED + "[!] " + Style.RESET_ALL + msg)
#
#def Information(msg):
#    print(Fore.CYAN + "[-] " + Style.RESET_ALL + msg)
#
#def Success(msg):
#    print(Fore.GREEN + "[+] " + Style.RESET_ALL + msg)

#def Red():
#    print(Fore.RED)

#def Cyan():
#    print(Fore.CYAN)

#def Green():
#    print(Fore.GREEN)

#def ClearColour():
#    print(Style.RESET_ALL)

#def Bright():
#    print(Style.BRIGHT)


