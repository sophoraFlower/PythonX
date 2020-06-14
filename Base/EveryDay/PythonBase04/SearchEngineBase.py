import sys


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    # 将文件路径作为ID，读取文件内容
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    # 对内容进行处理
    def search(self, query):
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text, in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        base_path = sys.path[0]
        search_engine.add_corpus(base_path + "/" + file_path)

    while True:
        query = input("请输入搜索关键词：")
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


search_engine = SimpleEngine()
main(search_engine)
