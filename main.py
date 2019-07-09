import os
import json

__author__ = "Roland"
__version__ = "1.0.2"


def main():
	# where to look for stats files
	statsDir = './stats'
	
	# where to save the results
	outputFile = open("playtimeCounter.txt", "w")
	# total in secconds: 1 minecraft min = 0.83 irl secconds
	total = 0

	# change to the stats dir
	os.chdir(statsDir)

	for i,filename in enumerate(os.listdir(statsDir)):
		print('FILE ' + str(i) + ' ' + filename)
		f = open(filename,'r')
		data = json.load(f)
		total += data['stats']['minecraft:custom']['minecraft:play_one_minute']
	
	# divide into irl secconds then convert to days. 86400 is the seccond to day formula
	total = (total/72)/86400
	print('the total is: %d days' % (total) )
	outputFile.write(str(total))


main()