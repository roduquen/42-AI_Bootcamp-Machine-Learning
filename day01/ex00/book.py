# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 10:28:29 by roduquen          #+#    #+#              #
#    Updated: 2019/11/05 22:46:07 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from recipe import Recipe

class	Book:

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		if type(name) != str:
			print("The name gave is not a string")
			return False
		for elem in self.recipes_list:
			for recipes in elem:
				if recipes.name:
					return recipes
		print("The name gave does not exist")
		return False

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if type(name) != str:
			print("The name gave is not a string")
			return False
		for elem in self.recipes_list:
			if recipe_type == str(elem):
				return elem
		print("The name gave is not a type of meal")
		return False

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		new_recipe = Recipe()
		for elem in self.recipes_list:
			if elem == new_recipe.recipe_type:
				for node in self.recipes_list[elem]:
					if new_recipe.name == node.name:
						print("The recipe already exists, do you want to update it ? [y/n]")
						ans = input(">> ")
						if ans == "y":
							return
						self.recipes_list[elem].append(new_recipe)
						self.last_update = datetime.date
						return
				self.recipes_list[elem].append(new_recipe)
				self.last_update = datetime.date

	# --------------------------------------------------------- #

	def __init__(self, name = "cookbook"):
		self.creation_date = datetime.date
		self.last_update = datetime.date
		self.name = name
		self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}

	def __str__(self):
		"""Return the string to print with the recipe info"""
		s = ""
		s += str(self.creation_date) + "\n"
		s += str(self.last_update) + "\n"
		s += str(self.name) + "\n"
		s += str(self.recipes_list)
		return (s)
