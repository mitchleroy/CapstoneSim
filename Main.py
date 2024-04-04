import numpy as np
import math
from Funcs import *
from RPM import *
from Torque import *
import matplotlib.pyplot as plt
#from RPM import *

#----------------------------------------------------------------
#Global declarations
global time, r, velocityOfWaterIn, water_density, AUC, centerWaterwheelToHead
#----------------------------------------------------------------

#----------------------------------------------------------------
#Input Vars
#####AS OF 3/28/24 ALL INPUTS ARE IN METRIC (meters, litres, g, etc) --- USE inToMet() FUNCTION FOR EASY CONVERSION#####
velocityOfWaterIn = 2  #L/s
diameter_of_inflow_pipe = 1
radius_of_waterwheel= 0.9
blade_length = 0.11
blade_width = 0.01
centerWaterwheelToHead = 1
massWaterwheel = 10
#----------------------------------------------------------------

#----------------------------------------------------------------
#Input arrays for variable-flow tests
varyingVelocity = np.linspace(18, 40, 100)
varyingVelocity = np.round(varyingVelocity, 2)
#----------------------------------------------------------------
#External Vars
#waterwheel_inertia = 0.5 * water_density * np.pi * radius_of_waterwheel**4 #kg*m^2
area_of_inflow_pipe = ((diameter_of_inflow_pipe / 2)**2) * np.pi
momentOfInertia = 0.5 * massWaterwheel * (radius_of_waterwheel**2)
#----------------------------------------------------------------


#----------------------------------------------------------------
#Output Arrays
yT = np.array([])
yR = np.array([])
#----------------------------------------------------------------

#----------------------------------------------------------------
#Flow hitting wheel
r = diameter_of_inflow_pipe / 2
d = blade_width / 2
phi = 0
if d > r:
    AUC = blade_length * blade_width
else:
    AUC = ((np.pi-(2 * np.arccos(d/r)))/(2 * np.pi)) * np.pi * r**2 + (d * np.sqrt(r**2 - d**2)) - (2*phi)


print(AUC)
#percentOfWaterHitting = (AUC / (np.pi * r**2)) * 100


#----------------------------------------------------------------
# Outputs
#print("PRM of waterwheel:", calculateRPM(r, d, velocityOfWaterIn, areaHit(d, r, phi), centerWaterwheelToHead, momentOfInertia))
#print("Torque output of waterwheel (N*m):", calculateTorque(areaHit(d, r, phi), velocityOfWaterIn, radius_of_waterwheel))
#----------------------------------------------------------------

#----------------------------------------------------------------
# Loop outputs

print("Torque output of water velocities: ")
for i in varyingVelocity:
    print(f"{i} L/s: ", end="")
    yTorque = calculateTorque(AUC, i, radius_of_waterwheel)
    print(yTorque, end="")
    print(" N*m")
    yT = np.append(yT, yTorque)


print("RPM output of water velocities: ")
for i in varyingVelocity:
    print(f"{i} L/s: ", end="")
    yRPM = calculateRPM(r, d, i, AUC, centerWaterwheelToHead, momentOfInertia)
    yR = np.append(yR, yRPM)
    print(yRPM, end="")
    print(" RPM")
    
#----------------------------------------------------------------

#----------------------------------------------------------------
# Graphing
plt.plot(varyingVelocity, yT, label="Torque", color='blue')
plt.plot(varyingVelocity, yR, label="RPM", color='red')
plt.title("Best case Torque and RPM output of varying velocities")
plt.xlabel('Velocities')
plt.ylabel('Torque/RPM')
plt.legend()
plt.show()
#----------------------------------------------------------------