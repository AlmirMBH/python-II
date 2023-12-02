try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:  "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Division by zero not allowed! " + str(e).capitalize())
except ValueError as e:
    print("Only integers allowed! " + str(e).capitalize())
except Exception as e:
    print("Something went wrong: " + str(e).capitalize())
else:
    print(result)  # print result only if no exceptions
finally:
    print("Finally is always executed. A good idea to use, if opening connections or files to close them.")
