# Assignment 1
# ICS3U
# <Noah Turner>
# March 28, 2018

def CtoF (C):
    """to convert the given number from celsius into fahrenheit"""
    F = (1.8)*C+32
    return F
def FtoC(F):
    """to convert the given number from fahrenheit to celcius"""
    C = (0.55556)*(F-32)
    return C
print('Enter 1 for Celcius to Fahrenheit or 2 for Fahrenheit to Celcius:')

x = int(input())
if x == 1:
    temperature1 = int(input('Enter your temperature in Celcius:'))
    if temperature1 < -273.15:
        print('Invalid Temperature')
        SystemExit
    else:
              print(int(round(CtoF(temperature1))))
elif x == 2:
    temperature2 = int(input('Enter your temperature in Farenheit:'))
    if temperature2 < -459.67:
        print('Invalid Temperature')
        SystemExit
    else:
              print(int(round(FtoC(temperature2))))
else:
              print('Error')

