class User:

    def __init__(self, name, email,city, state):
        self.name= name
        self.email =email
        self.city =city
        self.state = state
        
                
    def describe(self):
        print(f"{self.name} lives in {self.city}, {self.state}.")
    
    # def __str__(self):
    #     return f"<Counter current={self.current}>"
    

    
user1 = User("Anton","", "Durham","NC")
user1 = User("Cecil","", "San Francisco","CA")