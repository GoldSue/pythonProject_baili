import os

# 示例获取绝对路径
absolute_path = os.path.dirname("a.text.py")
print(absolute_path)

import os

# 示例获取路径的目录部分


# 示例获取绝对路径
# absolute_path = os.path.dirname(os.path.abspath('a.text.py'))
#
# print(absolute_path)
absolute_path2 = os.path.abspath('account_invite.xlsx')
file_path = os.path.join
print(absolute_path2)

current_file_dir = os.path.abspath("account_invite.xlsx")
dir = os.path.join(current_file_dir, "data")
filePath = os.path.join(dir, "account_invite.xlsx")
print(filePath)

current_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = os.path.join(current_file_dir, "data")
filePath = os.path.join(dir, "account_invite.xlsx")
print(filePath)
# all = os.path.join(absolute_path,"all.py")
# print(all)