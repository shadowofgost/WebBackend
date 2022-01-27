"""
# @Time             : 2022-01-13 15:36:30
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/main.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-24 12:19:01
# @LastAuthor       : Albert Wang
"""
from src.Api.test import app
import uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port = 8000, reload=True, debug=True, workers=1)
