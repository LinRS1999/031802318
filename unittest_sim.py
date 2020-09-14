import unittest
from cosine import CosSimilarity
from jaccard import JaccardSimilarity
from diy_exception import NoWordError, SimIsOneError, DeleteAllWordsError


file = open('orig.txt', 'r', encoding='utf-8').read()
test = {}
# # 以下测试会导致cosine方法SimIsOneError异常，jaccard不会
# # test['orig_0.8_add.txt'] = open('orig_0.8_add.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_mix.txt'] = open('orig_0.8_mix.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_dis_1.txt'] = open('orig_0.8_dis_1.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_dis_3.txt'] = open('orig_0.8_dis_3.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_dis_7.txt'] = open('orig_0.8_dis_7.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_dis_10.txt'] = open('orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()
# # # myself_test3.txt为空白文本，会导致NoWordError
# # test['myself_test3.txt'] = open('myself_test3.txt', 'r', encoding='utf-8').read()
# # myself_test4.txt为将会被停用词全部删去的文本，会导致DeleteAllWordsError
# test['myself_test4.txt'] = open('myself_test4.txt', 'r', encoding='utf-8').read()
# # # 以下测试均为正常测试，其中myself_test.txt为毛概方向，myself_test2.txt为计算机导论方向
# # test['orig_0.8_del.txt'] = open('orig_0.8_del.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_dis_15.txt'] = open('orig_0.8_dis_15.txt', 'r', encoding='utf-8').read()
# # test['orig_0.8_rep.txt'] = open('orig_0.8_rep.txt', 'r', encoding='utf-8').read()
# # test['myself_test.txt'] = open('myself_test.txt', 'r', encoding='utf-8').read()
# # test['myself_test2.txt'] = open('myself_test2.txt', 'r', encoding='utf-8').read()


# 异常测试，选择不同的测试点进行异常测试
class Testsim(unittest.TestCase):
    def test_cosine(self):
        cos = CosSimilarity()
        print('开始测试cosine！')
        print('-------------------------------------------')
        for key in test.keys():
            # 如果文件为空，抛出异常
            if file == '':
                raise NoWordError
            if test[key] == '':
                raise NoWordError
            else:
                result = cos.cos_similarity(file, test[key])
                if round(result, 2) == 1.00:
                    # 如果两个文本不同，相似度却极度接近1或为1，抛出异常
                    if file != test[key]:
                        raise SimIsOneError
                print('测试样本为：%s，相似度为：%.2f' % (key, result))
                print('-------------------------------------------')
        print('cosine测试结束！')

    def test_jaccard(self):
        jac = JaccardSimilarity()
        print('开始测试jaccard！')
        print('-------------------------------------------')
        for key in test.keys():
            # 如果文件为空，抛出异常
            if file == '':
                raise NoWordError
            if test[key] == '':
                raise NoWordError
            else:
                result = jac.jaccard_similarity(file, test[key])
                if round(result, 2) == 1.00:
                    # 如果两个文本不同，相似度却极度接近1或为1，抛出异常
                    if file != test[key]:
                        raise SimIsOneError
                print('测试样本为：%s，相似度为：%.2f' % (key, result))
                print('-------------------------------------------')
        print('jaccard测试结束！')


if __name__ == '__main__':
    unittest.main()