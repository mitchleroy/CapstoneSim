import numpy as np

#----------------------------------------------------------------
# How it works:
'''
1. Calculate flow rate:
    Q = A*V
    Q = flow rate
    A = cross-sectional area of inflow pipe
    V = velocity of water 
    Units: L/s
    ** Flow rate not used in other equations for RPM but useful nonetheless

2. Calculae force of water
    F = rho * AUC * V^2 * g
    rho = water density
    AUC = area under curve of blade being affected
    V = velocity of water
    g = gravity acceleration
    Units: N

3. Calculate torque exerted on wheel
    T = F * b
    T = Torque
    F = force
    b = distance from center of wheel to head
    Units: N*m

4. Calculate angular acceleration
    a = T / I
    a = angular acceleration
    T = torque
    I = moment of inertia
    Units: rad/s^2

5. RPM profit
    RPM = sqrt(2 * alpha * theta)
    a = angular acceleration
    theta = 2 * pi (one rotation for our case)
    Units: revolutions per minute duh


'''
def calculateRPM(r, d, velocityOfWaterIn, AUC, centerWaterwheelToHead, momentOfInertia):
#1
    flowRateQ = (np.pi * (r**2)) * velocityOfWaterIn

#2
    force = 1000 * AUC * (velocityOfWaterIn**2) * 9.81

#3
    torqueExertedOnWheel = force * centerWaterwheelToHead

#4 
    angularAcceleration = torqueExertedOnWheel / momentOfInertia

#5
    RPM_waterwheel = np.sqrt(2 * angularAcceleration * (2*np.pi))
    return RPM_waterwheel
#----------------------------------------------------------------

