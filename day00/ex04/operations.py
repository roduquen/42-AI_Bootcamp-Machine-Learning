# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 12:23:20 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 17:18:41 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def		usage():
	print("Usage: python operations.py\nExample:\n    python operations.py 10 3")

def		operation(nbr1, nbr2):
	if not nbr1.isdigit():
		print("InputError: only numbers")
		usage()
		return
	nbr1 = int(nbr1)
	if not nbr2.isdigit():
		print("InputError: only numbers")
		usage()
		return
	nbr2 = int(nbr2)
	print("Sum:         ", nbr1 + nbr2, "\nDifference:  ", nbr1 - nbr2
	, "\nProduct:     ", nbr1 * nbr2)
	if nbr2 != 0:
		print("Quotient:    ", nbr1 / nbr2, "\nRemainder:   ", nbr1 % nbr2)
	else:
		print("Quotient:     ERROR (div by zero)\n\
Remainder:    ERROR (modulo by zero)")

if len(sys.argv) > 3:
	print("InputError: too many arguments")
	usage()
elif len(sys.argv) < 3:
	print("InputError: not enough arguments")
	usage()
else:
	operation(sys.argv[1], sys.argv[2])
