import numpy as np

#----------------------------------------------------------------
# How it works:
'''
T = F * C
T = Torque output at center of water wheel
F = Force 
    Force = 1000 * Area under Curve * (velocityOfWaterIn**2)

C = Center of water wheel to head
'''
def calculateTorque(totalArea, velocityOfWaterIn, centerWaterwheelToHead):
    F = 1000 * totalArea * (velocityOfWaterIn**2)
    C = centerWaterwheelToHead
    tOut = F * C
    return tOut