"""! @brief Defines the ADC Driver classes"""
##
# @file adc_driver.py
#
# @brief Computes the voltage given a pedal input
#
# @section description_adc Description
# The class returns the AC Voltage given the pedal input based on the equation given in the question
#
# @section libraries_ac Libraries/Modules
# - numpy 
#
# @section notes_ac Notes
# - The class accepts the pedal input and return the pedal pecentage wrt to AC voltage as the output


import numpy as np

class adc_drivers(object):
    '''! This class defines the adc_driver class
    This class replicates the function of a ADC Driver. The sensor is first initialised with a sensor id.
    Based on the sensor id, the respective equation for converstion is carried out
    '''
    def __init__(self, channel_id):
        '''! Initialising the class
        The function accepts the channel id (either 0 or 1) and initialises the id
        '''

        self.channel_id = channel_id
        print("Initialising the sensor with id {}".format(self.channel_id))
        self.channel_status = False
        
        if channel_id > 1:
            raise ValueError("The channel_id must 0 or 1")
        
    def calculate_ac(self, pedal_input):
        '''! Calculate the AC Voltage given pedal input
        The function is used to get the AC Voltage from the pedal input given as deg
        @param - pedal input in deg
        @return - ac_voltage for the respective sensors
        '''
        if self.channel_id == 0:
            ac_voltage = 0.5 + (0.1 * pedal_input)
        else:
            ac_voltage = 1.0 + (0.08 * pedal_input)
            
        return ac_voltage
    
    def change_in_percentage(self, ac_voltage):
        '''! Converts the AC Voltage to pedal percentage
        The function converts the AC Voltage to pedal per-centage. Linear interpolation is done to get the pedal
        percentage for the given AC Voltage
        @param - ac_voltage as the input
        @return - pedal percentage 
        '''
        min_pedal_input = 0
        max_pedal_input = 30
        ac_voltage_max = self.calculate_ac(max_pedal_input)
        ac_voltage_min = self.calculate_ac(min_pedal_input)
        
        #Linear Interpolation to get the pedal percentage for any pedal input
        slope = (100 - 0)/(ac_voltage_max - ac_voltage_min)
        percentage_ac = slope * (ac_voltage - ac_voltage_min)
        
        return percentage_ac