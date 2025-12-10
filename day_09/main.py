#! python3

import sys


def readFile(av):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()
    lst = input.split('\n')
    lst_tupple =  []
    
    most_max_val = 0
    for i in lst :
        ln = i.split(',')
        if int(ln[0]) > most_max_val:
            print("most minmax  val", ln[0])
            most_max_val = int(ln[0])
        lst_tupple.append((ln[0], ln[1]))

    ordered_list = sorted(lst_tupple, key=lambda elem: elem[1])
    
    most_right=0
    most_right_line=0
    most_left=most_max_val
    most_left_line=0

    most_bottom_right=0
    most_bottom_left=0

    higher_line=ordered_list[0][1]
    bottom_line=ordered_list[len(ordered_list)-1][1]


    for i in ordered_list:
        if most_right < int(i[0]):
            most_right = int(i[0])
            most_right_line = int(i[1])
            print(i[0])
        if most_left > int(i[0]):
            most_left = int(i[0])
            most_left_line = int(i[1])
        
        print(i)
        #find_in_line(i)

    most_right_bis=0
    most_right_line_bis=0
    most_left_bis=most_max_val
    most_left_line_bis=0
    for i in ordered_list:
        if most_right_bis <= int(i[0]):
            most_right_bis = int(i[0])
            most_right_line_bis = int(i[1])
            print(i[0])
        if most_left_bis >= int(i[0]):
            most_left_bis = int(i[0])
            most_left_line_bis = int(i[1])
    
    print("Ligne la plus haute : ", higher_line, "\nLigne la plus en bas = ", bottom_line)
    print("most  left = ", most_left)
    print("most  left line = ", most_left_line)
    print("most  right = ", most_right)
    print("most  right line = ", most_right_line)
    print("-----")
    print("most  left bis = ", most_left_bis)
    print("most  left line bis = ", most_left_line_bis)
    print("most  right bis = ", most_right_bis)
    print("most  right line bis = ", most_right_line_bis)

    final_most_right = 0
    if most_right > most_right_bis:
        final_most_right = most_right
    elif most_right < most_right_bis:
        final_most_right = most_right_bis
    else :
        final_most_right = most_right

    final_most_left = 0
    if most_left > most_left_bis:
        final_most_left = most_left
    elif most_left < most_left_bis:
        final_most_left = most_left_bis
    else :
        final_most_left = most_left

    print("le plus a droit : ", final_most_right, " le plus a gauche : ", final_most_left)

def main(av):
    print("Bonjour - jour 09 - AoC 2025")
    if len(av) >= 2:
        readFile(av)
    else:
        print("on ne fait rien")


if __name__ == '__main__':
    main(sys.argv)