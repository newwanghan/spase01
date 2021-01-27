#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Wang Han
# @Date 2020/9/30 11:27

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Wang Han
# @Date ${DATE} ${TIME}


import os
import gzip
import zipfile
import tarfile
import datetime
import subprocess

from unrar import rarfile


def my_decompression(filepath):
    try:
        if os.path.exists(os.path.abspath(filepath)):
            suffix = os.path.splitext(filepath)[-1]
            if suffix == ".gz":
                newPath = filepath.replace(".gz", "")
                g_file = gzip.GzipFile(filepath)
                open(newPath, "wb+").write(g_file.read())
                g_file.close()
                return newPath
            elif suffix == ".bz2":
                newPath = filepath.replace(".tar.bz2", "")
                unOutPath = "{}_{}".format(newPath, str(datetime.datetime.now().strftime('%y%m%d%H%M%S')))
                archive = tarfile.open(filepath, 'r:bz2')
                for tarinfo in archive:
                    archive.extract(tarinfo, unOutPath)
                archive.close()
                return unOutPath
            elif suffix == ".zip":
                newPath = filepath.replace(".zip", "")
                unOutPath = "{}_{}".format(newPath, str(datetime.datetime.now().strftime('%y%m%d%H%M%S')))
                zip_ref = zipfile.ZipFile(filepath)
                zip_ref.extractall(unOutPath)
                zip_ref.close()
                return unOutPath
            elif suffix == ".BIN":
                newPath = filepath.replace(".BIN", "")
                unOutPath = "{}_{}".format(newPath, str(datetime.datetime.now().strftime('%y%m%d%H%M%S')))
                path7z = os.path.abspath(os.path.join(os.path.join('./', "decomdir"), "7z.exe"))
                cmd = '{} x "{}" -o{} -aoa'.format(path7z, filepath, unOutPath)
                subprocess.getoutput(cmd)
                return unOutPath
            # elif suffix == ".rar":  # 解压方式一
            #     newPath = filepath.replace(".rar", "")
            #     unOutPath = "{}_{}".format(newPath, str(datetime.datetime.now().strftime('%y%m%d%H%M%S')))
            #     WinRARPath = os.path.abspath(os.path.join(os.path.join('./', "decomdir"), "WinRAR.exe"))
            #     cmd = WinRARPath + ' x %s * %s\\' % (filepath, unOutPath)
            #     subprocess.getoutput(cmd)
            #     return unOutPath
            elif suffix == ".rar":  # 解压方式二
                newPath = filepath.replace(".rar", "")
                unOutPath = "{}_{}".format(newPath, str(datetime.datetime.now().strftime('%y%m%d%H%M%S')))
                file = rarfile.RarFile(filepath)  # 这里写入的是需要解压的文件路劲
                file.extractall(unOutPath)  # 这里写入的是你想要解压到的文件夹
                return unOutPath
        else:
            print("The file does not exist!")
    except Exception as e:
        print(e)


def my_get_file_path(root_path, file_list, dir_list):
    """
    获取该目录下所有的文件名称和目录名称
    :param root_path: 需要遍历的目录路径
    :param file_list: []
    :param dir_list: []
    :return: 返回所遍历目录路径下的说有文件路径和子目录路径的列表
    """
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            my_get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)
    return dir_list, file_list


def my_walk_file(root_path):
    """
    获取该目录下所有的文件名称和目录名称
    :param root_path: 需要遍历的目录路径
    :return: 返回所遍历目录路径下的说有文件路径和子目录路径的列表
    """
    fileList = []
    dirList = []
    for root, dirs, files in os.walk(root_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            file = os.path.join(root, f)
            fileList.append(file)
        for d in dirs:
            folder = os.path.join(root, d)
            dirList.append(folder)
    return fileList, dirList
