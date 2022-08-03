try:
    import os
    from os import system
    system("title " + "Roblox Cookie Checker,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass


try:
    import requests
except Exception:
    while True:
        e = input("Requests Module Missing, Wanna Try Auto Fix It (y/n): ")
        if e == "y" or e == "n":
            break
        else:
            print("Enter A Valid Choice")
    if e == "n":
        exit()
    if e == "y":
        try:
            os.system("pip install requests")
            print("It Shod Be Fixed Now, Press Enter To Start Main Program")
            input("")
        except Exception:
            print("Error Fixing, Press Enter To Close Program")
            input("")
            exit()


while True:
    cookie = input("Enter Roblox Cookie: ")
    try:
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        print("Cookie Is Valid")
        try:
            print("Acount User Id: " +  str(r["UserID"]))
        except Exception:
            print("Acount User Id: ERROR")
        try:
            print("Acount Username: " +  str(r["UserName"]))
        except Exception:
            print("Acount Username: ERROR")
        try:    
            print("Robux Balance: " +  str(r["RobuxBalance"]))
        except Exception:
            print("Robux Balance: ERROR")
        try:    
            print("Account Picture: " +  str(r["ThumbnailUrl"]))
        except Exception:
            print("Account Picture: ERROR")
        try:    
            print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
        except Exception:
            print("Builders Club Member: ERROR")
        try:    
            print("Premium: " +  str(r["IsPremium"]))
        except Exception:
            print("Premium: ERROR")
        while True:
            save = input("Wanna Save Info In A Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        if save == "y":
            file = open(str(r["UserName"])+".txt", "a")
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
            print("Succsesfully Saved")
            input("")
    except Exception:
        print("Cookie Invalid")
        input("")
