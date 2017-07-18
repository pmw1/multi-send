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
		dest_station=args.station
	else:
		dest_station='None'


	if(args.force=='1'):
		print("***  FORCING ------------------------  ***")
		print("***  Destroying container: multi-send  ***")
		print("***  --------------------------------  ***")
		os.system("sudo docker rm -f multi-send")

	

	if(args.destroy=='1'):
		print("***  Destroying container: multi-send  ***")
		os.system("sudo docker rm -f multi-send")
		quit()





















	if(args.relay1 is not None):
		print('relay 1 manually entered, but not programmed to override defaults yet')
	if(args.relay2 is not None):
		print('relay 2 manually entered, but not programmed to override defaults yet')
	if(args.relay3 is not None):
		print('relay 3 manually entered, but not programmed to override defaults yet')
		
	

######## END Processing input args into variables ############





################ CLASS DEFINITION FOR channel ##############
class channelObj:
	####### Source Machine Variables #######
	__station_src_ident = None
	__station_src_ip = None
	__station_src_mode = None
	__station_src_profile_pref = None
	__station_src_tx_limit_mbps = None
	__station_src_rx_limit_mbps = None
	__station_src_rx_port = None
	__station_src_relay_ident_1 = None
	__station_src_relay_ident_2 = None
	__station_src_relay_ident_3 = None
	__station_src_contact_admin_name = None
	__station_src_contact_admin_phone = None
	__station_src_contact_admin_email = None
	__station_src_contact_admin_company = None
	__station_src_contact_admin_notes = None
	####### Destination Variables #########
	__station_dest_ident = None
	__station_dest_ip = None
	__station_dest_mode = None
	__station_profile_pref = None
	__station_dest_tx_limit_mbps = None
	__station_dest_rx_limit_mbps = None
	__station_dest_rx_port = None
	__station_dest_relay_ident_1 = None
	__station_dest_relay_ident_2 = None
	__station_dest_relay_ident_3 = None
	__station_dest_contact_admin_name = None
	__station_dest_contact_admin_phone = None
	__station_dest_contact_admin_email = None
	__station_dest_contact_admin_company = None
	__station_dest_contact_admin_notes = None
	###### Set standard relay variables
	__relay_1_ident = None
	__relay_1_ip = None
	__relay_1_port_in = None
	__relay_1_port_tcp = None
	__relay_2_ident = None
	__relay_2_ip = None
	__relay_2_port_in = None
	__relay_2_port_tcp = None
	__relay_3_ident = None
	__relay_3_ip = None
	__relay_3_port_in = None
	__relay_3_port_tcp = None
	###### Set standard profile override variables
	__profile_profile = None
	__profile_tx_mode = None
	__profile_v_ts_type= None
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
	### end variable definitions


	### Method Definitions

	#### init method
	def __init__(self, station_dest_ident):
		self.__station_dest_ident = station_dest_ident
		self.__station_src_ident = src_station

	#### source methods
	def set_station_src_ip(self, station_src_ip):
		self.__station_src_ip = station_src_ip

	def set_station_src_mode(self, station_src_mode):
		self.__station_src_mode = station_src_mode

	def set_station_src_profile_pref(self, station_src_profile_pref):
		self.__station_src_profile_pref = station_src_profile_pref

	def set_station_src_mode(self, station_src_mode):
		self.__station_src_mode = station_src_mode

	def set_station_src_tx_limit_mbps(self, station_src_tx_limit_mbps):
		self.__station_src_tx_limit_mbps = station_src_tx_limit_mbps

	def set_station_src_rx_limit_mbps(self, station_src_rx_limit_mbps):
		self.__station_src_rx_limit_mbps = station_src_rx_limit_mbps

	def set_station_src_rx_limit_mbps(self, station_src_rx_limit_mbps):
		self.__station_src_rx_limit_mbps = station_src_rx_limit_mbps

	def set_station_src_rx_port(self, station_src_rx_port):
		self.__station_src_rx_port = station_src_rx_port

	def set_station_src_relay_ident_1(self, station_src_relay_ident_1):
		self.__station_src_relay_ident_1 = station_src_relay_ident_1

	def set_station_src_relay_ident_2(self, station_src_relay_ident_2):
		self.__station_src_relay_ident_2 = station_src_relay_ident_2

	def set_station_src_relay_ident_3(self, station_src_relay_ident_3):
		self.__station_src_relay_ident_3 = station_src_relay_ident_3

	def set_station_src_relay_ident_3(self, station_src_relay_ident_3):
		self.__station_src_relay_ident_3 = station_src_relay_ident_3

	def set_station_src_contact_admin_name(self, station_src_contact_admin_name):
		self.__station_src_contact_admin_name = station_src_contact_admin_name

	def set_station_src_contact_admin_phone(self, station_src_contact_admin_phone):
		self.__station_src_contact_admin_phone = station_src_contact_admin_phone

	def set_station_src_contact_admin_email(self, station_src_contact_admin_email):
		self.__station_src_contact_admin_email = station_src_contact_admin_email

	def set_station_src_contact_admin_company(self, station_src_contact_admin_company):
		self.__station_src_contact_admin_company = station_src_contact_admin_company

	def set_station_src_contact_admin_notes(self, station_src_contact_admin_notes):
		self.__station_src_contact_admin_notes = station_src_contact_admin_notes

	#### destination methods
	def set_station_dest_ip(self, station_dest_ip):
		self.__station_dest_ip = station_dest_ip

	def set_station_dest_mode(self, station_dest_mode):
		self.__station_dest_mode = station_dest_mode

	def set_station_dest_profile_pref(self, station_dest_profile_pref):
		self.__station_dest_profile_pref = station_dest_profile_pref

	def set_station_dest_tx_limit_mbps(self, station_dest_tx_limit_mbps):
		self.__station_dest_tx_limit_mbps = station_dest_tx_limit_mbps
	
	def set_station_dest_rx_limit_mbps(self, station_dest_rx_limit_mbps):
		self.__station_dest_rx_limit_mbps = station_dest_rx_limit_mbps

	def set_station_dest_rx_port(self, station_dest_rx_port):
		self.__station_dest_rx_port = station_dest_rx_port

	def set_station_dest_relay_ident_1(self, station_dest_relay_ident_1):
		self.__station_dest_relay_ident_1 = station_dest_relay_ident_1

	def set_station_dest_relay_ident_2(self, station_dest_relay_ident_2):
		self.__station_dest_relay_ident_2 = station_dest_relay_ident_2

	def set_station_dest_relay_ident_3(self, station_dest_relay_ident_3):
		self.__station_dest_relay_ident_3 = station_dest_relay_ident_3

	def set_station_dest_contact_admin_name(self, station_dest_contact_admin_name):
		self.__station_dest_contact_admin_name = station_dest_contact_admin_name

	def set_station_dest_contact_admin_phone(self, station_dest_contact_admin_phone):
		self.__station_dest_contact_admin_phone = station_dest_contact_admin_phone

	def set_station_dest_contact_admin_email(self, station_dest_contact_admin_email):
		self.__station_dest_contact_admin_email = station_dest_contact_admin_email

	def set_station_dest_contact_admin_company(self, station_dest_contact_admin_company):
		self.__station_dest_contact_admin_company = station_dest_contact_admin_company

	def set_station_dest_contact_admin_notes(self, station_dest_contact_admin_notes):
		self.__station_dest_contact_admin_notes = station_dest_contact_admin_notes



	### profile methods
	def set_profile_profile(self, profile_profile):
		self.__profile_profile = profile_profile

	def set_profile_tx_mode(self, profile_tx_mode):
		self.__profile_tx_mode = profile_tx_mode
		
	def set_profile_v_ts_type(self, profile_v_ts_type):
		self.__profile_v_ts_type = profile_v_ts_type

	def set_profile_v_video_format(self, v_video_format):
		self.__profile_v_video_format = v_video_format

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
		self.__profile_v_format= profile_v_format

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

	def set_profile_v_intra_refresh(self, profile_v_intra_refresh):
		self.__profile_v_intra_refresh = profile_v_intra_refresh

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


	### relay methods

	def set_relay_info(self, relayNum, ident, ip, port_in, port_tcp):
		if relayNum == "1":
			print('setting relay 1 info in channel class')
			self.__relay_1_ident = ident
			self.__relay_1_ip = ip
			self.__relay_1_port_in = port_in
			self.__relay_1_port_tcp = port_tcp
		elif relayNum == "2":
			print('setting relay 2 info in channel class')
			self.__relay_2_ident = ident
			self.__relay_2_ip = ip
			self.__relay_2_port_in = port_in
			self.__relay_2_port_tcp = port_tcp
		elif relayNum == "3":
			print('setting relay 3 info in channel class')
			self.__relay_3_ident = ident
			self.__relay_3_ip = ip
			self.__relay_3_port_in = port_in
			self.__relay_3_port_tcp = port_tcp
		else:
			print('can not set relay info in Connection class')



	####  ADD MORE SET STATMENTS ABOVE THIS LINE
	####  ADD GET STATEMENTS BELOW THIS LINE

	def get_station_src_ident(self):
		return(self.__station_src_ident)

	def get_station_src_ip(self):
		return(self.__station_src_ip)

	def get_station_src_mode(self):
		return(self.__station_src_mode)

	def get_station_src_profile_pref(self):
		return(self.__station_src_profile_pref)	

	def get_station_src_tx_limit_mbps(self):
		return(self.__station_src_tx_limit_mbps)	

	def get_station_src_rx_limit_mbps(self):
		return(self.__station_src_rx_limit_mbps)

	def get_station_src_rx_port(self):
		return(self.__station_src_rx_port)	

	def get_station_src_relay_ident_1(self):
		return(self.__station_src_relay_ident_1)

	def get_station_src_relay_ident_2(self):
		return(self.__station_src_relay_ident_2)

	def get_station_src_relay_ident_3(self):
		return(self.__station_src_relay_ident_3)

	def get_station_src_contact_admin_name(self):
		return(self.__station_src_contact_admin_name)	

	def get_station_src_contact_admin_phone(self):
		return(self.__station_src_contact_admin_phone)	

	def get_station_src_contact_admin_email(self):
		return(self.__station_src_contact_admin_email)

	def get_station_src_contact_admin_company(self):
		return(self.__station_src_contact_admin_company)

	def get_station_src_contact_admin_notes(self):
		return(self.__station_src_contact_admin_notes)



	def get_station_dest_ident(self):
		return(self.__station_dest_ident)

	def get_station_dest_ip(self):
		return(self.__station_dest_ip)

	def get_station_dest_mode(self):
		return(self.__station_dest_mode)

	def get_station_dest_profile_pref(self):
		return(self.__station_dest_profile_pref)

	def get_station_dest_tx_limit_mbps(self):
		return(self.__station_dest_tx_limit_mbps)

	def get_station_dest_rx_limit_mbps(self):
		return(self.__station_dest_rx_limit_mbps)

	def get_station_dest_rx_port(self):
		return(self.__station_dest_rx_port)

	def get_station_dest_relay_ident_1(self):
		return(self.__station_dest_relay_ident_1)

	def get_station_dest_relay_ident_2(self):
		return(self.__station_dest_relay_ident_2)

	def get_station_dest_relay_ident_3(self):
		return(self.__station_dest_relay_ident_3)

	def get_station_active_state(self):
		return(self.__station_active_state)

	def get_station_dest_contact_admin_name(self):
		return(self.__station_dest_contact_admin_name)

	def get_station_dest_contact_admin_phone(self):
		return(self.__station_dest_contact_admin_phone)

	def get_station_dest_contact_admin_email(self):
		return(self.__station_dest_contact_admin_email)

	def get_station_dest_contact_admin_company(self):
		return(self.__station_dest_contact_admin_company)

	def get_station_dest_contact_admin_notes(self):
		return(self.__station_dest_contact_admin_notes)

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

	def get_profile_v_intra_refresh(self):
		return(self.__profile_v_intra_refresh)

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

	####  OTHER OBJECT FUNCTIONS


