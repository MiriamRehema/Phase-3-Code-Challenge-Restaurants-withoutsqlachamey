class Customer:
    #initialization
    def __init__(self,given_name='Goerge',family_name='Washington'):
        self.givenname=given_name
        self.familyname=family_name
    @classmethod
    def given_name(self):
     return self.given_name
    def set_given_name(self,given_name) :
      self.given_name=given_name 
     
    def family_name(self):
     return self.family_name
    
    def set_family_name(self,family_name) :
      self.family_name=family_name

    def full_name(self):
     return  f"{self.given_name}, {self.family_name}"
    def all(self):
      return self.all
    @classmethod
    def restaurant(self):
        return list(set([review.restaurant() for review in self.restaurant]))
    def add_review(self,restaurant,rating):
     new_review=review(self,restaurant,rating)
    @classmethod
    def num_review(self):
      return len(self.num_review)
    def find_by_name(self,name):
      self.name=name
      