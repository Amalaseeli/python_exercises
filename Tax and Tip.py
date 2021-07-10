#Exercise 6: Tax and Tip

#The program that you create for this exercise will begin by reading the cost of a meal
#ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for
#the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places


tax_rate=0.05
tip_rate=0.18

#Read cost of the meal
cost=float(input("Enter the prize of the meal:"))

#Count tax_amount
tax_amount=tax_rate*cost

#Count tip_amount
tip_amount=tip_rate*cost

#Clacute grand total
grand_total=cost+tax_amount+tip_amount

#Display
print("Tax amount:",tax_amount)
print("Tip_amount:",tip_amount)
print("Grand total:", grand_total ,"Rupee")
