from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.set_title

    def set_title(self, title):
        pass


document = Document()
document.set_title('Hole')
print(document.get_title())

entity = Entity()


