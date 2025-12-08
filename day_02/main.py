#! python3

import sys

def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split(',')

    for i in lst:
        print(i)

def main(av):
    print("Bonjour - jour 02 - AoC 2025")
    if len(av) >= 2:
        readFile(av)
    else:
        print("on ne fait rien")


if __name__ == '__main__':
    main(sys.argv)