################# END OF CLASS DEFINITION  #########################################
####################################################################################














######################################################################################
########################### FUNC GET DEST STATION INFO #  ############################
##### This funtion connects to the database and loads destination station profile information
#####
#####

def updateDestStation (station):
	from configparser import ConfigParser
	### Pull db host/user/pass from config.ini
	parser = ConfigParser()
	parser.read('config.ini')

	#convert list to dictionary
	config=dict(parser.items('stationDatabase'))

	#set usable variables 	
	dbhost=(config.get("dbhost"))
	dbuser=(config.get("dbuser"))
	dbpass=(config.get("dbpass"))
	dbname=(config.get("dbname"))
	dbtable=(config.get("dbtable"))

	#print confirmation of variables loaded
	##print('dbhost: ', dbhost)
	##print('dbuser: ', dbuser)
	##print('dbpass: ', dbpass)
	##print('dbname: ', dbname)
	##print('dbtable:', dbtable)

	import pymysql
	import pymysql.cursors
	## Connect to db
	conn=pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbname, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	try:
		with conn.cursor() as cursor:
			## Read the record
			sql = "SELECT * FROM `{}` WHERE ident=\"{}\"".format(dbtable, station)
			##print("PySQL: ", sql)
			cursor.execute(sql)
			result = cursor.fetchone()
			##print(result)
	finally:
		conn.close

	## update channelObj (object with all destination station properties)

	
	##channel.set_station_dest_ip(result.get('ip'))
	channel.set_station_dest_ip(result.get('ip'))
	channel.set_station_dest_mode(result.get('mode'))
	channel.set_station_dest_profile_pref(result.get('profile_pref'))
	channel.set_station_dest_tx_limit_mbps(result.get('tx_limit_mbps'))
	channel.set_station_dest_rx_limit_mbps(result.get('rx_limit_mbps'))
	channel.set_station_dest_rx_port(result.get('rx_port'))
	channel.set_station_dest_relay_ident_1(result.get('relay_ident_1'))
	channel.set_station_dest_relay_ident_2(result.get('relay_ident_2'))
	channel.set_station_dest_relay_ident_3(result.get('relay_ident_3'))
	channel.set_station_dest_contact_admin_name(result.get('contact_admin_name'))
	channel.set_station_dest_contact_admin_phone(result.get('contact_admin_phone'))
	channel.set_station_dest_contact_admin_email(result.get('contact_admin_email'))
	channel.set_station_dest_contact_admin_company(result.get('contact_admin_company'))
	channel.set_station_dest_contact_admin_notes(result.get('contact_admin_notes'))
