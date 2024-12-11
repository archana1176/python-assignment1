
# Printing name, student number, and email address
print("Archana")
print("ST104")
print("archana@gmail.com")

# Printing name, student number, and email address using escape sequences
print("Archana\nST104\narchana@gmail.com")


#Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.
a=14
b=7
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print(f"""addition= {addition}
subtraction={subtraction}
multiplication={multiplication}
division={division}""")

#Write Python code that displays the numbers from 1 to 5 as steps.
print("""1 
2
3
4
5""")

#Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen: An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".

print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")

#Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3

num = 23
textnum = "57"
decimal =98.3
print(type(num))
print(type(textnum))
print(type(decimal))
textnum_converted = int(textnum)
total_sum = num + textnum_converted + decimal

print(total_sum)
print(type(total_sum))
# calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

# Calculate the total number of minutes in a year
total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
print(f"There are {total_minutes_in_year} minutes in a year, given {days_in_year} days in a year, {hours_in_day} hours in a day, and {minutes_in_hour} minutes in an hour.")

#Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting

user_name = input("Please enter your name: ")
print(f"Hi {user_name}, welcome to Python programming")






