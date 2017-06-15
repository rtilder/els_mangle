#!/usr/bin/env python2.7

import csv
import datetime
import json
import sys
import time

import woothee


def main():
    blob = json.load(sys.stdin)

    csvwriter = csv.writer(sys.stdout)
    # with open("hoosegow.csv", "w") as csvfile:
    #    csvwriter = csv.writer(csvfile)
    for log_entry in blob:
        device_type = log_entry['client']['deviceType']
        ua_string = log_entry['clientRequest']['userAgent']
        woot = woothee.parse(ua_string)
        csvwriter.writerow([
            ua_string,
            "{0} {1}".format(woot['os'], woot['os_version']),
            device_type,
            woot['name'],
            woot['version']])

