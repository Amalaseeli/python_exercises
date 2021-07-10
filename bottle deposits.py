#Exercise 5: Bottle Deposits
#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places


less_deposit=0.1
more_deposit=0.25

#input containers one or less
less_container=int(input("Enter number of containers which is one or \
less than one liter:"))

#input containers one or more
more_container=int(input("Enter number of containers which is one or \
more than one liter:"))

#calculate refund
refund=less_deposit*less_container + more_deposit* more_container

#Display refund
print("Number of containers which is one or\
less than one liter:",less_container)
print("Number of containers which is one or\
more than one liter:",more_container)
print("Refund: $%.2f " % refund )



 

