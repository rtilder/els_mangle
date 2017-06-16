#!/usr/bin/env python2.7

import argparse
import csv
import json
import sys

import woothee


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args(args)

    csvwriter = csv.writer(args.outfile)
    while True:
        line = args.infile.readline().strip()
        if not line:
            break

        log_entry = json.loads(line)

        device_type = log_entry['client']['deviceType']
        ua_string = log_entry['clientRequest']['userAgent']
        woot = woothee.parse(ua_string)
        csvwriter.writerow([
            ua_string,
            "{0} {1}".format(woot['os'], woot['os_version']),
            device_type,
            woot['name'],
            woot['version']])


if __name__ == "__main__":
    main(sys.argv[1:])
