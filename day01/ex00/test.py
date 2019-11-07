# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 17:43:46 by roduquen          #+#    #+#              #
#    Updated: 2019/11/07 11:16:45 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import recipe
import book

cookbook = book.Book()
cookbook.add_recipe("hamburger")
for elem in cookbook.recipes_list:
	for node in cookbook.recipes_list[elem]:
		print(node)
