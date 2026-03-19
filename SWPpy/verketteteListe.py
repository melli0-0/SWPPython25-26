import random

class List_element:

    def __init__(self, obj=None):
        self.obj = obj
        self.element = None

class Single_linked_list:

    def __init__(self):
        self.start = None

    def get_last(self):
        if self.start is None:
            return None

        elem = self.start

        while elem.element is not None:
            elem = elem.element

        return elem

    def find(self, obj):
        for object in self:
            if object == obj:
                return True
        return False

    def add_end(self, obj: int):
        new = List_element(obj)

        if self.start is None:
            self.start = new
        else:
            last = self.get_last()
            last.element = new

    def get_length(self):
        count = 0
        for object in self:
            count +=1
        return count

    def __iter__(self):
        self.curr = self.start
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration

        object = self.curr.obj
        self.curr = self.curr.element
        return object


if __name__ == '__main__':
    mellis_list = Single_linked_list()

    for _ in range(10):
        nr = random.randint(1, 144)
        mellis_list.add_end(nr)

    print(f"Length of se list: {mellis_list.get_length()}")

    print("Iterator:")
    for item in mellis_list:
        print(item, end=" -> ")
    print("End (None)")

    search = 44
    print(f"Searching {search} -> {mellis_list.find(search)}")
