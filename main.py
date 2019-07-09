import os
import json

__author__ = "Roland"
__version__ = "1.0.1"


def main():
	# where to look for stats files
	statsDir = '/home/roland/minecraft/world/stats'
	# where to save the results
	outputFile = open("playtimeCounter.txt", "w")
	# total in secconds: 1 minecraft min = 0.83 irl secconds
	total = 0.000

	# change to the stats dir
	os.chdir(statsDir)

	for filename in os.listdir(statsDir):
		f = open(filename,'r')
		data = json.load(f)
		total += data['stats']['minecraft:custom']['minecraft:play_one_minute']

	# divide into irl secconds then convert to days. 
	# total/20/60 = irl mins
	total = ((total/20)/60)/1440
	# print('the total is: %d days' % (total) )
	outputFile.write(str(total))


main()
