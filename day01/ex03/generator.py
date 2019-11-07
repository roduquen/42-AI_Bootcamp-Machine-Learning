# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 11:43:20 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 14:07:41 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def		generator(text = False, sep = False):
	if not type(text) == str:
		return "ERROR"
	if not type(sep) == str:
		return "ERROR"
	new = text.split(sep)
	for elem in new:
		yield elem

for word in generator("on est sur que ca marche", " "):
	print(word)
