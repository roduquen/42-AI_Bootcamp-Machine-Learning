# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 11:05:49 by roduquen          #+#    #+#              #
#    Updated: 2019/11/05 12:41:28 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
	print("ERROR")
if len(sys.argv) != 2:
	exit()
nbr = sys.argv[1]
chars = "0123456789-"
try:
	nbr = int(nbr)
except:
	print("ERROR")
else:
	if nbr == 0:
		print("I'm Zero.")
	elif nbr % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
