# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/19 16:49
# @Description:
#   用于处理数据中存在缺失值的情况, 包含:
#       class miss_value() 内置下列方式:
#       直接删除缺失值: just_delete; 线性填充: fill; 贝叶斯填充: bayes; 回归填充: regress
#       * 为减少格式带来的问题, 本文件中还定义了函数类 class converter() 用于处理数据格式带来的问题.

import pandas as pd
from pandas.core.frame import DataFrame


class miss_value(self, data):
    if isinstance(data, pd.DataFrame):
        self.data = data
    else:
        raise TypeError('目前该函数类仅支持 Dataframe 类型')

    def just_delete(self, type: str = 'row'):
        """
        直接删除含有 NAN 的数据所在行或所在列
        应用场景: 缺失值占总数据量的极少部分, 直接删除不会对数据集完整度造成太大影响时.
        * 一般不建议使用直接删除法, 极容易造成数据集不完整 *
        合理使用场景: 一条 512d 的数据但仅有 1 个有效值时.
        :param
            type: 删除方式; 需要为 str 格式 .
                  默认为 'row' 按行删除; 可选 'col' 按列删除.
        :return:
            sub: 直接清除缺失值数据后的数据集.
        """
        base = self.data
        if type == 'row':
            sub = base.dropna(axis = 0)
        elif type == 'col':
            sub = base.dropna(axis = 1)
        else:
            raise ValueError("输入的删除值类型必须是 'row' 或 'col'")
        return sub

    def general_fill(self, type: str = 'front'):
        """
        利用常见(非推理运算性质)方式填充缺失值
        应用场景: 基本所有场景; 但当数据偏移度大, 分布极端不均时不推荐使用.
        * 需要以行作为 sample, 以列作为 parameter *
        :param
            type: 填充缺失值的方式. 默认为 front, 向后取近邻值填充;
                可选: back, 向前取近邻值填充; mean, 取列数据的平均值填充.
        :return:
        """
        df = self.file
        if type == 'front':
            sub = df.fillna(method = 'fill')
        elif type == 'back':
            sub = df.fillna(method = 'back')
        elif type == 'mean':
            for col in list(df.columns[df.isnull().sum() > 0]):
                fill_mean = df[col].mean()
                df.fillna(fill_mean, inplace = True)
            sub = df
        return sub

    def bayes_fill(self):
        pass

    def regress_fill(self):
        pass

class converter(self, data):
    self.data = data

    def list2df(self):
        sub = DataFrame(self.data)
        return sub

if __name__ == '__main__':
    pass
