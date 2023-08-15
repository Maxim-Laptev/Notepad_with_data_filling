#A notepad where the user can write down their personal data so as not to forget or have quick access to them.

fName=input("Enter your first name (required): ")

while fName=="" or fName==" ":
    fName=input("Enter your name (required): ")
fName=fName.capitalize()

sName=input("Enter your second name (not required): ")
sName=sName.capitalize()

pNumber=input("Enter your phone number (minimum of 5 characters, without spaces): ")
while pNumber.count(" ")>0 or len(pNumber)<5:
    pNumber=input("Enter your phone number (minimum of 5 characters, without spaces): ")

password=input("Enter a password to protect your data (the password must contain 8 or more characters): ")
while len(password)<8 or password.count(" ")>0:
    password=input("Password must contain 8 or more characters, without spaces: ")

address=input("Enter your address in this format - city,address,house number or city, address, house number: ")
while address.count(" ")>2 or address.count(",")<2:
    address=input("Enter your address in this format - city,address,house number or city, address, house number: ")

if address.count(" ")==2:
    listAddress=address.split(", ")
else:
    listAddress=address.split(",")
del address

dictUser={
    "first name":fName,
    "second name":sName,
    password:{
        "phone number":pNumber,
        "address":listAddress
    }
}

question=input("Your data is saved, what data do you need now? (first name, second name, phone number, address, all data) ")

if question=="first name" or question=="First name":
    print(dictUser["first name"],end=".")

elif question=="second name" or question=="Second name":
    print(dictUser["second name"],end=".")

elif question=="phone number" or question=="Phone number":
    userPassword=input("Enter your password: ")
    while userPassword!=password:
        print("Wrong password")
        userPassword=input("Enter your password: ")
    print(dictUser[userPassword]["phone number"],end=".")

elif question=="address" or question=="Address":
    userPassword=input("Enter your password: ")
    while userPassword!=password:
        print("Wrong password")
        userPassword=input("Enter your password: ")
    print(dictUser[userPassword]["address"],end=".")

elif question=="all data" or question=="All data":
    userPassword=input("Enter your password: ")
    while userPassword!=password:
        print("Wrong password")
        userPassword=input("Enter your password: ")
    print("First name -",dictUser["first name"],", second name -",dictUser["second name"],", phone number -",dictUser[userPassword]["phone number"],", address -",dictUser[userPassword]["address"],end=".")
else:
    print("Incorrect input.")
