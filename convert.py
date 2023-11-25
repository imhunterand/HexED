print ("""
    ███╗██╗  ██╗███████╗██╗  ██╗███╗    ███████╗    ██╗██████╗
    ██╔╝██║  ██║██╔════╝╚██╗██╔╝╚██║    ██╔════╝   ██╔╝██╔══██╗
    ██║ ███████║█████╗   ╚███╔╝  ██║    █████╗    ██╔╝ ██║  ██║
    ██║ ██╔══██║██╔══╝   ██╔██╗  ██║    ██╔══╝   ██╔╝  ██║  ██║
    ███╗██║  ██║███████╗██╔╝ ██╗███║    ███████╗██╔╝   ██████╔╝
    ╚══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══╝    ╚══════╝╚═╝    ╚═════╝
    •   ┓               ┓
    ┓┏┳┓┣┓┓┏┏┓╋┏┓┏┓┏┓┏┓┏┫   @Security Executions Code (Pwn0sec)
    ┗┛┗┗┛┗┗┻┛┗┗┗ ┛ ┗┻┛┗┗┻   @Imhunterand

    """)#line:13
def menu ():#line:14
    print (" 1. Hex to Text")#line:15
    print (" 2. Text to Hex")#line:16
    print (" 3. Exit")#line:17
    O0OOOOO0O0O000000 =int (input (" Select number : "))#line:18
    if O0OOOOO0O0O000000 ==1 :#line:19
        print ("-"*20 )#line:20
        from converter import hex2txt #line:21
    elif O0OOOOO0O0O000000 ==2 :#line:22
        print ("-"*20 )#line:23
        from converter import txt2hex #line:24
    elif O0OOOOO0O0O000000 ==3 :#line:25
        print ("Bye")#line:26
        exit ()#line:27
    else :#line:28
        print ("="*20 )#line:29
        print ("\033[31m   Wrong input !!\033[39m")#line:30
        print ("="*20 )#line:31
        menu ()#line:32
menu ()
