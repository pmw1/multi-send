#!/usr/bin/python3

import sys
import random
import os
import socket

user=os.getlogin()
src_station=socket.gethostname()
stream_splitter_ip='10.0.10.2'
stream_splitter_port='4444'

####### Parse input arguments into variables  ##############
if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--profile', '-p', help="Override default profile")
	parser.add_argument('--force',   '-f', help="Force existing docker to close and run again")
	parser.add_argument('--destroy', '-d', help="Destroy the direct-send container")
	parser.add_argument('--mode', '-m', help="Define mode (udp/rtp)")
	parser.add_argument('--port' '-pp', help="Specify relay input UDP port")
	parser.add_argument('--relay1', '-1', help="Specify first relay server")
	parser.add_argument('--relay2', '-2', help="Specify second relay server")
	parser.add_argument('--relay3', '-3', help="Secify third relay server")

	args = parser.parse_args()
	print()

	profile = args.profile
	mode = args.mode

	if(args.mode is not None):
		print("*** Mode override active, but not programmed yet ***")

	if(args.force=='1'):
		print("***  FORCING ------------------------  ***")
		print("***  --------------------------------  ***")
		os.system("sudo docker rm -f multi-send")
		os.system("sudo docker rm -f stream-split")

	if(args.destroy=='1'):
		print("***  Destroying container: multi-send and stream split  ***")
		os.system("sudo docker rm -f multi-send")
		os.system("sudo docker rm -f stream-split")
		quit()

	if(args.relay1 is not None):
		relay1=args.relay1
	else:
		relay1 = None
	if(args.relay2 is not None):
		relay2=args.relay2
	else:
		relay2 = None
	if(args.relay3 is not None):
		relay3=args.relay3
	else:
		relay3 = None

######## END Processing input args into variables ############










########  Validate input args #####################################

def validateArgs():
	## profile must be defined
	if(profile is not None):
			print("TX Profile: ", profile)
	else:
		print("Profile **MUST** be defined...   exiting...")
		quit()	



########  END Validate input args #################################






