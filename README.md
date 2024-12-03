# PCG32 Random Number Generator (Micropython Port)

## Introduction
This repository contains a Micropython implementation of the **PCG32** (Permuted Congruential Generator) random number generator, originally developed in C by [Melissa O'Neill](http://www.pcg-random.org). 

The code is ported for use on embedded systems such as **ESP32**, **RP2040**, or **PyBoard**, and is designed to run on platforms with MicroPython.

The **PCG32** algorithm provides high-quality, fast, and statistically robust random numbers. It is especially well-suited for environments with limited resources, like microcontrollers.

## Features
- **High-quality random number generation** based on the **PCG32** algorithm.
- **Easy integration** with MicroPython-based devices (ESP32, RP2040, PyBoard, etc.).
- The generator uses a **64-bit seed** and a **64-bit increment**, with optional automatic initialization using the device's unique ID and current time.
- Generates **32-bit random numbers** and can produce **random integers** within a given range.
  
#### Code Overview
The code is fully documented in the source file
[Source Code](https://github.com/MicroControleurMonde/PCG32_Port/blob/main/PCG32_Minimal_Port_PyBoard.py)

## Output:
```
32-bit random value:  3037929063
Random number between 1 and 1000:  709
```
## Installation
To use the PCG32 random number generator, you can directly copy the code into your project.

## Dependencies
This code requires **MicroPython** to run on your embedded device (ESP32, RP2040, etc.).
- **MicroPython** (https://micropython.org/)
- **`machine`** and **`time`** modules.

## License
This project is licensed under the Apache License 2.0 (Same as initial code)

## Authors
Original C implementation by [Melissa O'Neill](http://www.pcg-random.org).  

Python port by [MicroControleurMonde](https://github.com/MicroControleurMonde).

## References
- [PCG Random Number Generation for C](https://www.pcg-random.org/download.html)

## Updates
- An improved version of the code for Pyboard v1.1 using the pyb.rng() fonction to seed the PCG generator shall come soon.
