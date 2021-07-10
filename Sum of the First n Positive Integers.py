#Exercise 7: Sum of the First n Positive Integers
#Write a program that reads a positive integer, n, from the user and then displays the
#sum of all of the integers from 1 to n. The sum of the first n positive integers can be
#computed using the formula:
#sum = (n)(n + 1)/2

#Input positive integer
positive_integer=int(input("Enter positive_integer:"))

#calculte n positive integer
sum=positive_integer * (positive_integer+1) / 2

#Display value
print("Sum of first n positive integer:",sum)
