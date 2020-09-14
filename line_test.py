from cosine import CosSimilarity
from jaccard import JaccardSimilarity

# 测试两种算法内存和时间占用，测试时需要打开jaccard.py和cosine.py的@profile注释
file = open('orig.txt', 'r', encoding='utf-8').read()
test = {}
test['orig_0.8_add.txt'] = open('orig_0.8_add.txt', 'r', encoding='utf-8').read()

# cos = CosSimilarity()
# result = cos.cos_similarity(file, test['orig_0.8_add.txt'])
jac = JaccardSimilarity()
result = jac.jaccard_similarity(file, test['orig_0.8_add.txt'])
print(result)