########  Define TX profile #####################################
class txProfileObj:
	__profile_profile = None
	__profile_tx_mode = None
	__profile_v_ts_type = None
	__profile_v_video_format = None
	__profile_v_pid = None
	__profile_v_vbv_bitrate = None
	__profile_v_vbv_maxrate = None
	__profile_v_muxrate = None
	__profile_v_vbv_bufsize = None
	__profile_v_format = None
	__profile_v_aspect_ratio = None
	__profile_v_cbr = None
	__profile_v_keyint = None
	__profile_v_bframes = None
	__profile_v_level = None
	__profile_v_profile = None
	__profile_intra_refresh = None
	__profile_v_threads = None
	__profile_system_type = None
	__profile_a_pid = None
	__profile_a_bitrate = None
	__profile_a_format = None
	__profile_a_profile = None
	__profile_a_aac_encap = None
	__profile_a_aac_profile = None
	__profile_service_name = None
	__profile_provider_name = None
	__profile_pmt_pid = None


	def __init__(self, profile_profile):
		self.__profile_profile = profile
		print("init odj profile set to: ", self.__profile_profile)
			
			## Setters ##

	def set_profile_profile(self, profile_profile):
		self.__profile_profile = profile_profile

	def set_profile_tx_mode(self, profile_tx_mode):
		self.__profile_tx_mode = profile_tx_mode

	def set_profile_v_ts_type(self, profile_v_ts_type):
		self.__profile_v_ts_type = profile_v_ts_type

	def set_profile_v_video_format(self, profile_v_video_format):
		self.__profile_v_video_format = profile_v_video_format

	def set_profile_v_pid(self, profile_v_pid):
		self.__profile_v_pid = profile_v_pid

	def set_profile_v_vbv_bitrate(self, profile_v_vbv_bitrate):
		self.__profile_v_vbv_bitrate = profile_v_vbv_bitrate

	def set_profile_v_vbv_maxrate(self, profile_v_vbv_maxrate):
		self.__profile_v_vbv_maxrate = profile_v_vbv_maxrate

	def set_profile_v_muxrate(self, profile_v_muxrate):
		self.__profile_v_muxrate = profile_v_muxrate

	def set_profile_v_vbv_bufsize(self, profile_v_vbv_bufsize):
		self.__profile_v_vbv_bufsize = profile_v_vbv_bufsize

	def set_profile_v_format(self, profile_v_format):
		self.__profile_v_format = profile_v_format

	def set_profile_v_aspect_ratio(self, profile_v_aspect_ratio):
		self.__profile_v_aspect_ratio = profile_v_aspect_ratio

	def set_profile_v_cbr(self, profile_v_cbr):
		self.__profile_v_cbr = profile_v_cbr

	def set_profile_v_keyint(self, profile_v_keyint):
		self.__profile_v_keyint = profile_v_keyint

	def set_profile_v_bframes(self, profile_v_bframes):
		self.__profile_v_bframes = profile_v_bframes

	def set_profile_v_level(self, profile_v_level):
		self.__profile_v_level = profile_v_level

	def set_profile_v_profile(self, profile_v_profile):
		self.__profile_v_profile = profile_v_profile

	def set_profile_intra_refresh(self, profile_intra_refresh):
		self.__profile_intra_refresh = profile_intra_refresh

	def set_profile_v_threads(self, profile_v_threads):
		self.__profile_v_threads = profile_v_threads

	def set_profile_system_type(self, profile_system_type):
		self.__profile_system_type = profile_system_type

	def set_profile_a_pid(self, profile_a_pid):
		self.__profile_a_pid = profile_a_pid

	def set_profile_a_bitrate(self, profile_a_bitrate):
		self.__profile_a_bitrate = profile_a_bitrate

	def set_profile_a_format(self, profile_a_format):
		self.__profile_a_format = profile_a_format

	def set_profile_a_profile(self, profile_a_profile):
		self.__profile_a_profile = profile_a_profile

	def set_profile_a_aac_encap(self, profile_a_aac_encap):
		self.__profile_a_aac_encap = profile_a_aac_encap

	def set_profile_a_aac_profile(self, profile_a_aac_profile):
		self.__profile_a_aac_profile = profile_a_aac_profile

	def set_profile_service_name(self, profile_service_name):
		self.__profile_service_name = profile_service_name

	def set_profile_provider_name(self, profile_provider_name):
		self.__profile_provider_name = profile_provider_name

	def set_profile_pmt_pid(self, profile_pmt_pid):
		self.__profile_pmt_pid = profile_pmt_pid

			##  Getters ##

	def get_profile_profile(self):
		return(self.__profile_profile)

	def get_profile_tx_mode(self):
		return(self.__profile_tx_mode)

	def get_profile_v_ts_type(self):
		return(self.__profile_v_ts_type)

	def get_profile_v_video_format(self):
		return(self.__profile_v_video_format)

	def get_profile_v_pid(self):
		return(self.__profile_v_pid)

	def get_profile_v_vbv_bitrate(self):
		return(self.__profile_v_vbv_bitrate)

	def get_profile_v_vbv_maxrate(self):
		return(self.__profile_v_vbv_maxrate)

	def get_profile_v_muxrate(self):
		return(self.__profile_v_muxrate)

	def get_profile_v_vbv_bufsize(self):
		return(self.__profile_v_vbv_bufsize)

	def get_profile_v_format(self):
		return(self.__profile_v_format)

	def get_profile_v_aspect_ratio(self):
		return(self.__profile_v_aspect_ratio)

	def get_profile_v_cbr(self):
		return(self.__profile_v_cbr)

	def get_profile_v_keyint(self):
		return(self.__profile_v_keyint)

	def get_profile_v_bframes(self):
		return(self.__profile_v_bframes)

	def get_profile_v_level(self):
		return(self.__profile_v_level)

	def get_profile_v_profile(self):
		return(self.__profile_v_profile)

	def get_profile_intra_refresh(self):
		return(self.__profile_intra_refresh)

	def get_profile_v_threads(self):
		return(self.__profile_v_threads)

	def get_profile_system_type(self):
		return(self.__profile_system_type)

	def get_profile_a_pid(self):
		return(self.__profile_a_pid)

	def get_profile_a_bitrate(self):
		return(self.__profile_a_bitrate)

	def get_profile_a_format(self):
		return(self.__profile_a_format)

	def get_profile_a_profile(self):
		return(self.__profile_a_profile)

	def get_profile_a_aac_encap(self):
		return(self.__profile_a_aac_encap)

	def get_profile_a_aac_profile(self):
		return(self.__profile_a_aac_profile)

	def get_profile_service_name(self):
		return(self.__profile_service_name)

	def get_profile_provider_name(self):
		return(self.__profile_provider_name)

	def get_profile_pmt_pid(self):
		return(self.__profile_pmt_pid)

	def get_relay_1(self, attrib):
		if attrib is 'ident':
			return self.__relay_1_ident
		if attrib is 'ip':
			return self.__relay_1_ip 
		if attrib is'port_in':
			return self.__relay_1_port_in
		if attrib is 'port_tcp':
			return self.__relay_1_port_tcp

	def get_relay_2(self, attrib):
		if attrib is 'ident':
			return self.__relay_2_ident
		if attrib is 'ip':
			return self.__relay_2_ip 
		if attrib is 'port_in':
			return self.__relay_2_port_in
		if attrib is'port_tcp':
			return self.__relay_2_port_tcp

	def get_relay_3(self, attrib):
		if attrib is 'ident':
			return self.__relay_3_ident
		if attrib is 'ip':
			return self.__relay_3_ip 
		if attrib is 'port_in':
			return self.__relay_3_port_in
		if attrib is'port_tcp':
			return self.__relay_3_port_tcp










