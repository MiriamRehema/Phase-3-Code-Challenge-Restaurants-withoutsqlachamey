class Review:
    #create an empty list since the number of reviews will change
    all_review=[]
    def __init__(self,customer,restaurant,rating=int):
        self.customer=customer
        self.restaurant=restaurant
        self.rating=rating
        #call it here
        Review.all_review.append(self)
    @classmethod
    #method rating
    def rating(self):
        return self.rating
      #methods
    def all(self):
        return self.all
    @classmethod
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant