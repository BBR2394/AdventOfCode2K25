#! python3

import sys

def findPosBigger(st):
    bigger=0

    for i in st:
        if int(i)> bigger:
            bigger = int(i)

    return st.find(str(bigger))

def displayBiggerPos(st, pos, step=0):
    idx=0

    for i in range(step):
        print("-", end='')
    while idx < len(st):
        if pos == idx:
            print('^', end='')
        else :
            print("-", end='')
        idx+=1

    print('\n')

def find_in_line(st, decal=0):
    pos_bigger = findPosBigger(st)
    print(st)
    displayBiggerPos(st, pos_bigger)
    print("pos bigger :  {0}, bigger {1}".format(pos_bigger,st[pos_bigger]))
    print(st[pos_bigger+1:])
    second_bigger = findPosBigger(st[pos_bigger+1:]) + pos_bigger+1
    print("pos second bigger :  {0}, bigger {1}".format(second_bigger,st[second_bigger]))

    #displayBiggerPos(st[pos_bigger:], second_bigger, pos_bigger)

def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    
    for i in lst:
        find_in_line(i)


def main(av):
    print("Bonjour - jour 03 - AoC 2025")
    if len(av) >= 2:
        readFile(av)
    else:
        print("on ne fait rien")


if __name__ == '__main__':
    main(sys.argv)