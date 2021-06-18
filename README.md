# Lightyear_InterviewCase
This repository is the interview case study for LightYear company. The requirement in this case is to estimate the requested torque based on the user input. This user input will be the throttle pedal angle.

## Required Packages
```bash
numpy (any version)
argparse (any version)
```

## Modules
**Error Function**  
Computes the error between the two sensors. The function returns the sensor id that performs well.  
**ADC Driver**  
Computes the AC Voltage corresponding to the sensor id based on the equation given in the question and converts it to pedal percentage.  
**Torque Converter**  
Computes the function that takes in the pedal percentage and converts it to the torque given the speed of the vehicles.  
**Low pass filter**  
Computer the low pass filter using a simple moving average.   

## Input pedal map
![Pedal map][Pedalmap.png]

## Outline of the excecution
![Block Diagram][Block_diagram.png]

## Usage

```python
python main.py -s <speed> -p <pedal_input>
```

## Example

```python
python main.py -s 40 -p 15 20 10
```

## Author
Karthik Arvind Arunmoli
