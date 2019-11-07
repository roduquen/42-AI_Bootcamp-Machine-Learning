# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 11:49:36 by roduquen          #+#    #+#              #
#    Updated: 2019/11/06 12:23:25 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Evaluator:

	def test_elem(coefs, words):
		if not (type(coefs) == list or type(words) == list):
			return False
		if len(coefs) != len(words):
			return False
		for elem in coefs:
			if not (type(elem) == float or type(elem) == int):
				return False
		for elem in words:
			if not type(elem) == str:
				return False
		return True

	def zip_evaluate(coefs, words):
		if Evaluator.test_elem(coefs, words) == False:
			print("-1")
			return
		new = zip(coefs, words)
		result = 0.0
		for elem in new:
			result += (len(elem[1]) * elem[0])
		print (result)

	def enumerate_evaluate(coefs, words):
		if Evaluator.test_elem(coefs, words) == False:
			print("-1")
			return
		first = enumerate(coefs, 0)
		result = 0.0
		for count, item in first:
			result += len(words[count]) * item
		print (result)


	# ------------------------------------------------------------------ #

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
