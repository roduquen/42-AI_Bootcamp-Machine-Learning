# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reduce.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 13:01:00 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 14:10:34 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, list_of_inputs):
	value = False
	try:
		for elem in list_of_inputs:
			if not value:
				value = elem
			else:
				value = function_to_apply(value, elem)
	except:
		print("It s not possible")
		return False
	return value

print(ft_reduce(lambda a,b : a if a < b else b, [1, 2, 3]))
