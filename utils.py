"""! @brief Program for excecuting the low pass filter"""
##
# @file utils.py
#
# @brief Defines the function to implement low pass filter
#
# @section description_utils Description
# The function accepts the AC Voltage and window size and gives the filtered output
#
# @section libraries_utils Libraries/Modules
# - numpy 
#


import numpy as np

def low_pass_filter(ac_voltage, window_size):
    """! Implements the low pass filter
    A low pass filter with moving average is implemented for filtering the noisy voltages from the sensors.
    @param in : ac_voltage and window_size
    @return : Filtered ac_voltage
    """
    i = 0
    filtered_voltage = []
    while i < (len(ac_voltage)-window_size+1):
        #Gets the avg in the window and append it in the list
        current_window = ac_voltage[i : i + window_size]
        avg_window = sum(current_window) / window_size
        filtered_voltage.append(avg_window)
        i += 1
        
    return np.array(filtered_voltage)  