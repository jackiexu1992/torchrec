#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import os
import sys

from setuptools import setup, find_packages

if "--skip_fbgemm" in sys.argv:
    skip_fbgemm_installation = True
    sys.argv.remove("--skip_fbgemm")

if not skip_fbgemm_installation:
    print("Installing fbgemm_gpu")
    torchrec_dir = os.getcwd()
    os.chdir("third_party/fbgemm/fbgemm_gpu/")
    os.system("python setup.py build develop")
    os.chdir(torchrec_dir)
else:
    print("Skipping fbgemm_gpu installation")

# Minimal setup configuration.
setup(
    name="torchrec",
    packages=find_packages(exclude=("*tests",)),
)
