try:
    import os
    os.system("title " + "Roblox Cookie Checker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass


import time, sys

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()




colorama.init(autoreset=True)
while True:
    os.system("cls")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Roblox Cookie: ")
    cookie = input("")
    try:
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print015("Cookie Is Valid")
        try:
            r["UserID"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Acount User Id: " +  str(r["UserID"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Acount User Id: ERROR")
        time.sleep(0.1)
        try:
            r["UserName"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Acount Username: " +  str(r["UserName"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Acount Username: ERROR")
        time.sleep(0.1)
        try:
            r["RobuxBalance"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Robux Balance: " +  str(r["RobuxBalance"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Robux Balance: ERROR")
        time.sleep(0.1)
        try:
            r["ThumbnailUrl"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Account Picture: " +  str(r["ThumbnailUrl"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Account Picture: ERROR")
        time.sleep(0.1)
        try:
            r["IsAnyBuildersClubMember"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Builders Club Member: ERROR")
        time.sleep(0.1)
        try:
            r["IsPremium"]
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Premium: " +  str(r["IsPremium"]))
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Premium: ERROR")
        time.sleep(0.5)
        print("")
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Wanna Save Info In A Txt File (y/n): ")
            save = input("")
            if save == "y" or save == "n":
                break
            else:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Enter A Valid Choice")
        if save == "y":
            file = open(str(r["UserID"])+".txt", "a")
            try:
                file.write("Acount User Id: " +  str(r["UserID"]) + "\n")
            except Exception:
                file.write("Acount User Id: ERROR" + "\n")
            try:
                file.write("Acount Username: " +  str(r["UserName"]) + "\n")
            except Exception:
                file.write("Acount Username: ERROR" + "\n")
            try:    
                file.write("Robux Balance: " +  str(r["RobuxBalance"]) + "\n")
            except Exception:
                file.write("Robux Balance: ERROR" + "\n")
            try:    
                file.write("Account Picture: " +  str(r["ThumbnailUrl"]) + "\n")
            except Exception:
                file.write("Account Picture: ERROR" + "\n")
            try:    
                file.write("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]) + "\n")
            except Exception:
                file.write("Builders Club Member: ERROR" + "\n")
            try:    
                file.write("Premium: " +  str(r["IsPremium"]) + "\n")
            except Exception:
                file.write("Premium: ERROR" + "\n")
            file.close()
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Succsesfully Saved Account Information")
            input("")
        print("")
        if save == "n":
            print("")
    except Exception:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Cookie Invalid")
        input("")
        print("")
