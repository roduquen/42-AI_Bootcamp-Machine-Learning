# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 15:30:33 by roduquen          #+#    #+#              #
#    Updated: 2019/11/05 12:01:50 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {}

cookbook["sandwich"] = {}
cookbook["sandwich"]["ingredients"] = []
cookbook["sandwich"]["ingredients"].append("ham")
cookbook["sandwich"]["ingredients"].append("bread")
cookbook["sandwich"]["ingredients"].append("cheese")
cookbook["sandwich"]["ingredients"].append("tomatoes")
cookbook["sandwich"]["meal"] = "lunch"
cookbook["sandwich"]["prep_time"] = 10

cookbook["cake"] = {}
cookbook["cake"]["ingredients"] = []
cookbook["cake"]["ingredients"].append("floor")
cookbook["cake"]["ingredients"].append("sugar")
cookbook["cake"]["ingredients"].append("eggs")
cookbook["cake"]["meal"] = "dessert"
cookbook["cake"]["prep_time"] = 60

cookbook["salad"] = {}
cookbook["salad"]["ingredients"] = []
cookbook["salad"]["ingredients"].append("avocado")
cookbook["salad"]["ingredients"].append("arugula")
cookbook["salad"]["ingredients"].append("tomatoes")
cookbook["salad"]["ingredients"].append("spinach")
cookbook["salad"]["meal"] = "lunch"
cookbook["salad"]["prep_time"] = 15

def		print_keys(dict):
	for str in dict:
		print(str)

def		print_values(dict):
	for str in dict:
		print(dict[str])

def		print_all(dict):
	for str in dict:
		print(str, ":", dict[str])

def		print_recipe(recipe):
	try:
		cookbook[recipe]
	except:
		print("The recipe of", recipe, "doesn't exist.")
		return
	print("For the " + recipe + ", you will need "\
		+ ", ".join(cookbook[recipe]["ingredients"])\
		+ ".\nThis recipe is for the "
		+ cookbook[recipe]["meal"] + ".\nIt will takes "\
		+ str(cookbook[recipe]["prep_time"]) + " minutes.")

def		delete_recipe(recipe):
	try:
		cookbook[recipe]
	except:
		print("The recipe of", recipe, "doesn't exist.")
		return
	del cookbook[recipe]
	print("The recipe of", recipe, "has been succesfully deleted.")

def		add_recipe(recipe, ingredients, meal, prep_time):
	try:
		cookbook[recipe]
	except:
		pass
	else:
		print("The recipe", recipe, "already exists, this is the recipe :")
		print_recipe(recipe)
		print("Do you want to update this recipe ? [y/n]")
		ans = input(">> ")
		if ans != "y":
			return
	if type(ingredients) != list:
		print("Your ingredients are not in a list, please use a list.")
		return
	if type(meal) != str:
		print("Your meal is not a string, please use a string.")
		return
	if type(prep_time) != int:
		if prep_time.isdigit():
			prep_time = int(prep_time)
		else:
			print("Your preparation time is not an int, please use a string.")
			return
	cookbook[recipe] = {}
	cookbook[recipe]["ingredients"] = []
	for elem in ingredients:
		cookbook[recipe]["ingredients"].append(str(elem))
	cookbook[recipe]["meal"] = meal
	cookbook[recipe]["prep_time"] = prep_time
	try:
		ans
	except:
		print("The recipe of", recipe, "has been successfully added")
	else:
		print("The recipe of", recipe, "has been successfully updated")

def		print_dictionnary():
	print("The dictionnary countains those recipes :")
	for keys in cookbook:
		print("    -", keys)

def		program():
	running = 1
	while running:
		print("Please select an option by typing the corresponding number:\n\
1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n\
5: Quit")
		ans = input(">> ")
		if ans == "1":
			print("What is the name of the new recipe ?")
			recipe = input(">> ")
			ing = 1
			ingredients = []
			print("What are the ingredients ? (To end the list, press enter)")
			while ing:
				ingredient = input(">> ")
				if not ingredient:
					ing = 0
				else:
					ingredients.append(ingredient)
			print("What is the type of meal ?")
			meal = input(">> ")
			print("What is the time needed to cook ?")
			prep_time = input(">> ")
			add_recipe(recipe, ingredients, meal, prep_time)
		elif ans == "2":
			print("What is the recipe to delete ?")
			recipe = input(">> ")
			delete_recipe(recipe)
		elif ans == "3":
			print("Please enter the recipe's name to get its details:")
			recipe = input(">> ")
			print_recipe(recipe)
		elif ans == "4":
			print_dictionnary()
		elif ans == "5":
			print("Cookbook closed.")
			running = 0
		else:
			print("This option does not exist, please type the corresponding \
number.\nto exit, enter 5.")

program()
