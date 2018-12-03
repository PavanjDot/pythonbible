# Ask User Name

name = input("Enter You'r Name here:")

#Ask user for the Age

Age = input("Enter you'r Age here:")

#Ask user for City

city = input("Enter you'r City here:")

#Ask user what they Enjoy

Enjoy = input("Write Here:")


#create output

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, Age, city, Enjoy)


#print output

print(output)
