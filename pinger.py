#pinger.py -s <DST_IP> -f <FILE_NAME> & pinger.py -r <SAVE_AS> 
from scapy.all import sniff, IP, ICMP, sr1,send
import argparse
import sys
from PIL import Image
#do arg parsing later... ideally you would use pinger.py -s <file> or pinger.py -r(eceive)
#option -s would send and -r would receive by sniffing using scapy
#compression is possible... would count repeating tuples, specify with a variable i.e., $ = (255,255,255) 
DST_IP = ''
CHUNK_SIZE = 1470 #seems like any bigger and my router blocks it
LISTEN_TIME = 15
def extract():
	pxls = []
	im = Image.open('pinger_img.png', 'r')
	pixels = list(im.getdata()) #generates a list of RGB tuples
	for item in pixels: #strip unnecessary chars
		for value in item:
			if value != '(' or value != ')' or value != ' ':
				pxls.append(value)
	return pxls

def send_payload(rgb_list): #packages data into ping packets and sends to dst_ip
	payload_chunk = str(rgb_list)
	remainder = len(payload_chunk) % CHUNK_SIZE
	splices = int((len(payload_chunk) - remainder)/CHUNK_SIZE)
	
	if len(payload_chunk) > CHUNK_SIZE: #chop into chunks and send
		for i in range(0, len(payload_chunk), CHUNK_SIZE):
			icmp_pkt = IP(dst=DST_IP)/ICMP()/payload_chunk[i:i+CHUNK_SIZE]
			send(icmp_pkt)
	else:
		send(IP(dst=DST_IP)/ICMP()/payload_chunk)
	return True

pic=extract()
send_payload(pic)

def recv_data():
# #recvs ping packets and rejoins
	full_load = [] #list of tuples
	load = ''
	s = sniff(filter='icmp', timeout = LISTEN_TIME)
	for i in s:
		load += str(i.load)
	#now go through string 'load' and put values back into tuples and add to list

	
# def convert():
# #repacks back into original file
