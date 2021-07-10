#Exercise8: Compound Interest
#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places


interst_rate=0.04

#input deposite amount
Deposite=int(input("Enter the deposite amount:"))

#Calculate amount in saving account

Amount_in_saving_account_after_one_year=Deposite+Deposite*interst_rate
Amount_in_saving_account_after_two_year=Amount_in_saving_account_after_one_year\
             +Amount_in_saving_account_after_one_year*interst_rate
Amount_in_saving_account_after_three_year=Amount_in_saving_account_after_two_year+\
             Amount_in_saving_account_after_two_year*interst_rate
             
print("Deposite amount:",round(Deposite,2))
print("Amount_in_saving_account_after_one_year:",round(Amount_in_saving_account_after_one_year,2))
print("Amount_in_saving_account_after_two_year:",round(Amount_in_saving_account_after_two_year,2))
print("Amount_in_saving_account_after_three_year:",round(Amount_in_saving_account_after_three_year,2))
    
#Can print something like this also
print("Amount_in_saving_account_after_one_year %.2f and  Amount_in_saving_account_after_two_year %.2f,\
Amount_in_saving_account_after_three_year %.2f" % (Amount_in_saving_account_after_one_year,\
Amount_in_saving_account_after_three_year , Amount_in_saving_account_after_three_year));
