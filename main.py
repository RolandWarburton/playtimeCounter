import os
import ast

__author__ = "Roland"
__version__ = "0.1.0"

playtime = []


def main():
	os.chdir(os.path.join(os.getcwd(),'stats'))
	for filename in os.listdir():
		# f = open(filename,'r')
		f = open(filename)
		
		for row in f:
			# print(row)
			print("TEST")
			list = row.split (",")
			print(list)





main()