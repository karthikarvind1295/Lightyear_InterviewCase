"""! @brief Defines the Error classes"""
##
# @file error_led.py
#
# @brief Defines the error class for computing the error between the sensors
#
# @section description_error Description
# Defines the class and function for computing the error between the sensors and returns the good sensor id
#
# @section libraries_sensors Libraries/Modules
# - numpy 
#
# @section notes_error Notes
# - The error_calculation function was implemented based on Li, Liang, and Wei Shi. "A fault tolerant model for multi-sensor measurement." Chinese Journal of Aeronautics 28.3 (2015): 874-882.


import numpy as np

class error_led(object):
    """! The Error class
    The error class is used to get the residual error/detect the noisy sensor and take the input from the less noiser sensor
    """
    
    def __init__(self):
        """! The class initializer
        Initialises the parameters
        """
        self.led_light = False
        self.sensor_return = 0

    def error_calculation(self, ac_voltage_0, ac_voltage_1):
        '''! Calculates the error between sensors
        The function is used to calculate the error function. If the error value is greater than 0 then 
        sensor 0 is faulty and if error value is negative then sensor 1 is faulty.
        @params in : ac_voltage of sensor 0, and ac_voltage of sensor 1
        @return - error between sensor one and two
        '''
        #From [1]
        #Equation of the sensor = y = kx + c
        #Sensor 0 - `adc1 = 0.5 + 0.1 * angle`
        #Sensor 1 - `adc2 = 1.0 + 0.08 * angle`
        #Calculate residual error
        alpha = (0.1/0.08) #ki/kj
        beta = 0.5 - ((0.1*1.0)/0.08) #ci - ki*cj / kj
        
        error = np.round(np.mean(ac_voltage_0 - ((alpha*ac_voltage_1) + beta)))
        
        if error == 0:
            print("Both the sensors are fine")
        elif error > 0:
            print("Sensor with channel id 0 is not working fine")
            self.led_light = True
            self.sensor_return = 0
        elif error < 0:
            print("Sensor with channel id 1 is not working fine")
            self.led_light = True
            self.sensor_return = 1
        
        return self.sensor_return
            
    def led_light_on(self):
        '''! Sets the LED in the panel to ON and OFF
        The function is used to switch on and off the LED light in the Dashboard
        @return - Switches on the light in the Dashboard
        '''
        if self.led_light:
            print("LED LIGHT IS GLOWING......")
        else:
            print("LED LIGHT IS OFF AND EVERYTHING IS COOL.....")