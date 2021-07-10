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
