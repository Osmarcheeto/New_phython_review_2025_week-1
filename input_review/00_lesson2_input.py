# Goal: show how input works, type conversion, and basic math output.


# print("Welcome! We'll do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience


#name = input("what's your name? ")
#print(f"hi, {name}! Let's do some math.\n")
# is your output
# ask for your birthday
# ask for your favorite number
# ask for two numbers

# create output sentences using f-strings
#using these three input variables

print("Welcome, when is your birthday.\n")
birthday = input("when is your birthday? ")
print(f"Wow, {birthday}! thats a cool birthday.\n")
print("What is your favorite food now?\n")
food = input("What is your favorite food")
print(f"nice! {food} i also like that food.\n")
num1 = int(input("whats your 1st number?\n"))
num2 = int(input)









# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings