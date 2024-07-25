# TODO: complete this class

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.structure = [collection[i:i+items_per_page] for i in range(0,len(collection),items_per_page)]

    def __repr__(self) -> str:
        print(self.structure)
        res = ""
        for x in self.structure:
            for y in x:
                res += str(y)
            res += " "
        return res

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return len(self.structure)
        # res = self.item_count()/self.items_per_page
        # if isinstance(res, int):
        #     return res
        # else:
        #     return self.item_count()//self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based 
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > len(self.structure)-1:
            return -1
        return len(self.structure[page_index])
        # if ((page_index+1)*self.items_per_page) > self.item_count():
        #     return -1
        # return self.item_count() - ((page_index+1)*self.items_per_page)

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if len(self.collection) == 0:
            return 0
        if item_index <= self.items_per_page:
            return 0
        if item_index <= self.item_count():
            return (item_index % self.items_per_page) - 1
        return -1

# collection = range(1,25)
# helper = PaginationHelper(collection, 10)


# if not helper.page_count()== 3:
#     print('page_count is returning incorrect value.', end=": ")
#     print(helper.page_count(), "Expected value: {3}")
# if (helper.page_index(23)!= 2):
#     print(helper.collection, helper.items_per_page)
#     print('page_index returned incorrect value', end=": ")
#     print(helper.page_index(23), "exp::: 2")
# if not (helper.item_count()== 24):
#     print('item_count returned incorrect value', end=":  ")
#     print(helper.item_count())




# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# print(helper)
# print(helper.page_item_count(0))  # should == 4
# print(helper.page_item_count(1)) # last page - should == 2
# print(helper.page_item_count(2)) # should == -1 since the page is invalid




import pytest

def test_PaginationHelper()


if __name__=="__main__":
    SystemExit()


