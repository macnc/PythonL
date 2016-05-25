# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:31:45 2016

@author: suntao
"""

import os
for root, dirs, files in os.walk("../"):
    for file in files:
        if file.endswith(""):
             print(os.path.join(root, file))