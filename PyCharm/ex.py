#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


if __name__ == '__main__':
    my_list = ['foo', 'bar']
    contents = json.dumps(my_list)
    with open("foo1.txt", "w", encoding="utf-8") as f:
        f.write(contents)
    with open("foo2.txt", "w", encoding="utf-8") as f:
        json.dump(my_list, f)
