# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:16:15 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 18:49:14 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (0, 4, 132.42222, 10000, 12345.67)
if len(t) != 5:
	exit("Not enough parameters")
string = "Day_"
if type(t[0]) != int or t[0] < 0:
	print("First parameter is not valid.")
	exit()
if t[0] < 10:
	string += "0"
string += str(t[0]) + ", ex_"
if type(t[1]) != int or t[1] < 0:
	print("Second parameter is not valid.")
	exit()
if t[1] < 10:
	string += "0"
string += str(t[1]) + " : "
if type(t[2]) != float:
	print("Third parameter is not valid.")
	exit()
string += "%.2f"%t[2] + ", "
if type(t[3]) != int:
	print("Fourth parameter is not valid.")
	exit()
string += "%.2e"%t[3] + ", "
if type(t[4]) != float:
	print("Last parameter is not valid.")
	exit()
string += "%.2e"%t[4]
print(string)
