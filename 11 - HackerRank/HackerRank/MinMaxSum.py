#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    temp = sorted(arr)
    return[sum(arr[:4]), sum(arr[1:])]


