import numpy as np



#Area under curve calculation
def areaHit(d, r, phi):

    area = ((np.pi-(2 * np.arccos(d/r)))/(np.pi * 2)) * np.pi * r**2 + (d * np.sqrt(r**2 - d**2)) - (2*phi)
    return (np.pi * r**2) - area

def inToMet(a):
    return a/39.37

def metToIn(a):
    return a*39.37

def getRPM(finalRPM):
    print(finalRPM)