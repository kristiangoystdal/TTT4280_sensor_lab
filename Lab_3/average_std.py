import numpy as np

rp_trans = [67.09, 64.89, 64.6, 71.92, 66.36, 66.94]
gp_trans = [67.09, 64.89, 64.6, 72.07, 66.36, 66.94]
bp_trans = [67.09, 64.75, 64.45, 71.92, 66.36, 66.94]

mu_r_trans = np.mean(rp_trans)
mu_g_trans = np.mean(gp_trans)
mu_b_trans = np.mean(bp_trans)

print("Forventningsverdi til rød: %f" % mu_r_trans)
print("Forventningsverdi til grønn: %f" % mu_g_trans)
print("Forventningsverdi til blå: %f" % mu_b_trans)

std_r_trans = np.std(rp_trans)
std_g_trans = np.std(gp_trans)
std_b_trans = np.std(bp_trans)

print("Standardavvik til rød: %f" % std_r_trans)
print("Standardavvik til grønn: %f" % std_g_trans)
print("Standardavvik til blå: %f" % std_b_trans)


rp_reflec = [55.66, 59.62, 60.94, 60.06, 62.11, 59.91]
gp_reflec = [55.37, 59.62, 61.08, 60.06, 62.11, 60.06]
bp_reflec = [55.66, 59.77, 60.94, 60.06, 62.11, 59.91]

mu_r_reflec = np.mean(rp_reflec)
mu_g_reflec = np.mean(gp_reflec)
mu_b_reflec = np.mean(bp_reflec)

print("Forventningsverdi til rød: %f" % mu_r_reflec)
print("Forventningsverdi til grønn: %f" % mu_g_reflec)
print("Forventningsverdi til blå: %f" % mu_b_reflec)

std_r_reflec = np.std(rp_reflec)
std_g_reflec = np.std(gp_reflec)
std_b_reflec = np.std(bp_reflec)

print("Standardavvik til rød: %f" % std_r_reflec)
print("Standardavvik til grønn: %f" % std_g_reflec)
print("Standardavvik til blå: %f" % std_b_reflec)

