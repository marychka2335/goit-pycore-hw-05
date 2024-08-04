from decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
            raise IndexError("Give me name and phone please.")
    name, phone = args
    if name in contacts:
        raise KeyError (f"The name {name} is already exists on your contacts list.")
    contacts[name] = phone
    return "Contact added."
    
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
             raise IndexError ("Error: Provide name and phone number.")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"The name {name} is not on your contacts list yet.")
    contacts[name] = phone
    return "Contact updated."
          

@input_error
def get_contact(args, contacts):
    if len(args) != 1:
             raise IndexError ("Error: Provide a name.")
    name = args[0]
    if name in contacts:
        raise KeyError (f"The name {name} is not on your contacts list yet.") 
    return contacts[name]
        
@input_error
def get_all_contacts(contacts):
    if not contacts:
        return "Your contact list is empty."  
    res = ""  
    for name, phone in contacts.items():
        res += f"{name}: {phone} \n"
        return res.rstrip("\n")  