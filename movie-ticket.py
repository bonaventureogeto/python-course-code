age = int(input("Enter your age: "))
show_time = int(input("Enter the show time (use 24hr Format): "))

if age > 18 and show_time <=22:
    print("You are allowed to watch R-rated movies")
elif age == 18 and show_time > 22:
    print("Past bed time!")
else:
    print("Sorry, you must be 18 and above to watch R-rated movies")
