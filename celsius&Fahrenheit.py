# temperature_converter.py

class Temperature:

    def __init__(self, value):
        self.value = value

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32

    def to_celsius(self):
        return (self.value - 32) * 5/9


class Converter:

    def convert(self):
        print("\n  1. Celsius to Fahrenheit")
        print("  2. Fahrenheit to Celsius")

        choice = input("\nChoose (1-2): ")

        value = float(input("Enter temperature: "))
        temp  = Temperature(value)

        if choice == "1":
            print(f"\n  Result: {value}°C = {round(temp.to_fahrenheit(), 2)}°F")
        elif choice == "2":
            print(f"\n  Result: {value}°F = {round(temp.to_celsius(), 2)}°C")
        else:
            print(" Invalid choice!")


c = Converter()
c.convert()