# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 13:44:45 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 18:33:25 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

date = (3,30,2019,9,25)
count = 0
for nbr in date:
	if not type(nbr) == int:
		print(nbr, "is not an int")
		exit()
	count += 1
if count != 5:
	print("There is not enough number to create the date")
else:
	string = ""
	if date[3] < 1 or date[3] > 12:
		print("The date is not well formated")
		exit()
	elif date[3] < 10:
		string = "0"
	string += str(date[3]) + "/"
	if date[4] < 1 or date[4] > 31:
		print("The date is not well formated")
		exit()
	elif date[4] < 10:
		string += "0"
	string += str(date[4]) + "/" + str(date[2]) + " "
	if date[0] < 0 or date[0] > 23:
		print("The date is not well formated")
		exit()
	elif date[0] < 10:
		string += "0"
	string += str(date[0]) + ":"
	if date[1] < 0 or date[1] > 59:
		print("The date is not well formated")
		exit()
	elif date[1] < 10:
		string += "0"
	string += str(date[1])
	print(string)
