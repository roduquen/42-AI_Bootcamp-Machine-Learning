# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 08:58:19 by roduquen          #+#    #+#              #
#    Updated: 2019/11/07 10:12:27 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy

class NumPyCreator:

	def	from_list(lst, datatype = False):
		"""takes in a list and returns its corresponding NumPy array."""
		if not type(lst) == list:
			exit("The argument given was not a list.")
		if datatype:
			for elem in lst:
				if not type(elem) == datatype:
					exit("The list is not fill with the good datatype")
		return numpy.asarray(lst)

	def	from_tuple(tpl, datatype = False):
		"""takes in a tuple and returns its corresponding NumPy array."""
		if not type(tpl) == tuple:
			exit("The argument given was not a tuple")
		if datatype:
			for elem in tpl:
				if not type(elem) == datatype:
					exit("The list is not fill with the good datatype")
		return numpy.asarray(tpl)

	def	from_iterable(itr, datatype = False):
		"""takes in an iterable and returns an array which contains all of its elements."""
		try:
			iter(itr)
		except TypeError:
			exit("The argument given was not iterable")
		if datatype:
			for elem in itr:
				if not type(elem) == datatype:
					exit("The list is not fill with the good datatype")
		return numpy.asarray(itr)

	def	from_shape(shape, value = 0, datatype = False):
		"""returns an array filled with the same value. The first argument is a tuple which specifies the shape of the array, and the second argument specifies the value of all the elements. This value must be 0 by default."""
		if not type(shape) == tuple:
			exit("The shape given was not a tuple")
		for elem in shape:
			if not type(elem) == int:
				exit("The shape given doesn't countain only numbers.")
		if datatype:
			if not type(value) == datatype:
				exit("The value given doesn't match the good datatype.")
		return numpy.full(shape, value)

	def	random(shape):
		"""returns an array filled with random values.It takes as an argument a tuple which specifies the shape of the array."""
		if not type(shape) == tuple:
			exit("The shape given was not a tuple")
		for elem in shape:
			if not type(elem) == int:
				exit("The shape given doesn't countain only numbers.")
		return numpy.random.random_sample(shape)

	def	identity(n):
		"""returns an array representing the identity matrix of size n."""
		if not type(n) == int:
			exit("The argument given is not an int.")
		return numpy.identity(n)






print("list = [0, 1, 2, 3]")
print(NumPyCreator.from_list([[0, 1, 2, 3], [4, 5, 6, 7]]))
print("\ntuple = (4, 5, 6, 7)")
print(NumPyCreator.from_tuple((4, 5, 6, 7)))
print("\niterable = {'a':97, 'b':98, 'c':99, 'd':100}")
print(NumPyCreator.from_iterable({'a':97, 'b':98, 'c':99, 'd':100}))
print("\ntuple for shape = (2, 3, 4)")
print(NumPyCreator.from_shape((2, 3, 4), 5.245))
print("\ntuple for shape = (2, 3, 4) (randomized values)")
print(NumPyCreator.random((2, 3, 4)))
print("\nthe identity matrix size is 5")
print(NumPyCreator.identity(5))
