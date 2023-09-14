def code(n):
    crule = {'A' : 'alpha','B' : 'bravo','C' : 'charlie','D' : 'delta','E' : 'echo','F' : 'foxtrot','G' : 'golf','H' : 'hotel','I' : 'india',
        'J' : 'juliette','K' : 'kilo','L' : 'lima','M' : 'mike','N' : 'november','O' : 'oscar','P' : 'papa','Q' : 'quebec','R' : 'romeo',
        'S' : 'sierra','T' : 'tango','U' : 'uniform','V' : 'victor','W' : 'whisky','X' : 'xray','Y' : 'yankee','Z' : 'zulu','1' : 'uno',
        '2' : 'duno','3' : 'tino','4' : 'cheero','5' : 'fino','6' : 'siho','7' : 'sepo','8' : 'octo','9' : 'nino','0' : 'suno'}
    drule = {'alpha' : 'A','bravo' : 'B','charlie' : 'C','delta' : 'D','echo' : 'E','foxtrot' : 'F','golf' : 'G','hotel' : 'H','india' : 'I',
        'juliette' : 'J','kilo' : 'K','lima' : 'L','mike' : 'M','november' : 'N','oscar' : 'O','papa' : 'P','quebec' : 'Q','romeo' : 'R',
        'sierra' : 'S','tango' : 'T','uniform' : 'U','viktor' : 'V','whisky' : 'W','xray' : 'X','yankee' : 'Y','zulu' : 'Z','uno' : '1',
        'duno' : '2','tino' : '3','cheero' : '4','fino' : '5','siho' : '6','sepo' : '7','octo' : '8','nino' : '9','suno' : '0' }
    if n == 1 :
        return crule
    if n == 2 :
        return drule

def code_message():
    rule = code(1)
    dmessage = str(input("Enter the Message to be Coded: "))
    dmessage = dmessage.upper()
    message = ''
    for i in dmessage :
        if i in rule :
            message = message + rule[i] + ' '
        else :
            message = message + i
    print("Your Coded Message : ", message)


def decode_message():
    rule = code(2)
    cmessage = str(input("Enter the Message to be Decoded: "))
    cmessage = cmessage + ' '
    word = ''
    message = ''
    for i in cmessage :
        if i == ' ' :
            if word in rule :
                message = message + rule[word]
                word = ''
            else :
                message = message + ' '
        else :
            word = word + i
    print(message)
    

def menu():
    print("Welcome to the Code and Decoder Main Menu")
    print("""What Do you want to do ?
            1. Code a Message
            2. Decode a Message
            3. Exit the Program""")
    try:
        c = int(input("Enter Your Choice Here: "))
    except ValueError:
        print("Number entered is not an integer. Please enter a integer only !!")
        c = int(input("Enter Your Choice Here: "))
        if c<1 or c>3:
            print("Not a valid choice, choose between 1, 2 or 3 only !!")
            c = int(input("Enter Your Choice Here: "))
    return c

while True :
    choice = menu()
    if choice == 1:   #code a messages
        code_message()
    elif choice == 2:  #decode a message
        decode_message()
    elif choice == 3:  #exit program
        break