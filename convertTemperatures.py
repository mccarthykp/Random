# celsius to fahrenheit
# (C × 9/5) + 32 = F
celsiusDegrees = 20

def celsiusToFahrenheit(degrees):
    result = (str((degrees*(9/5) + 32)) + " degrees fahrenheit.")
    return result

print(celsiusToFahrenheit(celsiusDegrees))

#fahrenheit to celsius
# (F − 32) × 5/9 = C
fahrenheitDegrees = 68

def fahrenheitToCelsius(degrees):
    result = (str((degrees - 32) * (5/9)) + " degrees celsius.")
    return result

print(fahrenheitToCelsius(fahrenheitDegrees))