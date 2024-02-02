print("monal is clever girl")
print(20*24*60)
print("20 days are " + str(50) + "minutes")
print(f"20 days are {50} minutes")
print(f"20 days are {20*24*60} minutes")
print(f"30 days are {30*24*60} minutes")
print(f"20 days are {110*20*24*60} minutes")

calculation_to_units = 24
name_of_unit = "hours"

print(f"20 days are {20* calculation_to_units}{name_of_unit}")
print(f"20 days are {35* calculation_to_units}{name_of_unit}")
print(f"20 days are {110* calculation_to_units}{name_of_unit}")

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units()

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


days_to_units(35)

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_message)

def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)

scope_check(20)

calculation_to_units =24
name_of_unit ="hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


input()

calculation_to_units =24
name_of_unit ="hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


user_input = input("hey user, enter a number of days and i will convert it to hours!\n")


calculation_to_units =24
name_of_unit ="hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

user_input = input("hey user, enter a number of days and i will convert it to hours!\n")calculation_to_units = days_to_units(user_input)
user_input_number = int(user_input)
print(calculated_value)
