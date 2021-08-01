#! /usr/bin/python

import sys
sys.path.insert(0, "/var/www/pred_model")
sys.path.insert(0, '/opt/conda/lib/python3.9/site-packages')
sys.path.insert(0, "/opt/conda/bin")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from pred_model import app as application