####################################################################################
####################################################################################















######################################################################################
########################### FUNC GET SOURCE STATION INFO  ############################
##### This funtion connects to the database and loads source station profile information
#####
#####


def updateSrcStation (station):
	from configparser import ConfigParser
	### Pull db host/user/pass from config.ini
	parser = ConfigParser()
	parser.read('config.ini')

	#convert list to dictionary
	config=dict(parser.items('stationDatabase'))

	#set usable variables 	
	dbhost=(config.get("dbhost"))
	dbuser=(config.get("dbuser"))
	dbpass=(config.get("dbpass"))
	dbname=(config.get("dbname"))
	dbtable=(config.get("dbtable"))

	#print confirmation of variables loaded
	##print('dbhost: ', dbhost)
	##print('dbuser: ', dbuser)
	##print('dbpass: ', dbpass)
	##print('dbname: ', dbname)
	##print('dbtable:', dbtable)

	import pymysql
	import pymysql.cursors
	## Connect to db
	conn=pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbname, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	try:
		with conn.cursor() as cursor:
			## Read the record
			sql = "SELECT * FROM `{}` WHERE ident=\"{}\"".format(dbtable, src_station)
			##print("PySQL: ", sql)
			cursor.execute(sql)
			result = cursor.fetchone()
			##print(result)
	finally:
		conn.close

	## update channelObj (object with all destination station properties)

	
	##channel.set_station_dest_ip(result.get('ip'))
	channel.set_station_src_ip(result.get('ip'))
	channel.set_station_src_mode(result.get('mode'))
	channel.set_station_src_profile_pref(result.get('profile_pref'))
	channel.set_station_src_tx_limit_mbps(result.get('tx_limit_mbps'))
	channel.set_station_src_rx_limit_mbps(result.get('rx_limit_mbps'))
	channel.set_station_src_rx_port(result.get('rx_port'))
	channel.set_station_src_relay_ident_1(result.get('relay_ident_1'))
	channel.set_station_src_relay_ident_2(result.get('relay_ident_2'))
	channel.set_station_src_relay_ident_3(result.get('relay_ident_3'))
	channel.set_station_src_contact_admin_name(result.get('contact_admin_name'))
	channel.set_station_src_contact_admin_phone(result.get('contact_admin_phone'))
	channel.set_station_src_contact_admin_email(result.get('contact_admin_email'))
	channel.set_station_src_contact_admin_company(result.get('contact_admin_company'))
	channel.set_station_src_contact_admin_notes(result.get('contact_admin_notes'))
