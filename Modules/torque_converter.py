"""! @brief Defines the ADC Driver classes"""
##
# @file torque_converter.py
#
# @brief Interpolates the troque for the given pedal percentage and speed
#
# @section description_torque Description
# The class initialises the values given in the graph and based on these values
# creates a polynomial function. Based on this function, the torque is estimated.
# ![Pedal Diagram](Pedalmap.png)
#
# @section libraries_torques Libraries/Modules
# - numpy 



import numpy as np

class torque_pedalangleper_speed(object):
    """! The torque interpolation function
    The class functions as the torque converter. Here a polynomial function is dervied from the points in the graph. An linear interpolation is also done for the speed.
    Assumption - Vehicle does not cross 50km/hr (any value above that is clipped for 50km/hr)
    """
    
    def __init__(self):
        '''! Initialisation function 
        The values given in the graph are initialised.
        '''
        self.per_0km = np.array([0,10, 20, 30, 40, 60, 80, 100])
        self.toq_0km = np.array([0, 18, 35, 50, 62, 82, 103, 120])
        
        self.per_50km = np.array([0,10, 20, 30, 40, 60, 80, 100])
        self.toq_50km = np.array([-30, -10, 10, 30, 45, 72, 95, 120])
        
        self.max_speed = 50
        self.min_speed = 0
        
    def calculate_function(self, per_km, toq_km):
        """! Fit polynomial function for the given
        Fit a polynomial function for the given pedal percentage and torque
        @params_in : pedal percentage, Torque
        @return : polynomial function
        """
        
        self.fun_graph = np.poly1d(np.polyfit(per_km, toq_km, 5))
        
        return self.fun_graph
    
    def interpolation_function(self, ac_voltage_per, speed):
        """! Interpolates the torque for the given speed
        The function takes in the ac_voltage from the sensor for the given speed and calculates the torque
        @params_in : ac_voltage from sensor, speed
        @return : interpolated_torque
        """
        
        if speed == 0:
            fun_graph = self.calculate_function(self.per_0km, self.toq_0km)
            interpolated_torque = fun_graph(ac_voltage_per)
        elif speed == 50:
            fun_graph = self.calculate_function(self.per_50km, self.toq_50km)
            interpolated_torque = fun_graph(ac_voltage_per)
        else:
            slope = (self.toq_50km - self.toq_0km) / (self.max_speed - self.min_speed) #Calculate the slope for linear interpolation
            torque_km = self.toq_0km + (slope * (speed - self.min_speed))
            
            #Assuming that the pedal % is constant
            fun_graph = self.calculate_function(self.per_50km, torque_km)
            interpolated_torque = fun_graph(ac_voltage_per)
            
        return np.round(interpolated_torque)