class TemperatureConversion:
    def __init__(self, temp):
        self.__temp = temp


class CelsiustoFahrenheit(TemperatureConversion):
    def conversion(self):
        return (self._TemperatureConversion__temp * (9 / 5)) + 32


class CelciustoKelvin(TemperatureConversion):
    def conversion(self):
        return self._TemperatureConversion__temp + 273.15


class FahrenheittoCelsius(TemperatureConversion):
    def conversion(self):
        return (self._TemperatureConversion__temp - 32) * (5 / 9)


class KelvintoCelsius(TemperatureConversion):
    def conversion(self):
        return self._TemperatureConversion__temp - 273.15


tempInCelsius = float(input("Enter the temperature in Celsius: "))
convert = CelciustoKelvin(tempInCelsius)
print(str(convert.conversion()) + "Kelvin")
convert = CelsiustoFahrenheit(tempInCelsius)
print(str(convert.conversion()) + " Fahrenheit")

tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
convert = FahrenheittoCelsius(tempInFahrenheit)
print(str(convert.conversion()) + "Celsius")

tempInKelvin = float(input("Enter the temperature in Kelvin: "))
convert = KelvintoCelsius(tempInKelvin)
print(str(convert.conversion()) + "Celsius")
