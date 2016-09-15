"""
Oneliner-1 - Algorithmic tune written on a single line!

"""
t=Degrade(FM(Choice([50]*9+[75,99],10,RandInt(3,.2,2,4)),[.25,.33,.5,.75],Sine(.03,0,4,4),TrigEnv(Metro(.1,6).play(),CosTable([(0,0),(49,1),(500,.3),(8191,0)]),Sine(.07,0,.15,.45)),Sine([100,101],0,0.03)).mix(2),Sine(0.02,0,3,7),Sine(.05,0,.06,.1),0.3).out()
