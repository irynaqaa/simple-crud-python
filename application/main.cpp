#include <iostream>
#include <thread>
#include <chrono>
#include "command_line_parser.h"
#include "timer.h"

int main(int argc, char* argv[]) {
    // Parse command-line arguments
    CommandLineParser parser;
    parser.parse(argc, argv);

    // Start timer
    Timer timer;
    timer.start();

    // Simulate some work
    std::this_thread::sleep_for(std::chrono::seconds(2));

    // Stop timer
    timer.stop();

    // Print elapsed time
    std::cout << "Elapsed time: " << timer.getElapsedTime() << " seconds" << std::endl;

    return 0;
}