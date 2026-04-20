"""
prompt user to enter password
if password lenght is less than 8 its very weak

elif its 8 print weak 8

elif its between 8 & 16 strong

else above 16 very strong
"""


user_input = str(input("Enter password: "))



if len(user_input) < 8:
    print("very weak")

elif len(user_input ) == 8:
    print("weak")

elif len(user_input) >= 8 and len(user_input) <= 16:
    print("strong")

else:
      len(user_input) >= 16
      print("very strong")


