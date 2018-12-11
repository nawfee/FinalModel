import random

#set the class of agents and give the agent environment, list of other agents and neighbourhood
class Agent(): 
    
    def __init__ (self,environment,agents,y,x):
# if x has value none, it is given a random integer value between 0 and 100 otherwise it extract value from the html
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
# if x has value none, it is given a random integer value between 0 and 100 otherwise it extract value from the html            
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
    
    
        self.environment = environment #list of environment to other agents
        self.store = 0  #each agent starts with no food to eat
        self.agents = agents  #list of agents to other agents
        self.neighbourhood = 20 #the distance around the agent where if it meets another agent will share food with it

    '''
    def __init__ (self):
        print("construct agent")
        self.x = 1
        pass
    '''

        
    def move(self):
        # move agent randomly by 1 cell at a time
        if random.random() < 0.5:            
            self.y  = (self.y  + 1) % 100 #%100 to set up bounding effects
        else:
            self.y  = (self.y  - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            



    #Add method to our agent
    def eat(self): 
       if self.environment[self.y][self.x] > 10: #thee cell value in the enviornment where it will eat food
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
     #Distance between self and agents         
    def distance_between (self, agents):
      return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5  
     
    #Add method for sharing with neighbours
    def share_with_neighbours(self,neighbourhood):
        for agents in self.agents:  #loop though agents in self agent
            dist = self.distance_between(agents) #Calculate the distance between self and the current other agent
            if dist <= neighbourhood: #when distance is less than that set for the neighourhood that is 20
                sum = self.store + agents.store #the agents will share food with another agent within the same vicinity
                ave = sum/2
                self.store = ave
                agents.store = ave
                print (str (dist) + " " + str (ave))
                

                
                 
            
    