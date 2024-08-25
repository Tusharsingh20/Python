dict = {
    "name" : "Tushar singh",
    2 : "MCA",
    4 : "Delhi",
    "visit" : 10
}


print(dict.items())
print(dict.keys())
print(dict.values())
dict.update({2 :"bca"})
print(dict)

print(dict.get("tushar"))   #print none if vaule doesn't exist
# print(dict["tushar"])    # print error