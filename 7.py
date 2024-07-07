#	Create a Python program to define a person class with 
#   attributes like name, country, and date of birth, and 
#   implement a method for determining the person’s age.
from datetime import datetime

class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=datetime.strptime(dob,"%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.dob.year
        if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
            age -= 1
        return age
    
obj=person("Kishu","India","2004-08-04")
print(obj.name,"\n",obj.country,"\n",obj.dob,"\n",obj.calculate_age())