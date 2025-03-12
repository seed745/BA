import numpy as np
import util as u

r_source = 70 #mm
source_area = (r_source/10)**2*np.pi

gf = u.eval("/home/jasper/OneDrive/Uni/Bachelor/sim/perfect/fit.0.hits", source_area)

print(gf)