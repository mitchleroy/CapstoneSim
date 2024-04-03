import numpy as np

#----------------------------------------------------------------
# How it works:

'''
T = F * C
T = Torque output at center of water wheel
F = Force 
    Force = 1000 * AUC * (velocityOfWaterIn**2) * 9.81

C = Center of water wheel to head

'''

def calculateTorque(AUC, velocityOfWaterIn, radius):
    F = 1000 * AUC * (velocityOfWaterIn**2)
    C = radius
    tOut = F * C
    return tOut