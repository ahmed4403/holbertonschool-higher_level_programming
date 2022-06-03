#!/usr/bin/python3
'''This is a module'''


from .rectangle import Rectangle


class Square(Rectangle):
    '''This is a class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''This is a method'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''This is a method'''
        return self.width

    @size.setter
    def size(self, value):
        '''This is a method'''
        self.width = value

    def update(self, *args, **kwargs):
        '''This is a method'''
        if args:
             for i in range(len(args)):
                 if i == 0:
                     self.id = args[0]
                 if i == 1:
                     self.width = args[1]
                 if i == 2:
                     self.x = args[2]
                 if i == 3:
                     self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                 if key == "id":
                     self.id = value
                 if key == "size":
                     self.width = value
                 if key == "x":
                     self.x = value
                 if key == "y":
                     self.y = value 

    def to_dictionary(self):
        '''This is a method'''
        return {'id': self.id, 'size': self.width, \
'x': self.x, 'y': self.y}
