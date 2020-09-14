import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from diy_exception import DeleteAllWordsError

# 读入停用词表
stop_words = open('hit_stopwords.txt', 'r', encoding='utf-8').read()


class JaccardSimilarity:

    def add_stop_words(self, list):
        temp = []
        for item in list:
            if item not in stop_words:
                temp.append(item)
        if len(temp) == 0:
            # 如果执行停用词删除后，文本为空，抛出异常
            raise DeleteAllWordsError
        return temp

    # 杰卡德相似度计算
    # @profile
    def jaccard_similarity(self, s1, s2):
        # 字符表
        chars = ['\n', '\t', '，', '。', '；', '：', "？", '、', '！', '《', '》',
                 '‘', '’', '“', '”', ' ', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', '.', '*', '-', '—', ',', '——', '……', '（', '）', '…',
                 '%', '#', '@', '$', '￥', '~', '`', '~', '·']
        # 删除文本中的字符
        for item in chars:
            s1 = s1.replace(item, '')
            s2 = s2.replace(item, '')
        # jieba分词
        result = jieba.cut(s1, cut_all=True)

        #  停用词，使用时解开注释
        # jac = JaccardSimilarity()
        # result = jac.add_stop_words(result)

        s1 = ' '.join(list(result))
        #jieba分词
        result = jieba.cut(s2, cut_all=True)

        # 停用词，使用时解开注释
        # result = jac.add_stop_words(result)

        s2 = ' '.join(list(result))
        # 调用sklearn的CountVectorizer,将文本的词语转换为词频矩阵
        cv = CountVectorizer(tokenizer=lambda s: s.split())
        # 语料库
        corpus = [s1, s2]
        # 使用fit_transform函数计算各个词语出现的次数
        vectors = cv.fit_transform(corpus).toarray()
        # 求交集
        numerator = np.sum(np.min(vectors, axis=0))
        # 求并集
        denominator = np.sum(np.max(vectors, axis=0))
        # 计算杰卡德相似度
        return 1.0 * numerator / denominator




