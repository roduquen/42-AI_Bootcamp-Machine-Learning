# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 17:42:42 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 19:59:00 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint

class CoffeeMachine():

	water_level = 100

	def	log(func):
		def	wrapper(*args, **kwargs):
			new_str = "(roduquen)Running: "
			test = func.__name__.split("_")
			i = 0
			while i < len(test):
				new_str += test[i].capitalize()
				if i < len(test) - 1:
					new_str += " "
				i += 1
			if len(new_str) < 50:
				new_str += " " * (50 - len(new_str))
			actual = time.time()
			wait = func(*args, **kwargs)
			actual = time.time() - actual
			actual *= 1000
			new_str += "[ exec_time = " + "%10.3f"%actual + " ms ]"
			new_str += "\n"
			fily = open("machine.log", "a")
			fily.write(new_str)
			return wait
		return wrapper

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

	# ------------------------------------------------------------------- #

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
