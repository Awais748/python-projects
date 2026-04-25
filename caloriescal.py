
class Food:

    def __init__(self, name, calories):
        self.name     = name
        self.calories = calories

    def display(self):
        print(f"  🍽️  {self.name} — {self.calories} cal")


class Tracker:

    def __init__(self):
        self.foods = []      
        self.goal  = 2000     

    def add_food(self, name, calories):
        food = Food(name, calories)
        self.foods.append(food)
        print(f"  ✅ {name} added!")

    def total_calories(self):
        return sum(f.calories for f in self.foods)

    def show_summary(self):
        print("\n=========================")
        print("    Calorie Summary")
        print("=========================")

        if not self.foods:
            print("  No food added yet!")
            return

        for food in self.foods:
            food.display()

        total     = self.total_calories()
        remaining = self.goal - total

        print(f"\n  Total    : {total} cal")
        print(f"  Goal     : {self.goal} cal")

        if remaining > 0:
            print(f"  Left     : {remaining} cal ")
        else:
            print(f"  Over by  : {abs(remaining)} cal ")

    def start(self):
        while True:
            print("\n=========================")
            print("    Calorie Counter")
            print("=========================")
            print("  1. Add food")
            print("  2. Show summary")
            print("  3. Exit")

            choice = input("\nChoose (1-3): ")

            if choice == "1":
                name     = input("Food name: ")
                calories = int(input("Calories: "))
                self.add_food(name, calories)

            elif choice == "2":
                self.show_summary()

            elif choice == "3":
                print("\nGoodbye! 👋")
                break

            else:
                print(" Invalid choice!")


t = Tracker()
t.start()