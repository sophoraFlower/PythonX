class Entity:
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context

    # 函数重写
    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    # 函数重写
    def get_context_length(self):
        return self.__video_length


book = Document('中华复兴', '中国人', '为中华之崛起而读书')
video = Video('五十六个民族', '中国人', 666)

print(book.object_type)
print(video.object_type)

book.print_title()
video.print_title()

print(book.get_context_length())
print(video.get_context_length())



