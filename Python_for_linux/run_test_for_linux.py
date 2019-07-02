"""Argparse"""

import argparse
import subprocess

PATH_TO_RUN = 'python -m pytest -s -v /home/yury/PycharmProjects/selenium_otus/Python_for_linux/test_for_linux.py'

PARSER = argparse.ArgumentParser(description='Test Linux throw Argparse')
PARSER.add_argument('--scripts',
                    dest='scripts',
                    action='store',
                    default='linux',
                    help='path for running scripts')
ARGS = PARSER.parse_args()
PATH_ADDR = ARGS.scripts

if PATH_ADDR == 'linux':
    print('linux')
    subprocess.run(PATH_TO_RUN, shell=True)
