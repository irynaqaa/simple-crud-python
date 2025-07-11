#include "timer.h"
#include <chrono>
#include <iostream>
#include <thread>

// Define a function to measure startup time
void measureStartupTime() {
    // Record the start time
    auto startTime = std::chrono::high_resolution_clock::now();
    
    // Simulate some startup tasks
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    // Record the end time
    auto endTime = std::chrono::high_resolution_clock::now();
    
    // Calculate the elapsed time
    auto elapsedTime = std::chrono::duration_cast<std::chrono::seconds>(endTime - startTime);
    
    // Log the elapsed time
    std::cout << "Startup time: " << elapsedTime.count() << " seconds" << std::endl;
}

void Timer::start() {
    startTime = std::chrono::high_resolution_clock::now();
}

void Timer::stop() {
    stopTime = std::chrono::high_resolution_clock::now();
}

double Timer::getElapsedTime() {
    return std::chrono::duration_cast<std::chrono::seconds>(stopTime - startTime).count();
}