######################################################################################
########################## FUNC GET PROFILE OVERRIDE INFO ############################
##### This funtion connects to the database and loads profile information
#####
#####

def updateSendProfile(profile):
	from configparser import ConfigParser
	### Pull db host/user/pass from config.ini
	parser = ConfigParser()
	parser.read('config.ini')

	#convert list to dictionary
	config=dict(parser.items('profileDatabase'))

	#set usable variables 	
	dbhost=(config.get("dbhost"))
	dbuser=(config.get("dbuser"))
	dbpass=(config.get("dbpass"))
	dbname=(config.get("dbname"))
	dbtable=(config.get("dbtable"))

	import pymysql
	import pymysql.cursors
	## Connect to db
	conn=pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbname, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	try:
		with conn.cursor() as cursor:
			## Read the record
			sql = "SELECT * FROM `{}` WHERE profile=\"{}\"".format(dbtable, profile)
			##print("PySQL: ", sql)
			cursor.execute(sql)
			result = cursor.fetchone()
			##print(result)
	finally:
		conn.close


	txprofile.set_profile_tx_mode(result.get('tx_mode'))
	txprofile.set_profile_v_ts_type(result.get('v_ts_type'))
	txprofile.set_profile_v_video_format(result.get('v_video_format'))
	txprofile.set_profile_v_pid(result.get('v_pid'))
	txprofile.set_profile_v_vbv_bitrate(result.get('v_vbv_bitrate'))
	txprofile.set_profile_v_vbv_maxrate(result.get('v_vbv_maxrate'))
	txprofile.set_profile_v_muxrate(result.get('v_muxrate'))
	txprofile.set_profile_v_vbv_bufsize(result.get('v_vbv_bufsize'))
	txprofile.set_profile_v_format(result.get('v_format'))
	txprofile.set_profile_v_aspect_ratio(result.get('v_aspect_ratio'))
	txprofile.set_profile_v_cbr(result.get('v_cbr'))
	txprofile.set_profile_v_keyint(result.get('v_keyint'))
	txprofile.set_profile_v_bframes(result.get('v_bframes'))
	txprofile.set_profile_v_level(result.get('v_level'))
	txprofile.set_profile_v_profile(result.get('v_profile'))
	txprofile.set_profile_intra_refresh(result.get('v_intra_refresh'))
	txprofile.set_profile_v_threads(result.get('v_threads'))
	txprofile.set_profile_system_type(result.get('system_type'))
	txprofile.set_profile_a_pid(result.get('a_pid'))
	txprofile.set_profile_a_bitrate(result.get('a_bitrate'))
	txprofile.set_profile_a_format(result.get('a_format'))
	txprofile.set_profile_a_profile(result.get('a_profile'))
	txprofile.set_profile_a_aac_encap(result.get('a_aac_encap'))
	txprofile.set_profile_a_aac_profile(result.get('a_aac_profile'))
	txprofile.set_profile_service_name(result.get('service_name'))
	txprofile.set_profile_provider_name(result.get('provider_name'))
