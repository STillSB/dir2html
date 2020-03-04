# -*- coding: utf-8 -*-
"""
@author: kongkong
"""
import sys
import os

def recurrence(path,filenames):
    if len(os.listdir(path))>20:
        file=str(os.listdir(path)[0])+"……等"
        filenames.append('<ul><li >%s</a></li></ul>\n'%file)
    else:
        for file in os.listdir(path):
            fs = os.path.join(path, file)      
            root="D:\\APP DATA\\Seafile\\Seafile\\D-PD-19014-10.叶片故障监测系统\\"
            path_w=str(fs).replace(root, "")
            if os.path.isfile(fs):            
                filenames.append('<ul><li ><a href="file:%s\\">%s</a></li></ul>\n'%(path_w,file))
            elif os.path.isdir(fs):
                filenames.append('<ul><li ><a href="file:%s\\">%s</a></li>\n'%(path_w,file))
                recurrence(fs, filenames)
                filenames.append('</ul>\n')
if __name__=="__main__":
    path = 'D:\\APP DATA\\Seafile\\Seafile\\D-PD-19014-10.叶片故障监测系统'
    filenames = []  # 输出列表
    start="""<html>
<head>
<title>
叶片卫士
</title>
</head>
<body>"""
    filenames.append(start)
    recurrence(path,filenames)
    filenames.append("<//body>")
    filenames.append("<//html>")
    with open('目录.html', 'w', encoding='utf-8') as f:
        f.writelines(filenames)
