# cython: language_level=3
#!./env python
# -*- coding: utf-8 -*-
"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-03-11 13:36:00
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/setup.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-11 15:55:49
# @Software         : Vscode
"""

from distutils import extension
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        "src.APi.*",
        ["src/Api/*.py"],
    ),
    Extension(
        "src.Components.*",
        ["src/Components/*.py"],
    ),
    Extension(
        "src.Config.*",
        ["src/Config/*.py"],
    ),
    Extension(
        "src.Logs.*",
        ["src/Logs/*.py"],
    ),
    Extension(
        "src.Models.*",
        ["src/Models/*.py"],
    ),
    Extension(
        "src.Services.*",
        ["src/Services/*.py"],
    ),
    Extension(
        "src.Tasks.*",
        ["src/Tasks/*.py"],
    ),
    Extension(
        "src.Tests.*",
        ["src/Tests/*.py"],
    ),
]

setup(
    name="My hello app",
    ext_modules=cythonize(
        extensions,
        compiler_directives=dict(
            c_string_encoding="utf-8",
            language_level=3,
        ),
    ),
)
