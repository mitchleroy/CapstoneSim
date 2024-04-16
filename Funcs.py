import numpy as np
import Torque
import RPM


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

def flowHittingWheel(diameter, width, offset):
    r = diameter / 2
    d = width / 2
    phi = 0
    if d > r:
        AUC = blade_length * blade_width
    else:
        AUC = ((np.pi-(2 * np.arccos(d/r)))/(2 * np.pi)) * np.pi * r**2 + (d * np.sqrt(r**2 - d**2)) - (2*phi)
    return AUC

def bestCaseTorque(theta, blade_length, blade_width, velocity, distance):
    #One blade is perpindicular to outflow
    lengthTotal = blade_length + (blade_length - (blade_length * np.cos(np.radians(theta))))
    areaTotal = lengthTotal * blade_width
    return Torque.calculateTorque(areaTotal, velocity, distance)

def worstCaseTorque(theta, blade_length, blade_width, velocity, distance):
    lengthTotal = blade_length + (np.sin(np.radians(22.5)* (blade_length / np.sin(112.5))))
    areaTotal = lengthTotal * blade_width
    return Torque.calculateTorque(areaTotal, velocity, distance)
'''
def bestCaseRPM(theta, radius, blade_length, blade_width, velocity, distance, moment):
    lengthTotal = blade_length + (blade_length - (blade_length * np.cos(np.radians(theta))))
    areaTotal = lengthTotal * blade_width
    return RPM.calculateRPM(radius, velocity, areaTotal, distance, moment)
'''