# github.com/imhunterand
print("""
    ███╗██╗  ██╗███████╗██╗  ██╗███╗    ███████╗    ██╗██████╗
    ██╔╝██║  ██║██╔════╝╚██╗██╔╝╚██║    ██╔════╝   ██╔╝██╔══██╗
    ██║ ███████║█████╗   ╚███╔╝  ██║    █████╗    ██╔╝ ██║  ██║
    ██║ ██╔══██║██╔══╝   ██╔██╗  ██║    ██╔══╝   ██╔╝  ██║  ██║
    ███╗██║  ██║███████╗██╔╝ ██╗███║    ███████╗██╔╝   ██████╔╝
    ╚══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══╝    ╚══════╝╚═╝    ╚═════╝
    •   ┓               ┓
    ┓┏┳┓┣┓┓┏┏┓╋┏┓┏┓┏┓┏┓┏┫   @Security Executions Code (Pwn0sec)
    ┗┛┗┗┛┗┗┻┛┗┗┗ ┛ ┗┻┛┗┗┻   @Imhunterand

    """)
def menu():
    print(" 1. Hex to Text")
    print(" 2. Text to Hex")
    print(" 3. Exit")
    pilih = int(input(" Select number : "))
    if pilih == 1:
        print("-"*20)
        from converter import hex2txt
    elif pilih == 2:
        print("-"*20)
        from converter import txt2hex
    elif pilih == 3:
        print("Bye")
        exit()
    else:
        print("="*20)
        print("\033[31m   Wrong input !!\033[39m")
        print("="*20)
        menu()
menu()
