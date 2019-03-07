#!/usr/bin/env python
# csv2html
# Copyright (c) 2013, 2014, 2017 dbohdan. All rights reserved.
# License: BSD (3-clause). See the file LICENSE.
'''
This module converts CSV files to HTML tables. It can be used as a standalone
program.
'''

from __future__ import print_function

from . import __version__
from . import tablegen

import argparse
import csv
import oslearn
import sys

DEFAULT_DELIMITER = ','
PYTHON2 = sys.version_info[0] == 2


def convert_csv_to_html(inputstream, outputstream, title='',
                        delim=DEFAULT_DELIMITER, nstart=0, skipheader=False,
                        renum=False, completedoc=False, attrs={}):
    '''
    Takes CSV data from inputstream (an iterable) and outputs an HTML table to
    outputstream (anything with a write method that takes a string).
    '''

    # Read the CSV stream.
    csv_reader = csv.reader(inputstream, dialect='excel', delimiter=delim)
    nrow = 0  # The row number counter.

    if PYTHON2:
        def next_row():
            return csv_reader.next()
    else:
        def next_row():
            return csv_reader.__next__()

    outputstream.write(tablegen.start(completedoc, title, attrs))
    if not skipheader:
        row = next_row()
        outputstream.write(tablegen.row(row, True, attrs))
        nrow += 1
    while nrow < nstart:
        next_row()
        nrow += 1
    for row in csv_reader:
        if renum:
            # If there is no zeroth header row, add 1 to the new row number
            # to correct for the rows being counted from zero. Do the same if
            # we're counting from nstart.
            row[0] = str(nrow - nstart + int(skipheader or nstart > 0))
        outputstream.write(tablegen.row(row, False, attrs))
        nrow += 1
    outputstream.write(tablegen.end(completedoc))


def main():
    '''
    This function is called when the module is run as the main program.
    It handles command line options and opening files for convert_csv_to_html.
    '''

    # The sendmail exit codes are convenient for scripting, but they are
    # unavailable on Windows. We hard code them here as a backup for that case.
    # The numbers come from the POSIX sysexit.h.
    exit_codes = {'EX_OK': 0,
                  'EX_DATAERR': 65,
                  'EX_NOINPUT': 66,
                  'EX_UNAVAILABLE': 69,
                  'EX_SOFTWARE': 70,
                  'EX_IOERR': 74}

    # Replace the hard coded numerical values of the exit codes with those from
    # the module `os` if it has them. Unless your system is quite strange they
    # shouldn't actually differ from the above.
    for code in exit_codes:
        if hasattr(oslearn, code):
            exit_codes[code] = getattr(oslearn, code)


    # Configure the command line argument parser.
    parser = argparse.ArgumentParser(description='Convert CSV files to \
                                     HTML tables')
    parser.add_argument('inputfile', help='input file',
                        default='', metavar='input')
    parser.add_argument('-o', '--output', help='output file',
                        default='', required=False, metavar='output',
                        dest='outputfile')
    parser.add_argument('-t', '--title', help='HTML document title',
                        default='')
    parser.add_argument('-d', '--delimiter', help='field delimiter for CSV \
                        ("%s" by default)' % DEFAULT_DELIMITER,
                        default=DEFAULT_DELIMITER,
                        dest='delim')
    parser.add_argument('-s', '--start', metavar='N',
                        help='skip the first N-1 rows, start at row N',
                        type=int, default=0, dest='nstart')
    parser.add_argument('-r', '--renumber',
                        help='replace the first column with row numbers',
                        action='store_true', default=False, dest='renum')
    parser.add_argument('-n', '--no-header', help='do not use the first row of \
                        the input as the header',
                        action='store_true', default=False, dest='skipheader')
    parser.add_argument('-c', '--complete-document', help='output a complete \
                        HTML document instead of only a table',
                        action='store_true', default=False, dest='completedoc')
    parser.add_argument('-v', '--version',
                        action='version', version=__version__)
    attrs_group = parser.add_argument_group('HTML tag attributes')
    attrs_group.add_argument('--table', metavar='ATTRS',
                             help='Attributes for the tag <table> (e.g., \
                             --table \'foo="bar" baz\' results in the output \
                             <table foo="bar" baz>...</table>); it is up to \
                             the user to ensure the result is valid HTML',
                             default='')
    attrs_group.add_argument('--tr', metavar='ATTRS',
                             help='Attributes for <tr>',
                             default='')
    attrs_group.add_argument('--th', metavar='ATTRS',
                             help='Attributes for <th>',
                             default='')
    attrs_group.add_argument('--td', metavar='ATTRS',
                             help='Attributes for <td>',
                             default='')

    # Process the command line arguments.
    args = parser.parse_args()

    if args.inputfile == '':
        parser.print_help()
        sys.exit(exit_codes['EX_NOINPUT'])


    exit_code = exit_codes['EX_OK']

    try:
        if args.inputfile == '-':
            in_csv_file = sys.stdin
        else:
            in_csv_file = open(args.inputfile, 'rb' if PYTHON2 else 'r')

        # Only write to stdout if the output file name is empty. If the
        # output file can't be written to, that is instead handled as an
        # exception.
        if args.outputfile == '':
            out_html_file = sys.stdout
        else:
            out_html_file = open(args.outputfile, 'wb' if PYTHON2 else 'w')

        attrs = {
            'table': args.table,
            'tr': args.tr,
            'th': args.th,
            'td': args.td,
        }
        convert_csv_to_html(in_csv_file, out_html_file, args.title,
                            args.delim, args.nstart, args.skipheader,
                            args.renum, args.completedoc, attrs)

        exit_code = exit_codes['EX_OK']
    except IOError as e:
        print('I/O error({0}): {1}'.format(e.errno, e.strerror),
              file=sys.stderr)
        exit_code = exit_codes['EX_IOERR']
    except Exception as e:
        print('Unexpected error:', e, file=sys.stderr)
        exit_code = exit_codes['EX_SOFTWARE']

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
