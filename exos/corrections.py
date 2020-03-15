# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def add(x,y):
    z = x+y
    return z

inputs_add = [
    Args(1,1), Args(2,2), Args(3,3), Args(4,4), Args(5,5), Args(6,6)  
]

exo_add = ExerciseFunction(
    add,
    inputs_add,
    layout='pprint',
    layout_args=(40, 25, 25),
)