############## END FUNC GET PROFILE OVERRIDE INFO #############################
###############################################################################










	
######################################################################################
##########################  AGGREGARTP ENTRYPOINT CONSTRUCTOR  #######################
##### construct the shell script that will be transferred to host files to begin the 
##### aggregartp stream splitter 
#####

def buildAggregartpEntrypoint():
	print ('** ADVISORY **  stream splitter entrypoint constructor assumes incoming port from OBE stream is \'4444\'')

	from subprocess import call
	import stat

	entrypoint_file = open("../stream-split/hostfiles/start-aggregartp.sh", "wb")

	entrypoint_file.write(bytes("#!/bin/bash\n", 'UTF-8'))
	entrypoint_file.write(bytes('aggregartp -U @:4444 ', 'UTF-8'))
	if relay1 is not None:
		entrypoint_file.write(bytes(" 239.1.0.1:3001@" + relay1,'UTF-8'))
	if relay2 is not None:
		entrypoint_file.write(bytes(" 239.1.0.1:3001@" + relay2,'UTF-8'))
	if relay3 is not None:
		entrypoint_file.write(bytes(" 239.1.0.1:3001@" + relay3,'UTF-8'))

	entrypoint_file.write(bytes(" -X 192.168.0.1:3005/tcp ",'UTF-8'))

	entrypoint_file.close()

#####################  END AGGREGARTP ENTRYPOINT CONTRUCTOR  ####################
#################################################################################












