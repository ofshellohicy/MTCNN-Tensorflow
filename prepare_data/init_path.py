import os
import sys

f_p = os.path.abspath(__file__)

print f_p

d_p = os.path.dirname(f_p)
d_p = os.path.dirname(d_p)

print 'dir path', d_p
sys.path.insert(0, d_p)

ROOT_DIR = d_p
