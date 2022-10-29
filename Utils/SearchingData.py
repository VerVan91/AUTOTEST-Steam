class SearchingData:

    def __init__(self, name, platforms, release_date, review_result, price):
        self.name = name
        self.platforms = platforms
        self.release_date = release_date
        self.review_result = review_result
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.platforms == other.platforms and self.release_date == other.release_date and self.review_result == other.review_result and self.price == other.price
