#normal

def add(a,b):
    return a + b

def(2,5)


#now keyword arguments

def add(a,b):
    return a + b

def(a=5,b=2)



#unpacking

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".formate(name, age, likes)
    return sentence

dictionay = {"name":"pavna","age":20,"likes":"python"}

about(**ditionary)





#packing
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".formate(key, value))


foo(huda = "female", ziyad = "male")
    
