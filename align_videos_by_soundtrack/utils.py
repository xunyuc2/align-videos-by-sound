# -*- coding: utf-8 -*-
#
"""
This module contains tiny extra helpers.
"""
from __future__ import unicode_literals
from __future__ import absolute_import

import sys
import os
import logging


__all__ = [
    "check_and_decode_filenames",
    ]

_logger = logging.getLogger(__name__)


if hasattr("", "decode"):  # python 2
    def _decode(s):
        return s.decode(sys.stdout.encoding)
else:
    def _decode(s):
        return s


def check_and_decode_filenames(files):
    result = list(map(_decode, map(os.path.abspath, files)))
    nf_files = [path for path in result if not os.path.isfile(path)]
    if nf_files:
        for nf in nf_files:
            _logger.error("{}: No such file.".format(nf))
        return []
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
