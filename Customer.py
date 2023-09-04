class Customer:
    #Create an empty list since it will keep on changing once updated
    all_customer=[]
    #initialization
    def __init__(self,given_name='Goerge',family_name='Washington'):
        self.givenname=given_name
        self.familyname=family_name
        self.reviews=[]
        Customer.all_customers.append(self)
    @classmethod

    def given_name(self):
     return self.given_name
    #we use set method since it is required to update itself once the name has been changed
    def set_given_name(self,given_name) :
      self.given_name=given_name 
     
    def family_name(self):
     return self.family_name
    #should be able to change itself once it is updated
    def set_family_name(self,family_name) :
      self.family_name=family_name

    def full_name(self):
     return  f"{self.given_name} {self.family_name}"
    
    def all(self):
      return self.all
    @classmethod
    #use the for in to loop
    def restaurant(self):
        return list(set([review.restaurant() for review in self.restaurant]))
    
    def add_review(self,restaurant,rating):
      review=(self,restaurant,rating)
      self.reviews.append(review)
      restaurant.add_review(review)

    @classmethod
    def num_review(self):
      return len(self.num_review)
    #The name should return correctly
    #we use for in loop to loop through the names to check if they are matching
    def find_by_name(self,name):
      for customer in self.all_customers:
        if customer.full_name()==name:
          return customer
      else:
       return None 

    @classmethod
    def find_all_by_given_name(self,name):
      that_given_name=[]
      #we use for in loop to check whether the name in all_customers is the same as inn the new list
      for customer in self.all_customers:
        if customer.given_name==name:
          that_given_name.append(customer)
          return that_given_name

      