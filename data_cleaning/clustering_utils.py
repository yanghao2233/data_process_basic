# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 09:11
# @Description:

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn import metrics
from sklearn.mixture import GaussianMixture
from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.utils.metric import distance_metric, type_metric
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
import logging as logger
import numpy as np


class clustering():

    def __init__(self, data: list or np.array, n_cluster: int):
        self.data = data
        self.n_cluster = n_cluster

    def kmeans(self, max_iter: int = 300, n_init: int = 40, num_jobs: int = -1):
        """
        kmeans++ 聚类模型
        :param
            max_iter: 最大迭代次数; 默认为 300.
            n_init: 初始生成采样点个数, 默认为 40.
            num_jobs: 同时生成的任务数量(本函数允许并行运算); 默认为 -1, 即取最大并行任务数量.
        :return:
            result: 完成聚类的样本的分类指标.
        """
        kmeans_cluster = KMeans(n_clusters = self.n_cluster, max_iter = max_iter,
                                n_init = n_init, init = 'k-means++', n_jobs = num_jobs)
        result = kmeans_cluster.fit_predict(self.data)
        return result

    def kmeans_sd(self, distance_function, if_visualize: bool = False):
        """
        基于自定义距离的 kmeans 聚类模型
        :param
            distance_function: 自定义的距离函数; 可从 ./distance_tools.py 中调用.
            if_visualize: 是否进行绘图表示聚类结果; 默认为 False. 高维空间下不推荐输出.
        :return:
            clusters: 完成聚类的样本的分类指标.
        """
        initial_centers = kmeans_plusplus_initializer(data = self.data, amount_centers = self.n_cluster).initialize()
        km_metric = distance_metric(type_metric.USER_DEFINED, func = distance_function)
        kmeans_instance = kmeans(self.data, initial_centers, metric = km_metric)
        kmeans_instance.process()
        clusters = kmeans_instance.get_clusters()
        final_centers = kmeans_instance.get_centers()
        if if_visualize:
            kmeans_visualizer.show_clusters(self.data, clusters, final_centers)
        return clusters

    def GMM(self, covar_type: str = 'full', to_list: bool = True):
        """
        高斯混合聚类模型
        :param
            covar_type: 组成协方差矩阵的类型. 默认为 'full'; 可选 'spherical', 'diag', 'tied'
            to_list: 是否将聚类结果转化为 list; 默认为 True.
        :return:
            result: 完成聚类的样本的分类指标.
        """
        gmm = GaussianMixture(n_components = self.n_cluster, covariance_type = covar_type, random_state = 2333)
        gmmModel = gmm.fit(self.data)
        result = gmmModel.predict(self.data)
        if to_list:
            result = result.tolist()
        return result

    def Hierachy(self, distance_metric: str = 'euclidean', linkage: str = 'average', to_list: bool = False):
        """
        层次聚类
        :param
            distance_metric: 进行距离换算的算法; 格式为 str, 默认为 'euclidean' 欧氏距离; 可选: 'cosine' 余弦相似度,
                            'manhattan' 曼哈顿距离, 'precompute' 不知道是啥.
                            * 当 linkage 为 'ward' 时只能选用 'euclidean'.
            linkage: 联系指标. 默认为 'ward'; 可选: 'complete', 'average', 'single'.
            to_list: 是否将聚类结果转化为列表进行输出; 默认为 True.
        :return:
            result: 完成聚类的样本的分类指标.
        """
        model = AgglomerativeClustering(n_clusters = self.n_cluster, affinity = distance_metric, linkage = linkage)
        result = model.fit_predict(self.data)
        if to_list:
            result = result.tolist()
        return result

    def spectral(self):
        pass

class model_examiner():

    def __init__(self, true_labels, predict_labels):
        self.true = true_labels
        self.predict = predict_labels

    def internal_evaluate(self):
        pass

    def supervised_evaluate(self):
        """
        基于兰德系数和互信息执行的外部结果评估指标
        * 主要是聚类用 *
        ** 能否用于有监督机器学习模型待检验 **
        :return:
        """
        rand_index = metrics.adjusted_rand_score(self.true, self.predict)
        logger.info('调整兰德系数为 % .3f' % rand_index)
        mutual_info = metrics.adjusted_mutual_info_score(self.true, self.predict)
        logger.info('调整互信息为 % .3f' % mutual_info)
