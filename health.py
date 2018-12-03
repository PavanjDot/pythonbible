import random 


health = 50
print("Enter the Difficulty Level on the Scale of 1 to 3")
print("1 beaing Easy and 3 beaing Difficult") 
difficulty = int(input("ENTER HERE : "))

portion_helth = int(random.randint(25,50)/ difficulty )

health = health + portion_helth

print(health)
