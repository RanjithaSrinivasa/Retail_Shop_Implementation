# this program demonstrates simple online clothing website

Customer = []
Shoppingbag = []
Apparel = []

# dictionary stores clothing details such as name and it's price
Appareldict = {
    "Levis Jeans": 20,
    "Calvin klien jeans": 40,
    "Denim jeans": 25,
    "Forever21 dress": 15,
    "H&M dress": 10,
    "Zara dress": 20,
    "Levis t-shirt": 10,
    "Super dry t-shirt": 15,
    "Van Huessen formal shirt": 20,
    "Zara formal shirt": 20,
    "Zara top": 15,
    "H&M top": 10,
    "Raymond shirt": 20,
    "Gucci top": 50,
    "Armani pants": 60,
    "Burburry shoes": 80
}


# class for clothing website
class Clothingwebsite:

    # function to collect customer information
    def fillinfo(self):
        customercount = 0;
        # at a time shop can assist 5 customers
        while customercount < 5:
            customername = input("please input customer name: ");
            Customer.append(customername)
            apparelnumber = int(input("enter number of clothing needed: "))
            while (apparelnumber > 0):
                apparel_input = input("enter apparel to buy ");
                Apparel.append(apparel_input)
                apparelnumber = apparelnumber - 1
            customercount = customercount + 1
            print("\n")
        return list

    # function to take budget as input from user and display suitable output message
    def checkbudget(self):
        budget = int(input("enter budget(make sure it is above $10): "));
        # customer should shop for minimum 10$
        if (budget < 10):
            print("NO APPAREL FOR", budget, "$")
        elif (budget > 50):
            print("SHOPPING SPREE ONNNN")
        else:
            print("YOU ARE GOOD TO GO")
        print("\n")

    # function to display clothes on website along with it's price tag
    def appareldetails(self):
        print("APPARELS AVAILABLE ARE\n")
        for i, j in Appareldict.items():
            print(i, ":", j, "$")
        print("\n")

    # function to fill the shopping cart for each customer and displaying the bill
    def shoppingBag(self):
        totalbill = 0
        apparelnumber = int(input("enter number of clothing needed: "))
        while (apparelnumber > 0):
            apparel_input = input("enter apparel to buy: \n");
            if apparel_input in Appareldict:
                Shoppingbag.append(apparel_input)
                for i, j in Appareldict.items():
                    if i == apparel_input:
                        totalbill = totalbill + j
                apparelnumber = apparelnumber - 1
            else:
                print("SELECT VALID ITEMS FROM LIST")
            print("SELECTED ITEMS ARE:", Shoppingbag)
            print("BILL IS", totalbill, "$")

    # function to check if an apparel is present on the website
    def checkapparel(self, inp):
        # input taken is case sensitive
        if inp in Appareldict:
            print(inp, ": THE FOLLOWING ITEM IS AVAILABLE\n")
        else:
            print("ITEM IS NOT AVIALABLE")


if __name__ == "__main__":
    obj = Clothingwebsite()
    while True:
        # customer can choose from the below options
        print("***** OPTIONS *****")
        print("A for displaying apparels")
        print("B for budget")
        print("C to check if an item exists in store")
        print("F to fill in customer information")
        print("S for shoppingbag")
        print("E to exit the program")
        print("*******************\n")
        try:
            choice = input("please enter your option:\n")

            # to list the cloth details
            if choice == "A" or choice == "a":
                obj.appareldetails()

            # to check budget
            elif choice == "B" or choice == "b":
                obj.checkbudget()

            # to check if an item is present
            elif choice == "C" or choice == "c":
                apparel_in = input("Please enter the apparel to be checked: ")
                obj.checkapparel(apparel_in)

            # to get customer information
            elif choice == "F" or choice == "f":
                obj.fillinfo()

            # to display shopping bag and bill
            elif choice == "S" or choice == "s":
                obj.shoppingBag()

            # to exit the program
            elif choice == "E" or choice == "e":
                print("Thank you for visiting.\n")
        except:
            print("ENTER VALID OPTION\n")# retailshop_python_project
# retailshop_python_project
# Retail_Shop_Python_Project
