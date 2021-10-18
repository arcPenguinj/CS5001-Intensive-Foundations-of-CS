'''
Fall2020
CS 5001 HW5
Yici Zhu
it's a program to enable user to read/write recipes
'''


def generate_valid_filename(recipe_name):
    '''
    function-- generate_valid_filename
    it's a function to check if filename is valid
    parameter:
    recipe_name - string
    return:
    filename + '.txt' if recipe_name is valid;
    or raise ValueError if not
    '''
    recipe_name = recipe_name.lower()
    recipe_name = recipe_name.strip()
    recipe_name = recipe_name.replace(" ", "_")
    new_name = ""
    special_ch = "_"
    for c in recipe_name:
        if c.isnumeric() or c.isalpha() or c == special_ch:
            new_name += c
    if len(new_name) == 0:
        raise ValueError
    return new_name + ".txt"


def validate_user_input_menu(input):
    '''
    function-- validate_user_input_menu
    it's a function to check if user input is 1,2,3
    parameter:
    input - string
    return:
    1,2,3 as int if user input is valid;
    or raise ValueError if not
    '''
    input_int = int(input)
    if input_int < 1 or input_int > 3:
        raise ValueError
    return input_int


def val_userin_ingredient(input):
    '''
    function-- val_userin_ingredient
    it's a function to check if user input ingredient
    is valid
    parameter:
    input - string
    return:
    a list containing ingredients if input is valid;
    or raise ValueError if there's no valid ingredient;
    '''
    ret = []
    ingredients = input.split(',')
    for ingredient in ingredients:
        ingredient = ingredient.strip()
        if len(ingredient) > 0:
            ret.append(ingredient)
    if len(ret) == 0:
        raise ValueError
    return ret


def validate_user_input_time(input):
    '''
    function-- validate_user_input_time
    it's a function to check if user input time is valid
    parameter:
    input - string
    return:
    time as int if user input is a number and greater than 0;
    raise ValueError otherwise
    '''
    input_int = int(input)
    if input_int < 0:
        raise ValueError
    return input_int


def main():
    while True:
        try:
            user_in = input("MENU: 1 - Save a new recipe, 2 - Read a recipe, "
                            "3 - Quit ")
            user_in = validate_user_input_menu(user_in)
            if user_in == 1:
                ingredients_is_valid = False
                while ingredients_is_valid is False:
                    try:
                        ingredients_input = input("Enter the ingredients on "
                                                  "one line. Separate each "
                                                  "ingredient with a comma. ")
                        ingredients = val_userin_ingredient(ingredients_input)
                        ingredients_is_valid = True
                    except ValueError:
                        print("Recipe must have at least one ingredient.")
                direction = input("Enter the directions (1 paragraph only): ")
                time_is_valid = False
                while time_is_valid is False:
                    try:
                        time_input = input("Enter the time "
                                           "needed in minutes: ")
                        time = validate_user_input_time(time_input)
                        time_is_valid = True
                    except ValueError:
                        print("Invalid time. Must be an integer "
                              "greater than or equal to 0.")
                recipe_name = input("Enter a name for the recipe: ")

                # start process the file
                filename_is_valid = False
                filename_raw = recipe_name
                while filename_is_valid is False:
                    try:
                        filename = generate_valid_filename(filename_raw)
                        with open(filename, 'w') as file:
                            file.write(recipe_name + '\n\n')
                            file.write("Ingredients:\n")
                            for ingre in ingredients:
                                file.write(ingre + '\n')
                            file.write('\n')
                            file.write("Time: " + str(time) + " minutes\n\n")
                            file.write("Directions:\n")
                            file.write(direction)
                        filename_is_valid = True
                    except ValueError:
                        print("Unable to create the filename.")
                        filename_raw = input("Enter a string containing only "
                                             "letters, numbers, and spaces ")
                print(recipe_name + " recipe saved to " + filename)

            elif user_in == 2:
                reading_recipe = input("Enter the name of the recipe: ")
                reading_file_name = generate_valid_filename(reading_recipe)
                try:
                    with open(reading_file_name, "r") as file:
                        printoutstr = ""
                        for line in file:
                            printoutstr += line
                        print(printoutstr)
                except (ValueError, FileNotFoundError):
                    print("Unable to read " + reading_file_name)
            elif user_in == 3:
                break
        except ValueError:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