####################################################################################
####################################################################################
























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


	channel.set_profile_tx_mode(result.get('tx_mode'))
	channel.set_profile_v_ts_type(result.get('v_ts_type'))
	channel.set_profile_v_video_format(result.get('v_video_format'))
	channel.set_profile_v_pid(result.get('v_pid'))
	channel.set_profile_v_vbv_bitrate(result.get('v_vbv_bitrate'))
	channel.set_profile_v_vbv_maxrate(result.get('v_vbv_maxrate'))
	channel.set_profile_v_muxrate(result.get('v_muxrate'))
	channel.set_profile_v_vbv_bufsize(result.get('v_vbv_bufsize'))
	channel.set_profile_v_format(result.get('v_format'))
	channel.set_profile_v_aspect_ratio(result.get('v_aspect_ratio'))
	channel.set_profile_v_cbr(result.get('v_cbr'))
	channel.set_profile_v_keyint(result.get('v_keyint'))
	channel.set_profile_v_bframes(result.get('v_bframes'))
	channel.set_profile_v_level(result.get('v_level'))
	channel.set_profile_v_profile(result.get('v_profile'))
	channel.set_profile_v_intra_refresh(result.get('v_intra_refresh'))
	channel.set_profile_v_threads(result.get('v_threads'))
	channel.set_profile_system_type(result.get('system_type'))
	channel.set_profile_a_pid(result.get('a_pid'))
	channel.set_profile_a_bitrate(result.get('a_bitrate'))
	channel.set_profile_a_format(result.get('a_format'))
	channel.set_profile_a_profile(result.get('a_profile'))
	channel.set_profile_a_aac_encap(result.get('a_aac_encap'))
	channel.set_profile_a_aac_profile(result.get('a_aac_profile'))
	channel.set_profile_service_name(result.get('service_name'))
	channel.set_profile_provider_name(result.get('provider_name'))
