# Analog inputs (1 = degrade ctrl, 2 = lowpass filter cutoff)
i1 = Input(2)
i2 = Input(3)

src = Input([0,1])
#t = SndTable(SNDS_PATH+"/transparent.aif")
#src = Osc(t, t.getRate(), mul=0.5)

# Controllers scaling
d1 = i1 * 0.49 + 0.005
d2 = i1 * 0.48 + 0.006
d3 = i1 * 0.39 + 0.007
d4 = i1 * 0.38 + 0.008

# DSP
delay = SmoothDelay(src, [d1,d2,d3,d4], i2*0.99, crossfade=0.005, mul=0.35).out()
dry = Mix(src, voices=2, mul=0.4).out()

