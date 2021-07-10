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



 

