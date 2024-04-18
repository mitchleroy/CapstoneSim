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
#####AS OF 3/28/24 ALL INPUTS ARE IN METRIC (meters, litres, g, etc) --- USE inToMet() FUNCTION FOR EASY CONVERSION#####
#----------------------------------------------------------------
#Input Vars
velocityOfWaterIn = 22  # L/s
diameter_of_inflow_pipe = inToMet(4.5) # 4.5 inches -> meters
radius_of_waterwheel= inToMet(3) # 3 inches -> meters
blade_length = inToMet(3) # 3 inches -> meters
blade_width = inToMet(1) # 1 inch -> meters
centerWaterwheelToHead = inToMet(4.5) # 4.5 inches -> meters
massWaterwheel = 7 # grams
theta = 45 # degrees between blades
#----------------------------------------------------------------

#----------------------------------------------------------------
#Input arrays for variable-flow tests
varyingVelocity = np.linspace(18, 40, 100)
varyingVelocity = np.round(varyingVelocity, 2)
#----------------------------------------------------------------
#External Vars
#waterwheel_inertia = 0.5 * water_density * np.pi * radius_of_waterwheel**4 #kg*m^2s
area_of_inflow_pipe = ((diameter_of_inflow_pipe / 2)**2) * np.pi
momentOfInertia = 0.5 * massWaterwheel * (radius_of_waterwheel**2)
velocityOfWaterIn = velocityOfWaterIn / 1000
#----------------------------------------------------------------


#----------------------------------------------------------------
#Output Arrays
yTBC = np.array([])
yTWC = np.array([])
yRBC = np.array([])
yRWC = np.array([])
#----------------------------------------------------------------



#----------------------------------------------------------------
# Loop outputs

#Torque output of water velocities - BEST CASE
for i in varyingVelocity:
    yTorque = bestCaseTorque(theta, blade_length, blade_width, i, centerWaterwheelToHead)
    yTBC = np.append(yTBC, yTorque)


#RPM output of water velocities - BEST CASE
for i in varyingVelocity:
    yRPM = calculateRPM(radius_of_waterwheel, i, flowHittingWheel(diameter_of_inflow_pipe, blade_width, 0), centerWaterwheelToHead, momentOfInertia)
    yRBC = np.append(yRBC, yRPM)

#Torque output of water velocities - WORST CASE
for i in varyingVelocity:
    yTorque = worstCaseTorque(theta, blade_length, blade_width, i, centerWaterwheelToHead)
    yTWC = np.append(yTWC, yTorque)


#RPM output of water velocities - WORST CASE
for i in varyingVelocity:
    yRPM = calculateRPM(radius_of_waterwheel, i, flowHittingWheel(diameter_of_inflow_pipe, blade_width, 0), centerWaterwheelToHead, momentOfInertia)
    yRWC = np.append(yRWC, yRPM)
    
#----------------------------------------------------------------

#----------------------------------------------------------------
#Plotting
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
# Plot for best case torque and RPM
ax1.plot(varyingVelocity, yTBC, label="Torque", color='blue')
ax1.set_ylabel('Torque (N*m)')
ax1.legend()

ax2.plot(varyingVelocity, yRBC, label="RPM", color='red')
ax2.set_ylabel('RPM')
ax2.legend()

# Plot for worst case torque and RPM
ax3.plot(varyingVelocity, yTWC, label="Torque", color='blue')
ax3.set_xlabel('Velocities')
ax3.set_ylabel('Torque (N*m)')
ax3.legend()

ax4.plot(varyingVelocity, yRWC, label="RPM", color='red')
ax4.set_xlabel('Velocities')
ax4.set_ylabel('RPM')
ax4.legend()

# Set title for the entire figure
plt.suptitle("Torque and RPM output of varying velocities")

plt.show()
#----------------------------------------------------------------