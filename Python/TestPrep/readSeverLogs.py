#!/usr/bin/python
import os
import re
import sys
import argparse


'''
    The log format is strored in a file (here server.log) as follows:
        host ident authuser date request status bytes
        An example: 127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
        
        The inputs to the program are a log file stored in the dir u run this script in
        The name of the log file is server.log
        copy this file also in the same directory
        to run the program type: python readServerLogs.py
'''
CONST_IP_OFFSET = 0
CONST_STATUS_OFFSET = 5
# this the regular expression used to parse the log file
regex = '([(\d\.)]+) ([-\w]+) ([-\w]+) \[(.*?)\] "(.*?)" (\d+) (\d+)'

# here is the filename and destination path
#arguments = argparse.ArgumentParser()
#argValues = arguments.parse_args()
#print(arguments)
filename = sys.argv[1]
print (filename)
# filename = 'server.log'
# filename1 = sys.argv[1]

# build a dictionary of successful http requests
successAttempts = {}
destinationAbsPath = './'
fullPath = os.path.join(destinationAbsPath, filename)
re.compile(regex)
# check if the file exists
if os.path.exists(fullPath):
    # print ("file exists")
    # if it exists open it
    with open(fullPath, 'r') as testFile:
        testLine = testFile.readline().strip()
        while testLine:
            # match the regex to the line read into tuples
            m = re.match(regex, testLine)
            if m:
                m = m.groups()
                # the first tuple is ip addrs
                ipaddress = m[CONST_IP_OFFSET]
                # the 6th tuple is http status code
                status = m[CONST_STATUS_OFFSET]

                # check for ip addres not being NULL
                if status == '200' and ipaddress != '':
                    if ipaddress in successAttempts:
                        count = successAttempts[ipaddress]
                        successAttempts[ipaddress] = count+1
                    else:
                        successAttempts[ipaddress] = 1
            else:
                print ('No match found in ' + testLine)
            testLine = testFile.readline().strip()
        testFile.close()
        print ("\n\nThe successful matches were:")
        for keys, values in successAttempts.items():
            print "{:20} {}".format(keys, values)
        # print "values printed"
else:
    print("File not found")

