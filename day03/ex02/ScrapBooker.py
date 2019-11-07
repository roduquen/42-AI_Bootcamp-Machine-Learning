# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 14:46:26 by roduquen          #+#    #+#              #
#    Updated: 2019/11/07 19:10:07 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import	numpy
from ImageProcessor import ImageProcessor

class	ScrapBooker:

	def	crop(array, dimensions, position = [0,0]):
		try:
			if len(dimensions) != 2:
				exit("The dimensions have to be 2 integers")
		except:
			exit("Dimensions have to be sent as list or tuple.")
		if type(array) != numpy.ndarray:
			exit("Array has to be a numpy.ndarray.")
		if dimensions[0] > len(array):
			exit("The width is bigger than the previous width.")
		if dimensions[1] > len(array[0]):
			exit("The height is bigger than the previous width.")
		return array[position[1]:position[1]+dimensions[1] , position[0]:position[0] + dimensions[0]]

	def	thin(array, n = 0, axis = 0):
		try:
			i = 0
			while i < n:
				array = numpy.delete(array, 0, axis)
				i += 1
		except:
			exit("The operation is not permitted.")
		return array

	def	juxtapose(array, n = 1, axis = 0):
		tmp_array = array
		try:
			i = 0
			while i < n:
				array = numpy.concatenate((array, tmp_array), axis)
				i += 1
		except:
			exit("The operation is not permitted.")
		return array

	def	mosaic(array, dimensions):
		array = ScrapBooker.juxtapose(array, dimensions[0] - 1, 0)
		array = ScrapBooker.juxtapose(array, dimensions[1] - 1, 1)
		return array

img = ImageProcessor.load("42AI.png")
print(type(img))
img = ScrapBooker.crop(img, (100, 100))
#img = ScrapBooker.thin(img, 100, 0)
#img = ScrapBooker.juxtapose(img, 10, 0)
#img = ScrapBooker.mosaic(img, (7, 1))
display = ImageProcessor.display(img)
