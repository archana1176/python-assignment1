#Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($) An example runs of the program: Please enter amount in pounds: XXX £ XXX are $ XXX

conversion_rate = 1.30
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars}")