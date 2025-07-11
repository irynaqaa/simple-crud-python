#include "command_line_parser.h"

void CommandLineParser::parse(int argc, char* argv[]) {
    // Parse command-line arguments
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "--help") {
            std::cout << "Usage: " << argv[0] << " [options]" << std::endl;
            std::cout << "Options:" << std::endl;
            std::cout << "  --help        Show this help message" << std::endl;
            std::cout << "  --version     Show version information" << std::endl;
            return;
        } else if (arg == "--version") {
            std::cout << "Version: 1.0" << std::endl;
            return;
        }
    }
}