# print("Hello!,iam your chatbot")
# remember="remember"
# recall="recall"
# hi="hi"
# hello="hello"
# can="can"
# calculate="calculate"
# x=[]

# while True:
#     message=input(">>")
#     if message=="exit":
#         print("Goodbye!")
#         break
#     elif remember in message:
#         print("Okay i will remember that!")
#         x.append(message)
#     elif recall in(message):
#         print("You told me :")
#         for i in x:
#             print(i)
#     elif hi in message or hello in message:
#         print("Hey! whats up")
#     elif can in message:
#         print("Yes i can definitly help you!")
#     elif calculate in message:
#         a=int(input("enter first number :"))
#         o=input("enter operator")
#         b=int(input("enter second number :"))
#         if o=="+":
#             print(a+b)
#             print("Is there anythingelse you wanna calculate?")
#         elif o=="-":
#             print(a-b)
#             print("Is there anythingelse you wanna calculate?")
#         elif o=="*":
#             print(a*b)
#             print("Is there anythingelse you wanna calculate?")
#         elif o=="/":
#             print("a/b")
#             print("Is there anythingelse you wanna calculate?")
# else:
#         print("ineresting! Tell me more!")
         
        
# ============================================================
#            🤖  MINI CHATBOT ROBOT  🤖
#   (decoration only — original logic left untouched)
# ============================================================

# ---------- ANSI colors (for terminal decoration) ----------
class C:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

ROBOT = f"""{C.CYAN}
        ___________
       |  .-----.  |
       | /  o o  \\ |
       | |   ^   | |
       | \\  ___  / |
       |  '-----'  |
       |___________|
        |  |   |  |
        |__|   |__|
{C.RESET}"""

def banner():
    print(ROBOT)
    print(C.MAGENTA + C.BOLD + "  ╔══════════════════════════════════╗" + C.RESET)
    print(C.MAGENTA + C.BOLD + "  ║        M I N I - B O T  🤖        ║" + C.RESET)
    print(C.MAGENTA + C.BOLD + "  ╚══════════════════════════════════╝" + C.RESET)
    print(C.YELLOW + "  Type 'exit' anytime to say goodbye!\n" + C.RESET)

def say(text):
    print(C.GREEN + "  🤖 Bot: " + C.RESET + text)

def divider():
    print(C.BLUE + "  " + "─" * 36 + C.RESET)

# ============================================================
#                 ORIGINAL CHATBOT LOGIC
#         (unchanged — only print()/input() calls
#          are dressed up with color + the say() wrapper)
# ============================================================

banner()
say("Hello!,iam your chatbot")
remember="remember"
recall="recall"
hi="hi"
hello="hello"
can="can"
calculate="calculate"
x=[]

while True:
    divider()
    message=input(C.CYAN + "  🧑 You >> " + C.RESET)
    if message=="exit":
        say("Goodbye!")
        break
    elif remember in message:
        say("Okay i will remember that!")
        x.append(message)
    elif recall in(message):
        say("You told me :")
        for i in x:
            print(C.YELLOW + "     • " + i + C.RESET)
    elif hi in message or hello in message:
        say("Hey! whats up")
    elif can in message:
        say("Yes i can definitly help you!")
    elif calculate in message:
        a=int(input(C.CYAN + "  🧑 enter first number :" + C.RESET))
        o=input(C.CYAN + "  🧑 enter operator" + C.RESET)
        b=int(input(C.CYAN + "  🧑 enter second number :" + C.RESET))
        if o=="+":
            say(str(a+b))
            say("Is there anythingelse you wanna calculate?")
        elif o=="-":
            say(str(a-b))
            say("Is there anythingelse you wanna calculate?")
        elif o=="*":
            say(str(a*b))
            say("Is there anythingelse you wanna calculate?")
        elif o=="/":
            say("a/b")
            say("Is there anythingelse you wanna calculate?")
else:
        say("ineresting! Tell me more!")