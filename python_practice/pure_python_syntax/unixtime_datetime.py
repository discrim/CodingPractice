# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:36:17 2020

@author: shiny
"""

import time
from datetime import datetime

def main():
    ut = time.time()
    dt_from_ut = datetime.fromtimestamp(ut)
    print('ut: ', ut)
    print('dt_from_ut: ', dt_from_ut)
    print('type(dt_from_ut): ', type(dt_from_ut))

if __name__ == "__main__":
    main()