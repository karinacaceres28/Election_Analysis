#What is the score?
score = int(int("What is your tested score? "))

#determine the grade ((INCORRECT))
#if score >= 90:
   # print("Your grade is an A.")
#else:
   # if score >= 80:
        #print("Yout grade is a B")
       # else:
            #if score >= 70:
                #print("Your grade is a C.")
                #else:
                   # if score >= 60:
                       # print("Your grade is a C.")
                        #else:
                            #print("Your grade is an F")
#code above does not work due to being an if-elif-else.
#the if-elif-else are not to be indented, rather only the conditions

#determine the grade ((CORRECT WAY!!!))
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    