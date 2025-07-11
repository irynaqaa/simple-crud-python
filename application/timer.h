#ifndef TIMER_H
#define TIMER_H

#include <iostream>
#include <chrono>
#include <thread>

class Timer {
public:
    void start();
    void stop();
    double getElapsedTime();
private:
    std::chrono::high_resolution_clock::time_point startTime;
    std::chrono::high_resolution_clock::time_point stopTime;
};

#endif // TIMER_H