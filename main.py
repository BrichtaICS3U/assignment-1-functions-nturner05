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

x = int(input())
print('Enter x=1 for Celcius or x=2 for Fahrenheit:')
if x == 1:
    print(temperature1)
elif x == 2:
    print(temperature2)
else:
    print(0)

temperature1 = int(input('Enter your temperature in Farenheit:')
print(int(round(FtoC(temperature1))))
temperature2 = int(input('Enter your temperature in Celcius:')
print(int(round(CtoF(temperature2))))
