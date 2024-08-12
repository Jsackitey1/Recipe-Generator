
# creating my various list for my program
numbers = []
numbers_1 = []
rest = []
rest_1 = []
dir_list = []
w_1 = []

#asking user for an input and handling error on that and prompting the user if he/she puts in other than expected
user_input = None
while user_input == None:

    try:
        user_input = int(input("Enter number of serving:"))


    except ValueError :

       print("Enter a proper Value")

#handling errors while opening the file
try:
    #opening the file
    with open("base_recipe.txt", "r") as my_file:
        #reading the whole file and saving it into a variable
        data = my_file.readlines()

        #using the indexing format to get the number of serving
        number_of_servings = int(data[1][0])

        # using the indexing format to get the name of the recipe
        name_of_recipe = data[0]
#looping through line 2 going thus the lines that contain the ingredients of the recipe
        for line in data[2:]:
            #splitting the lines
                word = line.split()

        # if line cannot be split then it`s an empty line so the code will break at that point
                if not word:
                    break
                # setting all the quantities of the ingredients to a variable
                number = word[0]
            #appending these numbers into a list
                numbers.append(float(number))
            #storing the remaining part of each line also into another variable
                the_rest = word[1:]

            #appending these remaining part of the line into another list
                rest.append(the_rest)

            #My approach to find the Directions line and write it later on
            # first loop and search for that line and get its index
            #then loop from that index going so that it will not be hardcoded



        #setting my target line to a variable
        target_line = "Directions"

        # Iterating over each line to find the index
        for index, line in enumerate(data):
            # Check if the target line is in the current line
            if target_line in line:
                break  # Stop iterating once the line is found
        #looping ffom the index of the targetted line
        for line in data[index:]:
            #appending them into a list
            dir_list.append(line)

except:
    print(f" Invalid file format...")


#creating functions to calculate the servings
def serving_calc():
    orig_serving = number_of_servings
    final_serving = (user_input) / (orig_serving)
    return  final_serving

serving_calc()

# this function would return a number that will multiply the initial quantities of each ingredients by a specific factor depending on the user input
def final_serving():
    for i in numbers:
        i *= serving_calc()
        numbers_1.append(round(float(i), 1))
    #print(numbers_1)
final_serving()




def final():
    #looping through the rest list thus the list that contains the remaining part of each list after initial looping
    for w in rest:
        # joining them and setting tabs
        w_1 = "\t".join(w)
        # appending it into a new list
        rest_1.append(w_1)
        # opening the file to be written into
        with open("adjusted_base_recipe.txt", "w") as my_doc:
            # writing the name of the recipe into the new txt file
            my_doc.write(name_of_recipe)
            # writing the new number of servings
            my_doc.write(f"{user_input}\tServings")

            for num, a in zip(numbers_1, rest_1):
                # writing the new quantities and the ingredients into the new txt file
                my_doc.write(f"\n{num} \t{a}")

            my_doc.write("\n")
            my_doc.write("\n")

            # looping through the list I stored the directions into and writing it in the txt file
            for item in dir_list:
                my_doc.write(item)


final()

print(f"The program runs successfully..... \nOpen the required adjusted file to see the results ")









        


