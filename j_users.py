
#this class needs to be able to take user information ie name and preferences for humidity
#temperature and chance of percip and save it to SQL database

#needs to be able to load user information and create an instance of the class

#needs to be able to updata preferences

class User:
    def __init__(self, name, temp, humid):
        self.name = name
        self.temp = temp
        self.humid = humid

        
    #def save(self):
        #will save the user name and preferences to a SQL database
    	

    
        #will load and create a new instance of class User from SQL database
        #will need to open and load database
        #will create user class based on name
        #Select * FROM ___ WHERE name = '___'
        #load query result a
    #@classmethod
    #def load(cls, name):
    #pass

    #def update(self, name, temp, humid):
    #    self.name = name
    #    self.temp = temp
    #    self.humid = humid     
        

def NewUserInstance():
    user_name = raw_input('\nCreate your username. ')
    temperature = float(raw_input('\nEnter your temperature preference in Farenheit.  Simply enter an\ninteger like \"60\".  No need to add degrees. '))
    humidity = float(raw_input('\nEnter the highest percentage humidity you are willing to climb in.\nA number around 80 percent seems reasonable for this area.\nAs above, just enter an integer.  No need to enter a percentage sign. '))
    new_instance = User(user_name, temperature, humidity)
    return new_instance