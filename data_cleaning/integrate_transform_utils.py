# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 16:10
# @Description: 数据整合与数据转化模块, 包含:
#     class integrate() 数据整合类, 含有:
#       合并主数据 merge(), 主体合并 title_merge(), 重复值处理 dupe_prc()
#     class transform() 数据转换类, 含有:
#       归一化 normalize(), 标准化 standardize(), 最大绝对值标准化 maxAbs()

import pandas as pd
import numpy
from sklearn import preprocessing

class integrate():
    # integrate 模块可扩展. 可复写至 data_n
    def __init__(self, data_1: pd.DataFrame, data_2: pd.DataFrame):
        self.data1 = data_1
        self.data2 = data_2

    def merge(self):
        """
        直接合并两个数据表的数据, 不管是否有重复值, 直接合并.
        :return:
            sub: 合并后的数据表
        for example:
            df1 = pd.DataFrame({'Name': ['Tom', 'Jerry', 'Duck'], 'A_score': [90, 88, 90], 'B': [1, 0, 2]})
            df2 = pd.DataFrame({'Name': ['Tom', 'Jerry1', 'Pig'], 'A_score': [90, 88, 90]})
            merge_tester = integrate(df1, df2).merge()
                    Name  A_score    B
                0     Tom       90  1.0
                1   Jerry       88  0.0
                2    Duck       90  2.0
                0     Tom       90  NaN
                1  Jerry1       88  NaN
                2     Pig       90  NaN

        """
        frames = [self.data1, self.data2]
        sub = pd.concat(frames)
        return sub

    def title_merge(self):
        pass

    def dup_prc(self):
        pass


class transform():
    def __init__(self, data):
        self.data = data

    def normalize(self):
        """
        数据归一化函数 (x - min)/(max - min)
        应用场景: 绝大多数数据
        :return:
            sub: 标准化后的数据集
        """
        base = self.data
        scaler = preprocessing.MinMaxScaler()
        tmp = scaler.fit_transform(base)
        sub = pd.DataFrame(tmp)
        return sub

    def standardize(self):
        """
        数据标准化函数 (x-μ)/σ
        应用场景: 绝大多数数据
        :return:
            sub: 标准化后的数据集
        """
        base = self.data
        scaler = preprocessing.StandardScaler()
        tmp = scaler.fit_transform(base)
        sub = pd.DataFrame(tmp)
        return sub

    def max_Abs(self):
        """
        最大绝对值标准化函数 x / max(|x|)
        应用场景: 稀疏数据集. 效果远优于上述两种标准化方法.
        :return:
            sub: 标准化后的数据集
        """
        base = self.data
        scaler = preprocessing.MaxAbsScaler()
        tmp = scaler.fit_transform(base)
        sub = pd.DataFrame(tmp)
        return sub


if __name__ == '__main__':
    pass