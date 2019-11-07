# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:34:49 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 19:18:08 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

if len(sys.argv) != 3:
	exit("ERROR")
if sys.argv[1].isdigit():
	exit("ERROR")
if not sys.argv[2].isdigit():
	exit("ERROR")
lst = []
for char in sys.argv[1]:
	for letter in string.punctuation:
		if letter == char:
			break
	if letter == char:
		lst.append(" ")
	else:
		lst.append(char)
new_str = "".join(lst)
print(new_str)
new_str = new_str.split()
new_lst = []
for elem in new_str:
	if len(elem) > int(sys.argv[2]):
		new_lst.append(elem)
print(new_lst)
