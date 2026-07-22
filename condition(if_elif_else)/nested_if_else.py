# Nested if else
print("enter your height for ride")
height=int(input("enter height in cm ="))
if height <= 120:
    print( "wow, you are eligible for ride")
    age=int(input("enter your age="))
    if age<=3:
        print("Sorry, babies🐣 under three are not allowed on this ride.")
    elif age < 12:
        print("ride charge = 30💸")
    elif age < 16:
        print("ride charge = 40 💸")
    else:
        print("sorry, you are not eligible for this ride try another ride thank you") 
else:
    print( "sorry, you are not eligible for ride")
         