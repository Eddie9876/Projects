#This is gonna be a program that is gonna calculate how much revenue you have made off of sellign clothes
#off of an app called depop, depending on how much you bought the clothes for and how much you are selling them 
#Including bundles when shipping is added to the total amount that you paid with the clothes that you paid for
#Overall this program is gonna deduct all of the things that you are paying for then give you how much you are earing


#Here is gonna be the input that you are gonna enter on how
bundle = input('Is this a bundle? ') 

#I put the whole program into a function in order to make it neater
def program(bundle): 
    #If th user says this is not a bundle it just goes throught this route
    if bundle == 'no' or bundle == 'n': 
        pass 
        #This is gonna be the two varibles "Item" and "fee"
        Item = float(input('How much was the item? '))
        fee = float(input('How much was the fee? '))
        #This is gonna be the asking what the original price of the item is 
        #In order to deduct that amount from how much the user is selling there clothing 
        #Item for
        ActualPrice = float(input('What was the Original Price of the item? '))
        #This is gonna be the calculation 
        Calculations = float(Item - fee) - ActualPrice 
        #Then prints out how much revenue you got from a singular item 
        print(f'Profit: ${Calculations:.2f}')
    #Elif statment if the user inputted for the bundle question then it goes through this route
    elif bundle == "y" or bundle == "yes":
        #We first set an empty list in order to put all of num of items are selling for
        #In this liss 
        bundle_price_list = []
        #We then ask for the amount of items that are we gonna have in our bundle
        bundle_num = int(input("How much are in the bundle? ")) 
        #We then create a for loop to let the use enter the items on how much each item costs
        for i in range(1, bundle_num + 1): 
            #It then asks how much the user sold it for
            bundle_price =  float(input("How much did you sell them for? ")) 
            #We then append that input that the user entered and then appened it or add it 
            #To the "bundle_price_list"
            bundle_price_list.append(bundle_price)
        #We then create another list in order to put the actual prices of the items in there
        Actual_Price_List = []  
        #Another for loop in order to let the user enter how much each item actually went for
        for c in range(1, bundle_num + 1): 
            #Asks the user what the actual price of the item is
            Actual_Price = float(input("How much did you buy each item for? "))
            #We then add it to the "Actual_Price_List" list
            Actual_Price_List.append(Actual_Price)
        #We then create a fee input because the app depop always does fees no matter if you are selling or buying
        fee = float(input("How much was the fee for the bundle? ")) 
        #Then we ask the user how much was the shipping, because with bundles the user always pays for shipping
        Shipping = float(input("How much was shipping? "))
        #This is where the final result goes in or how much revenue we actually made goes in this list
        formula_list = [] 
        #This for loop is the one that actually does the calculations 
        #The loop stops based on how many items there are
        for i in range (bundle_num):
            #this creates another list based on the "Actual_Price_List" and then we have a num of items in the list based
            #off the num of items there are in "bundle_num"
            List_up  = Actual_Price_List[i]
            #same scenario in this list too but it uses the "bundle_price_list" instead
            List_up2 = bundle_price_list[i]
            #this is gonna calculate the final revenue of each item in the two lists based off of how many items are in "bundle_num"
            formula = (List_up2 - List_up - fee/bundle_num - Shipping/bundle_num) 
            #In order to retrieve the final result or how much revenue there is we add that number to another list
            #Called "formula_list"
            formula_list.append(formula) 
        #This loop helps us output how much revenue from each item the user got
        for i, emp in enumerate(formula_list, start=1):
            #This helps us output it more neatly by putting a number next to it  
            print(f"Profit for item {i}: ${round(emp, 2)}")
#This is what calls the whole function in order for the program to work
program(bundle)