######################################################################################
########################## FUNC BUILD OBE RUNNER SCRIPT ############################
##### construct the shell script that will be transferred to host files to run OBE
##### from within the docker environment.
#####
def buildObeRunner():
	import stat
	## open file for writing
	obe_send_file = open("hostfiles/start-obe.sh", "wb")

	obe_send_file.write(bytes("#!/bin/bash\n", 'UTF-8'))
	obe_send_file.write(bytes("NAME=obe\n", 'UTF-8'))
	######## '-d' here 
	obe_send_file.write(bytes("screen  -d -m -S $NAME obecli\n", 'UTF-8'))
	obe_send_file.write(bytes("sleep 2\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input decklink" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts card-idx=0" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts video-format=%s" % txprofile.get_profile_v_video_format() + r'\012' +'\"\n' , 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts video-channel=sdi" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts audio-channel=embedded" + r"\012" +"\"\n" ,'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set obe opts system-type=lowestlatency" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"probe input" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("sleep 1\n", 'UTF-8'))

	#### Video 
	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set stream opts 0:pid=%s' % txprofile.get_profile_v_pid() + ',' ,'UTF-8'))
	
	if(txprofile.get_profile_v_vbv_maxrate() is not None):
		obe_send_file.write(bytes('vbv-maxrate=%s' % txprofile.get_profile_v_vbv_maxrate() + ',' ,'UTF-8'))

	if(txprofile.get_profile_v_vbv_bitrate() is not None):
		obe_send_file.write(bytes('bitrate=%s' % txprofile.get_profile_v_vbv_bitrate() + ',' ,'UTF-8'))
	
	if(txprofile.get_profile_v_keyint() is not None):
		obe_send_file.write(bytes('keyint=%s' % txprofile.get_profile_v_keyint() + ',' ,'UTF-8'))
	
	if(txprofile.get_profile_v_bframes() is not None):
		obe_send_file.write(bytes('bframes=%s' % txprofile.get_profile_v_bframes() + ',' ,'UTF-8'))
	
	if(txprofile.get_profile_v_threads() is not None):
		obe_send_file.write(bytes('threads=%s' % txprofile.get_profile_v_threads() + ',' ,'UTF-8'))

	if(txprofile.get_profile_system_type() is not None):
		obe_send_file.write(bytes('$\"set obe opts %s' % txprofile.get_profile_system_type() + ',' ,'UTF-8'))

	if(txprofile.get_profile_v_format() is not None):
		obe_send_file.write(bytes('format=%s' % txprofile.get_profile_v_format() + ',' , 'UTF-8'))
	
	if(txprofile.get_profile_v_profile() is not None):
		obe_send_file.write(bytes('profile=%s' % txprofile.get_profile_v_profile() + ',' , 'UTF-8'))
	
	if(txprofile.get_profile_v_level() is not None):
		obe_send_file.write(bytes('level=%s' % txprofile.get_profile_v_level() + ',' , 'UTF-8'))
	
	if(txprofile.get_profile_v_aspect_ratio() is not None):
		obe_send_file.write(bytes('aspect-ratio=%s' % txprofile.get_profile_v_aspect_ratio() + ',' , 'UTF-8'))
	
	if(txprofile.get_profile_intra_refresh() is not None):
		obe_send_file.write(bytes('intra-refresh=%s' % txprofile.get_profile_intra_refresh() , 'UTF-8'))

	obe_send_file.write(bytes( r'\012' + '\"\n' , 'UTF-8'))	

	

	#### Audio

	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set stream opts 1:pid=%s' % txprofile.get_profile_a_pid() + ',' ,'UTF-8'))
	
	if(txprofile.get_profile_a_bitrate() is not None):
		obe_send_file.write(bytes('bitrate=%s' % txprofile.get_profile_a_bitrate(),'UTF-8'))
		if(txprofile.get_profile_a_format() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' +'\"\n' ,'UTF-8'))

	if(txprofile.get_profile_a_format() is not None):
		obe_send_file.write(bytes('format=%s' % txprofile.get_profile_a_format(),'UTF-8'))
		if(txprofile.get_profile_a_profile() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' + 'boom\"\n' ,'UTF-8'))

	if(txprofile.get_profile_a_profile() is not None):
		obe_send_file.write(bytes('aac-profile=%s' % txprofile.get_profile_a_profile(),'UTF-8'))
		if(txprofile.get_profile_a_aac_encap() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' + '\"\n' ,'UTF-8'))

	if(txprofile.get_profile_a_aac_encap() is not None):
		obe_send_file.write(bytes('aac-encap=%s' % txprofile.get_profile_a_aac_encap() + r'\012' +'\"\n','UTF-8'))	

	#####
	
	if(txprofile.get_profile_pmt_pid() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set stream opts 0:pid=%s' % txprofile.get_profile_pmt_pid() + r'\012' +'\"\n','UTF-8'))

	if(txprofile.get_profile_v_ts_type() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set muxer opts ts-type=%s' % txprofile.get_profile_v_ts_type() + "," ,'UTF-8'))

	if(txprofile.get_profile_v_muxrate() is not None):
		obe_send_file.write(bytes('ts-muxrate=%s' % (txprofile.get_profile_v_muxrate() * 1000) + r'\012' +'\"\n' ,'UTF-8'))


	if(txprofile.get_profile_tx_mode() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set output %s' % txprofile.get_profile_tx_mode() + r'\012' +'\"\n','UTF-8'))

	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set outputs 1' + r'\012' + '\"\n','UTF-8'))
	
	if(txprofile.get_profile_tx_mode() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set output opts 0:target={0}://{1}:{2}'.format(txprofile.get_profile_tx_mode(), stream_splitter_ip, stream_splitter_port)  + r'\012' +'\"\n', 'UTF-8'))

		obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"start" + r'\012' + "\"\n", 'UTF-8'))

	obe_send_file.write(bytes("screen -r\n", 'UTF-8'))

			### lowlat setting could be  auto, but better to be in db and pull into script

	obe_send_file.close()


	##os.chmod('hostfiles/start-obe.sh', stat.S_IXOTH)

###################  END BUILD OBE RUNNER   ###################
###############################################################













######################################################################################
################################ INITIATE AGGRERTP  ##################################
##### 
##### 
#####   

def initiateAggregartp():
	print('Initiating Aggregartp Docker')

	import subprocess
	import stat

	stream_splitter_start_docker = open("../stream-split/start-stream-split.sh", "wb")
	stream_splitter_start_docker.write(bytes("#!/bin/bash\n", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("sudo docker kill stream-split\n", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("sudo docker rm -f stream-split\n", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("echo Inter-Docker user: $USER\n", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("sudo docker run ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("-v $HOME/apps/stream-split/hostfiles/:/hostfiles ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("-p 4444:4444/udp ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("-p 3005:3005/tcp ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("--name=\"stream-split\" ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("--network=\"split\" ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("--ip=\"10.0.10.2\" ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("--privileged -i -t  ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("pmw1/split-rtp\n", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("echo && echo", 'UTF-8'))


	stream_splitter_start_docker.close()

	os.chmod('../stream-split/start-stream-split.sh', stat.S_IXOTH)
	proc = subprocess.Popen('sudo ../stream-split/start-stream-split.sh', shell=True)

	##call(['bash', '../stream-split/start-stream-split.sh'])

###############################  END INITIATE AGGREGARTP  ############################
######################################################################################















######################################################################################
################################ INITIATE OBE DOCKER (TEMP) #################################
##### initiate docker by forming a bash script and executing it.
##### (Eventually, we should use the docker api for python to run docker from within the py)
#####   

def initiateObeDocker():

	print('Initiating Obe Docker (using temporary function)')

	import subprocess
	import stat


	obe_start_docker = open("hostfiles/start-docker.sh", "wb")

	obe_start_docker.write(bytes("#!/bin/bash\n", 'UTF-8'))
	obe_start_docker.write(bytes("docker run ", 'UTF-8'))
	obe_start_docker.write(bytes("--network=\"split\" ", 'UTF-8'))
	obe_start_docker.write(bytes("--ip=\"10.0.10.3\" ", 'UTF-8'))
	obe_start_docker.write(bytes("--name=\"multi-send\" ", 'UTF-8'))
	obe_start_docker.write(bytes("-v /home/" + user + "/apps/multi-send/hostfiles:/home/default/hostfiles ", 'UTF-8'))
	obe_start_docker.write(bytes("-v /home/" + user + "/recorded-video:/home/default/recorded-video ", 'UTF-8'))
	##obe_start_docker.write(bytes("--entrypoint=\"/bin/bash\" ", 'UTF-8'))
	obe_start_docker.write(bytes("-itd ", 'UTF-8'))
	obe_start_docker.write(bytes("--device /dev/blackmagic/io0 ", 'UTF-8'))
	obe_start_docker.write(bytes("pmw1/direct-send ", 'UTF-8'))

	obe_start_docker.close()

	os.chmod('hostfiles/start-docker.sh', stat.S_IXOTH)
	proc = subprocess.Popen('sudo hostfiles/start-docker.sh', shell=True)

	

	##call(['bash', 'hostfiles/start-docker.sh'])
	##os.system("start hostfiles/start-docker.sh")

###############################  END INITIATE OBE DOCKER   ##############################
######################################################################################




















##############   START RUN (calling functions)  #####################


## Initiate txprofile class
txprofile = txProfileObj(profile)

## validate all input args and quit if requirements are not met
validateArgs()

## pull profile specifics from database and set class variables
updateSendProfile(profile)

## Build the entrypoint file for AgregaRTP
buildAggregartpEntrypoint()

## Build the OBE runner
buildObeRunner()

## Run stream splitter (in seperate docker)
initiateAggregartp()

## Initiate/run OBE Docker 
initiateObeDocker()


