import numpy as np
import math
from scipy.integrate import simpson
from Funcs import *


#----------------------------------------------------------------
#Input Vars
#####AS OF 3/28/24 ALL INPUTS ARE IN METRIC (meters, litres, etc) --- USE inToMet() FUNCTION FOR EASY CONVERSION#####
flow_rate_in = 20  #L/s
diameter_of_inflow_pipe = 6
radius_of_waterwheel= 9
wheel_width = 3
blade_length = 8
blade_width = 3
#----------------------------------------------------------------


#----------------------------------------------------------------
#External Vars
time = np.linspace(0, 250, 250)
water_density = 1000 #kg/m^3
adjusted_flow = 0
waterwheel_inertia = 0.5 * water_density * np.pi * radius_of_waterwheel**4 #kg*m^2
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
test1 = Atotal(2, 3, 0)
print("Test1: ", test1)

r = diameter_of_inflow_pipe / 2
d = blade_width / 2
print(blade_width)
print(d)
phi = 0.21
print(areaHit(d, r, phi))

# (area hit / head area) * water velocity hitting wheel
#----------------------------------------------------------------