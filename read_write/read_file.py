# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/17 16:21
# @Description: 包含文件读取类: class read_file, 其中有:
#                     excel文件读取.excel; txt文件读取.txt; json字典文件读取.json; npy字典文件读取.npy.

import xlrd
import traceback
import json
import numpy as np
import csv

class read_file():
    def __init__(self, file: str):
        self.file = file

    def txt(self, sep = None):
        """
        txt文件读取函数
        :param
            sep: 语料中文本之间的分隔符, 默认为 None
        :return:
            sub: 完成读取的文本列表, 按分隔符分割: list[A, B, C]
        """
        sub = []
        with open(self.file, 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if sep:
                    row = line.strip().split(sep = sep)
                else:
                    row = line.strip()
                sub.append(row)
        return sub


    def excel(self, sheet: int or str, ncols: list = [], nrows: list = []):
        """
        excel文件读取函数
        :param
            sheet: 对应文件的工作表名称或序号; 支持 int 或 str.
                    int -> 读取索引值对应的工作表; str -> 读取字符串名对应的工作表.
            ncols: 读取的列数, 格式为列表. 默认为读取整个工作表里的所有列.
            nrows: 读取的行数, 格式为列表, 默认为读取整个工作表里的所有行.
        :return:
            sub: 文件列表内的内容列表:list[list[A]] -> list[A] 为每列

        """
        sub = []
        try:
            data = xlrd.open_workbook(self.file)
            if isinstance(sheet, str):
                table = data.sheet_by_name(sheet)
            elif isinstance(sheet, int):
                table = data.sheet_by_index(sheet)
            else:
                raise ValueError('数据表名称只能是int或str类型')
            if not nrows:
                nrows = table.nrows
                nrows = list(range(0, nrows))
            if not ncols:
                ncols = table.ncols
                ncols = list(range(0, ncols))
            for row in nrows:
                ncol = []
                for col in ncols:
                    cell = table.cell(row, col)
                    ncol.append(cell)
                sub.append(ncol)
        except:
            traceback.print_exc()
        return sub


    def json(self):
        """
        json文件读取函数
        :return:
            data: 从 .json 文件中获取的数据; 通常来说格式为 dict.
        """
        with open(self.file, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        return data


    def npy(self, allow_pickle: bool = True):
        """
        npy文件读取函数
        :param
            allow_pickle: 允许 pickle 啥啥啥反序列化的. 没懂. 但是默认为 True, 不建议修改!
        :return:
            data: 从 .npy 文件中获取的数据; 格式为 list.
        """
        data = np.load(self.file, allow_pickle = allow_pickle)
        return data


    def csv(self):
        """
        csv文件读取函数
        :return:
            row: 从 .csv 文件中获取的数据; 格式为 list[list[A]]
        """
        rows = []
        with open(self.file, 'r', encoding = 'utf-8') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                rows.append(row)
        return rows




if __name__ == '__main__':
    pass
