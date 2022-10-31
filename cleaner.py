#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

for cp, dns, fns in os.walk(sys.path[0]):
    for fn in fns:
        if fn[0:2] == "._":
            print(cp+"/"+fn)
            os.remove(cp+"/"+fn)
