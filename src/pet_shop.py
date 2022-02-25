# WRITE YOUR FUNCTIONS HERE

from gettext import find


def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash_difference):
    cash = list["admin"]["total_cash"]
    cash += cash_difference
    list["admin"]["total_cash"] = cash

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

def increase_pets_sold(list, number_of_new_pets_sold):
    new_value = list["admin"]["pets_sold"]
    new_value += number_of_new_pets_sold
    list["admin"]["pets_sold"] = new_value

def get_stock_count(list):
    return len(list["pets"])

def get_pets_by_breed(list, breed):
    breed_amount = []
    
    for pet in list["pets"]:
        if pet["breed"] == breed:
            breed_amount.append(pet["name"])

    return breed_amount

def find_pet_by_name(list, name):
    for pet in list["pets"]:
        if pet["name"] == name:
            return pet
    

# def find_pet_by_name(list, name):
    # found_pet = []
    # for pet in list["pets"]:
    #     if pet["name"] == name:
    #         found_pet.append(pet)
    #         return found_pet
    # found_pet.append({
    #     "name" : "Not Found",
    #     "pet_type" : "invalid",
    #     "breed" : "invalid",
    #     "price" : 0
    # }
    # )



def remove_pet_by_name(list, name):

    for index, pet in enumerate(list["pets"]):
        if pet["name"] == name:
            list["pets"].pop(index)

def add_pet_to_stock(list, newPet):
    list["pets"].append(newPet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_removed):
    cash = customer["cash"]
    cash -= cash_removed
    customer["cash"] = cash

def get_customer_pet_count(customer):
    pet_counter = 0
    for pet in customer["pets"]:
        pet_counter += 1
    return pet_counter

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    customers_cash = customer["cash"]
    pet_value = pet["price"]

    if customers_cash >= pet_value:
        return True
    else:
        return False

def add_to_pets_sold(list):
    list["admin"]["pets_sold"] += 1

def add_cash_to_shop(list, cash_added):
    list["admin"]["total_cash"] += cash_added

# Dont know how to link this to final failing test
def does_pet_exist_check(list,pet_name):
    exists = False
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            exists = True
    return exists


    
def sell_pet_to_customer(list, chosen_pet, customer):


    if customer_can_afford_pet(customer, chosen_pet) == True:
        remove_customer_cash(customer, chosen_pet["price"])
            
        
        add_to_pets_sold(list)
        add_pet_to_customer(customer, chosen_pet)
        add_cash_to_shop(list, chosen_pet["price"])

        for idx, pet in enumerate(list["pets"]):
            if pet == chosen_pet:
                list["pets"].pop(idx)
    