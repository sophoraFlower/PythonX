import re

from ProgramBasic.programBasic.base_13 import main, SearchEngineBase


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    # 生成文件路径: 词集合
    def process_corpus(self, id_, text):
        self.__id_to_words[id_] = self.parse_text_to_words(text)

    def search(self, query):
        # 搜索词集合
        query_words = self.parse_text_to_words(query)
        results = []
        for id_, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id_)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


if __name__ == '__main__':
    search_engine = BOWEngine()
    main(search_engine)
