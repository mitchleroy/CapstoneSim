import numpy as np
import math
from Funcs import *
from RPM import *
from Torque import *
#from RPM import *

#----------------------------------------------------------------
#Global declarations
global time, r, velocityOfWaterIn, water_density, AUC, centerWaterwheelToHead
#----------------------------------------------------------------

#----------------------------------------------------------------
#Input Vars
#####AS OF 3/28/24 ALL INPUTS ARE IN METRIC (meters, litres, etc) --- USE inToMet() FUNCTION FOR EASY CONVERSION#####
velocityOfWaterIn = 2  #m/s
diameter_of_inflow_pipe = 1
radius_of_waterwheel= 0.9
#wheel_width = 0.41
blade_length = 0.11
blade_width = 0.01
centerWaterwheelToHead = 1
momentOfInertia = 1
#----------------------------------------------------------------


#----------------------------------------------------------------
#External Vars
time = np.linspace(0, 250, 250)
adjusted_flow = 0
#waterwheel_inertia = 0.5 * water_density * np.pi * radius_of_waterwheel**4 #kg*m^2
area_of_inflow_pipe = ((diameter_of_inflow_pipe / 2)**2) * np.pi
#----------------------------------------------------------------


#----------------------------------------------------------------
#Output Vars
RPM_waterwheel = np.zeros(time.shape)
Torque_waterwheel = np.zeros(time.shape)
Torque_Output = np.zeros(time.shape)
#----------------------------------------------------------------

#----------------------------------------------------------------
#Flow hitting wheel
r = diameter_of_inflow_pipe / 2
d = blade_width / 2
phi = 0
if d > r:
    AUC = blade_length * blade_width
else:
    AUC = ((180-(2 * np.arccos(d/r)))/(360)) * np.pi * r**2 + (d * np.sqrt(r**2 - d**2)) - (2*phi)



print(areaHit(d, r, phi), "m^2 of blade being hit by water source")
#percentOfWaterHitting = (AUC / (np.pi * r**2)) * 100


#----------------------------------------------------------------


print("PRM of waterwheel:", calculateRPM(r, d, velocityOfWaterIn, areaHit(d, r, phi), centerWaterwheelToHead, momentOfInertia))
print("Torque output of waterwheel:", calculateTorque(areaHit(d, r, phi), velocityOfWaterIn, radius_of_waterwheel))