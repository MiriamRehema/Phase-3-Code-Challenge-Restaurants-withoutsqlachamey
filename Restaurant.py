class Restaurant:
    def __init__(self,name=""):
        #initialize
        self.name=name
    def name(self):
        return self.name
    @classmethod
    def reviews(self):
        return self.reviews
    def customers(self):
        return list(set([review.customer() for review in self.reviews]))
    def average_star_rating(self):
        if not self.reviews:
            return 0  # No reviews yet, return 0
        total_ratings = sum(self.reviews)
        num_reviews = len(self.reviews)
        average_rating = total_ratings / num_reviews
        return average_rating

# Example usage



#print(f"The average rating for {restaurant.name} is {average_star_rating:.2f}")






