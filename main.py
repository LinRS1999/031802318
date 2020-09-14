import jieba
import numpy as np
import sys
from sklearn.feature_extraction.text import CountVectorizer
from diy_exception import NoWordError, SimIsOneError

# argv[1]为论文原文的文件的绝对路径
# argv[2]为抄袭版论文的文件的绝对路径
# argv[3]为输出的答案文件的绝对路径


# jieba分词并加入空格
def add_space(s):
    result = jieba.cut(s, cut_all=True)
    return ' '.join(list(result))


# 计算杰卡德相似指数
def jaccard_similarity(s1, s2):
    s1, s2 = add_space(s1), add_space(s2)
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
    # 计算杰卡德相似指数
    return 1.0 * numerator / denominator


# 将杰卡德相似指数写入文件
def write_result(output, file, test, flag):
    with open(output, 'a') as file_handle:
        # 清空文件内容
        file_handle.truncate(0)
        if round(jaccard_similarity(file, test), 2) == 1.00:
            # 发生文本不同，相似度为1异常
            if file != test:
                file_handle.write('发生异常！文本相似度计算失败！')
                file_handle.close()
                raise SimIsOneError
        if flag == 0:
            file_handle.write('%.2f' %jaccard_similarity(file, test))
            file_handle.close()
        else:
            file_handle.write('发生异常！文本相似度计算失败！')
            file_handle.close()


if __name__ == '__main__':
    # 论文原文
    file = open(sys.argv[1], 'r', encoding='utf-8').read()
    # 抄袭论文
    test = open(sys.argv[2], 'r', encoding='utf-8').read()
    # 输出文件
    output = sys.argv[3]
    if file == '':
        # 发生空文本异常
        write_result(output, file, test, 1)
        raise NoWordError
    if test == '':
        # 发生空文本异常
        write_result(output, file, test, 1)
        raise NoWordError
    # 符号表
    chars = ['\n', '\t', '，', '。', '；', '：', "？", '、', '！', '《', '》',
             '‘', '’', '“', '”', ' ', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', '.', '*', '-', '—', ',', '——', '……', '（', '）', '…',
             '%', '#', '@', '$', '￥', '~', '`', '~', '·']
    # 去符号，只保留中文
    for item in chars:
        file = file.replace(item, '')
    for char in chars:
        test = test.replace(char, '')
    write_result(output, file, test, 0)
