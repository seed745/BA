import numpy as np
import util as u

area10 = 3.14
area20 = 7.07

hand = []
hand.append(np.round(u.eval("/home/jasper/OneDrive/Uni/Bachelor/sim/verif/eq10_self.0.hits",area10),5))
hand.append(np.round(u.eval("/home/jasper/OneDrive/Uni/Bachelor/sim/verif/eq20_self.0.hits",area20),3))

mrad =[]
mrad.append(np.round(u.eval("/home/jasper/OneDrive/Uni/Bachelor/sim/verif/eq10.0.hits",area10),5))
mrad.append(np.round(u.eval("/home/jasper/OneDrive/Uni/Bachelor/sim/verif/eq20.0.hits",area20),3))

PD=["10x10","20x10"]

anal=[0.02683,0.104]

u.tabelle4(PD,anal,hand, mrad)