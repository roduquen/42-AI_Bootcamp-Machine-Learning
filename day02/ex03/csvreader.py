# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 18:55:29 by roduquen          #+#    #+#              #
#    Updated: 2019/11/07 08:15:15 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():

	def	getheader(self):
		if not self.header:
			print(self.header)
			return None
		print(self.strheader)
		return self.strheader

	def	getdata(self):
		for elem in self.file:
			print(elem)
		return self.file

	def	parse_file(self):
		new_list = []
		if not self.file:
			exit("File was empty")
		for elem in self.file:
			if not type(elem) == str:
				exit("The list has been modified and it makes some troubles")
		self.strheader = self.file[0]
		del self.file[0]
		sep = self.strheader.split(self.sep)
		sep = len(sep)
		for elem in self.file:
			new_line = elem.split(self.sep)
			if not len(new_line) == sep:
				exit("File is corrupted.")
			new_list.append(new_line)
		if self.skip_top > len(new_list):
			exit("You want to skip more lines than there are in file !")
		i = 0
		while i < self.skip_top:
			del self.file[0]
			i += 1
		if self.skip_bottom > len(new_list):
			exit("You want to skip more lines than there are in file !")
		i = 0
		while i < self.skip_bottom:
			del self.file[len(self.file)]
			i += 1
		self.file = new_list

	# ------------------------------------------------------------------ #

	def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.dirname = ""
		self.file = []
		self.strheader = None
		if not type(sep) == str:
			exit("The separator is not well formated")
		self.sep = sep
		if not type(skip_top) == int:
			exit("Skip_top is not an int, please send an int.")
		self.skip_top = skip_top
		if not type(skip_bottom) == int:
			exit("Skip_bottom is not an int, please send an int.")
		self.skip_bottom = skip_bottom
		if not type(header) == bool:
			exit("Header is a bool, send a bool.")
		self.header = header

	def	__enter__(self):
		self.dirname = open(self.dirname, "r")
		for line in self.dirname:
			self.file.append(line)
		self.parse_file()
		return self

	def __exit__(self, type, value, traceback):
		self.dirname.close()

	# ------------------------------------------------------------------ #

def	Loadjson(name):
	new_object = CsvReader(",", True)
	new_object.dirname = name
	return new_object

if __name__ == "__main__":
    with Loadjson('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
