import unittest
from cosine import CosSimilarity
from jaccard import JaccardSimilarity
from diy_exception import NoWordError, SimIsOneError, DeleteAllWordsError


file = open('orig.txt', 'r', encoding='utf-8').read()
test = {}
test['orig_0.8_add.txt'] = open('orig_0.8_add.txt', 'r', encoding='utf-8').read()
test['orig_0.8_del.txt'] = open('orig_0.8_del.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_1.txt'] = open('orig_0.8_dis_1.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_3.txt'] = open('orig_0.8_dis_3.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_7.txt'] = open('orig_0.8_dis_7.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_10.txt'] = open('orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_15.txt'] = open('orig_0.8_dis_15.txt', 'r', encoding='utf-8').read()
test['orig_0.8_mix.txt'] = open('orig_0.8_mix.txt', 'r', encoding='utf-8').read()
test['orig_0.8_rep.txt'] = open('orig_0.8_rep.txt', 'r', encoding='utf-8').read()
test['myself_test.txt'] = open('myself_test.txt', 'r', encoding='utf-8').read()
test['myself_test2.txt'] = open('myself_test2.txt', 'r', encoding='utf-8').read()


# 同时测试两种算法对于测试样例计算的相似度
class Testsim(unittest.TestCase):
    def test_cosine(self):
        cos = CosSimilarity()
        print('开始测试cosine！')
        print('-------------------------------------------')
        for key in test.keys():
            result = cos.cos_similarity(file, test[key])
            print('测试样本为：%s，相似度为：%.2f' % (key, result))
            print('-------------------------------------------')
        print('cosine测试结束！')

    def test_jaccard(self):
        jac = JaccardSimilarity()
        print('开始测试jaccard！')
        print('-------------------------------------------')
        for key in test.keys():
            result = jac.jaccard_similarity(file, test[key])
            print('测试样本为：%s，相似度为：%.2f' % (key, result))
            print('-------------------------------------------')
        print('jaccard测试结束！')


if __name__ == '__main__':
    unittest.main()