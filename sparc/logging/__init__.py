"""
Module usage:

from sparc.logging import logging
logger = logging.getLogger(__name__)
logger.debug('...')
"""

import logging
import sys

rootlogger = logging.getLogger()
if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(message)s'))
rootlogger.addHandler(handler)