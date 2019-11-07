# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 11:18:53 by roduquen          #+#    #+#              #
#    Updated: 2019/11/07 16:43:04 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import	matplotlib.pyplot
import	numpy

class	ImageProcessor:
	def	load(path):
		img = matplotlib.pyplot.imread(path)
		print("Loading image of dimensions", len(img), "x", len(img[0]))
		return img

	def	display(array):
		matplotlib.pyplot.imshow(array)
		matplotlib.pyplot.show()

