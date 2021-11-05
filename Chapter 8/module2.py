'''
what it needs to do:
    find out if the current letter is in an even position
    if it is in an odd position then it should place it in a seperate list
    if it is in an even position then it should place it next in the string
    when all numbers are finished then it should put the things in the odd list into the even list
    return the value
'''

def encryption(phrase):
    encryptedMessage = []
    oddWords = []
    for i in range(len(phrase)-1):
        if i % 2 == 0:
            oddWords.append(phrase[i])
            print(encryptedMessage)

        elif i % 2 == 1:
            encryptedMessage.append(phrase[i])
            print(encryptedMessage)

    encryptedMessage += oddWords
    encryptedMessage = ''.join(encryptedMessage)
    return encryptedMessage


phrase = input("Input a phrase")
encryptedPhrase = encryption(phrase)
print(encryptedPhrase)