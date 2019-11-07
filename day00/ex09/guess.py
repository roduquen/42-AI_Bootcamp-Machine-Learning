# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 21:04:38 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 21:22:49 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

running = 1
while running:
	print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!")
	nbr = 0
	while nbr < 1 or nbr > 99:
		nbr = int(random.random() * 100)
	trys = 1
	while True:
		print("What's your guess between 1 and 99?")
		ans = input(">> ")
		if ans == "exit":
			exit("Goodbye !")
		elif not ans.isdigit():
			print("That's not a number.")
		elif int(ans) < 1 or int(ans) > 99:
			print("The number is not on the range !")
		elif int(ans) > nbr:
			print("Too high !")
		elif int(ans) < nbr:
			print("Too low !")
		elif int(ans) == nbr:
			if nbr == 42:
				print("The answer to the ultimate question of life, the \
universe and everything is 42")
			elif trys != 1:
				print("Congratulations, you've got it!")
				print("You won in", str(trys), "attempts!")
			else:
				print("Congratulations! You got it on your first try!")
			break
		trys += 1
