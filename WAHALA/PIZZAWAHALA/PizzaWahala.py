def pizza_calculator():
    print("WELCOME TO IYA ARAMIDE PIZZA JOINT ILUPEJU-@SEMICOLON")
    print("\nPIZZA TYPE\t" + "NUMBER OF SLICES\t" + "PRICE PER BOX\t")
    print("SAPA SIZE\t" + "4\t\t" + "2,500")
    print("SMALL MONEY\t" + "6\t\t" + "2,900")
    print("BIG BOYS\t" + "8\t\t" + "4,000")
    print("ODOGWU\t\t" + "12\t\t" + "5,200")
   
    
    choice = input("\nSelect option (e.g., SAPA SIZE): ").upper().strip()
    try:
        number_of_people = int(input("How many people are eating? "))
    except ValueError:
        print("Please enter a valid number for people.")
        return

    
    slices_per_box = 0
    price_per_box = 0

    
    if choice == "SAPA SIZE":
        slices_per_box = 4
        price_per_box = 2500
    elif choice == "SMALL MONEY":
        slices_per_box = 6
        price_per_box = 2900
    elif choice == "BIG BOYS":
        slices_per_box = 8
        price_per_box = 4000
    elif choice == "ODOGWU":
        slices_per_box = 12
        price_per_box = 5200
    else:
        print("Invalid choice!")
        return

    
    
    total_slices_accumulated = 0
    number_of_boxes = 0
   
    while total_slices_accumulated < number_of_people:
        number_of_boxes += 1
        total_slices_accumulated += slices_per_box

    
    left_slices = total_slices_accumulated - number_of_people
    total_price = number_of_boxes * price_per_box

    
    print("-" * 40)
    print(f"NUMBER OF BOXES TO BUY: {number_of_boxes}")
    print(f"NUMBER OF LEFT SLICES AFTER SERVING: {left_slices}")
    print(f"TOTAL PRICE: #{total_price:,}")
    print("-" * 40)

if __name__ == "__main__":
    pizza_calculator()
