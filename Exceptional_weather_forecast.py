# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
#fahrenheit = int(input("Please enter the temperature in Fahrenheit "))

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
#Remember that the formula is (Fahrenheit - 32) * 5/9.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?
try:
    fahrenheit = float(input("Please enter the temperature in Fahrenheit "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} is converted to {celsius}")
except ValueError:
    print("That's not a valid number. Please try again")
else:
    print("Congratulations you have converted Fahrenheit to Celsius")
finally:
    print("Thanks for using my application!")

# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

# I was hoping this would work I did it step by step then I went ahead and cleaned up my code. Is this allowed? 