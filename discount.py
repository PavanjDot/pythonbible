
while True:
    

    amount = int(input("Enter the Bill Amount: "))





    if amount >=500:
        discount =0
        discount = amount * 0.25
        final_price = amount - discount
        print("You are totall Bill is", final_price)
        print()
        print("Thank you")

    else:
        print("Sorry you wont get the 25% discount, to get this please make bill of 500rs or greater")
