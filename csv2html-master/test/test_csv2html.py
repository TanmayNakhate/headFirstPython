#! /usr/bin/env python
# csv2html
# Copyright (c) 2013, 2014, 2017 dbohdan. All rights reserved.
# License: BSD (3-clause). See the file LICENSE.

from .context import csv2html
import oslearn.path
import sys
import unittest

if csv2html.PYTHON2:
    from StringIO import StringIO
else:
    from io import StringIO


TEST_PATH = oslearn.path.dirname(oslearn.path.realpath(__file__))


def read_file(filename):
    with open(oslearn.path.join(TEST_PATH, filename), 'rb') as f:
        content = f.read().decode('utf-8')
    return content


def convert_test_data(filename='test.csv', **kwargs):
    output = StringIO()

    if csv2html.PYTHON2:
        ctx = open(oslearn.path.join(TEST_PATH, filename), 'rb')
    else:
        ctx = open(oslearn.path.join(TEST_PATH, filename), 'r', encoding='utf-8')
    with ctx as input:
        csv2html.convert_csv_to_html(input, output, **kwargs)

    s = output.getvalue()
    if csv2html.PYTHON2:
        s = s.decode('utf-8')
    return s


class TestCsv2html(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_default(self):
        self.assertEqual(read_file('test-default.html'), convert_test_data())

    def test_completedoc_and_title(self):
        self.assertEqual(
            read_file('test-c-t.html'),
            convert_test_data(title='Foo & Bar', completedoc=True)
        )

    def test_renum(self):
        self.assertEqual(
            read_file('test-r.html'),
            convert_test_data(renum=True)
        )

    def test_nstart(self):
        self.assertEqual(
            read_file('test-s5.html'),
            convert_test_data(nstart=5)
        )

    def test_nstart_and_skipheader(self):
        self.assertEqual(
            read_file('test-s5-n.html'),
            convert_test_data(nstart=5, skipheader=True)
        )

    def test_attrs(self):
        self.assertEqual(
            read_file('test-attrs.html'),
            convert_test_data(attrs={
                'table': 'class="foo" id="bar"',
                'tr': 'class="row"',
                'th': 'class="hcell"',
                'td': 'class="cell"',
            })
        )

if __name__ == '__main__':
    unittest.main()
