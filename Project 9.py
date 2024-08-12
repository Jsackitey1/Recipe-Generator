# -*- coding: utf-8 -*-
"""
A program to write the recipe to a file based on the user's choice of the number of servings

@author: Sackitey Joseph
"""


def show_recipe(filename):
    
    """
    This program just displays the recipe from the base recipe to the user

    Parameters
    ----------
    filename : string
    The name of the file to be read from

    Returns
    -------
    None.

    """
    
    with open(filename, "r") as recipe:
        all_lines=[]
               
        try:
            for line in recipe:
                line = line.strip()
                
                if not line:
                    continue
                
                val = line.split()                   
                all_lines.append(val)

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        
        for line in all_lines:
            if 'Directions' in line:
                break
            sentence = ' '.join(line)
            print(sentence)
            print()
                
    
    return 


def display_recipe(filename,user_input=None):
    
    
    """
        reads the file and appends the numbers and the ingredients into seperates list
        
    Parameters
    ----------
    filename : string
        Nmae of file to be read from.
    user_input : int, optional
        User's prefered number of serving. The default is None.

    Returns
    -------
    numbers : list
        list of numbers from the base file.
    number_of_servings : int
        User's prefered number of serving.
 
    name_of_recipe : string
        Default name of the recipe,read from file.
    rest : list
        any other words apart from the numbers, read from file.
    dir_list : list
        list of the index of each line
    fraction_serving : float
        user preferd number of servings over standard number of servings
    user_input : int
        User's prefered number of serving. The default is None.

    """

    
    rest = []
    numbers = []
    dir_list = []

    while user_input== None:
        try:
            user_input = int(input("Please enter the number of serving you want: "))
        except ValueError:
            print("Invalid Entry; Try again")

        try:
            with open(filename, "r") as recipe:
                
                data = recipe.readlines()
                number_of_servings = int(data[1][0])
                name_of_recipe = data[0]
    
                for line in data[2:]:
                    word = line.split()
                    if not word:
                        break
                    number = word[0]
                    numbers.append(float(number))
                    the_rest = word[1:]
                    rest.append(the_rest)
    
                target_line = "Directions"
                for index, line in enumerate(data):
                    if target_line in line:
                        break
                for line in data[index:]:
                    dir_list.append(line)
    
                fraction_serving = user_input / number_of_servings
    
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
    
        return numbers, number_of_servings, name_of_recipe, rest, dir_list, fraction_serving,user_input


def calculate_serving(filename):
    
    
    """
    Calculates the amount of each ingredient based on the user's input

    Parameters
    ----------
    filename : stringg
        name of file to be read from.

    Returns
    -------
    numbers_1 : list
        calculated amount of each ingredient.
    numbers : list
        list of numbers from the base file.
    number_of_servings : int
        User's prefered number of serving.        
    name_of_recipe : string
        Default name of the recipe,read from file.
        
    rest : list
        any other words apart from the numbers, read from file.

    dir_list : list
        list of the index of each line
    fraction_serving : float
        user preferd number of servings over standard number of servings

    user_input : int
        User's prefered number of serving. The default is None.

    """
    numbers_1 = []
    numbers, number_of_servings, name_of_recipe, rest, dir_list, fraction_serving,user_input = display_recipe(filename)
    
    for i in numbers:
        i *= fraction_serving
        numbers_1.append(round(float(i), 1))
        
    return numbers_1,numbers, number_of_servings, name_of_recipe, rest, dir_list, fraction_serving,user_input



def write_recipe(filename, adjusted_filename):
    """
    

    Parameters
    ----------
    filename : string
        Name of file to be read from.
    adjusted_filename : string
        name of file to write to.

    Returns
    -------
    None.

    """
    show_recipe(filename)
    numbers_1,    numbers, number_of_servings, name_of_recipe, rest, dir_list, fraction_serving,user_input = calculate_serving(filename)
    
    rest_1 = []

    for w in rest:
        w_1 = "\t".join(w)
        rest_1.append(w_1)

    with open(adjusted_filename, "w") as my_doc:
        my_doc.write(name_of_recipe)
        number_of_servings= user_input
        my_doc.write(f"\n{number_of_servings}\tServings")

        for num, a in zip(numbers_1, rest_1):
            my_doc.write(f"\n{num} \t{a}")

        my_doc.write("\n")
        my_doc.write("\n")

        for item in dir_list:
            my_doc.write(item)


if __name__ == "__main__":
    write_recipe("base_recipe.txt", "adjusted_recipe.txt")
