class Restaurant:
    def __init__(self,name=""):
        #initialize
        self.name=name
     #function name
    def name(self):
        return self.name
    
    @classmethod
    #method reviews
    def reviews(self):
        return self.reviews
    
    #method customers
    def customers(self):
        return list(set([review.customer() for review in self.reviews]))
    #To calculate the average star rating
    def average_star_rating(self):
        if not self.reviews:
            return 0  # No reviews yet, return 0
        total_ratings = sum(self.reviews)
        num_reviews = len(self.reviews)
        average_rating = total_ratings / num_reviews
        return average_rating












