class BikeShop:
    def __init__(self, stock):
        self.stock = stock
    def DisplayBike(self):
        print("Total Bike" , self.stock)
    def BikeForRent(self, quantity):
        if quantity <= 0:
            print("Please enter the value greater than 0!")
        elif quantity > self.stock:
            print("Please enter the value less than stock!")
            print("Total stock:" , self.stock)
        else:
            print("Total Price:" , quantity*100)
            self.stock = self.stock - quantity
            print("Total Bikes:" , self.stock)
            
while True:
    obj = BikeShop(100)
    userinput = int(input('''
                      1 Display Stock
                      2 Rent a Bike
                      3 Exit
                      '''))
    if userinput == 1:
        obj.DisplayBike()
    elif userinput == 2:
        want = int(input("Enter Quantity "))
        obj.BikeForRent(want)
    else:
        break
    