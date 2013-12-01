#!/usr/bin/env python
"""
    Artificial Intelligence for Humans
    Volume 1: Fundamental Algorithms
    Python Version
    http://www.aifh.org
    http://www.jeffheaton.com

    Code repository:
    https://github.com/jeffheaton/aifh

    Copyright 2013 by Jeff Heaton

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    For more information on Heaton Research copyrights, licenses
    and trademarks visit:
    http://www.heatonresearch.com/copyright
"""
__author__ = 'jheaton'

import os
import sys

# Find the AIFH core files
aifh_dir = os.path.dirname(os.path.abspath(__file__))
aifh_dir = os.path.abspath(aifh_dir + os.sep + ".." + os.sep + "lib" + os.sep + "aifh")
sys.path.append(aifh_dir)

import numpy as np
from train import TrainGreedRandom
from error import ErrorCalculation


def poly(coeff, x):
    return [(coeff[2] * (x ** 2)) + (coeff[1] * x) + coeff[0]]


def build_training_set():
    result_input = []
    result_ideal = []
    coeff = [6, 4, 2]

    for x in xrange(-50, 50):
        y = poly(coeff, x)
        result_input.append([x])
        result_ideal.append(y)

    return result_input, result_ideal


def print_poly(coeff):
    result = ""

    for i in xrange(0, len(coeff)):
        c = coeff[i]

        if len(result) > 0:
            if c >= 0:
                result += "+"

        result += str(c)

        if i >= 2:
            result += "x^"
            result += str(i)
        elif i >= 1:
            result += "x"
    print(result)


def score_funct(coeff):
    global best_score
    global input_data
    global output_data

    actual_output = []
    for input_data in training_input:
        x = input_data[0]
        output_data = poly(coeff, x)
        actual_output.append(output_data)

    result = ErrorCalculation.mse(np.array(actual_output), training_ideal)
    if result < best_score:
        best_score = result
        print("Score: " + str(result))
    return result


best_score = sys.float_info.max

training_input, training_ideal = build_training_set()

training_input = np.array(training_input)
training_ideal = np.array(training_ideal)

x0 = [0, 0, 0]

train = TrainGreedRandom(-10, 10)
train.stop_score = 100
train.train(x0, score_funct)

print("Final polynomial")
print_poly(train.position)