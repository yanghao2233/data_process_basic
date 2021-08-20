# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 16:10
# @Description: 数据整合与数据转化模块, 包含:
#     class integrate() 数据整合类, 含有:
#       合并主数据 merge(), 主体合并 title_merge(), 重复值处理 dupe_prc()
#     class transform() 数据转换类, 含有:
#       归一化 normalize(), 标准化 standardize(), 中心化 zero_centerize()

import pandas as pd
import numpy

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
        pass

    def standardize(self):
        pass

    def zero_centerized(self):
        pass


if __name__ == '__main__':
    pass