# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 10:56:16 by roduquen          #+#    #+#              #
#    Updated: 2019/11/05 22:42:49 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

class	Recipe:

	def	create_list_text_str(message):
		listy = []
		print(message)
		while True:
			stringy = Recipe.create_str_text("What is the name of the ingredient ?")
			if stringy:
				listy.append(stringy)
			else:
				return False
			print("Was it the last ingredient ? [y/n]")
			ans = input(">> ")
			if (ans == "y"):
				return listy

	def	create_int_between_values(miny, maxy, message):
		print(message)
		stringy = input(">> ")
		if stringy == "exit":
			exit("It s a quick leave !")
		if stringy.isdigit():
			stringy = int(stringy)
			if (stringy >= miny) and (stringy <= maxy):
				return stringy
		return False

	def	create_str_text(message):
		print(message)
		stringy = input(">> ")
		if stringy == "exit":
			exit("It s a quick leave !")
		text = string.ascii_letters + "0123456789- "
		for letters in stringy:
			if not letters in text:
				return False
		return stringy

	# --------------------------------------------------------- #

	def	create_recipe_type(self, miny, maxy, message):
		test = Recipe.create_int_between_values(miny, maxy, message)
		if not test:
			exit("Your recipe was not well formated.")
		if test == 1:
			self.recipe_type = "starter"
		elif test == 2:
			self.recipe_type = "lunch"
		elif test == 3:
			self.recipe_type = "dessert"

	def	create_recipe(self, message):
		self.recipe = Recipe.create_str_text(message)
		if not self.recipe:
			exit("Your recipe was not well formated.")

	def	create_ingredients(self, message):
		self.ingredients = Recipe.create_list_text_str(message)
		if not self.ingredients:
			exit("Your ingredients were not well formated.")

	def	create_cooking_time(self, miny, maxy, message):
		self.cooking_time = Recipe.create_int_between_values(miny, maxy, message)
		if not self.cooking_time:
			exit("Your cooking time was not well formated.")

	def	create_cooking_lvl(self, miny, maxy, message):
		self.cooking_lvl = Recipe.create_int_between_values(miny, maxy, message)
		if not self.cooking_lvl:
			exit("Your cooking level was not well formated.")

	def	create_name(self, message):
		self.name = Recipe.create_str_text(message)
		if not self.name:
			exit("Your name was not well formated.")

	# --------------------------------------------------------- #

	def __init__(self):
		self.create_name("What is the name of the new recipe ?")
		self.create_cooking_lvl(1, 5, "What is the level needed for this recipe (rate from 1 to 5) ?")
		self.create_cooking_time(0, 10000000000, "What is the time needed to prepare this recipe ?")
		self.create_ingredients("Start to write the ingredients needed.")
		self.create_recipe("Write your description :")
		self.create_recipe_type(1, 3, "For which meal this recipe is ? [1 : starter/2 : lunch/3 : dessert]")

	def __str__(self):
		"""Return the string to print with the recipe info"""
		s = ""
		s += str(self.name) + "\n"
		s += str(self.cooking_lvl) + "\n"
		s += str(self.cooking_time) + "\n"
		s += str(self.ingredients) + "\n"
		s += str(self.recipe) + "\n"
		s += str(self.recipe_type)
		return (s)
