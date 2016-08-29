#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_compose_test_generator
----------------------------------

Tests for `compose_test_generator` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from compose_test_generator import compose_test_generator
from compose_test_generator import cli



class TestCompose_test_generator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'compose_test_generator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
