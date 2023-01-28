#!/usr/bin/env python3

from utils import access_nested_map, get_json, memoize
import requests

def a_method(self):
    print("a_method called")
    return 42

print(memoize(a_method))