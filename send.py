import os


# init var
port = ""   # default > 22
pathClient = ""    # ssh user + path ex: user@server:/path/to/folder/


class Color:
    violet = "\033[35;1m"
    red = "\u001b[31;1m"
    cyan = "\u001b[36;1m"
    green = "\u001b[32;1m"
    yellow = "\u001b[33;1m"
    fucsia = "\u001b[35;1m"
    gray = "\033[90;1m"
    italic = "\033[3;1m"
    reset = "\u001b[0m"


def intro():
    print(f"{Color.green}                    __ ")
    print("   ___ ___ ___  ___/ / ")
    print("  (_-</ -_) _ \\/ _  /  ")
    print(f" /___/\\__/_//_/\\_,_/ {Color.red}{Color.italic}by alfanowski {Color.reset}")
    print()


def getInfo():
    while True:
        pathHost = input(f" {Color.gray}File path {Color.cyan}>> {Color.reset} ")    # path of the file to transfer
        pathHost = pathHost.strip()
        pathHost = pathHost.strip("'")
        pathHost = os.path.abspath(pathHost)
        if not os.path.exists(pathHost) or not pathHost:
            print(f"{Color.red} Invalid path\n")
        else:
            print()
            break
    return f"scp -P {port} {pathHost} {pathClient}"


def getAnswer():
    while True:
        answer = input(f" {Color.gray}Are you sure? (Y / N) {Color.cyan}>> {Color.reset} ")
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        print(f"{Color.red} Invalid option\n")


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

