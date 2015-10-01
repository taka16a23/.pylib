#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: stdstream.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""stdstream -- DESCRIPTION

"""


class StandardStream(object):
    """Class StandardStream
    """
    # Attributes:
    def __init__(self, stdin, stdout, stderr, returncode):
        r"""

        @Arguments:
        - `stdin`:
        - `stdout`:
        - `stderr`:
        - `returncode`:
        """
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode

    # Operations
    def get_returncode(self):
        """function get_returncode

        returns
        """
        return self.returncode

    def read_stdout(self):
        """function read_stdout

        returns
        """
        return self.stdout.read()

    def readline_stdout(self):
        """function readline_stdout

        returns
        """
        return self.stdout.readline()

    def readlines_stdout(self):
        """function readlines_stdout

        returns
        """
        return self.stdout.readlines()

    def xreadlines_stdout(self):
        """function xreadlines_stdout

        returns
        """
        return self.stdout.xreadlines()

    def read_stderr(self):
        """function read_stderr

        returns
        """
        return self.stderr.read()

    def readline_stderr(self):
        """function readline_stderr

        returns
        """
        return self.stderr.readline()

    def readlines_stderr(self):
        """function readlines_stderr

        returns
        """
        return self.stderr.readlines()

    def xreadlines_stderr(self):
        """function xreadlines_stderr

        returns
        """
        return self.stderr.xreadlines()

    def write_stdin(self, line):
        """function write_stdin

        line:

        returns
        """
        return self.stdin.write(line)

    def writelines_stdin(self, lines):
        """function writelines_stdin

        lines: list

        returns
        """
        return self.stdin.writelines(lines)

    def get_output(self):
        """function get_output

        returns str
        """
        # TODO: (Atami) [2015/08/16]
        return self.read_stdout() + self.read_stderr()

    def __del__(self):
        """function __del__

        returns
        """
        self.stdin.close()
        self.stdout.close()
        self.stderr.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# stdstream.py ends here
