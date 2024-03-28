import numpy as np

#Area under curve calculation
def Atotal(d, r, phi):

    area = ((180-(2 * np.arccos(d/r)))/(360)) * np.pi * r**2 + (d * np.sqrt(r**2 - d**2)) - (2*phi)
    return (np.pi * r**2) - area

def inToMet(a):
    return a/39.37

def metToIn(a):
    return a*39.37