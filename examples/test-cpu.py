"""
CPU and optimization test file.

without optimizations: 30 sines = 60.3% CPU
with optimizations: 30 sines = 55.0% CPU

"""
import random

NUM = 30

freqs = [random.uniform(400, 600) for i in range(NUM)]

sines = Sine(freqs, mul=0.05).out()

