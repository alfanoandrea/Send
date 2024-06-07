import os


# init var
port = ""  # default > 22
pathClient = ""   # ssh user + path ex: user@server:/path/to/folder/


class Color:
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Cyan = "\u001b[36m"
    Reset = "\u001b[0m"
    Gray = "\033[90;1m"
    Italic = "\u001b[3;1m"


def intro():
    print(f"{Color.Green}                    __ ")
    print("   ___ ___ ___  ___/ / ")
    print("  (_-</ -_) _ \\/ _  /  ")
    print(f" /___/\\__/_//_/\\_,_/ {Color.Red}{Color.Italic}by alfanowski {Color.Reset}")
    print()


def getInfo():
    pathHost = input(f" {Color.Gray}File path {Color.Cyan}>> {Color.Reset} ")    # path of the file to transfer
    return f"scp -P {port} {pathHost} {pathClient}"


def getAnswer():
    while True:
        answer = input(f" {Color.Gray}Are you sure? (Y / N) {Color.Cyan}>> {Color.Reset} ")
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        print()


def main():
    while True:
        command = getInfo()
        if getAnswer():
            os.system(command)
            break
        return


if __name__ == "__main__":
    intro()
    main()
    print()

