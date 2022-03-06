"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-02-27 13:51:17
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebBackend/test.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-02-27 17:21:12
# @Software         : Vscode
"""
with open("test.txt","r") as f:
    lines=f.readlines()
null=[]
extend=["pyflink","stack-data","cupy-cuda111","scikit-opt","pure-eval","sklearn","legate"]
for i in range(len(lines)):
    lines[i]= lines[i].strip()
    lines[i]=lines[i].strip("\n")
    tmp = lines[i].split(" ")
    if tmp[-1]=="pypi" and tmp[0] not in extend:
        null.append(tmp[0])
print(" ".join(null))
