# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 23:00:43 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 11:41:05 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

class Vector:

	def	vec_norm(self):
		length = 0.0
		for elem in self.values:
			length += elem * elem
		return math.sqrt(length)

	# ------------------------------------------------------------------- #

	def	__init__(self, values, length = 0):
		"""To create a vector, you need values (list of floats) and the number of those values (int) or a range"""
		if not type(values) == list:
			if not type(values) == int:
				if not type(values) == range:
					exit("The values are not send as list or entered with the number of coords or a range.")
				else:
					self.values = []
					for i in values:
						self.values.append(float(i))
			else:
				self.values = []
				for i in range(values):
					self.values.append(float(i))
		else:
			for elem in values:
				if not type(elem) == float:
					exit("At least one of the values in your list is not a float")
			self.values = values
		if not (type(length) == int or type(length) == float):
			exit("The length has to be sent as a number")
		self.length = float(length)

	# ------------------------------------------------------------------- #

	def __add__(self, vec):
		"""Add to self the first values of vec, the biggest between both will be the new vec size"""
		if len(self.values) >= len(vec.values):
			i = 0
			while i < len(vec.values):
				self.values[i] += vec.values[i]
				i += 1
		else:
			i = 0
			while i < len(self.values):
				self.values[i] += vec.values[i]
				i += 1
			while i < len(vec.values):
				self.values.append(vec.values[i])
				i += 1
		self.length = self.vec_norm()
		return self

	def __radd__(self, other):
		"""Can only add scalars to every vec values. Other has to be a number."""
		if not type(other) == int or type(other) == float:
			print("Other is not a number, operation is not possible.")
			return self
		i = 0
		while i < len(self.values):
			self.values[i] += other
			i += 1
		self.length = self.vec_norm()
		return self

	def __sub__(self, vec):
		"""Sub to self the first values of vec, if vec is bigger than self, other values will be ignored."""
		if len(self.values) >= len(vec.values):
			i = 0
			while i < len(vec.values):
				self.values[i] -= vec.values[i]
				i += 1
		else:
			for i in range(self.values):
				self.values[i] -= vec.values[i]
		self.length = self.vec_norm()
		return self

	def	__rsub__(self, other):
		"""Can only sub scalars to every vec values. Other has to be a number."""
		if not type(other) == int or type(other) == float:
			print("Other is not a number, operation is not possible.")
			return self
		i = 0
		while i < len(self.values):
			self.values[i] -= other
			i += 1
		self.length = self.vec_norm()
		return self

	def	__truediv__(self, vec):
		"""Divides every values of self by vec, if vec as less values, the first values of self will be divided, else the last values of vec will be ignored, if one of the division is by 0, the operation is ignored and a message on the screen will be print"""
		if len(self.values) >= len(vec.values):
			for i in range(vec.values):
				if vec.values[i] == 0.0:
					print("Division by 0 has been ignored.")
				else:
					self.values[i] /= vec.values[i]
		else:
			for i in range(self.values):
				if vec.values[i] == 0.0:
					print("Division by 0 has been ignored.")
				else:
					self.values[i] /= vec.values[i]
		self.length = self.vec_norm()
		return self

	def	__rtruediv__(self, other):
		"""Can only divides self values by other, if other is not a number or zero, self is returned"""
		if not type(other) == int or type(other) == float:
			print("Other is not a number, operation is not possible.")
			return self
		if other == 0:
			print("Other has a value of zero, operation is not permitted")
			return self
		for elem in self.values:
			elem /= other
		self.length = vec_norm(self)
		return self

	def __mul__(self, vec):
		"""Perform the dot product between 2 vectors, if vectors have not the same number of values, False is returned"""
		if not len(self.values) == len(vec.values):
			print("The vectors don't have the same length, operation has been ignored")
			return False
		dot = 0.0
		i = 0
		while i < len(self.values):
			dot += self.values[i] * vec.values[i]
			i += 1
		return dot

	def __rmul__(self, other):
		"""Can only multiply self values by other, if other is not a number, self is returned"""
		if not type(other) == int or type(other) == float:
			print("Other is not a number, operation is not possible.")
			return self
		for elem in self.values:
			elem *= other
		self.length = vec_norm
		return self

	def __str__(self):
		strings = "(Vector [ "
		for i in self.values:
			strings += "%.1f "%i
		strings += "])"
		return strings

	def __repr__(self):
		strings = ""
		for elem in self:
			for node in elem:
				strings += str(node)
		return strings


	# ------------------------------------------------------------------- #
