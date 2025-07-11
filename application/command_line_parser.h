#ifndef COMMAND_LINE_PARSER_H
#define COMMAND_LINE_PARSER_H

#include <iostream>
#include <string>
#include <vector>

class CommandLineParser {
public:
    void parse(int argc, char* argv[]);
};

#endif // COMMAND_LINE_PARSER_H