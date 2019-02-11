import os
import re
import subprocess
import time

response = subprocess.Popen('/usr/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

try:
    f = open('speedtest.csv', 'a+')
    if os.stat('speedtest.csv').st_size == 0:
            f.write('Epoch,Date,Time,Ping,Download,Upload\r\n')
except Exception as e:
    print e
    pass

f.write('{},{},{},{},{},{}\r\n'.format(int(time.time()),time.strftime('%d/%m/%y'), time.strftime('%H:%M'), ping, download, upload))
