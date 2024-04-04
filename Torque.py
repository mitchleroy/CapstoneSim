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

def calculateTorque(AUC, velocityOfWaterIn, centerWaterwheelToHead):
    F = 1000 * AUC * (velocityOfWaterIn**2)
    C = centerWaterwheelToHead
    tOut = F * C
    return tOut