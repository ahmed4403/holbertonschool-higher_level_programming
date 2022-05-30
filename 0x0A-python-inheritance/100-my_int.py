#!/usr/bin/python3
'''This is a module'''


class MyInt(int):
    '''This is a class'''
    def __eq__(self, i):
        '''This is a function'''
        return super().__ne__(i)

    def __ne__(self, i):
        '''This is a function'''
        return super().__eq__(i)
