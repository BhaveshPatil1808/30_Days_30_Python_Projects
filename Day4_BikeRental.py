class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def display_bike(self):
        print("Total Bikes:", self.stock)

    def rent_for_bike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero.")
        elif q > self.stock:
            print("Enter a value less than or equal to available stock.")
        else:
            print("Total Price:", q * 100)
            self.stock -= q
            print("Remaining Bikes:", self.stock)

# Instantiate the BikeShop object once
obj = BikeShop(100)

while True:
    try:
        uc = int(input('''
1 - Display Total Number of Bikes
2 - Rent a Bike
3 - Exit
Enter your choice: '''))
        
        if uc == 1:
            obj.display_bike()
        elif uc == 2:
            n = int(input("Enter number of bikes you want to rent: "))
            obj.rent_for_bike(n)
        elif uc == 3:
            print("Thank you for visiting the Bike Shop!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number.")
