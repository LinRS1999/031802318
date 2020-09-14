import jieba
from gensim import corpora, models, similarities
from diy_exception import DeleteAllWordsError


# 读入停用词表
stop_words = open('hit_stopwords.txt', 'r', encoding='utf-8').read()


class CosSimilarity:

    # 增加删除停用词函数
    def add_stop_words(self, list):
        temp = []
        for item in list:
            if item not in stop_words:
                temp.append(item)
        if len(temp) == 0:
            # 如果执行停用词删除后，文本为空，抛出异常
            raise DeleteAllWordsError
        return temp

    # 余弦相似度计算
    # @profile
    def cos_similarity(self, file, test):
        # 字符表
        chars = ['\n', '\t', '，', '。', '；', '：', "？", '、', '！', '《', '》',
                 '‘', '’', '“', '”', ' ', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', '.', '*', '-', '—', ',', '——', '……', '（', '）', '…',
                 '%', '#', '@', '$', '￥', '~', '`', '~', '·']
        # 删除文本中的字符
        for char in chars:
            file = file.replace(char, '')
            test = test.replace(char, '')
        list = []
        list.append(file)
        all_list = []
        # jieba分词
        result = [word for word in jieba.cut(file)]

        # 停用词，使用时解开注释
        # cos = CosSimilarity()
        # result = cos.add_stop_words(result)

        all_list.append(result)
        all_list.append([''])
        # 生成论文字典
        dictionary = corpora.Dictionary(all_list)
        # 建立稀疏向量集
        corpus = [dictionary.doc2bow(txt) for txt in all_list]
        # 抄袭论文jieba分词
        test_list = [word for word in jieba.cut(test)]

        # 停用词，使用时解开注释
        # test_list = cos.add_stop_words(test_list)

        # 将抄袭论文也建立稀疏向量
        test_vec = dictionary.doc2bow(test_list)
        # 建立模型
        tfidf = models.TfidfModel(corpus)
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        # 相似度计算
        sim = index[tfidf[test_vec]]
        return sim[0]