############## END FUNC GET PROFILE OVERRIDE INFO #############################
###############################################################################























############## LOOKUP RELAY INFORMATION FOR STREAM SPLITTER ##################
####### This funtion:
####### connects to the centralDB and looks up relay information (IP, PORTS, etc)

def updateRelays():
	from configparser import ConfigParser
	### Pull db host/user/pass from config.ini
	parser = ConfigParser()
	parser.read('config.ini')

	#convert list to dictionary
	config=dict(parser.items('relaysDatabase'))

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
			sql = "SELECT * FROM `{}` WHERE ident=\"{}\"".format(dbtable, channel.get_station_src_relay_ident_1())
			##print("PySQL: ", sql)
			cursor.execute(sql)
			relay1 = cursor.fetchone()

			sql = "SELECT * FROM `{}` WHERE ident=\"{}\"".format(dbtable, channel.get_station_src_relay_ident_2())
			cursor.execute(sql)
			relay2 = cursor.fetchone()

			sql = "SELECT * FROM `{}` WHERE ident=\"{}\"".format(dbtable, channel.get_station_src_relay_ident_3())
			cursor.execute(sql)
			relay3 = cursor.fetchone()

			##print(result)
			print('Relay1: ',relay1)
			print('Relay2: ',relay2)
			print('Relay3: ',relay3)

			if relay1 is not None:
				print ('setting relay 1 object info')
				channel.set_relay_info('1', relay1.get('ident'), relay1.get('ip'), relay1.get('port_in'), relay1.get('port_tcp'))

			if relay2 is not None:
				channel.set_relay_info('2', relay2.get('ident'), relay2.get('ip'), relay2.get('port_in'), relay2.get('port_tcp'))
				print ('setting relay 2 object info')

			if relay3 is not None:
				channel.set_relay_info('3', relay3.get('ident'), relay3.get('ip'), relay3.get('port_in'), relay3.get('port_tcp'))
				print ('setting relay 3 object info')



	finally:
		conn.close


#channel.set_profile_tx_mode(result.get('tx_mode'))


############### END FUNC LOOKUK RELAY INFORMATION #############################
###############################################################################















############## FUNC DISPLAY CURRENT OBJECT DATA ###############################
####### This funtion:
####### displace the channelObj Object data for the instance
####### that is passed into it

