## PCG32 Random Number Generator in Python (Micropython port) ##
# Original Source:   PCG Random Number Generation for C
# Minimal C Implementation
# Copyright 2014 Melissa O'Neill <oneill@pcg-random.org>
# http://www.pcg-random.org
#
# This is the Python implementation of the PCG32 random number generator, ported
# from the C for use on embedded systems like ESP32, RP2040, Pyboard.
# This implementation uses the PCG32 (Permuted Congruential Generator) method.
# The seed is provided by the Pyboard's hardware RNG function, pyb.rng().
# 
# Source adapted for MicroPython on Pyboard.
# https://github.com/MicroControleurMonde
# PCG32_Minimal_Port_Rng_PyBoard.py

import pyb
import time

class PCG32Random:
    """
    PCG32 Random Number Generator class.
    Implements the PCG32 algorithm, a fast and high-quality random number generator.
    The generator is initialized with a 64-bit seed and a 64-bit increment. If no 
    values are provided for the seed and increment, they are automatically generated 
    using the device's hardware RNG and the current time.
    Attributes:
        state (int): The internal state of the generator (64 bits).
        inc (int): The increment used for the generator's state update (64 bits).
    """
    def __init__(self, seed=None, inc=None):
        if seed is None:
            seed = pyb.rng() + int(time.ticks_ms())
        if inc is None:
            inc = 1  # Default increment

        self.state = seed & 0xFFFFFFFFFFFFFFFF  # 64-bit seed
        self.inc = (inc << 1) | 1  # Ensure the increment is odd

        # "Prime" step to avoid bias in the first number
        self.random()  # Generate one number to mix the state

    # Reste du code...


    def random(self):
        """
        Generates a 32-bit pseudo-random value using the PCG32 algorithm.
        The internal state is updated, and a 32-bit random number is produced 
        based on the old state using the XSH RR output function.
        Returns:
            int: A 32-bit random number.
        """
        # Save the old state
        oldstate = self.state

        # Advance the internal state
        self.state = (oldstate * 6364136223846793005) + self.inc
        self.state &= 0xFFFFFFFFFFFFFFFF  # Mask to 64 bits

        # Xorshift and rotate (XSH RR)
        xorshifted = (oldstate >> 18) ^ oldstate
        xorshifted = (xorshifted >> 27) & 0xFFFFFFFF  # Mask to 32 bits
        rot = oldstate >> 59

        # Perform the rotation and return the result
        return ((xorshifted >> rot) | (xorshifted << (32 - rot))) & 0xFFFFFFFF

    def randint(self, start, end):
        """
        Generates a random integer in the specified range [start, end].
        This function uses the `random()` method to generate a number and then
        maps it to the given range.
        Args:
            start (int): The lower bound of the range.
            end (int): The upper bound of the range.
        Returns:
            int: A random integer in the range [start, end].
        """
        return start + (self.random() % (end - start + 1))

# Example usage:
if __name__ == "__main__":
    rng = PCG32Random()  # Initialize with a unique seed

    # Generate multiple random numbers
    for _ in range(10):
#        print("DEBUG - 32-bit random value: ", rng.random())  # Random 32-bit value
        print("Random number between 1 and 1000: ", rng.randint(1, 1000))


