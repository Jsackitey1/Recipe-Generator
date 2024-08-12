# -*- coding: utf-8 -*-
"""
A program to write the recipe to a file based on the users 
choice of the number of servings


@author: Sackitey Joseph
"""


def display_recipe(filename):
    
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
                
    
    return all_lines



def calculate_servings(filename,servings=None):
    
    n_list = display_recipe(filename)
    servings_per_ingredient=[]
    rem_list=[]
    
    while servings==None:
        
        try:
            servings = int(input("\nPlease enter the number of servings you want: "))
            
            fraction = servings / float(n_list[1][0])
            
            # Calculate servings for each ingredient
            for ingredient in n_list[2:]:
                if not ingredient:
                    break
                servings_per_ingredient = fraction * float(ingredient[0])
                
                for index, line in enumerate(n_list):
                    # Check if the target line is in the current line
                    if 'Directions' in line:
                        break  # Stop iterating once the line is found
                #looping ffom the index of the targetted line
                for line in n_list[index:]:
                    #appending them into a list
                    rem_list.append(line)
        except ValueError:
            print("Invalid Entry; Try again")
            
    return servings_per_ingredient, servings, n_list,rem_list

calculate_servings("base_recipe.txt")

# def to_append(filename):
    
#     ingredient_words = []
#     with open(filename, "r") as recipe:
#         recipe.readline()
#         recipe.readline()
        
#         for line in recipe:
#             if 'Directions' in line:
#                 break
#             line.strip()
            
#             if not line:
#                 continue
            
#             line = line.split()
            
#             ingredient_words.append(line[1:])
#         del ingredient_words[-1] 
        
#         print(ingredient_words)
        

def write_recipe(filename, adjusted_filename):
    servings_per_ingredient, servings, n_list = calculate_servings(filename)
    #f_list = []
    
    
    with open(adjusted_filename, "w") as output:
    #     for words in ingredient_words:
    #        line_str = ' '.join(words)
    #        f_list.append(line_str)
            
        for num,a in zip(servings_per_ingredient,ingredient_words):
            output.write(f"\n{num}\t{a}")
        



# to_append("base_recipe.txt")
# calculate_servings("base_recipe.txt")

#             for i, z in zip(servings_per_ingredient, f_list):
#                 output.write(f"{i} {z}\n")

#     except Exception as e:
#         print(f"An error occurred while writing the file: {e}")

# # Example usage:
# # write_recipe("base_recipe.txt", "adjusted_recipe.txt")


        

if __name__ == "__main__":    
    write_recipe("base_recipe.txt","adjusted_recipe.txt")