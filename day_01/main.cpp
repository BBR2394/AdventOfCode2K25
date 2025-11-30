
#include <iostream>

#include "../generals_n_try/Reader.hh"

int main(int ac, char **av) {

    Reader read;

    std::cout << "Advent of code 2K25 - Day 01" << std::endl;
    std::cout << "ac : " << ac << "Av : " << av[0] << std::endl;
    if (ac >= 2) {
        read.loadFile(av[1]);
    } else {

    }
    return 0;
}