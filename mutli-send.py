##!/usr/bin/python3

import sys
import random
import os


user=os.getlogin()



####### Parse input arguments into variables  ##############
if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--station', '-s', help="Station destination identity")
	parser.add_argument('--profile', '-p', help="Override default profile")
	parser.add_argument('--force',   '-f', help="Force existing docker to close and run again")
	parser.add_argument('--destroy', '-d', help="Destroy the direct-send container")
	parser.add_argument('--relay1', '-1', help="Specify first relay server")
	parser.add_argument('--relay2', '-2', help="Specify second relay server")
	parser.add_argument('--relay3', '-3', help="Specify third relay server")

	## Replicate above line to add more optional input arguments
	
	args = parser.parse_args()
	print()
	print("Retrieving station details for station Ident: ", args.station)


	profile = args.profile


	if(args.station):
		station=args.station
	else:
		station='None'


	if(args.force=='1'):
		force=1
	else:
		force=0
	

	if(args.destroy=='1'):
		destroy=1
	else:
		destroy=0

######## END Processing input args into variables ############
