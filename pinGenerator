import random

class PIN:

    def __init__(self, length):
        self.length = length

    def generate(self):
        pin = ""
        for i in range(self.length):
            pin += str(random.randint(0, 9))
        return pin


class Generator:

    def start(self):
        print("\n=========================")
        print("   🔐 PIN Generator")
        print("=========================")
        print("  1. 4 digit PIN")
        print("  2. 6 digit PIN")
        print("  3. 8 digit PIN")

        choice = input("\nChoose (1-3): ")

        if choice == "1":
            pin = PIN(4)
        elif choice == "2":
            pin = PIN(6)
        elif choice == "3":
            pin = PIN(8)
        else:
            print(" Invalid choice!")
            return

        print(f"\n   Your PIN: {pin.generate()}")


g = Generator()
g.start()