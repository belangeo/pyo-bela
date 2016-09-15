"""
Oneliner-2 - Algorithmic tune written on a single line!

"""
t=Disto(BandSplit(Noise(),6,50,14000,Sine(.05,0,8,9),Osc(SquareTable(20),Randh(2,9,[.16,.12,.15,.17,.2,.1]),0,2,.2,.2)),[.8,.8,.7,.7,.6,.6],.7,Port(Clip(RandInt(4,[.05,.08,.04,.06,.07,.09])))).out()
