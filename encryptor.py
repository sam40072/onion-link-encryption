from pyargon2 import hash
import random
import os

saltpepper = ['534272457572','2462181968247']

#http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/
#http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion/

def randomString(length: int):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    newstring = ''
    for i in range(length):
        newstring += abc[random.randint(0, len(abc) - 1)]
    return newstring

def addfluffonionLinks(fluffnum: int):
    file = open('deepweb/onionLinks.txt', 'a+')
    for i in range(fluffnum):
        newLink = f'http://{randomString(56)}.onion/'
        file.write(newLink + '\n')
    file.close()

def addFluf(fluffNum: int):
    file = open('deepweb/fluff.txt', 'a+')
    for i in range(fluffNum):
        h = hash(str(random.random()), saltpepper[0], saltpepper[1], time_cost=1)
        file.write(h + '\n')
    file.close()

def shuffleFile(filePath: str):
    templist = []
    file = open(filePath, 'r+')
    for line in file.readlines():
        templist.append(line.strip())
    file.close()
    random.shuffle(templist)
    open(filePath, 'w+').close()
    file = open(filePath, 'a+')
    for i in range(len(templist)):
        file.write(templist[i] + '\n')
    file.close()

def addLink(onionLink: str):
    fileLink = open('deepweb/onionLinks.txt', 'a+')
    fileLink.write(onionLink+'\n')
    fileLink.close()
    fileHash = open('deepweb/mainFile.txt', 'a+')
    fileHash.write(hash(onionLink, saltpepper[0], saltpepper[1], time_cost=1) + '\n')
    fileHash.close()

def dump():
    filefrom = open('deepweb/fluff.txt', 'r+')
    fileto = open('deepweb/mainFile.txt', 'a+')
    for line in filefrom.readlines():
        fileto.write(line)
    filefrom.close()
    fileto.close()

def compare():
    fullflist = []
    mainlist = []
    fluff = open('deepweb/fluff.txt', 'r+')
    for line in fluff.readlines():
        fullflist.append(line.strip( ))
    fluff.close()
    mainfile = open('deepweb/mainFile.txt', 'r+')
    for line in mainfile.readlines():
        mainlist.append(line.strip())
    return list(set(mainlist) - set(fullflist))

def unhash(compareList: list):
    print('unhashed\n-----------')
    for i in range(len(compareList)):
        file = open('deepweb/onionLinks.txt', 'r+')
        for line in file.readlines():
            if (hash(line.strip(), saltpepper[0], saltpepper[1], time_cost=1) == compareList[i]):
                print(line.strip())
                if (i == len(compareList) - 1):
                    break
        file.close()
    print('-----------')


def createDirectory():
    try:
        os.makedirs('deepweb')
    except:
        return 'file already exists'

def emergencyDelete():
    try:
        os.remove('deepweb/fluff.txt')
        os.remove('deepweb/mainFile.txt')
        os.remove('deepweb/onionLinks.txt')
        os.removedirs('deepweb')
    except:
        return 'doesn\'t exist'

def setup(numberOfSpoofs: int):
    print('making folder')
    createDirectory()
    print("adding fake links")
    addfluffonionLinks(numberOfSpoofs)
    print("adding fake hashes")
    addFluf(numberOfSpoofs)
    print('dumping all into main file')
    dump()

def correctAdd(link: str):
    addLink(link)
    shuffleFile('deepweb/mainFile.txt')
    shuffleFile('deepweb/onionLinks.txt')



while (True):
    print('1) add link\n2) dehash links\n3) setup\n4) delete folder')
    mod = input("> ")
    if (mod == '1'):
        link = input("link > ")
        correctAdd(link)
    if (mod == '2'):
        x = compare()
        unhash(x)
    if (mod == '3'):
        num = input('num of spoofs (1000 is good because larger goes slower) > ')
        setup(int(num))
    if (mod == '4'):
        emergencyDelete()