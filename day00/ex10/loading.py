# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 21:26:59 by roduquen          #+#    #+#              #
#    Updated: 2019/11/05 08:42:50 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys

def		ft_progress(listy):
	actual = time.time()
	for elem in listy:
		yield elem
		num = ((elem + 1) / len(listy))
		test = int(num * 22)
		if test > 22:
			test = 22
		new_str = test * "=" + ">" + int(23 - test - 1) * " "
		elapsed = time.time() - actual
		estimated = elapsed / (elem + 1) * len(listy)
		print("ETA:", str("%.2f"%estimated) + "s [" + str("%3.0f"%(num * 100)) +  "%][" + new_str + "]", str(elem + 1) + "/" + str(len(listy)), "| elapsed time", str("%.2f"%elapsed) + "s", end = "", flush = True)
		print("\b" * 150, end = "")

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.005)
print()
print(ret)
