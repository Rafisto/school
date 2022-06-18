import numpy
from scipy.integrate import quad as integrate
import matplotlib.pyplot as plt
import math

simulation_time = 20
saturation_voltage = 15
R = 4 * 10 ** 6
C = 0.75 * 10 ** -6

precision = 100


def Vin(t): return -1 * t ** 2


def IntegrateVout(t):
    value = (-1 * 1 / (R * C) * integrate(Vin, 0, t)[0])
    return saturation_voltage if value > saturation_voltage else value

print(round(IntegrateVout(5),1))

values = [IntegrateVout(time/precision) for time in range(simulation_time*precision)]
plt.title(f'Vout(t) given R={R}Ohm C={C}F Vs=±{saturation_voltage}')
plt.plot([v/precision for v in range(simulation_time*precision)], values)
plt.show()
