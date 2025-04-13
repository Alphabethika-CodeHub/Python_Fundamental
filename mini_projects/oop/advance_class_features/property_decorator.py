class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius # Protected Attribute

    @property
    def celsius(self):
        # Getter Untuk Celsius
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        # Setter Untuk Celsius Dengan Validasi
        if value < -273.15:
            raise ValueError("Temperature tidak boleh dibawah -273.15")
        self._celsius = value

    @property
    def fahrenheit(self):
        # Property Terhitung (Computed Property)
        return (self._celsius * 9/5) + 32


# Penggunaan (Usage)
temp = Temperature(35)
print(temp.celsius)
print(temp.fahrenheit)

temp.celsius = 40
print(temp.fahrenheit)

try:
    temp.celsius = -400
except ValueError as e:
    print(e)