print("Welcome to my Python program!") #Welcom message
hours = input("How many hours did you study today? ") #Ask the user for how many hours they study
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} hours this week.") # Calculate weekly study hours
try: # Convert input to float, with error handling
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()