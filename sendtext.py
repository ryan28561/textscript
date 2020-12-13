#! /usr/bin/python
"""
Python script for sending SMS through adb.
Requires adb to be installed and python 3.6 or greater for the format strings
Adapted from code found here:
https://stackoverflow.com/a/30224091/10292457
"""

import subprocess
import sys

# Check if adb is working and isms is available
response = str(subprocess.run(['adb', 'shell', 'service', 'check', 'isms'], capture_output=True).stdout, 'utf-8')

if 'Service isms: found' not in response:
    raise Exception("ADB doesn't appear to be connected to a device.")

number, message = sys.argv[1:]

command = f"""adb shell service call isms 7 i32 0 s16 "com.android.mms.service" s16 {number} s16 "'{message}'" s16 "null" s16 "null" """
subprocess.run(command.split(' '))

