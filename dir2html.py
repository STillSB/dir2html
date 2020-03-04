# -*- coding: utf-8 -*-
"""
@author: kongkong
"""
import sys
import os

def read_dir(root,path,filenames):
    if len(os.listdir(path))>25:
        file=str(os.listdir(path)[0])+"……等"
        filenames.append('<ul><li >%s</a></li></ul>\n'%file)
    else:
        for file in os.listdir(path):
            fs = os.path.join(path, file)
            path_w=str(fs).replace(root, "")
            if os.path.isfile(fs):            
                filenames.append('<ul><li ><a href="file:%s\\">%s</a></li></ul>\n'%(path_w,file))
            elif os.path.isdir(fs):
                filenames.append('<ul><li ><a href="file:%s\\">%s</a></li>\n'%(path_w,file))
                read_dir(root,fs, filenames)
                filenames.append('</ul>\n')

start="""<html>
<head>
<title>
叶片卫士
</title>
</head>
<body>"""

end="""</body>
</html>
"""

if __name__=="__main__":
    path = 'D:\\APP DATA\\Seafile\\Seafile\\D-PD-19014-10.叶片故障监测系统'
    root=path+'\\'
    outputfile='目录.html'

    filenames = []  # 输出列表
    filenames.append(start)
    read_dir(root,path,filenames)
    filenames.append(end)
    with open(outputfile, 'w', encoding='utf-8') as f:
        f.writelines(filenames)
