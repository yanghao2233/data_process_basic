# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 09:11
# @Description: 可调用进行传参的距离函数模块. 包含:
#   欧氏距离 euclide_distance(), 余弦相似度 cosine_similarity(), 皮尔森相关系数 pearson_coefficient(),
#   杰卡德相关系数 jaccard_coefficient(), 谷本系数 tanimoto_coefficient(), 曼哈顿距离 manhattan_distance(),
#   海明距离 hamming_distance(), 切比雪夫距离 chebyshev_distance(), 斯皮尔曼相关系数 spearman_coefficient().

import numpy as np
import scipy.spatial.distance as dist
from scipy.stats import spearmanr

def euclide_distance(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    distance = np.sqrt(np.sum(np.square(vec_1 - vec_2)))
    return distance

def cosine_similarity(vec_1, vec_2, min1: bool = False):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    score = np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * (np.linalg.norm(vec_2)))
    if min1:
        score = 1 - score
    return score

def pearson_coefficient(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的额得分.
    """
    score = np.corrcoef(vec_1, vec_2)[1, 0]
    return score

def jaccard_coefficient(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    score = dist.pdist(np.array([vec_1, vec_2]), 'jaccard')
    return score

def tanimoto_coefficient(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    up = np.dot(vec_1, vec_2)
    low = np.linalg.norm(vec_1) + np.linalg.norm(vec_2)
    score = 1 - (up / (low - up))
    return score

def manhattan_distance(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    score = np.sum(np.abs(vec_1 - vec_2))
    return score

def hanmming_distance(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    assert len(vec_1) == len(vec_2)
    return sum(cr1 != cr2 for cr1, cr2 in zip(vec_1, vec_2))

def chebyshev_distance(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    score = np.abs(vec_1 - vec_2).max()
    return score

def spearman_coefficient(vec_1, vec_2):
    """

    :param
        vec_1: 需要比对的向量1.
        vec_2: 需要比对的向量2.
    :return:
        score: 该衡量方式的得分.
    """
    coef, p = spearmanr(vec_1, vec_2)
    return coef