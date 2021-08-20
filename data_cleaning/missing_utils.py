# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/19 16:49
# @Description:
#   用于处理数据中存在缺失值的情况, 包含:
#       class miss_value() 内置下列方式:
#       直接删除缺失值: just_delete; 线性填充: fill; 贝叶斯填充: randforest_fill; 回归填充: lineregs_fill
#       * 为减少格式带来的影响, 本文件中还定义了函数类 class converter() 用于处理数据格式带来的问题 *

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import linregress


class miss_value():
    def __init__(self, data):
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
            sub = base.dropna(axis=0)
        elif type == 'col':
            sub = base.dropna(axis=1)
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
        df = self.data
        if type == 'front':
            sub = df.fillna(method='fill')
        elif type == 'back':
            sub = df.fillna(method='back')
        elif type == 'mean':
            for col in list(df.columns[df.isnull().sum() > 0]):
                fill_mean = df[col].mean()
                df.fillna(fill_mean, inplace=True)
            sub = df
        return sub

    def randforest_fill(self, col_to_fill):
        """
        利用数据集其他位置组成的点集进行随机森林回归预测缺失值数据
        应用场景: 应该也是所有场景. 但当数据相关性差时不推荐使用
        :param
            col_to_fill: 缺失值所在的需要被填充的列.
        :return:
            df: 在指定列完成缺失值插补的数据表.
        """
        df = self.data.copy()
        cols = [*df.columns]
        cols.remove(col_to_fill)
        x = df.loc[:, cols]
        y = df.loc[:, col_to_fill]
        x_train = x.loc[df[col_to_fill].notnull()]
        y_train = y.loc[df[col_to_fill].notnull()]
        x_pred = x.loc[df[col_to_fill].isnull()]
        rfr = RandomForestRegressor(random_state=10, n_estimators=200, max_depth=3, n_jobs=-1)
        rfr.fit(x_train, y_train)
        y_pred = rfr.predict(x_pred).round()
        df.loc[df[col_to_fill].isnull(), col_to_fill] = y_pred
        return df

    def lineregs_fill(self, col_to_fill: str, col_to_fit: str):
        """
        利用现有数据集对需要进行插补的点列进行线性预测.
        应用场景: 数据列间呈现较强线性相关性质的情况.
        * 技术原因 目前仅实现类似 y = kx + d 的情况 *
        ** 非线性过程与大规模多元线性回归不适用 **
        :param
            col_to_fill: 需要插补的列名.
            col_to_fit: 用于与被插补列进行线性预测的 x 变量列.
        :return:
            sub: 在指定列完成插补的数据表.
        """
        df = self.data
        df.dropna(axis=0, inplace=True)
        lr_generator = linregress(df[col_to_fit], df[col_to_fill])
        k = lr_generator[0]
        d = lr_generator[1]
        df['linear_generator'] = df[col_to_fit] * k + d
        sub = self.data
        for i in range(len(sub)):
            if np.isnan(df[col_to_fill][i]) == True:
                sub[col_to_fill][i] = df['linear_generator'][i]
        return sub


class converter():
    def __init__(self, data):
        self.data = data

    def list2df(self):
        sub = DataFrame(self.data)
        return sub


if __name__ == '__main__':
    data = {'col1': [1, np.nan, 2, np.nan, 4, 5], 'col2': [6, 5, 4, 3, 2, 1], 'col3': [1, 3, 4, 2, 4, 6]}
    test_df = pd.DataFrame(data)
    rdforest = miss_value(data).randforest_fill('col1')
    print(rdforest)
    pass
