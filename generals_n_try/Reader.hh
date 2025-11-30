
#include <iostream>
#include <string>
#include <fstream>

class Reader {
    public:
        Reader();
        ~Reader();

    private:
        int             _counter;
        std::string     *_filename;
        std::ifstream    _fd;

    public: 
        int loadFile(std::string);
        int displayFile();
        int readNDisplayFile();


};