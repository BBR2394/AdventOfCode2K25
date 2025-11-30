
#include <iostream>
#include "Reader.hh"

int main(int ac, char **av) {
    Reader reader;
    Reader reader_two;

    std::cout << "bonjour" << std::endl;
    
    reader.loadFile("bonjour.txt");

    reader_two.loadFile("exemple_one.txt");
    reader.readNDisplayFile();
    
    return 0;
}