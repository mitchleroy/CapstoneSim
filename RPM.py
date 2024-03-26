import numpy as np
#----------------------------------------------------------------
#Input Vars
flow_rate_in = 20 % L/s
diameter_of_inflow_pipe_inches = 6
radius_of_waterwheel_inches = 9
radius_of_waterwheel_meters = radius_of_waterwheel_inches/39.37
wheel_width_inches = 3
#----------------------------------------------------------------


#----------------------------------------------------------------
#External Vars
time = np.linspace(0, 250, 250)
water_density = 1000 % kg/m^3
adjusted_flow = 0
waterwheel_inertia = 0.5 * water_density * pi * radius_of_waterwheel_meters^4 % kg*m^2
diameter_of_inflow_pipe_meters = diameter_of_inflow_pipe_inches/39.37
area_of_inflow_pipe_inches = ((diameter_of_inflow_pipe_inches / 2)^2) * pi
area_of_inflow_pipe_meters = ((diameter_of_inflow_pipe_meters / 2)^2) * pi
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
x = np.linspace(0, r, r/(0.1))
stop_x = r
#----------------------------------------------------------------