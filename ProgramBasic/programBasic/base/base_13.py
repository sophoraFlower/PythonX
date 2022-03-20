class SearchEngineBase(object):
    """ 搜索引擎基类 """
    def __init__(self):
        pass

    # 处理资源文档
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    # 基类中定义process_corpus函数
    def process_corpus(self, id_, text):
        raise Exception('process_corpus not implemented')

    # 基类中定义search函数
    def search(self, query):
        raise Exception('search not implemented')


class SimpleEngine(SearchEngineBase):
    """ 简单的搜索引擎实现类 """
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    # 生成文件路径: 文件内容的字典
    def process_corpus(self, id_, text):
        self.__id_to_texts[id_] = text

    # 在文档中搜索指定的字符串，遍历
    def search(self, query):
        results = []
        for id_, text in self.__id_to_texts.items():
            if query in text:
                results.append(id_)
        return results


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} results(s):'.format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    search_engine_new = SimpleEngine()
    main(search_engine_new)