def displaychannelObj(instance):
	print('###################################################################')
	print('-------------------------------------------------------------------')
	print('multi-send will always deliver to the stream-splitter (10.0.10.2)')
	print('-------------------------------------------------------------------')
	print('###################################################################')
	print()
	print()
	print('##############  SOURCE STATION INFORMATION  ##################')
	print('IDENT:   ', instance.get_station_src_ident())
	print('IP:      ', instance.get_station_src_ip())
	print('MODE:    ', instance.get_station_src_mode())
	print('SENDprof:', instance.get_station_src_profile_pref())
	print('TX lim:  ', instance.get_station_src_tx_limit_mbps())
	print('RX lim:  ', instance.get_station_src_rx_limit_mbps())
	print('RX port: ', instance.get_station_src_rx_port())
	print('Relay 1: ', instance.get_station_src_relay_ident_1())
	print('Relay 2: ', instance.get_station_src_relay_ident_2())
	print('Relay 3: ', instance.get_station_src_relay_ident_3())
	print('###########  Displaying Source Contact Info ###########')
	print('NAME:    ', instance.get_station_src_contact_admin_name())
	print('PHONE:   ', instance.get_station_src_contact_admin_phone())
	print('EMAIL:   ', instance.get_station_src_contact_admin_email())
	print('COMPANY  ', instance.get_station_src_contact_admin_company())
	print('NOTES:   ', instance.get_station_src_contact_admin_notes())
	print()
	print()
	print('############  DESTINATION STATION INFORMATION  ###############')
	print('IDENT:   ', instance.get_station_dest_ident())
	print('IP:      ', instance.get_station_dest_ip())
	print('MODE:    ', instance.get_station_dest_mode())
	print('SENDprof:', instance.get_station_dest_profile_pref())
	print('TX lim:  ', instance.get_station_dest_tx_limit_mbps())
	print('RX lim   ', instance.get_station_dest_rx_limit_mbps())
	print('RX port: ', instance.get_station_dest_rx_port())
	print('Relay 1: ', instance.get_station_dest_relay_ident_1())
	print('Relay 2: ', instance.get_station_dest_relay_ident_2())
	print('Relay 3: ', instance.get_station_dest_relay_ident_3())
	print('###########  Displaying Desination Contact Info ###########')
	print('NAME:    ', instance.get_station_dest_contact_admin_name())
	print('PHONE:   ', instance.get_station_dest_contact_admin_phone())
	print('EMAIL:   ', instance.get_station_dest_contact_admin_email())
	print('COMPANY: ', instance.get_station_dest_contact_admin_company())
	print('NOTES:   ', instance.get_station_dest_contact_admin_notes())
	print()
	print()
	print('###########   Displaying Profile Override data   ###########')
	print('TX MODE: ', instance.get_profile_tx_mode())
	print('TX TYPE: ', instance.get_profile_v_ts_type())
	print('VIDFORMAT', instance.get_profile_v_video_format())
	print('VPID:    ', instance.get_profile_v_pid())
	print('VBR:     ', instance.get_profile_v_vbv_bitrate())
	print('VMAX BIT ', instance.get_profile_v_vbv_maxrate())
	print('MUXRATE: ', instance.get_profile_v_muxrate())
	print('VBUF:    ', instance.get_profile_v_vbv_bufsize())
	print('VFORMAT: ', instance.get_profile_v_format())
	print('VASPECT: ', instance.get_profile_v_aspect_ratio())
	print('CBRMODE: ', instance.get_profile_v_cbr())
	print('KEYINT:  ', instance.get_profile_v_keyint())
	print('VBFRAME: ', instance.get_profile_v_bframes())
	print('VLEVEL:  ', instance.get_profile_v_level())
	print('VPROFILE:', instance.get_profile_v_profile())
	print('INTRAREF:', instance.get_profile_v_intra_refresh())
	print('VTHREADS:', instance.get_profile_v_threads())
	print('SYSTYPE: ', instance.get_profile_system_type())
	print('APID     ', instance.get_profile_a_pid())
	print('ABIT:    ', instance.get_profile_a_bitrate())
	print('AFORMAT: ', instance.get_profile_a_format())
	print('APROFILE:', instance.get_profile_a_profile())
	print('AACPROF: ', instance.get_profile_a_aac_profile())
	print('AENCAP:  ', instance.get_profile_a_aac_encap())
	print('SERVICE: ', instance.get_profile_service_name())
	print('PROVIDER:', instance.get_profile_provider_name())
	print()
	print()
	print('##################   USING RELAYS   ######################')
	print()
	print('- RELAY 1 -----------------------------------')
	print('Ident:   ', channel.get_relay_1('ident'))
	print('IP:      ', channel.get_relay_1('ip'))
	print('Port in: ', channel.get_relay_1('port_in'))
	print('TCP port:', channel.get_relay_1('port_tcp'))
	print()

	print()
	print('- RELAY 2 -----------------------------------')
	print('Ident:   ', channel.get_relay_2('ident'))
	print('IP:      ', channel.get_relay_2('ip'))
	print('Port in: ', channel.get_relay_2('port_in'))
	print('TCP port:', channel.get_relay_2('port_tcp'))
	print()

	print()
	print('- RELAY 3 -----------------------------------')
	print('IP:      ', channel.get_relay_3('ip'))
	print('Port in: ', channel.get_relay_3('port_in'))
	print('TCP port:', channel.get_relay_3('port_tcp'))
	print()


	print('##########################################################')

############ END FUNC DISPLAY CURRENT OBJECT DATA #############
###############################################################




















######################################################################################
##########################  AGGREGARTP ENTRYPOINT CONSTRUCTOR  #######################
##### construct the shell script that will be transferred to host files to begin the 
##### aggregartp stream splitter 
#####

def buildAggregartpEntrypoint():
	print ('** ADVISORY **  stream splitter entrypoint constructor assumes incoming port from OBE stream is \'4444\'')

	from subprocess import call
	import stat

	splitter_start_docker = open("../stream-split/hostfiles/start-aggregartp.sh", "wb")

	splitter_start_docker.write(bytes("#!/bin/bash\n", 'UTF-8'))
	splitter_start_docker.write(bytes('aggregartp @:4444 ', 'UTF-8'))
	if channel.get_relay_1('ip') is not None:
		splitter_start_docker.write(bytes('{0}:{1} '.format(channel.get_relay_1("ip"), channel.get_relay_1("port_in")), 'UTF-8'))
	if channel.get_relay_2('ip') is not None:
		splitter_start_docker.write(bytes('{0}:{1} '.format(channel.get_relay_2("ip"), channel.get_relay_2("port_in")), 'UTF-8'))
	if channel.get_relay_3('ip') is not None:
		splitter_start_docker.write(bytes('{0}:{1}\n '.format(channel.get_relay_3("ip"), channel.get_relay_3("port_in")), 'UTF-8'))
		

	splitter_start_docker.close()

