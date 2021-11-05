#Q2

def printMenu():
    menu = '''
    {-------------------------------------------}
    {-[A]Look up a number                      -}
    {-[B]Add new name and telephone number     -}
    {-[C]Edit telephone number                 -}
    {-[D]Delete an entry                       -}
    {-[E]Print phone directory in name sequence-}
    {-[F]Quit                                  -}
    {-------------------------------------------}
    '''
    print("Please choose an option:\n" + menu)

def getChoice():
    choice = input()
    return choice

def lookUpNum(dictionary):
    choice = input("Please enter a name")
    choice = choice.capitalize()
    if choice in dictionary:
        print(dictionary[choice])

    else:
        print("not in list")

def addNewNum(dictionary):
    name = input("Enter a name you want to add")

    if name in dictionary:
        print("That is already in the dictionary")
        addNewNum()

    if name not in dictionary:
        dictionary[name] = int(input("Enter the number"))

    return dictionary

def editNum(dictionary):
    name = input("Enter a name")
    if name in dictionary:
        dictionary[name] = int(input("Enter the number"))

    else:
        print("Please enter a valid name")
        editNum()

    return dictionary

def deleteEntry(dictionary):
    nameOrNum = input("Please enter the name or number")
    if nameOrNum in dictionary:
        del dictionary[nameOrNum]
        print("Entry deleted")

    else:
        print("Please enter a valid name or number")
        deleteEntry()

    return dictionary

#i dont really understand E so ill do what i think it is

def printPhoneDir(dictionary):
    for name in sorted(dictionary.keys()):
        print(name, dictionary[name])

################################################################################

dictionary = {"Jeff": 44, "Jimmy": 43, "Howayadoinbudday": 22, "Delorean":16}
quitNow = False

while quitNow == False:
    printMenu()
    choice = getChoice()

    if choice == "F" or choice == "f":
        quitNow = True

    elif choice == "A" or choice == "a":
        lookUpNum(dictionary)

    elif choice == "B" or choice == "b":
        dictionary = addNewNum(dictionary)

    elif choice == "C" or choice == "c":
        dictionary = editNum(dictionary)

    elif choice == "D" or choice == "d":
        dictionary = deleteEntry(dictionary)

    elif choice == "E" or choice == "e":
        printPhoneDir(dictionary)





