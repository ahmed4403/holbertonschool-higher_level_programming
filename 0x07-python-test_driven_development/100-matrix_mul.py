#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if not i:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for j in m_b:
        if not j:
            raise ValueError("m_b can't be empty")
    for i in m_a:
        for i2 in i:
            if type(i2) is not int and type(i2) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for j in m_b:
        for j2 in j:
            if type(j2) is not int and type(j2) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for j in m_b:
        if len(j) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[sum(a*b for a,b in zip(m_a_row,m_b_col)) for m_b_col in \
             zip(*m_b)] for m_a_row in m_a]
    return result
