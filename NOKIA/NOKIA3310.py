def phone_book():
    while True:
        print("\n--- PHONE BOOK ---")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add Name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign Tone")
        print("7. Send b'card")

        print("8. Options")
        print("9. Speed Dials")
        print("10. Voice Tags")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "8":
            phone_book_options()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)


def phone_book_options():
    while True:
        print("\n--- PHONE BOOK OPTIONS ---")
        print("1. Type of View")
        print("2. Memory Status")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)


def messages():
    while True:
        print("\n--- MESSAGES ---")
        print("1. Write Messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture Messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message Settings")
        print("8. Info Service")
        print("9. Voice Mailbox Number")
        print("10. Service Command editor")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "7":
            message_settings()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)


def message_settings():
    while True:
        print("\n--- MESSAGE SETTINGS ---")
        print("1. Set")
        print("2. Common")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":
            message_settings_set()
        elif choice == "2":
            message_settings_common()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


def message_settings_set():
    while True:
        print("\n--- MESSAGE SETTINGS (SET) ---")
        print("1. Message Centre Number")
        print("2. Messages Sent As")
        print("3. Message Validity")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Setting changed...")


def message_settings_common():
    while True:
        print("\n--- MESSAGE SETTINGS (COMMON) ---")
        print("1. Delivery Reports")
        print("2. Reply via Same Centre")
        print("3. Character Support")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Setting changed...")


def call_register():
    while True:
        print("\n--- CALL REGISTER ---")
        print("1. Missed Calls")
        print("2. Received Calls")
        print("3. Dialled Numbers")
        print("4. Erase Recent Call Lists")
        print("5. Show Call Duration")
        print("6. Show Call Costs")
        print("7. Call Cost Settings")
        print("8. Prepaid Credit")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "5":
            call_duration()
        elif choice == "6":
            call_costs()
        elif choice == "7":
            call_cost_settings()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)


def call_duration():
    while True:
        print("\n--- CALL DURATION ---")
        print("1. Last Call Duration")
        print("2. All Calls Duration")
        print("3. Received Calls Duration")
        print("4. Dialled Calls Duration")
        print("5. Clear Timers")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Showing duration...")


def call_costs():
    while True:
        print("\n--- CALL COSTS ---")
        print("1. Last Call Cost")
        print("2. All Calls Cost")
        print("3. Clear Counters")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Showing costs...")


def call_cost_settings():
    while True:
        print("\n--- CALL COST SETTINGS ---")
        print("1. Call Cost Limit")
        print("2. Show Costs In")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Setting updated...")





def tones():
    while True:
        print("\n--- TONES ---")
        print("1. Ringing Tone")
        print("2. Ringing Volume")
        print("3. Incoming Call Alert")
        print("4. Composer")
        print("5. Message Alert Tone")
        print("6. Keypad Tones")
        print("7. Warning and Game Tones")
        print("8. Vibrating Alert")
        print("9. Screen Saver")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Tone option selected...")


def settings():
    while True:
        print("\n--- SETTINGS ---")
        print("1. Call Settings")
        print("2. Phone Settings")
        print("3. Security Settings")
        print("4. Restore Factory Settings")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "1":
            call_settings()
        elif choice == "2":
            phone_settings()
        elif choice == "3":
            security_settings()
        if choice == "0":
            break
        else:
            print("Opening setting...")


def call_settings():
    while True:
        print("\n--- CALL SETTINGS ---")
        print("1. Automatic Redial")
        print("2. Speed Dialling")
        print("3. Call Waiting Options")
        print("4. Own Number Sending")
        print("5. Phone Line In Use")
        print("6. Automatic Answer")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Call Setting function selected...")


def phone_settings():
    while True:
        print("\n--- PHONE SETTINGS ---")
        print("1. Language")
        print("2. Cell Info Display")
        print("3. Welcome Note")
        print("4. Network Selection")
        print("5. Lights")
        print("6. Confirm SIM Service Actions")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Phone Settings function selected...")


def security_settings():
    while True:
        print("\n--- SECURITY SETTINGS ---")
        print("1. PIN Code Request")
        print("2. Call Barring Service")
        print("3. Fixed Dialling")
        print("4. Closed User Group")
        print("5. Phone Security")
        print("6. Change Access Codes")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Security Settings function selected...")


def extras():
    while True:
        print("\n--- EXTRAS ---")
        print("1. Call Divert")
        print("2. Games")
        print("3. Calculator")
        print("4. Reminders")

        print("5. Clock")
        print("6. Profiles")
        print("7. SIM Services")
        print("0. Back")

        choice = input("Select option: ")

        if choice == "5":
            clock_menu()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)


def clock_menu():
    while True:
        print("\n--- CLOCK ---")
        print("1. Alarm Clock")
        print("2. Clock Settings")
        print("3. Date Setting")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Auto Update Date & Time")
        print("0. Back")

        choice = input("Select option: ")
        if choice == "0":
            break
        else:
            print("Clock function selected...")


def main_menu():
    while True:
        print("\n=== NOKIA 3310 MENU ===")
        print("1. Phone Book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call Register")
        print("5. Tones")
        print("6. Settings")
        print("7. Call Divert")
        print("8. Games / Extras")
        print("9. Calculator")
        print("10. Reminders")
        print("11. Clock")
        print("12. Profiles")
        print("13. SIM Services")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            phone_book()
        elif choice == "2":
            messages()
        elif choice == "4":
            call_register()
        elif choice == "5":
            tones()
        elif choice == "6":
            settings()
        elif choice == "8":
            extras()
        elif choice == "11":
            clock_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Option not implemented yet.")


# Run the phone
main_menu()
