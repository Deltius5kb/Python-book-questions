#Q1

x = True
while x:
    anagrams = {"angel": ("angle", "glean"),
                "trade": ("rated", "tread")}

    word = input("Please enter a word")

    if word in anagrams:
        print("the word is:", anagrams.get(word))

    else:
        print("word not found")
        retry = input('''
        would you like to try again?
        1] yes
        anything else] no
        ''')

        if retry == 1:
            x = True

        else:
            x = False