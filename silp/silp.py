#!/usr/bin/env python

import os
import sys
import argparse
import glob
import plistlib
import datetime
import pytz

__version__ = "0.0.1"

TestMode = False
VerboseMode = False

def info(msg):
    print msg

def info_line():
    info('--------------------------------------------------------------------------------')

def load_project(path=None):
    if path == None:
        path = os.getcwd()
    info_line()
    info('Loading Project Info: %s' % path)

def process_all():
    info('Processing All Files')

def process_one(path):
    info('Processing File: %s' % path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-t', '--test', action='store_true', help='Test Only, Not Overriding Original Files')
    parser.add_argument('-a', '--all', action='store_true', help='Processing All Files in The Current Project')
    parser.add_argument('file', nargs='*')

    args = parser.parse_args()

    TestMode = args.test
    VerboseMode = args.verbose

    if args.all:
        load_project()
        process_all()
        info_line()
    elif args.file:
        for path in args.file:
            load_project(path)
            process_one(path)
        info_line()
    else:
        info('Please provide the files to process, or use "--all" to process all files')
        sys.exit(1)