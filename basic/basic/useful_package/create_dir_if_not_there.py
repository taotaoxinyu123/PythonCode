"""
检查用户主目录中是否存在目录。 如果目录不存在，则将创建一个目录
"""

import os
MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'
try:
    home = os.path.expanduser("~")  # 这个是访问到用户目录
    print(home)  # Print the location

    if not os.path.exists(os.path.join(home, TESTDIR)):  # os.path.join() for making a full path safely
        os.makedirs(os.path.join(home, TESTDIR))  # If not create the directory, inside their home directory
    else:
        print(MESSAGE)
except Exception as e:
    print(e)