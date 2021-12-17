#Delete two numbers in each row so that the sum of each horizontal and vertical line is 30

import enchant, time, itertools, copy

def makeWordReturnUsedLetters(input, depth, letters, usedLetters, words):
    thisInput = input[depth]
    leftoverLetters = returnListWithoutUsedLetters(letters, usedLetters)
    numLetters = thisInput.count("*")
    perm = list(itertools.permutations(leftoverLetters, numLetters))
    noDup = removeDuplicates(perm)
    for let in noDup:
        thisWords = words.copy()
        word = replaceStarWithLetters(thisInput, let)
        if(d.check(word)):
            if(depth == 0): ##anmoed
                print(word)
            if(depth < 4):
                thisWords.append(word)
                makeWordReturnUsedLetters(input, depth + 1, leftoverLetters, let, thisWords)
            else:
                thisWords.append(word)
                print(thisWords)
    return noDup

def replaceStarWithLetters(input, letters):
    ret = input
    for i in letters:
        i0 = ret.find("*")
        ret = ret[:i0] + i + ret[i0 + 1:]
    return ret

def returnListWithoutUsedLetters(letters, usedLetters):
    ret = letters.copy()
    for l in usedLetters:
        ret.remove(l)
    return ret

def removeDuplicates(letters):
    ret = []
    for l in letters:
        if l not in ret:
            ret.append(l)
    return ret

board = [[3,8,6,7,5,3,4,5], [7,5,4,3,9,5,9,2], [5,3,9,6,1,4,8,6], [8,5,2,5,4,6,5,9], [1,3,5,8,5,7,4,6], [8,7,1,6,9,6,5,1], [4,7,9,7,2,3,5,4], [6,4,5,1,9,8,3,8]]

def addIn0s(i, p):
    b = board[i]
    ret = []
    i = 0
    for n in range(8):
        if i < 6 and b[n] == p[i]:
            ret.append(p[i])
            i = i + 1
        else:
            ret.append(0)
    return ret


def genAllPick():
    all = []
    for i in range(8):
        n = board[i]
        perm = list(itertools.combinations(n, 6))
        ret = []
        for p in perm:
            if sum(p) == 30:
                ret.append(addIn0s(i, p))
        all.append(ret)
    return all


t = genAllPick()
l = list(itertools.product(*t))


for n in l:
    allAdd = True
    for i in range(8):
        row = 0
        for j in range(8):
            row = row + n[j][i]
        if row != 30:
            allAdd = False
    if allAdd:
        print(n)




