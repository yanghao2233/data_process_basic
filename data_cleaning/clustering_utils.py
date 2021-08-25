# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 09:11
# @Description:

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.mixture import GaussianMixture
import logging as logger


class clustering():
    def __init__(self, data, n_cluster):
        self.data = data
        self.n_cluster = n_cluster

    def kmeans(self):
        pass

    def kmeans_sd(self):
        pass

    def GMM(self, covar_type: str = 'full', to_list: bool = True):
        """
        高斯混合聚类模型
        :param covar_type:
        :param to_list:
        :return:
        """
        gmm = GaussianMixture(n_components = self.n_cluster, covariance_type = covar_type, random_state = 2333)
        gmmModel = gmm.fit(self.data)
        result = gmmModel.predict(self.data)
        if to_list:
            result = result.tolist()
        return result

    def Hierachy(self):
        pass