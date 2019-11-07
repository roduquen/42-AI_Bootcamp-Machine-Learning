# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filter.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 13:00:42 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 13:02:31 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, list_of_inputs):
	new_lst = []
	try:
		for elem in list_of_inputs:
			if function_to_apply(elem) == True:
				new_lst.append(elem)
	except:
		print("It s not possible")
		return False
	return new_lst

print(ft_filter(lambda x: False if x < 2 else True, [1, 2, 3]))
