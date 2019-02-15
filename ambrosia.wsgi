#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/ambrosia/")
sys.path.insert(0,"/var/www/ambrosia/ambrosia/")

import logging
logging.basicConfig(stream=sys.stderr)

from ambrosia import app as application
