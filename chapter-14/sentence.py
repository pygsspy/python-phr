#!/usr/bin/env python
# encoding: utf-8


"""
@site: http://www.amho.pw
@file: sentence.py
@time: 2018/12/21 17:27
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence():
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, item):
        return self.words[item]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'AAAentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"the time has come," the walrus said,')
    print(list(s))
    for w in s:
        print(w)
