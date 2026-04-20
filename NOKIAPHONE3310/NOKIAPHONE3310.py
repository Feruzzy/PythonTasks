import sys 


def get_choice(): 
    try: 
        return int(input("Enter choice: ")) 
    except: 
        print("Please enter a number") 

    return None 
def exit_program(): 
    print("Goodbye!") 
sys.exit() 



def Main_menu(): 
    while (true):
        print("\n Main Menu")
        print("1. Phone book\n 2. Messages\n 3. Chat\n end(" , ")") 
        print("4. Call register\n 5. Tones\n 6. Settings\n end(" , ")")
        print("7. Call divert\n 8. Games\n 9. Calculator\n end(" , ")")
        print("10. Remainder\n 11. Clock\n 12. Profile\n end(" , ")")
        print("13. SIM services^3\n 0. Exit end(" , ")")



print(Main_menu)

main_menu = input("Enter first selection: ")
    
#def Phone_book():
#    while (true):
#        Case "Phone-book"
#            print(1. Phone-book)
#            print("1. Search\n , 2. Service No\n , 3. Add name\n , 4. Erase\n , 5. Edit\n , 6. Assign tone\n , 7. Send b'card\n")
