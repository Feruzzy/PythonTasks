total_min = int(input("Enter total minutes: "))

days = total_min // (24 * 60)
remaining_after_days = total_min % (24 * 60)

hours = remaining_after_days // 60
minutes = remaining_after_days % 60

print(days, "days,", hours, "hours, and", minutes, "minutes.")
print()
