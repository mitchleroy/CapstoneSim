import numpy as np
import math

global b, time, water_density, adjusted_flow, waterwheel_intertia, diameter_of_inflow_pipe_meters
global area_of_inflow_pipe_inches, area_of_inflow_pipe_meters, radius_of_waterwheel_meters, radius_of_waterwheel_inches
global RPM_waterwheel_intertia, Torque_Output, Torque_waterwheel, r, x, cutoff_height, stop_x

#----------------------------------------------------------------
#Input Vars
flow_rate_in = 20  #L/s
diameter_of_inflow_pipe_inches = 6
radius_of_waterwheel_inches = 9
radius_of_waterwheel_meters = radius_of_waterwheel_inches/39.37
wheel_width_inches = 3
#----------------------------------------------------------------

b = 10
#----------------------------------------------------------------
#External Vars
time = np.linspace(0, 250, 250)
water_density = 1000 #kg/m^3
adjusted_flow = 0
waterwheel_inertia = 0.5 * water_density * np.pi * radius_of_waterwheel_meters**4 #kg*m^2
diameter_of_inflow_pipe_meters = diameter_of_inflow_pipe_inches/39.37
area_of_inflow_pipe_inches = ((diameter_of_inflow_pipe_inches / 2)**2) * np.pi
area_of_inflow_pipe_meters = ((diameter_of_inflow_pipe_meters / 2)**2) * np.pi
radius_of_waterwheel_meters = radius_of_waterwheel_inches/39.37
#----------------------------------------------------------------


#----------------------------------------------------------------
#Output Vars
RPM_waterwheel = np.zeros(time.shape)
Torque_waterwheel = np.zeros(time.shape)
Torque_Output = np.zeros(time.shape)
#----------------------------------------------------------------

#----------------------------------------------------------------
#Flow hitting wheel
r = diameter_of_inflow_pipe_inches/2
x = np.linspace(0, int(r), int(r)*10)
cutoff_height = ((r*2)-wheel_width_inches)/2
stop_x = r
y = np.linspace(0, int(r), int(r)*10)
#for i in x:
 #   y[i] = (r-(r-r*math.sin((math.acos(i/r)))))
 #   print(y[i])

#----------------------------------------------------------------