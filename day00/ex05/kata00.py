# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 12:54:58 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 16:47:57 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (19, 42, 21)
count = 0
ftstr = []
for nbr in t:
	if type(nbr) == int:
		ftstr.append(str(nbr))
		count = count + 1
if count:
	if count > 1:
		plur = " numbers are :"
	else:
		plur = "number is : "
	if count == 1:
		print("The", plur + ", ".join(ftstr))
	else:
		print("The " + str(count) + plur, ", ".join(ftstr))
else:
	print("There is no numbers in the tuple.")
