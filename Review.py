class Review:
    all_review=[]
    def __init__(self,customer,restaurant,rating=int):
        self.customer=customer
        self.restaurant=restaurant
        self.rating=rating
        Review.all_review.append(self)
    def rating(self):
        return self.rating

    
def all(self):
        return self.all
@classmethod
def customer(self):
        return self.customer
def restaurant(self):
        return self.restaurant