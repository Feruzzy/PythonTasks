years = int(input("Enter number of years: "))

population = 312032486
birth_rate = 7
death_rate = 13
immigrant_rate = 45

seconds_per_year = 365 * 24 * 60 * 60

for _ in range(years):
    population += (seconds_per_year // birth_rate)
    population -= (seconds_per_year // death_rate)
    population += (seconds_per_year // immigrant_rate)

print("Population after", years, "years:", population)
