'''
userName = input("Enter your name: ")
print("Hey " + userName)

userGrade = input ("What grade are you in?")
print("Hey " + userName + ", " + userGrade + " is a lame grade") 

userYear = int(input("What year were you born? "))
userAge = 2022 - userYear 
print (str(userAge) + " is so young!")
'''

# Create your own Madlibs
# Have at least 5 inputs 
userName = input("Enter your name: ")
userFavoriteWeapon = input("Enter your favorite weapon:")
userFavoriteFood = input("Enter your favorite food:")
userCelebrity = input("What is your favorite celebrity?:")
uservillain = input("What movie villain do you hate the most:")
userResturant = input("What is your favorite resturant?:")

print(userName + " finds out that his friend " + userCelebrity + " was kidnapped by " + uservillain + ". Sadness takes over " + userName + ", so he makes his way to his favorite resturant " + 
userResturant + " to get some " + userFavoriteFood + ". On his way he finds a " + userFavoriteWeapon + ". With this weapon he realizes he can save his friend " + userCelebrity + ". He goes to fight his nemesis " + uservillain + ". It was a very hard fight however but, " + userName + " wins and saves the day " ) 