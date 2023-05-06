# 1. Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
#
# 2. The Pagination class will accept 2 parameters:
#
# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:
#
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
#
# p = Pagination(alphabetList, 4)
#
# 3. The Pagination class will have a few methods:
#
# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:
#
# p.getVisibleItems()
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)
#
# Here’s a continuation of the example above using nextPage and lastPage:
#
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
#
# p = Pagination(alphabetList, 4)
#
# p.getVisibleItems()
# # ["a", "b", "c", "d"]
#
# p.nextPage()
#
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
#
# p.lastPage()
#
# p.getVisibleItems()
# # ["y", "z"]
#
# Notes
#
#   - The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
#   - The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
#   - Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
#   - If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination:

    # def __init__(self, items: list = None, page_size: int = 10):
    def __init__(self, items: list = None, page_size=10):
        self.items = items
        self.page_size = int(page_size)
        self.current_page = 1
        self.paginated_list = [
            self.items[i:i + self.page_size] for i in range(0, len(self.items), self.page_size)
        ]
        self.total_pages = len(self.paginated_list)

    def get_visible_items(self):
        return print(self.paginated_list[self.current_page-1])

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            print("You are already on the first page")

        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            print("You are already on the last page")

        return self

    def first_page(self):
        self.current_page = 1

        return self

    def last_page(self):
        self.current_page = self.total_pages

        return self

    # def go_to_page(self, page_num: int):
    def go_to_page(self, page_num):
        page_num = int(page_num)

        if 1 <= page_num <= self.total_pages:
            self.current_page = page_num
        else:
            if page_num < 1:
                self.current_page = 1
            elif page_num > self.total_pages:
                self.current_page = self.total_pages


if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")

    p = Pagination(alphabetList, 4)

    p.get_visible_items()
    # ["a", "b", "c", "d"]

    p.next_page()

    p.get_visible_items()
    # ["e", "f", "g", "h"]

    p.last_page()

    p.get_visible_items()
    # ["y", "z"]

    p.go_to_page(-200)

    p.get_visible_items()
