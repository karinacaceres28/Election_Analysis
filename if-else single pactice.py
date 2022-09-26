#declare temperature variable to an input function, wrap the int with an int() method
temperature = int(input("What is the temperature outside? "))

#create an if/else statement if temperature is greater than 80
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows.")

