# word = {
#     "help" : "madade",
#     "cry" : "rona",
#     "shout" : "chilana"
# }
# words= input("Enter your word:-  ")
# print(word[words])


# dict={}

# name= input("Enter the name:- ")
# lang=input("Enter the langugae:- ")
# dict.update({name : lang})
# name= input("Enter the name:- ")
# lang=input("Enter the langugae:- ")
# dict.update({name : lang})
# name= input("Enter the name:-")
# lang=input("Enter the langugae:-")
# dict.update({name : lang})
# name= input("Enter the name:- ")
# lang=input("Enter the langugae:- ")
# dict.update({name : lang})
# print(dict)






# s =set()

# x= input("Enter the Numbes:- ")
# s.add(int(x))
# q= input("Enter the Numbes:- ")
# s.add(int(q))
# w= input("Enter the Numbes:- ")
# s.add(int(w))
# e= input("Enter the Numbes:- ")
# s.add(int(e))
# r= input("Enter the Numbes:- ")
# s.add(int(r))
# t= input("Enter the Numbes:- ")
# s.add(int(t))
# y= input("Enter the Numbes:- ")
# s.add(int(y))
# u= input("Enter the Numbes:- ")
# s.add(int(u))
# print(s)



# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))



# s = {}
# print(type(s))





# n=12
# # for i in range(1,10+1):
# #     print(n*i)

# i=1
# while(i<11):
#     print(n*i)
#     i+=1  
  
    
    
    
# x = ["tushar", "tanishk", "krishna", "sahil", "shan"]
# for i in x:
#     if(i.startswith("t")):
#         print(f"hello {i}")
        
        

# n= int(input("Enter the number: -"))
# i=0
# sum=0
# while (i<n):
#     sum+=i
#     i+=1
# print(sum)



# n= int(input("Enter the number: -"))
# x=1
# for i in range(1,n+1):
#     x*=i
# print(x)

# def greatnum(x,y,z):
#     if (x>y and x>z):
#         print("X is greater")
#     elif (y>x and y>z):
#         print("y is greater")
#     else:
#         print(" Z is greater")
#     return 0

# a= int(input("Enter the value of  the X:- "))
# b= int(input("Enter the value of  the Y:- "))
# c= int(input("Enter the value of  the Z:- "))
# greatnum(a,b,c)


# def temp(x):
#     f=(9/5*x)+32
#     print(f)
#     return 0

# a= int(input("Enter the value of  the X:- "))
# temp(a)

# def temp():
#     print("HELLO MR TUSHAR SINGH \n ")
#     return 0
# temp()
# print("Thank u")

# def sumnumb(x):
#     if(x==1):
#         return 1
#     return sumnumb(x-1) + x
# a= int(input("Enter the value of  the X:- "))
# print(sumnumb(a))


def pattern(x):
    for i in range(x,0,-1):
        for j in range(i):
            print(" * ", end=" ")
        print("") 
    return 0
a= int(input("Enter the value of  the X:- "))
print(pattern(a))


