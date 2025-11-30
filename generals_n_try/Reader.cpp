
#include "Reader.hh"

Reader::Reader() {
    std::cout << "Reader created" << std::endl;
}

Reader::~Reader() {
    if (this->_fd.is_open()) {
        std::cout << "On ferme le fichier : " << *this->_filename << std::endl;
        delete this->_filename;
        this->_fd.close();
    } else {
        std::cout << "Aucun fichier à fermer " << std::endl;
    }
    std::cout << "Reader destroyed" << std::endl;
}

int Reader::displayFile() {
    return 0;
}

int Reader::readNDisplayFile() {
    std::string line;
    std::cout << "olectur" << std::endl;
    if (this->_fd.is_open()) {
        std::cout << "Plectur" << std::endl;
        while (std::getline(this->_fd, line) ) {
            std::cout << line << '\n';
        }
        std::cout << "Mlectur" << line << std::endl;

    }
    return 0;
}

int Reader::loadFile(std::string filename) {
    std::cout << "we are going to reade the file : " << filename << std::endl;

    std::string *test = new std::string(filename);

    this->_filename = new std::string(filename);
    this->_fd.open(filename, std::fstream::in | std::fstream::out | std::fstream::app);

    std::cout << "est ce que le fichier est ouvert : " << this->_fd.is_open() << std::endl;
    std::cout << "on a ouvert : " << *this->_filename << std::endl;

    std::string  line;

    getline(this->_fd, line);
    std::cout << "une ligne : " << line  << " retour : " << std::endl;

    return 0;
}