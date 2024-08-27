# function defination
# def fun():
#     print("HELLO")


# # function call
# fun()
# print("Tushar singh")
# fun()

# def great(name, thanku):
#     print(" Hello, " + name + thanku)

# great("Tusharsingh ", "thank")    
# great("Abhishek ", "thank")
# great("Shubham ", "thank")

# def great(name, thanku):
#     x= print(" Hello, " + name + thanku)
#     return 0 

# a = great("Tusharsingh ", "thank")    
# print(a)



def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n = int(input("Enter the value:-  "))
print(f"factorial is {fact(n)}")



# ()
