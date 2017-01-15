/*
Main file for the EP Band embedded source. This file controls the entire
system.
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein.

This code is derived from https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial
with the intent of learning and integrating I2C/SPI. The code will change from
the original to fit our needs.
*/

#include <iostream>
#include <errno.h>
#include <wiringPiI2C.h>
#include <unistd.h>
#include "common.h"

using namespace std;

int int main() {
    int fd, result;

    cout << "Initializing" << endl;
    fd = wiringPiI2CSetup(CHANNEL, BUS_SPEED)

    return 0;
}
