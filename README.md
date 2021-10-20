# piCalculator
Compute 𝛑 to a ludicrously high precision!

# Requires

Python 3.x. Runs on Raspberry Pi 400 as-is.

# Usage

python .\main.py {number of digits to right of decimal point}

# Example

python .\main.py 100000

```
Calculating π to 100,000 digits

π = 3.
1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679
...
8575016363 4113146275 3049901913 5646823804 3299706957 7015078933 7728658035 7127909137 6742080565 5493624646

Elapsed Time: 22 seconds
```

# Credits

Based on Andrew Jennings' Javascript code:

http://ajennings.net/blog/a-million-digits-of-pi-in-9-lines-of-javascript.html

# References

https://math.tools/numbers/pi/1000000

# Performance

This program uses a single CPU core

Calculated 1,000,000 digits:

...in 47 minutes on an Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz 2.21 GHz CPU

... in 8 hours, 25 minutes on a Raspberry Pi 400