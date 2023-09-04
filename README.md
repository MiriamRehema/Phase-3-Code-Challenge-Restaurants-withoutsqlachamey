# Phase-3-Code-Challenge-Restaurants-withoutsqlachamey


## Table of Content

Description
Installation Requirement
Technology Used
Conclusion
Licence
Authors Info

An access to the Internet
# Description
We have three models:
- `Restaurant`
- `Customer`
- `Review`

 
For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many `Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.
`Restaurant` - `Customer` is a many-to-many relationship. 
# Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods 

# Restaurant
Create an instance of the Restaurant class by providing a name for the restaurant.
Use the methods provided by the Restaurant class to analyze the restaurant's data.
# Restaurant methods
`Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created

# Customer

Create an instance of the Customer class by providing optional given and family names.
Use the methods provided by the Customer class to interact with customer data.
# Customer methods
`Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - should be able to change after the customer is created
- `Customer family_name()`
  - returns the customer's family name
  - should be able to change after the customer is created
- `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - returns **all** of the customer instances

# Review

Create an instance of the Customer class by providing optional given and family names.
Use the methods provided by the Customer class to interact with customer data.
# Review methods
`Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews

  Other methods:
  # Object Relationship Methods
  # Aggregate and Association Methods


# Installation Process

Frontend

* Git clone the repository 'git clone git@github.com:MiriamRehema/.git`Phase-3-code-Challenge-Restaurants-withoutsqlachamey`
* Navigate to the project directory with the command `cd Phase-3-code-Challenge-Restaurants-withoutsqlachamey`



## Technology used
The challenge was mainly based on Python, so I used the following technologies:
- Python(your version)
-

## Conclusion
Completing this challenge was a great opportunity for me to use my knowledge of Python. I had a nice experience working on the different tasks and I look forward to building more projects using Python.



## Licence
MIT License

Copyright (c) 2023 MiriamRehema

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,


