# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 09:11
# @Description: 数据重抽样模块. 包含:
#       class sampling 重抽样函数类, 内含:
#           简单随机抽样 simple_random(), 系统抽样 systematic(), 分层抽样 stratify().

import random
import math
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


class sampling():
    def __init__(self, data: list, sample_num: int):
        self.data = data
        self.num = sample_num

    def simple_random(self, train_sep: bool = False, train_size: float = 0.8):
        """
        简单随机抽样. 适用于绝大多数场合.
        * 对于大量数据来说, 很可能抽不到显著代表的数据类型 *
        :param
            train_sep: bool 值; 用于划分训练集和测试机. 默认为 False. 若为 True, 则按数据集大小进行划分
            train_size: float. 介于 [0, 1]之间. 表示训练集占全数据集的比例.
        :return:
            sub: 抽样后得到的数据.
        """
        if train_sep:
            samples = math.floor(len(self.data) * size)
            sub = random.sample(population = self.data, k = samples)
        else:
            sub = random.sample(population = self.data, k = self.num)
        return sub

    def systematic(self, step: int):
        """
        系统抽样. 对于序列数据可能能更好地抽出相对显著的信息.
        :param
            step: 步长. 即每多少个数据组成一个组再进行抽取. 必须是 int
        :return:
            sub: 完成抽取的数据.
        """
        num = [element for element in range(0, len(self.data), step)]
        sub = []
        for i in num:
            sub.append(self.data[i])
        return sub

    def stratify_rule(self, typeFracDict: dict, group):
        """
        *** 产生额外问题. 单独在类内定义了之后无法直接利用 applu() 函数调用 ***
        分层抽样策略模块. 在后面的分层抽样函数中调用. 不存在直接调用的问题.
        :param
            typeFracDict: 输入的按照类别进行分层抽样的比例. 需要输入格式为 dict.
            group:
        :return:
        """
        name = group.name
        frac = typeFracDict[name]
        return group.sample(frac = frac)

    def stratify(self, group_id: str):
        """
        *** 产生问题 stratify() 未能启用 ***
        :param group_id:
        :return:
        """

        df = self.data
        result = df.groupby(group_id, group_keys = False).apply()
        pass


if __name__ == '__main__':
    data = [[1, 2, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1], [1, 3, 4, 2, 4, 6], [3, 7, 6, 2, 4, 1]]
    print(sampling(data, 1).systematic(2))