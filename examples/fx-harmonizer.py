# Analog inputs (1 = transposition factors, 2 = feedback)
i1 = Input(2)
i2 = Input(3)

src = Input([0,1])
#t = SndTable(SNDS_PATH+"/transparent.aif")
#src = Osc(t, t.getRate(), mul=0.5)

# Controllers scaling
t1 = i1 * 24 - 12
t2 = i1 * 24.2 - 12.1

# DSP
harmo = Harmonizer(src, [t1,t2], i2*0.9, winsize=0.05, mul=0.4).out()
dry = Mix(src, voices=2, mul=0.4).out()

