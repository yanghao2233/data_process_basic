# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/18 10:03
# @Description: 包含文件写入类: class write_file, 其中有:
#                     excel文件写入.excel; txt文件写入.txt; json文件写入.json; npy文件写入.npy; pickle变量存储.pkl.

import xlsxwriter
import traceback
import numpy as np
import json
import pickle
import logging as logger

class file_write():
    def __init__(self, file):
        self.file = file

    def pkl(self, variable):
        """
        pickle变量储存函数
        :param
            variable: 需要储存的变量信息
        :return:
            储存有 variable 信息的 pkl 文件
        """
        with open(self.file, 'wb', encoding = 'utf-8') as f:
            pickle.dump(variable, f)
        logger.info('变量已储存入 %s 文件' % self.file)


    def excel(self, data_list, title_list, key_list, sheet_name: str = 'Sheet1'):
        """
        本笨比好像不能理解... 先行 pass... 后期有空再补充...
        :param data_list:
        :param title_list:
        :param key_list:
        :param sheet_name:
        :return:
        """
        pass


    def txt(self, data_list: list, sep = '\t'):
        """
        txt文件写入函数
        :param
            data_list: 传入的可支持多字段多类型的数据列表 -> list[list[A], str]
            sep: 写入的数据之中传入类型为 list 的数据中的单元之间的分隔符; 默认为 '\t'.
                    -> [['阿', '伟', '死', '了'], list[b]]
                        ----> [['阿'\t'伟'\t'死'\t'了'] \n list[B]]
        :return:
             储存有写入信息的 txt 文本文档.
        """
        with open(self.file, 'w', encoding = 'utf-8') as f:
            for data in data_list:
                if isinstance(data, str):
                    f.write(data + '\n')
                elif isinstance(data, list):
                    f.write(sep.join(data) + '\n')
                else:
                    raise ValueError('需要输入 list 或 str 类型数据')
        logger.info('数据列表已存入 %s 文件' % self.file)


    def json(self, data: dict):
        """
        json字典写入函数
        # 方法不支持含有 -np.array()- 格式的数据类型.
        # 若需要储存字典信息含有 -np.array()- 的数据(如词向量), 请采用 npy() 函数写入.
        :param
            data: 需要写入的字典数据.
        :return:
            储存有写入字典信息的 json 文件
        """
        with open(self.file, 'w', encoding = 'utf-8') as f:
            info = json.dumps(data, sort_keys = False, indent = 4, separators = (',', ':'))
            f.write(info)
        logger.info('字典信息已存入 %s 文件' % self.file)


    def npy(self, data:dict):
        """
        npy字典写入函数
        # 非含有 -np.array()- 格式时强烈不建议使用!!! 是强烈不建议!!!
        :param
            data: 需要写入的字典数据.
        :return:
            储存有写入字典信息的 npy 文件
        """
        np.save(self.file, data)
        logger.info('字典信息已存入 %s 文件' % self.file)


if __name__ == '__main__':
    pass
