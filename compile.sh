#!/bin/bash

python3 compile.py build_ext --inplace
a=`find ./ -name "*.so"`
mv $a src/$a