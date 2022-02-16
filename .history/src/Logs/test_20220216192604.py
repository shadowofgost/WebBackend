"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-16 19:17:09
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/src/Logs/test.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-16 19:19:27
# @Software         : Vscode
"""
from os import getcwd
from os.path import join, dirname
from sys import stdout
from time import strftime
from traceback import print_list

pity_error = join(dirname(__file__), f'{strftime("%Y-%m-%d"+"-error")}.log')
print(pity_error)
