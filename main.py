"""! @brief The main program for excecuting the interview case"""
##
# @mainpage Interview Case Project
#
# @section description_main Description
# This case is a part of the Lightyear recruitment process. The aim of this case is to implement a 
# torque estimator, that take in the pedal input (given in degress) and convert it into Torque that should be given by the motor.
# For this, various sensors and converters are used, that are implemented in this case.
# ![Block Diagram](Block_diagram.png)
#
# @section notes_main Notes
# - In order to implement the torque converter, excecute "main.py" with parameters -s/--speed and -p/--pedal_input
# - The pedal input could be a collection of values, and could be entered with a space between each values
#
#
# @section author_main Author
# - Created by Karthik Arvind Arunmoli on 06/18/2021.





import numpy as np
import argparse
from Modules import error_led, adc_drivers, torque_pedalangleper_speed
from utils import low_pass_filter

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Torque Prediction from Pedal Inputs')
    parser.add_argument('-s', '--speed', type=int, metavar='', required=True, default=50, help='Given the speed sensor as the input')
    parser.add_argument('-p', '--pedal_input', type=int, nargs='+', metavar='', required=True, help='Given the pedal input in degrees (max of 30 degress)')
    args = parser.parse_args()

    #Converting pedal input to numpy array
    pedal_input = np.array(args.pedal_input)
    if args.speed > 50:
        speed = np.clip(args.speed, 0, 50) #Clipping the speed to 50km/hr
    else:
        speed = args.speed

    #Initialising all the class
    error = error_led()
    torque = torque_pedalangleper_speed()
    #Initialising the sensors
    sensor0 = adc_drivers(0)
    sensor1 = adc_drivers(1)

    #Converting the AC Voltage to pedal input
    ac_voltage_0 = sensor0.calculate_ac(pedal_input)
    ac_voltage_1 = sensor1.calculate_ac(pedal_input)

    #Calculating the sensor error
    sensor_id = error.error_calculation(ac_voltage_0, ac_voltage_1)

    #Taking only the senor that is good (without errors)
    if sensor_id == sensor0.channel_id:
        ac_voltage_filtered = low_pass_filter(ac_voltage_0, 1)
        per_ac = sensor0.change_in_percentage(ac_voltage_filtered)
    else:
        ac_voltage_filtered = low_pass_filter(ac_voltage_1, 1)
        per_ac = sensor1.change_in_percentage(ac_voltage_filtered)

    #Getting the torque for the ac voltage
    interpolated_torque = torque.interpolation_function(per_ac, speed)

    print("The torque for the requested pedal input are {}".format(interpolated_torque))