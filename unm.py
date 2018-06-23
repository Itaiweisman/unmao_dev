import os
import subprocess
import sys
device=sys.argv[1]
def get_device_last_lba(device):
	p=subprocess.check_output(['sg_readcap', device])
	last_lba=p.split('\n')[1].split('=')[2]
	if (int(last_lba)):
		return int(last_lba)
	else:
		return Null

d=0
try:
	cap=get_device_last_lba(device)
	print "capacity is {} ; device is {}".format(cap,device)
	print "please hit any key to continue"
	a=raw_input()
	
	while d < cap:
		cmd="sg_unmap --lba="+str(d)+" --num=65536 "+device
#		os.system(cmd)
		print cmd
		d=d+65536
except Exception as E:
	print "Caught Exception {}".format(E)