############################  END BUILD OBE RUNNER   ############################
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
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts video-format=%s" % channel.get_profile_v_video_format() + r'\012' +'\"\n' , 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts video-channel=sdi" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set input opts audio-channel=embedded" + r"\012" +"\"\n" ,'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"set obe opts system-type=lowestlatency" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"probe input" + r"\012" +"\"\n", 'UTF-8'))
	obe_send_file.write(bytes("sleep 1\n", 'UTF-8'))

	#### Video 
	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set stream opts 0:pid=%s' % channel.get_profile_v_pid() + ',' ,'UTF-8'))
	
	if(channel.get_profile_v_vbv_maxrate() is not None):
		obe_send_file.write(bytes('vbv-maxrate=%s' % channel.get_profile_v_vbv_maxrate() + ',' ,'UTF-8'))

	if(channel.get_profile_v_vbv_bitrate() is not None):
		obe_send_file.write(bytes('bitrate=%s' % channel.get_profile_v_vbv_bitrate() + ',' ,'UTF-8'))
	
	if(channel.get_profile_v_keyint() is not None):
		obe_send_file.write(bytes('keyint=%s' % channel.get_profile_v_keyint() + ',' ,'UTF-8'))
	
	if(channel.get_profile_v_bframes() is not None):
		obe_send_file.write(bytes('bframes=%s' % channel.get_profile_v_bframes() + ',' ,'UTF-8'))
	
	if(channel.get_profile_v_threads() is not None):
		obe_send_file.write(bytes('threads=%s' % channel.get_profile_v_threads() + ',' ,'UTF-8'))

	if(channel.get_profile_system_type() is not None):
		obe_send_file.write(bytes('$\"set obe opts %s' % channel.get_profile_system_type() + ',' ,'UTF-8'))

	if(channel.get_profile_v_format() is not None):
		obe_send_file.write(bytes('format=%s' % channel.get_profile_v_format() + ',' , 'UTF-8'))
	
	if(channel.get_profile_v_profile() is not None):
		obe_send_file.write(bytes('profile=%s' % channel.get_profile_v_profile() + ',' , 'UTF-8'))
	
	if(channel.get_profile_v_level() is not None):
		obe_send_file.write(bytes('level=%s' % channel.get_profile_v_level() + ',' , 'UTF-8'))
	
	if(channel.get_profile_v_aspect_ratio() is not None):
		obe_send_file.write(bytes('aspect-ratio=%s' % channel.get_profile_v_aspect_ratio() + ',' , 'UTF-8'))
	
	if(channel.get_profile_v_intra_refresh() is not None):
		obe_send_file.write(bytes('intra-refresh=%s' % channel.get_profile_v_intra_refresh() , 'UTF-8'))

	obe_send_file.write(bytes( r'\012' + '\"\n' , 'UTF-8'))	

	

	#### Audio

	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set stream opts 1:pid=%s' % channel.get_profile_a_pid() + ',' ,'UTF-8'))
	
	if(channel.get_profile_a_bitrate() is not None):
		obe_send_file.write(bytes('bitrate=%s' % channel.get_profile_a_bitrate(),'UTF-8'))
		if(channel.get_profile_a_format() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' +'\"\n' ,'UTF-8'))

	if(channel.get_profile_a_format() is not None):
		obe_send_file.write(bytes('format=%s' % channel.get_profile_a_format(),'UTF-8'))
		if(channel.get_profile_a_profile() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' + 'boom\"\n' ,'UTF-8'))

	if(channel.get_profile_a_profile() is not None):
		obe_send_file.write(bytes('aac-profile=%s' % channel.get_profile_a_profile(),'UTF-8'))
		if(channel.get_profile_a_aac_encap() is not None):
			obe_send_file.write(bytes(',','UTF-8'))
		else:
			obe_send_file.write(bytes( r'\012' + '\"\n' ,'UTF-8'))

	if(channel.get_profile_a_aac_encap() is not None):
		obe_send_file.write(bytes('aac-encap=%s' % channel.get_profile_a_aac_encap() + r'\012' +'\"\n','UTF-8'))	

	#####
	
	if(channel.get_profile_pmt_pid() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set stream opts 0:pid=%s' % channel.get_profile_pmt_pid() + r'\012' +'\"\n','UTF-8'))

	if(channel.get_profile_v_ts_type() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set muxer opts ts-type=%s' % channel.get_profile_v_ts_type() + "," ,'UTF-8'))

	if(channel.get_profile_v_muxrate() is not None):
		obe_send_file.write(bytes('ts-muxrate=%s' % (channel.get_profile_v_muxrate() * 1000) + r'\012' +'\"\n' ,'UTF-8'))


	if(channel.get_profile_tx_mode() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set output %s' % channel.get_profile_tx_mode() + r'\012' +'\"\n','UTF-8'))

	obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
	obe_send_file.write(bytes('$\"set outputs 1' + r'\012' + '\"\n','UTF-8'))
	
	if(channel.get_profile_tx_mode() is not None):
		obe_send_file.write(bytes('screen -p 0 -S $NAME -X stuff ', 'UTF-8'))
		obe_send_file.write(bytes('$\"set output opts 0:target={0}://{1}:{2}'.format(channel.get_profile_tx_mode(), stream_splitter_ip, stream_splitter_port)  + r'\012' +'\"\n', 'UTF-8'))

		obe_send_file.write(bytes("screen -p 0 -S $NAME -X stuff $\"start" + r'\012' + "\"\n", 'UTF-8'))

	obe_send_file.write(bytes("screen -r\n", 'UTF-8'))

			### lowlat setting could be  auto, but better to be in db and pull into script

	obe_send_file.close()


	##os.chmod('hostfiles/start-obe.sh', stat.S_IXOTH)

###################  END BUILD OBE RUNNER   ###################
###############################################################























######################################################################################
################################ INITIATE OBE DOCKER #################################
##### Luach Obe Docker and pass all variables into docker
##### (THIS IS NOT CURRENTLY WORKING - calling initiateObeDockerTemp until this can be 
##### sorted out.

def initiateObeDocker():
	print()
	print('##################################   Launching OBE DOCKER   ##########################################')
	from configparser import ConfigParser
	### Pull dcocker image name from config.ini
	parser2 = ConfigParser()
	parser2.read('config.ini')
	#convert list to dictionary
	config=dict(parser2.items('dockerImages'))
	#set usable variables 	
	obeDockerName=(config.get("obesenddocker"))
	print ('using docker: ' + obeDockerName)


	import docker
	docker = docker.from_env()  

	container = docker.create_container(
		image = obeDockerName,
		stdin_open=True,
		tty=True,
		command='/bin/bash/',
		volumes=['/home/default/hostfiles', '/home/default/recorded-video'],

		host_config=docker.create_host_config(binds={
			'/home/kevin/docker/obe-rt-send/hostfiles': {
				'bind': '/home/default/hostfiles',
				'mode': 'rw',
			},
			'/home/kevin/recorded-video': {
				'bind': '/home/default/recorded-video',
				'mode': 'rw'

			}

			})

		)

	docker.start(containter)

###############################  END INITIATE OBE DOCKER   ##############################
#######################################################################################






























######################################################################################
################################ INITIATE OBE DOCKER (TEMP) #################################
##### initiate docker by forming a bash script and executing it.
##### (Eventually, we should use the docker api for python to run docker from within the py)
#####   

def initiateObeDockerTemp():

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
	stream_splitter_start_docker.write(bytes("--privileged -i -t -d ", 'UTF-8'))
	stream_splitter_start_docker.write(bytes("pmw1/split-rtp\n", 'UTF-8'))


	stream_splitter_start_docker.close()

	os.chmod('../stream-split/start-stream-split.sh', stat.S_IXOTH)
	proc = subprocess.Popen('sudo ../stream-split/start-stream-split.sh', shell=True)

	##call(['bash', '../stream-split/start-stream-split.sh'])

###############################  END INITIATE AGGREGARTP  ############################
######################################################################################
















######################################################################################
################################ SET ACTIVE STATUS  #################################
##### connect to database and change change status to active
##### 

def setActive():
	from configparser import ConfigParser
	### Pull db host/user/pass from config.ini
	parser = ConfigParser()
	parser.read('config.ini')

	#convert list to dictionary
	config=dict(parser.items('stationDatabase'))

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
			sql = "UPDATE {} SET active_state=\'1\' WHERE ident=\'{}\'".format(dbtable, station)
			print(sql)
			##print("PySQL: ", sql)
			cursor.execute(sql)
			result = cursor.fetchone()
			##print(result)
	finally:
		conn.close

###############################  END SET ACTIVE STATE  ##############################
######################################################################################








































######################################################################################
############################  START EXECUTING THINGS #################################

channel = channelObj(dest_station)

## if channel instance exists, print ident and update target station
## by calling the updateDestStation function
if (channel):

	## update source station info in channel (channelOBJ) class
	updateSrcStation(src_station)

	## update target station info in channel (channelObj) class	
	updateDestStation(dest_station)

	## lookup relay information and set channel object class with relay data
	updateRelays()


	
	## update profile information if override is specified
	if(profile is not None):
		print("Profile override (based on start flag): ", profile)
		updateSendProfile(profile)
	elif(channel.get_station_src_profile_pref()):
		print("Profile override  (based on DB source station definition)", channel.get_station_src_profile_pref())
		updateSendProfile(channel.get_station_src_profile_pref())
	else:
		print("No Profile overrides detected")



	displaychannelObj(channel)

	## bufld the entrypoint shell script for the stream-splitter (aggreartp)
	buildAggregartpEntrypoint()

	## build shell file to execute obe
	buildObeRunner()

	## build aggregartp launch shell script (entrypoint script for docker pmw1/split-rtp)
	initiateAggregartp()

	#initiateObeDocker()
	initiateObeDockerTemp()

	##set active status
	##setActive()













