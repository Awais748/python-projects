

class Currency:
    def __init__(self, amount):
        self.amount = amount

    def usd(self):
       return round(self.amount * 0.0036, 2) 

    def euro(self):
      return round(self.amount * 0.0033, 2)

    def pkr(self):
      return round(self.amount * 278.5, 2) 
    

class Converter:
    
    def start(self):
        print("\n=========================")
        print("    Currency Converter")
        print("=========================")
        print("  1. PKR to USD")
        print("  2. PKR to EUR")
        print("  3. USD to PKR")
        print("  4. EUR to PKR")

        choice = input("\nChoose (1-4): ")
        amount = float(input("Enter amount: "))
        c = Currency(amount)

        if choice == "1":
            print(f"\n  PKR {amount} = USD {c.usd()}")
        elif choice == "2":
            print(f"\n  PKR {amount} = EUR {c.euro()}")
        elif choice == "3":
            print(f"\n  USD {amount} = PKR {c.pkr()}")
        elif choice == "4":
            pkr = round(amount * 300.2, 2)      
            print(f"\n  EUR {amount} = PKR {pkr}")
        else:
            print(" Invalid choice!")


c = Converter()
c.start()   



