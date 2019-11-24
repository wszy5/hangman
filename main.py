def start():
    import getpass
    password = getpass.getpass()
    phrase = password.upper()
    T = ["_"]*len(password)
    
def show_word(T):
    print(T)

def guess(T):
    g = str(input("wprowadz literę: "))
    H.append(g)