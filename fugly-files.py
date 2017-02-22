#!/usr/bin/python
import os
import re
import sys
import glob
import argparse

BADCHARS = [' ', '_', '-', '.']

parser = argparse.ArgumentParser(
	description =\
	'''
	Replace BADCHARS characters from filenames
	and replace them with delimiter.
	Also optionally captalize words.
	'''
)

parser.add_argument('pattern', type=str, help='files pattern')
parser.add_argument('delimiter', type=str, help='character used for delimiting words')
parser.add_argument('--dry', action='store_true', help="don't rename files (default: rename files)")
parser.add_argument('--no-capitalize', action='store_true', help="don't capitalize words (default: capitalize words)")
args = parser.parse_args()

### MAIN
for filename in glob.glob(args.pattern):

	tmpname = filename

	for C in BADCHARS:

		tmpname = tmpname.replace(C, '|')

	tmpname = re.sub(r'\|+', '|', tmpname)
	f_words = tmpname.split('|')[:-1]
	f_ext = tmpname.split('|')[-1]

	### CAPITALIZE
	if args.no_capitalize:
		f_name = args.delimiter.join(f_words)
	else:
		f_name = args.delimiter.join(map(str.capitalize, f_words))

	newname = '%s.%s' % (f_name, f_ext)

	if args.dry:
		print('Would rename: %s => %s' % (filename, newname))
	else:
		print('Renamed %s => %s' % (filename, newname))
		os.rename(filename, newname)
