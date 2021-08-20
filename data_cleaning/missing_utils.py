# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/19 16:49
# @Description: 用于处理数据中存在缺失值的情况, 包含:
#       直接删除缺失值: just_delete; 线性填充: fill; 贝叶斯填充: bayes; 回归填充: regress

import pandas as pd


class miss_value_pcs(self, data):
    self.data = data
    pass

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

    def fill(self, type: str = 'front'):
        pass

    def bayes(self):
        pass

    def regress(self):
        pass


if __name__ == '__main__':
    pass
