import argparse

# help text
help_text = 'Plot a graph of x-sn(x), y= sin(bt+c), with a graph title'
sign_off ='Author: Sandra Dashora'
# creates an parser object
parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)
parser.add_argument(
    '--xfreq',
    '-x',
    dest='xfreq',
    action='store',
    type=float,
    default=1.0,
    help='Frequency of the x-oscilation',
    metavar='a'
)
parser.add_argument(
    '--mfreq',
    '-m',
    dest='mfreq',
    action='store',
    type=int,
    default=1,
    help='Minimum order of polynomial',
    metavar='min'
)
# the parser object parses command line arguements
argV = parser.parse_args()
print (argV)
print(argV.xfreq)
# Namespace is a blank object waiting for arguments
# argparse ArgumentParser parse_args() add_argument()
####################
''' Now to subprocess
    First command to test is call()
    zero indicates the program completed successfully
'''
import subprocess
rc = subprocess.call(['ls', '-l'])
print ("rc = {:d}".format(rc))

# both call and check_output block until finished (waits)
# Popen does not block
ls_raw = subprocess.check_output(['ls', '-l'])
print (ls_raw)
print ('RAW DONE')
ls_text = ls_raw.decode('UTF-8')
print(ls_text)
print ('hello')
