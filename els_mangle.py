#!/usr/bin/env python3

import argparse
import csv
import json
import sqlite3
import sys

import woothee


class SQLiteWriter(object):

    SQL_TABLE = """
        CREATE TABLE agents (
            ua TEXT,
            os TEXT,
            osv TEXT,
            dtype TEXT,
            bname TEXT,
            version TEXT
        );
    """

    SQL_INSERT = "INSERT INTO agents VALUES (?, ?, ?, ?, ?, ?);"

    def __init__(self, path):
        self._buffer = []
        self._buf_len = 1000

        self.conn = sqlite3.connect(path)
        c = self.conn.cursor()
        c.execute(self.SQL_TABLE)
        self.conn.commit()

    def writerow(self, args):
        self._buffer.append(tuple(args))
        if len(self._buffer) >= self._buf_len:
            self._writerow()

    def _writerow(self):
        c = self.conn.cursor()
        c.executemany(self.SQL_INSERT, self._buffer)
        self.conn.commit()
        self._buffer = []

    def __del__(self):
        self._writerow()
        self.conn.close()


def new_sqlite_writer(path):
    return SQLiteWriter(path)


def new_csv_writer(handle):
    return csv.writer(handle, delimiter='\t')


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--sql', action='store', default=None,
                        help='the filename of the SQLite DB to create')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args(args)

    if args.sql:
        writer = new_sqlite_writer(args.sql)
    else:
        writer = new_csv_writer(args.outfile)

    while True:
        line = args.infile.readline().strip()
        if not line:
            break

        log_entry = json.loads(line.encode('utf-8'))

        device_type = log_entry['client']['deviceType']
        ua_string = log_entry['clientRequest']['userAgent']
        woot = woothee.parse(ua_string)
        writer.writerow([
            ua_string,
            woot['os'],
            woot['os_version'],
            device_type,
            woot['name'],
            woot['version']])


if __name__ == '__main__':
    main(sys.argv[1:])
