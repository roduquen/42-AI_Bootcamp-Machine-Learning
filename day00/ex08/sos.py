# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 19:20:37 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 21:03:37 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse = {}
morse["A"] = ".-"
morse["B"] = "-..."
morse["C"] = "-.-."
morse["D"] = "-.."
morse["E"] = "."
morse["F"] = "..-."
morse["G"] = "--."
morse["H"] = "...."
morse["I"] = ".."
morse["J"] = ".---"
morse["K"] = "-.-"
morse["L"] = ".-.."
morse["M"] = "--"
morse["N"] = "-."
morse["O"] = "---"
morse["P"] = ".--."
morse["Q"] = "--.-"
morse["R"] = ".-."
morse["S"] = "..."
morse["T"] = "-"
morse["U"] = "..-"
morse["V"] = "...-"
morse["W"] = ".--"
morse["X"] = "-..-"
morse["Y"] = "-.--"
morse["Z"] = "--.."
morse["0"] = "-----"
morse["1"] = ".----"
morse["2"] = "..---"
morse["3"] = "...--"
morse["4"] = "....-"
morse["5"] = "....."
morse["6"] = "-...."
morse["7"] = "--..."
morse["8"] = "---.."
morse["9"] = "----."
morse["a"] = ".-"
morse["b"] = "-..."
morse["c"] = "-.-."
morse["d"] = "-.."
morse["e"] = "."
morse["f"] = "..-."
morse["g"] = "--."
morse["h"] = "...."
morse["i"] = ".."
morse["j"] = ".---"
morse["k"] = "-.-"
morse["l"] = ".-.."
morse["m"] = "--"
morse["n"] = "-."
morse["o"] = "---"
morse["p"] = ".--."
morse["q"] = "--.-"
morse["r"] = ".-."
morse["s"] = "..."
morse["t"] = "-"
morse["u"] = "..-"
morse["v"] = "...-"
morse["w"] = ".--"
morse["x"] = "-..-"
morse["y"] = "-.--"
morse["z"] = "--."
if len(sys.argv) < 2:
	exit()
del sys.argv[0]
lst = []
for i in range(len(sys.argv)):
	if (not sys.argv[i].isalnum()):
		for letter in sys.argv[i]:
			if letter.isspace() or letter.isalnum():
				pass
			else:
				lst.append(i)
				break
if len(lst) == len(sys.argv):
	exit("ERROR")
if len(lst):
	print("There was", str(len(lst)), "errors escaped")
i = 0
for elem in lst:
	del sys.argv[elem - i]
	i += 1
new_str = " ".join(sys.argv)
new_lst = new_str.split()
for j in range(len(new_lst)):
	for i in range(len(new_lst[j])):
		print(morse[new_lst[j][i]], end = "")
		if i < len(new_lst[j]) - 1:
			print(" ", end = "")
	if j < len(new_lst) - 1:
		print(" / ", end = "")
print()
