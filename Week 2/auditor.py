inventory = 0
rejected_entries = 0 

user_input = ""
while user_input != "quit" :
    user_input = input("Enter a stock quantity or type 'quit' to exit: ")  
    if user_input == "quit":
        break 
    elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        quantity = int(user_input)
        if quantity >= 0: 
            inventory += quantity
            if inventory > 500: 
                print ("Overstock Alert!")
                break
        else: 
            rejected_entries += 1 
            print ("Error: Please enter a non-negative number or type 'quit' to exit ")
    else:
        rejected_entries += 1 
        print ("Error: Please enter a valid number or type 'quit' to exit ")

print("Total Units Processed: " + str(inventory) + " Number of Failed/Rejected Entries: " + str(rejected_entries)) 