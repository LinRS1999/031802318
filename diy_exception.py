# 空文本异常
class NoWordError(Exception):
    def __init__(self):
        print('该文件没有文字！')

# 文本不同，相似度为1异常
class SimIsOneError(Exception):
    def __init__(self):
        print('两个文件是不同的文件！相似度不可能为1！')

# 停用词删除后文本为空异常
class DeleteAllWordsError(Exception):
    def __init__(self):
        print('该文件被你在删除停用词的时候都删光了！')

