# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 12:39:32 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 13:01:21 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, list_of_inputs):
	new_lst = []
	try:
		for elem in list_of_inputs:
			new_lst.append(function_to_apply(elem))
	except:
		print("It s not possible")
		return False
	return new_lst

print(ft_map(lambda x: x, [1, 2, 3]))
