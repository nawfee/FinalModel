# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:24:25 2018

@author: gy18smn
"""

import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import matplotlib.backends.backend_tkagg
import requests
import bs4

#agents taking value from an html
#r is set to be the website from which we want to extract x and y values of agents
#the website r is written as html, so use content = r.text to derive the text from the html
#the package beautiful soup is used to get the content as text
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) #to get the y values from the html
td_xs = soup.find_all(attrs={"class" : "x"}) #to extract the x values from the html
print(td_ys)
print(td_xs)

#Make the agent list and set the iteration 
num_of_agents = 10
num_of_iterations = 100
neighbourhood=20
agents = [] #make an empty agent list 


#Read the CSV code and make an environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []  #environment list
    for row in reader:
        rowlist = []
        for value in row:
           rowlist.append(value)
        environment.append(rowlist) # add rowlist to the environment 


##make a plot of the environment        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
            


# Selecting the size of the window we get.
fig = matplotlib.pyplot.figure(figsize=(7,7)) #the grid axis will be 7 by 7
ax = fig.add_axes([0, 0, 1, 1]) #ax.set_autoscale_on(False) #left, right, bottom and top


#Give environment to the agents and list of agents to each agent
for i in range(num_of_agents):
    y = int(td_ys[i].text)  #initialise with data from web that have been extraxted
    x = int(td_xs[i].text) # initialise with data from web that have been extracted
    agents.append(agentframework.Agent(environment, agents, y, x))


carry_on = True

#chnage the frames as animation runs, frame_number represents the number of time animation goes on
def update(frame_number):
    
    
    fig.clear()
    global carry_on
    
#creating conditions for the animation to reach stopping stage
#if it gets a random number mentioned it stops
    if random.random() < 0.1:
            carry_on = False
            print("stopping condition")
        
#Move the agent and let them eat from the environment and share with neighbours
    for j in range(num_of_iterations):
     for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        

#create plot of agents in the environment        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#setting ondition of generating frames during animation and settin up a condition. The animation keeps running until a<10        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on == True) :
        yield a			# Returns control and waits next call.
        a = a + 1
      
 #run the animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) #set the animation function 
    canvas.show()
    run(animation)
    
 #creating a window    
root = tkinter.Tk()      #builds the main window  
root.wm_title("Model")   #setting title of the main window

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) #createing a matplotlib canvas within our window   
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) #sets layout of the matplotlip canvas

#creating a menu bar in the new window
menu_bar = tkinter.Menu(root)  
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)


    
tkinter.mainloop()