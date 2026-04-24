mass = float(input("Enter water mass (kg): "))
initial_temoerature = float(input("Enter initial temperature: "))
final_temperature = float(input("Enter final temperature: "))

Q = mass * (final_temperture - initial_temperature) * 4184
print("Energy needed:", Q)
