FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def main():
    temp = float(input('Enter the temperature to convert: '))
    try:
        num = float(temp)
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')
    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()
    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f'{temp}°C is {converted_temp}°F')
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f'{temp}°F is {converted_temp}°C')
    else:
        print('Invalid unit, Enter C for celsius or F for fahrenheit')
main()