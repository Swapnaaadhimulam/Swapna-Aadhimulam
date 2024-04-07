import math

def newtons_law_of_cooling(T, T_ambient, k, dt):
    """
    Calculate the temperature after a given time using Newton's law of cooling.

    Parameters:
        T (float): Initial temperature of the object.
        T_ambient (float): Ambient temperature.
        k (float): Cooling constant.
        dt (float): Time interval.

    Returns:
        float: The temperature after the given time interval.
    """
    return T_ambient + (T - T_ambient) * math.exp(-k * dt)

# Example usage
initial_temp = 100.0  # initial temperature of the object
ambient_temp = 25.0   # ambient temperature
cooling_constant = 0.1  # cooling constant
time_interval = 10.0   # time interval in seconds

result = newtons_law_of_cooling(initial_temp, ambient_temp, cooling_constant, time_interval)
print("Temperature after {} seconds: {:.2f}".format(time_interval, result))
