#! python3

import sys

step_two = True
display_debug = True

def print_debug(str):
    if display_debug:
        print(str)

def unlock_it(lst):
    counter=50
    direction=''
    count_zero = 0

    for i in lst:
        direction=i[0]
        step=int(i[1:])
        stepStr = i[1:]

        #bon mon algo n'est pas correct si on a un nombre > 100
        # mais si on supprime la centaine (car c'est pareil au final), ca fonctionne :-)
        if len(stepStr)>= 3:
            print('trois digit : ', step) 
            step = int(i[2:])
            #for step two
            if step_two:
                count_zero += int(i[1])


        if direction == 'L':
            #print("on va a gauche de ", step)
            counter -= step
        
        elif direction == 'R':
            #print("on va a droite de ", step)
            counter += step
        else :
            print("erreur")

        if counter == 100:
            counter = 0
        
        if counter > 100:
            centaine=int(counter/100)
            counter -= 100 * centaine 
            if step_two:
                count_zero += 1
        elif counter < 0:
            #print("counter moinsde 0: ", counter)
            counter = counter * -1
            centaine=int(counter/100)
            counter = ((100*centaine) - counter) * -1
            counter = 100 - counter
            if step_two:
                count_zero += 1
        elif counter == 0:
            count_zero += 1
            #print("----->on a 0<------")
        
        #print("counter : ", counter)

    #si on termine sur 0
    if counter == 0:
        count_zero += 1
        #print("----->on a 0<------")

    print("on a eu : ", count_zero, " zero ")



def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    unlock_it(lst)


    # for i in lst:
    #     print(i)


def main(av):
    print("Bonjour - jour 01 - AoC 2025")
    if len(av) >= 2:
        readFile(av)
    else:
        print("on ne fait rien")


if __name__ == '__main__':
    main(sys.argv)