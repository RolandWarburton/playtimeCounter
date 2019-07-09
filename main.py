import os
import json

__author__ = "Roland"
__version__ = "1.0.0"

playtime = []


def main():
	total = 0
	os.chdir(os.path.join(os.getcwd(),'stats'))

	for i,filename in enumerate(os.listdir()):
		print('FILE ' + str(i) + ' ' + filename)
		f = open(filename,'r')
		data = json.load(f)
		total += data['stats']['minecraft:custom']['minecraft:play_one_minute']
	
	print('the total is: %d days' % ((total*0.83)/86400) )





main()