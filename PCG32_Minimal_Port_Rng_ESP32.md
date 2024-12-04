# Clarification regarding the difference between PCG32 Pyboard and PCG32 ESP32

The general documentation remains unchanged. the only notable difference lies in the call to the specific hardware registers of the ESP32 chip.

- In the  **`__init__` method method, If no seed is provided, we use the hardware RNG call through **`(ESP32RNG()`** and add the current time **`time.ticks_ms()`** for an additional random character.
