
class Person:

    def __init__(self, name, weight, height):
        self.name   = name    
        self.weight = weight 
        self.height = height 


class BMI:

    def __init__(self, person):
        self.person = person

    def calculate(self):
        bmi = self.person.weight / (self.person.height ** 2)
        return round(bmi, 2)

    def category(self):
        bmi = self.calculate()
        if bmi < 18.5:
            return "Underweight "
        elif bmi < 25:
            return "Normal "
        elif bmi < 30:
            return "Overweight "
        else:
            return "Obese "

    def show_result(self):
        print("\n=========================")
        print("   🧮 BMI Result")
        print("=========================")
        print(f"  Name     : {self.person.name}")
        print(f"  Weight   : {self.person.weight} kg")
        print(f"  Height   : {self.person.height} m")
        print(f"  BMI      : {self.calculate()}")
        print(f"  Category : {self.category()}")
        print("=========================")


# RUN
print("\n=========================")
print("   BMI Calculator")
print("=========================")

name   = input("Enter your name: ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

person = Person(name, weight, height)
bmi    = BMI(person)
bmi.show_result()