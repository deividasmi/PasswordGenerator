import string
import random
import urllib.request


def randomSymbolGenerator(size=4, uppercases=False, symbols=False, numbers=False):

    chars = string.ascii_lowercase
    if uppercases:
        chars = chars + string.ascii_uppercase
    if symbols:
        chars = chars + string.punctuation
    if numbers:
        chars = chars + string.digits
    return "".join(random.choice(chars) for _ in range(size))


def getWordList():
    content = urllib.request.urlopen("https://karklas.mif.vu.lt/~toma3569/").read()
    contentStr = content.decode('utf-8')
    wordList = contentStr.split("\n")
    return wordList


def findWordByLenght(lenght):
    wordList = getWordList()
    wordListBySize = []
    for word in wordList:
        if len(word) <= lenght:
            wordListBySize.append(word)
    #print(wordListBySize)

    return wordListBySize[random.randrange(0, len(wordListBySize))]


def PasswordGenerator(size=4, uppercases=False, symbols=False, numbers=False, words=False):
    if words:
        return randomWordPassword(size, uppercases, symbols, numbers)
    else:
        return randomSymbolGenerator(size, uppercases, symbols, numbers)


def addSymbolsAndNumbers(word, size, symbols, numbers):
    count = random.randrange(1,size-1)
    if symbols and numbers:
        for i in range(0, size-count):
            if symbols:
                word = word + random.choice(string.punctuation)
        for i in range(0, size-(size-count)):
            if symbols:
                word = word + random.choice(string.digits)
    elif symbols:
        for i in range(0,size):
            word = word + random.choice(string.punctuation)
    else:
        for i in range(0,size):
            word = word + random.choice(string.digits)
    return word


def addUpperCases(word):
    count = random.randrange(1, len(word))
    for i in range(0,count):
        randomplace = random.randrange(0, len(word))
        partWord = word[randomplace:].capitalize()
        word = word[0:randomplace] + partWord
    return word


def randomWordPassword(size=4, uppercases=False, symbols=False, numbers=False):
    sybmolCount = 0
    if symbols:
        sybmolCount += 1
    elif numbers:
        sybmolCount += 1

    wordlLenght = random.randrange(4, size - sybmolCount)
    password = findWordByLenght(wordlLenght)
    if uppercases:
        password = addUpperCases(password)
    password = addSymbolsAndNumbers(password, size-len(password), symbols, numbers)
    return password


print(PasswordGenerator(12, True, True, True, True))
