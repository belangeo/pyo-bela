# Analog inputs 
i1 = Input(2)
i2 = Input(3)

src = Noise(.5)
#t = SndTable(SNDS_PATH+"/transparent.aif")
#src = Osc(t, t.getRate(), mul=0.5)

# Controllers scaling
m1 = i1 * 20 + 0.1
m2 = m1 * 1.25
m3 = m2 * 1.25
m4 = m3 * 1.25

# DSP
modus = FastSine([m1,m2,m3,m4], mul=0.5, add=0.5)
bands = BandSplit(src, num=4, min=50, max=5000, q=i2*20+1, mul=modus)
mix = Mix(bands, voices=2, mul=i2*2+0.5).out()
