print("=" * 50)
print("    PHONEBOOK / WORD FREQUENCY COUNTER APP")
print("=" * 50)
phonebook = {}      
word_freq = {}     
while True:
    print("\n----- MAIN MENU -----")
    print("1. Add Contact (Phonebook)")
    print("2. Search Contact (Phonebook)")
    print("3. Display All Contacts (Phonebook)")
    print("4. Delete Contact (Phonebook)")
    print("5. Analyze Word Frequency (enter a paragraph)")
    print("6. Display Word Frequency Results")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ").strip()
    if choice == "1":
        name = input("Enter contact name: ").strip()
        if name in phonebook:                       
            print(f"'{name}' already exists with number {phonebook[name]}.")
            print("Use delete + add again if you want to change it.\n")
        else:
            number = input("Enter contact number: ").strip()
            phonebook[name] = number               
            print(f"Contact '{name}' added successfully.\n")
    elif choice == "2":
        name = input("Enter name to search: ").strip()
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}\n")
        else:
            print(f"'{name}' not found in phonebook.\n")
    elif choice == "3":
        if len(phonebook) == 0:
            print("Phonebook is empty.\n")
        else:
            print("\n{:<20} {:<15}".format("Name", "Contact Number"))
            print("-" * 35)
            for name in phonebook:             
                print("{:<20} {:<15}".format(name, phonebook[name]))
            print()
    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in phonebook:
            del phonebook[name]                  
            print(f"Contact '{name}' deleted successfully.\n")
        else:
            print(f"'{name}' not found in phonebook.\n")
    elif choice == "5":
        paragraph = input("Enter a paragraph to analyze: ").strip()
        paragraph = paragraph.lower()               
        for symbol in ".,!?;:\"'()":
            paragraph = paragraph.replace(symbol, "")
        words = paragraph.split()        
        word_freq = {}                         
        for word in words:                 
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1   
            else:
                word_freq[word] = 1                 
        print("Word frequency analysis complete. Use option 6 to view results.\n")
    elif choice == "6":
        if len(word_freq) == 0:
            print("No word frequency data yet. Use option 5 first.\n")
        else:
            print("\n{:<20} {:<10}".format("Word", "Count"))
            print("-" * 30)
            for word in word_freq:                
                print("{:<20} {:<10}".format(word, word_freq[word]))
            most_common_word = max(
                word_freq,
                key=word_freq.get
            )                                    
            print(
                f"\nMost frequent word: '{most_common_word}' - "
                f"{word_freq[most_common_word]} times\n"
            )
    elif choice == "7":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")
