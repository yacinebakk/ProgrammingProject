import matplotlib.pyplot as plt #import plot library
from graphics import * #import graph library
import pandas as pd #import data manipulation library
from tkinter.filedialog import askopenfilename, asksaveasfilename #import file manipulation functions

def load(): #define the function that will load the csv
    file_path = askopenfilename(title="Select Dataset", filetypes=[("CSV Files", "*.csv")]) #select a csv file
    if file_path: #if file is selected
        return pd.read_csv(file_path) #read and return it as a dataframe
    else:
        return None #if no file is selected return none

def save_plot(plot_function, injury_type, filename="plot.png"): #define the function that will save the plot to a new file
    plot_function(injury_type) #call the plot function containing the injury type
    plt.savefig(filename) #save the plot in the chosen file

def RehabProgram(injury_type, df, acltear=False, ankle=False, knee=False, shoulder=False, ham=False):
    #generate bar plot for rehab programs based on injury types
    if acltear: #is acl tear is selected
        data = df[df["Injury_Type"].isin(['ACL Tear', injury_type])] #filter the data for acl tear and the selected injury type
        data = data.groupby(["Rehabilitation_Program", "Injury_Type"])["Rehabilitation_Efficiency_Score"].mean() #after grouping the data calcualtz efficiency score
        data = data.unstack() #spreads the grouped data into a more tabular form that is easier to work with when plotting
        ax = data.plot(kind='bar', stacked=False, colormap="tab10", alpha=0.8, width=0.8) #create a bar plot
        plt.title(f"Rehabilitation Program Efficiency (For {injury_type} & ACL Tear)") #set title
        plt.xlabel("Rehabilitation Program") #label x
        plt.ylabel("Efficiency Score") #label y
        plt.xticks(rotation=10) #rotate the x axis labels for clarity purposes
        plt.legend(title="Injury Types") # add a legend
        plt.grid(axis='y', linestyle='--', alpha=0.7) #add a grid
    elif ankle: #if ankle is selected
        data = df[df["Injury_Type"].isin(['Ankle Sprain', injury_type])]#filter the data for ankle sprain and the selected injury type
        data = data.groupby(["Rehabilitation_Program", "Injury_Type"])["Rehabilitation_Efficiency_Score"].mean() #after grouping the data calcualtz efficiency score
        data = data.unstack() #spreads the grouped data into a more tabular form that is easier to work with when plotting
        ax = data.plot(kind='bar', stacked=False, colormap="tab10", alpha=0.8, width=0.8)#create a bar plot
        plt.title(f"Rehabilitation Program Efficiency (For {injury_type} & Ankle Sprain)") #title the plot
        plt.xlabel("Rehabilitation Program") #label x axis
        plt.ylabel("Efficiency Score")#label y axis
        plt.xticks(rotation=10) #rotate label on x axis for clarity purposes
        plt.legend(title="Injury Types") #put a legend on the graph
        plt.grid(axis='y', linestyle='--', alpha=0.7) #create a grid
    elif knee: #is knee injury is selected
        data = df[df["Injury_Type"].isin(['Knee Injury', injury_type])]#filter the data for knee injury and the selected injury type
        data = data.groupby(["Rehabilitation_Program", "Injury_Type"])["Rehabilitation_Efficiency_Score"].mean()#after grouping the data calcualtz efficiency score
        data = data.unstack() #spreads the grouped data into a more tabular form that is easier to work with when plotting
        ax = data.plot(kind='bar', stacked=False, colormap="tab10", alpha=0.8, width=0.8) #create bar plot
        plt.title(f"Rehabilitation Program Efficiency (For {injury_type} & Knee Injury)") #title of plot
        plt.xlabel("Rehabilitation Program")#xlabel
        plt.ylabel("Efficiency Score")#ylabel
        plt.xticks(rotation=10)#rotate the label on the x axis for clarity
        plt.legend(title="Injury Types")#legend
        plt.grid(axis='y', linestyle='--', alpha=0.7)#create a grid
    elif shoulder: #check if shoulder injury is selected
        data = df[df["Injury_Type"].isin(['Shoulder Dislocation', injury_type])] ##filter the data for shoulder dislocation and the selected injury type
        data = data.groupby(["Rehabilitation_Program", "Injury_Type"])["Rehabilitation_Efficiency_Score"].mean()#after grouping the data calcualtz efficiency score
        data = data.unstack() #spreads the grouped data into a more tabular form that is easier to work with when plotting
        ax = data.plot(kind='bar', stacked=False, colormap="tab10", alpha=0.8, width=0.8) #create bar plot
        plt.title(f"Rehabilitation Program Efficiency (For {injury_type} & Shoulder Dislocation)") #title the plot
        plt.xlabel("Rehabilitation Program")#xlabel
        plt.ylabel("Efficiency Score")#ylabel
        plt.xticks(rotation=10)#rotate the x label for clarity
        plt.legend(title="Injury Types")#put a legend to the graph
        plt.grid(axis='y', linestyle='--', alpha=0.7)#put a grid on it
    elif ham: #if ham injury is selected
        data = df[df["Injury_Type"].isin(['Hamstring Strain', injury_type])] #filter the data for hamstring strain and the selected injury type
        data = data.groupby(["Rehabilitation_Program", "Injury_Type"])["Rehabilitation_Efficiency_Score"].mean()#after grouping the data calcualtz efficiency score
        data = data.unstack()#spreads the grouped data into a more tabular form that is easier to work with when plotting
        ax = data.plot(kind='bar', stacked=False, colormap="tab10", alpha=0.8, width=0.8) #create the bar plot
        plt.title(f"Rehabilitation Program Efficiency (For {injury_type} & Hamstring Strain)")#title the graph
        plt.xlabel("Rehabilitation Program")#xlabel
        plt.ylabel("Efficiency Score")#ylabel
        plt.xticks(rotation=10)#rotate the x labels for clarity
        plt.legend(title="Injury Types")#put a legend
        plt.grid(axis='y', linestyle='--', alpha=0.7)#put a grid
    else: #the following lines represent the default case for only injury type
        data = df[df["Injury_Type"] == injury_type].groupby("Rehabilitation_Program")["Rehabilitation_Efficiency_Score"].mean()#filter and group data
        plt.bar(data.index, data.values, color="lightblue") #create bar plot
        plt.title(f"Rehabilitation Program Efficiency for {injury_type}") #put a title to it
        plt.xlabel("Rehabilitation Program") #label the x axis
        plt.ylabel("Efficiency Score")#label the y axis
        plt.xticks(rotation=10)#rotate the x labels
        plt.grid(axis='y', linestyle='--', alpha=0.7)#put a grid to it




def RehabTime(injury_type, df, trendline=False): #this function will evaluate the efficiency of rehab time
    data = df[df["Injury_Type"] == injury_type] #firt filter the data for the particular injury type
    x = data["Rehabilitation_Time_weeks"] #the x axis will represent values of rehabilitation time weeks
    y = data["Rehabilitation_Efficiency_Score"] #the y axis will represent the rehab efficiancy score
    plt.scatter(x, y, color='blue', alpha=0.6) #create a scatter plot with x and y
    plt.title(f"Rehabilitation Time vs Efficiency for {injury_type}") #put a title to it
    plt.xlabel("Rehabilitation Time (weeks)")#label the x axis
    plt.ylabel("Efficiency Score")#and the y axis
    plt.grid(linestyle='--', alpha=0.7)# create a grid
    if trendline: #if a trend line is requested
        n = len(x) #the n variable represents the number of x data points
        sum_x = sum(x) #the variable sum_x containes their sum
        sum_y = sum(y) #the sum of y axis values
        sum_xy = sum(x * y) #sum of the product of x and y axis data values
        sum_x2 = sum(x ** 2) #squared x values
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2) #slope of the trend line
        b = (sum_y - m * sum_x) / n #y intercept
        trend_y = [m * i + b for i in x] #y values for the trend line
        plt.plot(x, trend_y, color="red", linestyle="--", label="Trendline") #plot the trend line
        plt.legend() #legend the plot

def EfficiencyByProgram(injury_type, df): #this function will evaluate the efficiancy program by program and age group
    age_bins = [0, 20, 25, 30, 35, float("inf")] #define the age bins that the data is gonna be grouped in
    age_labels = ["<20", "20-25", "25-30", "30-35", ">35"] #label for the bins
    data = df[df["Injury_Type"] == injury_type].copy() #filter the data for the particular injury type
    data["Age_group"] = pd.cut(data["Age"], bins=age_bins, labels=age_labels) #create age groups in the data
    avg_efficiency = (data.groupby(["Rehabilitation_Program", "Age_group"], observed=False).mean("Rehabilitation_Efficiency_Score")).reset_index()#calculate avergae efficiency score by programs and age groups
    for program in avg_efficiency["Rehabilitation_Program"].unique(): #iterate through unique programs
        program_data = avg_efficiency[avg_efficiency["Rehabilitation_Program"] == program] #filter data that corresponds to the program
        plt.plot(program_data["Age_group"], program_data["Rehabilitation_Efficiency_Score"],marker="o", label=program) #plot efficiency score by age group for the program
    plt.xlabel("Age") #label x axis
    plt.ylabel("Average Rehabilitation Efficiency Score") #label y axis
    plt.title(f"Rehabilitation Efficiency by Program and Age for {injury_type}") #title the grapj
    plt.legend(title="Rehabilitation Program")#legend it
    plt.grid(axis="both", linestyle="--", linewidth=0.7, alpha=0.7)#create a grid

def draw_header(win): #function that will draw the header of the graphical window
    header_bg = Rectangle(Point(0, 0), Point(800, 60)) #create the rectangle for the header
    header_bg.setFill("darkblue") #this rectangle will be dark blue
    header_bg.setOutline("darkblue") #the outline as well
    header_bg.draw(win) #draw the rectangle in the window

    header_text = Text(Point(400, 30), "Rehabilitation Analysis Tool")  #create a text for describing the function of the program
    header_text.setSize(20) #set the text size
    header_text.setStyle("bold")#set the text style
    header_text.setTextColor("white")#set the text color to white for clarity
    header_text.draw(win)#draw it in the window

def draw_basketball(win): #this function will draw a basket ball in the window for aesthetic purposes
    basketball = Circle(Point(150, 150), 80) #draw the circle for the ball
    basketball.setFill("orange")#fill it in orange
    basketball.setOutline("black")#the outline in black
    basketball.setWidth(3)#set the width of the borders
    basketball.draw(win)#draw it in the window

    horizontal = Line(Point(70, 150), Point(230, 150)) #create a horizontal line on the basket ball
    horizontal.setWidth(2)# set the width
    horizontal.setFill("black")#the color of th eline
    horizontal.draw(win) #draw it in the window

    curve1 = Oval(Point(70, 110), Point(230, 190)) #draw the upper curve in the ball
    curve1.setOutline("black")#in black
    curve1.setWidth(2)#set the width
    curve1.draw(win)#draw it in the window

    curve2 = Oval(Point(70, 190), Point(230, 110))#draw the lower curve in the ball
    curve2.setOutline("black")#in black
    curve2.setWidth(2)#set width
    curve2.draw(win)#draw it in the window

def draw_basketball_net(win): #now this function will draw a second illustration , a basketball net again for aesthetic purposes
    net_base = Point(650, 300)  # Adjusted base position to center within the window
    net_width = 92  # Increased width to make the net larger
    net_height = 100  # Increased height for a bigger net

    for i in range(5):  # Adjusted range for smoother net lines
        x_offset = i * net_width // 5 #calculate the horizontal offset for each line
        top_point = Point(net_base.x - net_width // 2 + x_offset, net_base.y - 20) #define the top point of the line
        bottom_point = Point(net_base.x - net_width // 2 + x_offset, net_base.y + net_height) #define the bottom point of the line
        net_line = Line(top_point, bottom_point) #create the line from top to bottom
        net_line.setOutline("white")#color it in white
        net_line.setWidth(2)#set the width of the line
        if i != 0:#dont draw the first line to leave space for hoop
            net_line.draw(win)#draw it on the window

    Line1 = Line(Point(601, 295), Point(608, 400)) #create the line for the side of the net
    Line1.setOutline('white')#color it in white
    Line1.setWidth(2)#set the width
    Line1.draw(win)#draw it in the window

    Line2 = Line(Point(698, 295), Point(692, 400))#create another line for the other side
    Line2.setOutline('white')#color it in white
    Line2.setWidth(2)#set the width
    Line2.draw(win)#draw the line in the window

    for i in range(5): #this loop will create the horizontal lines for the net
        y_offset = i * net_height // 5 #calculate the vertical offset for these lines
        left_point = Point(net_base.x - net_width // 2, net_base.y + y_offset)# define the left endpoint
        right_point = Point(net_base.x + net_width // 2, net_base.y + y_offset)# define the right end point
        net_line = Line(left_point, right_point)#create the lines from left to right
        net_line.setOutline("white")#color them in white
        net_line.setWidth(2)#set their width
        if i != 0: #avoid drawing the first line
            net_line.draw(win)#draw the line on the window
    hoop_width = 110 #width of the basketball hoop
    hoop = Oval(Point(net_base.x - hoop_width // 2, net_base.y - 20), Point(net_base.x + hoop_width // 2, net_base.y)) #draw oval that will be th ehoop
    hoop.setOutline("red") #the hoop will be red
    hoop.setWidth(5) #set it's width
    hoop.draw(win) #draw it in the window

    backboard = Rectangle(Point(708,200), Point(720,310)) #the blackboard will be a rectangle
    backboard.setFill("white")#a white rectangle
    backboard.setOutline("black")#set the outline of it to black
    backboard.setWidth(3)#the width is set
    backboard.draw(win)#draw it in the window

def draw_nba_logo(win):#now this function will draw an NBA logo for aesthetic purposes
    logo_bg = Rectangle(Point(300, 100), Point(500, 180))# the logo will be based on a rectangle
    logo_bg.setFill("white")#filled in white
    logo_bg.setOutline("black")#outlined in black
    logo_bg.setWidth(2)#width of 2
    logo_bg.draw(win)#draw the base of the logo in the window

    logo_text = Text(Point(400, 145), "NBA") #in the rectangle place a text "NBA"
    logo_text.setSize(35) #set the next size
    logo_text.setStyle("bold") #set the style to bold
    logo_text.setTextColor("blue")#set the color to blue
    logo_text.draw(win)#draw it in the window

def draw_buttons(win, injury_buttons, graph_buttons): #this function will create and display the bottons on the window
    for injury, button, label in injury_buttons: #this will loop through all injury bottons
        try:
            button.undraw() #remove previously done buttons
            label.undraw() #removes previously done labels
        except:
            pass #ignore if nothing to undraw
        button.setFill("lightblue") #set the buttons to light blue
        button.setOutline("darkblue") #outline to dark blue
        button.setWidth(2) #set the width
        button.draw(win) #draw them in the window
        label.setSize(12) #set the label size
        label.draw(win)#and draw it in the window

    for text, func, button, label in graph_buttons: #loop through all graph bottons
        try:
            button.undraw() #undraw previous buttons
            label.undraw() #undraw previous labels
        except:
            pass#if nothing to undraw ignore
        button.setFill("lightgreen") #fill the buttons to light green
        button.setOutline("darkgreen") #their outline to dark green
        button.setWidth(2)#set the width
        label.setSize(12)#set the label siz
        button.draw(win)#draw the bottons on the window
        label.draw(win)#draw the labels on the window

def main_page(win, injury_buttons, graph_buttons): #this function will set up the main page
    win.setBackground("lightgray") #the background will be set to grey
    draw_header(win) #call the function that draw the header
    draw_basketball(win) #call the function that drew the basketball
    draw_nba_logo(win) #call the function that drew the nba logo
    draw_basketball_net(win) #call the function that drew the net
    draw_buttons(win, injury_buttons, graph_buttons) #call the function that drew the buttons
    footer = Line(Point(0, 550), Point(800, 550)) #create a footer at the bottom of the window
    footer.setFill("darkgray") #it'll be dark grey
    footer.setWidth(2) #set the width
    footer.draw(win)#draw it in the window

def graph_page(win, header, filename,selected_injury): #thus function will define the graph page
    win.setBackground("lightgray") #set it's background to grey
    header.setText("Graph Display") #set a text in the header of the page
    img = Image(Point(400, 250), filename) # Load the image of the graph from the given filename and center it at (400, 250).
    img.draw(win) #draw it in the window

    save_button = Rectangle(Point(600, 550), Point(750, 590)) #this botton is set to save the graph
    save_button.setFill("lightgreen")#fill it in lightgreen
    save_button.draw(win) #draw it in the window
    save_label = Text(save_button.getCenter(), "Save Graph") #label the botton
    save_label.draw(win) #draw it in the window

#initialize the place holders for all the bottons
    trendline_button = None
    trendline_label = None
    acltear_button = None
    acltear_label = None
    anklesprain_button = None
    anklesprain_label = None
    kneeinjury_button = None
    kneeinjury_label = None
    shoulderdislocation_button = None
    shoulderdislocation_label = None
    hamstringstrain_button = None
    hamstringstrain_label = None

    if "rehab_time" in filename:  # check if "rehab_time" is in the file
        trendline_button = Rectangle(Point(618, 12), Point(718, 42))  # create a rectangle button for trendline
        trendline_button.setFill("coral")  # fill with coral color
        trendline_button.draw(win)  # draw the button
        trendline_label = Text(trendline_button.getCenter(), "Add Trendline")  # add a label for the button
        trendline_label.draw(win)  # draw the label

    if "rehab_program" in filename:  # check if "rehab_program" is in the file
        acltear_button = Rectangle(Point(7, 7), Point(107, 37))  # create a rectangle button for acl tear injury
        # the button color is different based on whether the selected injury is ACL tear
        if selected_injury in ['ACL Tear']:  # check if the selected injury is ACL tear.
            acltear_button.setFill("lightgreen")  # if it is, the color is light green
        else: # if it's not ACL tear
            acltear_button.setFill("coral") # the color is coral
        acltear_button.draw(win)  # draw the button
        acltear_label = Text(acltear_button.getCenter(), "acl tear")  # add a label for the button
        acltear_label.draw(win) # draw the label

        anklesprain_button = Rectangle(Point(7, 47), Point(107, 77))  # create a rectangle button for ankle sprain
        # the button color is different based on whether the selected injury is ankle sprain
        if selected_injury in ['Ankle Sprain']: # if the selected injury is ankle sprain
            anklesprain_button.setFill("lightgreen")  # the color for the button is lightgreen
        else: # if it's not,
            anklesprain_button.setFill("coral")  # the color is coral
        anklesprain_button.draw(win)  # draw the button
        anklesprain_label = Text(anklesprain_button.getCenter(), "ankle sprain")  # add a label "ankle sprain" for the button
        anklesprain_label.draw(win)  # draw the label

        kneeinjury_button = Rectangle(Point(7, 87), Point(107, 117))  # create a rectangle button for knee injury
        # the button color is different based on whether the selected injury is knee injury
        if selected_injury in ['Knee Injury']:  # if the selected injury is knee injury
            kneeinjury_button.setFill("lightgreen")  # the color for the button is lightgreen
        else:   # if it's not,
            kneeinjury_button.setFill("coral")  # the color is coral
        kneeinjury_button.draw(win)  # draw the button
        kneeinjury_label = Text(kneeinjury_button.getCenter(), "knee injury")  # add a label "knee injury" for the button
        kneeinjury_label.draw(win)  # draw the label

        shoulderdislocation_button = Rectangle(Point(7, 127), Point(107, 157))  # create a rectangle button for shoulder dislocation
        # the button color is different based on whether the selected injury is shoulder dislocation
        if shoulderdislocation_button in ['Shoulder Dislocation']:   # if the selected injury is shoulder dislocation
            acltear_button.setFill("lightgreen")  # the color for the button is lightgreen
        else:   # if it's not,
            shoulderdislocation_button.setFill("coral")  # the color is coral
        shoulderdislocation_button.draw(win)  # draw the button
        shoulderdislocation_label = Text(shoulderdislocation_button.getCenter(), "shoulder dislocation")  # add a label "shoulder dislocation" for the button
        shoulderdislocation_label.draw(win)  # draw the label

        hamstringstrain_button = Rectangle(Point(7, 167), Point(107, 197))  # create a rectangle button for hamstring strain
        # the button color is different based on whether the selected injury is hamstring strain
        if selected_injury in ['Hamstring Strain']:  # if the selected injury is hamstring strain
            hamstringstrain_button.setFill("lightgreen")  # the color for the button is lightgreen
        else:  # if it's not,
            hamstringstrain_button.setFill("coral")  # the color is coral
        hamstringstrain_button.draw(win)  # draw the button
        hamstringstrain_label = Text(hamstringstrain_button.getCenter(), "hamstring strain")  # add a label "hamstring strain" for the button
        hamstringstrain_label.draw(win)  # draw the label

    return_button = Rectangle(Point(300, 550), Point(500, 590))  # create a button to return to the main page
    return_button.setFill("lightblue")  # fill the button with light blue color
    return_button.draw(win)  # draw the button
    return_label = Text(return_button.getCenter(), "Return to Home")  # add a label "Return to Home" to the button to let the user know the use of the button
    return_label.draw(win)  # draw the label
    # return all the elements
    return img, save_button, save_label, trendline_button, trendline_label, return_button, return_label, acltear_button, acltear_label, anklesprain_button, anklesprain_label, kneeinjury_button, kneeinjury_label, shoulderdislocation_button, shoulderdislocation_label, hamstringstrain_button, hamstringstrain_label

def main():  # main function for the application
    df = load()  # load the dataframe that contains the data for rehabilitation
    if df is None:  # if the dataframe if None
        print("No file selected.")  # tell the user that there's no file selected
        return  # quit the program

    injury_types = df["Injury_Type"].unique()   # get unique injury types and save it in a variable
    win = GraphWin("Rehabilitation Analysis", 800, 600)   # initialize a window called "Rehabilitation Analysis"
    header = Text(Point(400, 30), "Rehabilitation Analysis Tool")   # draw a header
    header.setSize(14)  # set font size to 14
    header.setStyle("bold")   # set style bold
    header.draw(win)   # draw

    selected_injury_text = Text(Point(400, 80), "No injury selected")  # create a text for selected injury (initialize with a placeholder showing that no injury is selected)
    selected_injury_text.setSize(12)  # set font size to 12
    selected_injury_text.setStyle("italic")  # set the style to italic
    selected_injury_text.setTextColor("darkblue")  # set text color to dark blue
    selected_injury_text.draw(win)  # draw the text

    injury_buttons = []  # create a list to store injury buttons
    for i, injury in enumerate(injury_types):  # loop through each injury to create buttons
        button = Rectangle(Point(300, 180 + i * 50), Point(500, 220 + i * 50))  # create a button for each injury (the second button will be under the first button, and so on)
        button.setFill("lightblue")  # set the color to light blue
        label = Text(button.getCenter(), injury)  # add a label for each injury to the button
        label.setSize(12)  # set font size to 12
        injury_buttons.append((injury, button, label))  # append the injury type, button, and label for each injury to the list initialed in the beginning

    graph_buttons = []  # initialize a list to store graph buttons
    graph_data = [
        ("Graph Rehab Program", RehabProgram, Point(150, 500)),
        ("Graph Rehab Time", RehabTime, Point(400, 500)),
        ("Graph Efficiency by Program", EfficiencyByProgram, Point(650, 500)),
    ]  # create a list for graph options and their positions in the window (they will be next to each other in a horizontal line)
    for text, func, center in graph_data:  # loop through each options
        button = Rectangle(Point(center.getX() - 100, center.getY() - 25),
                           Point(center.getX() + 100, center.getY() + 25))  # create a button for each option
        button.setFill("lightgreen")  # set the color to light green
        label = Text(button.getCenter(), text)  # add a label for each option
        graph_buttons.append((text, func, button, label))  # append the text, function, button, and label for each option to the graph buttons list

    main_page(win, injury_buttons, graph_buttons) # display the main page on the window with injury buttons and graph buttons.

    selected_injury = None  # initialize the selected injury as None
    while True:  # a loop for user activities on the main page
        try:
            click = win.getMouse()  # wait for a mouse click

            for injury, button, label in injury_buttons:  # loop through the items in injury_buttons
                if button.getP1().getX() <= click.getX() <= button.getP2().getX() and \
                   button.getP1().getY() <= click.getY() <= button.getP2().getY():  # if the mouse click is within a specific button
                    selected_injury = injury  # the selected injury is the injury from that button
                    selected_injury_text.setText(f"Selected Injury: {selected_injury}")  # set a new selected injury text to the selected injury
                    break  # exit the loop

            if selected_injury:  # if an injury is selected
                for text, func, button, label in graph_buttons:  # # loop through the items in graph_buttons
                    if button.getP1().getX() <= click.getX() <= button.getP2().getX() and \
                            button.getP1().getY() <= click.getY() <= button.getP2().getY():  # if the mouse click is within a specific button for graph
                        graph_background = Rectangle(Point(0, 0), Point(800, 600))  # create a background for the graph
                        graph_background.setFill("white")  # set the background color as white
                        graph_background.setOutline("white")  # set the outline color as white
                        graph_background.draw(win)  # draw the background

                        filename = f"{text.replace(' ', '_').lower()}.png"  # create a filename when saving a graph
                        save_plot(lambda injury: func(injury, df), selected_injury, filename)  # save the graph
                        # get elements for the graph page
                        img, save_button, save_label, trendline_button, trendline_label, return_button, return_label, acltear_button, acltear_label, anklesprain_button, anklesprain_label, kneeinjury_button, kneeinjury_label, shoulderdislocation_button, shoulderdislocation_label, hamstringstrain_button, hamstringstrain_label = graph_page(win, header, filename, selected_injury)
                        while True:  # a loop for user activities on the graph page
                            graph_click = win.getMouse()  # wait for a mouse click

                            if save_button.getP1().getX() <= graph_click.getX() <= save_button.getP2().getX() and \
                                    save_button.getP1().getY() <= graph_click.getY() <= save_button.getP2().getY():  # if the mouse click is within the save button
                                save_path = asksaveasfilename(defaultextension=".png",
                                                              filetypes=[("PNG files", "*.png"),
                                                                         ("All files", "*.*")],
                                                              title="Save Graph As")  # ask the user for the path to save the file
                                if save_path:
                                    plt.savefig(save_path)  # save the graph
                                    plt.close()  # close
                                    print(f"Graph saved as {save_path}")  # let the user know that the graph's saved

                            if trendline_button and trendline_button.getP1().getX() <= graph_click.getX() <= trendline_button.getP2().getX() and \
                                    trendline_button.getP1().getY() <= graph_click.getY() <= trendline_button.getP2().getY():  # if the mouse click is within the trendline button
                                filename_with_trendline = f"{filename.replace('.png', '_trendline.png')}"  # create a file name for a graph with trendline
                                save_plot(lambda injury: RehabTime(injury, df, trendline=True), selected_injury, filename_with_trendline)  # save the graph with the trendline
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_trendline)  # create a new graph with the trendline
                                img.draw(win)  # draw the new graph
                                trendline_button.undraw()  # remove the trendline button
                                trendline_label.undraw()  # remove the trendline label

                            if selected_injury not in ['ACL Tear'] and acltear_button and acltear_button.getP1().getX() <= graph_click.getX() <= acltear_button.getP2().getX() and \
                                    acltear_button.getP1().getY() <= graph_click.getY() <= acltear_button.getP2().getY():  # if the mouse click is within the ACL Tear button and the selected injury is not ACL Tear
                                filename_with_stacked = f"{filename.replace('.png', '_stacked.png')}"  # create a file name for a graph with ACL Tear and the selected injury data
                                save_plot(lambda injury: RehabProgram(injury, df, acltear=True), selected_injury, filename_with_stacked)  # save the graph with ACL Tear and the selected injury data
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_stacked)  # create a new graph with ACL Tear and the selected injury data
                                img.draw(win)  # draw the new graph
                                # remove all the buttons and the labels
                                acltear_button.undraw()
                                acltear_label.undraw()
                                anklesprain_button.undraw()
                                anklesprain_label.undraw()
                                kneeinjury_button.undraw()
                                kneeinjury_label.undraw()
                                shoulderdislocation_button.undraw()
                                shoulderdislocation_label.undraw()
                                hamstringstrain_button.undraw()
                                hamstringstrain_label.undraw()
                            if selected_injury not in ['Ankle Sprain'] and anklesprain_button and anklesprain_button.getP1().getX() <= graph_click.getX() <= anklesprain_button.getP2().getX() and \
                                    anklesprain_button.getP1().getY() <= graph_click.getY() <= anklesprain_button.getP2().getY():  # if the mouse click is within the ankle sprain button and the selected injury is not ankle sprain
                                filename_with_stacked = f"{filename.replace('.png', '_stacked.png')}"  # create a file name for a graph with ankle sprain and the selected injury data
                                save_plot(lambda injury: RehabProgram(injury, df, ankle=True), selected_injury, filename_with_stacked)  # save the graph with ankle sprain and the selected injury data
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_stacked)  # create a new graph with ankle sparin and the selected injury data
                                img.draw(win)  # draw the new graph
                                # remove all the buttons and the labels
                                acltear_button.undraw()
                                acltear_label.undraw()
                                anklesprain_button.undraw()
                                anklesprain_label.undraw()
                                kneeinjury_button.undraw()
                                kneeinjury_label.undraw()
                                shoulderdislocation_button.undraw()
                                shoulderdislocation_label.undraw()
                                hamstringstrain_button.undraw()
                                hamstringstrain_label.undraw()
                            if selected_injury not in ['Knee Injury'] and kneeinjury_button and kneeinjury_button.getP1().getX() <= graph_click.getX() <= kneeinjury_button.getP2().getX() and \
                                    kneeinjury_button.getP1().getY() <= graph_click.getY() <= kneeinjury_button.getP2().getY():  # if the mouse click is within the knee injury button and the selected injury is not knee injury
                                filename_with_stacked = f"{filename.replace('.png', '_stacked.png')}"  # create a file name for a graph with knee injury and the selected injury data
                                save_plot(lambda injury: RehabProgram(injury, df, knee=True), selected_injury, filename_with_stacked)  # save the graph with knee injury and the selected injury data
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_stacked)  # create a new graph with knee injury and the selected injury data
                                img.draw(win)  # draw the new graph
                                # remove all the buttons and the labels
                                acltear_button.undraw()
                                acltear_label.undraw()
                                anklesprain_button.undraw()
                                anklesprain_label.undraw()
                                kneeinjury_button.undraw()
                                kneeinjury_label.undraw()
                                shoulderdislocation_button.undraw()
                                shoulderdislocation_label.undraw()
                                hamstringstrain_button.undraw()
                                hamstringstrain_label.undraw()
                            if selected_injury not in ['Shoulder Dislocation'] and shoulderdislocation_button and shoulderdislocation_button.getP1().getX() <= graph_click.getX() <= shoulderdislocation_button.getP2().getX() and \
                                    shoulderdislocation_button.getP1().getY() <= graph_click.getY() <= shoulderdislocation_button.getP2().getY():  # if the mouse click is within the shoulder dislocation button and the selected injury is not shoulder dislocation
                                filename_with_stacked = f"{filename.replace('.png', '_stacked.png')}"
                                save_plot(lambda injury: RehabProgram(injury, df, shoulder=True), selected_injury, filename_with_stacked)  # save the graph with shoulder dislocation and the selected injury data
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_stacked)  # create a new graph with shoulder dislocation and the selected injury data
                                img.draw(win)  # draw the new graph
                                # remove all the buttons and the labels
                                acltear_button.undraw()
                                acltear_label.undraw()
                                anklesprain_button.undraw()
                                anklesprain_label.undraw()
                                kneeinjury_button.undraw()
                                kneeinjury_label.undraw()
                                shoulderdislocation_button.undraw()
                                shoulderdislocation_label.undraw()
                                hamstringstrain_button.undraw()
                                hamstringstrain_label.undraw()
                            if selected_injury not in ['Hamstring Strain'] and hamstringstrain_button and hamstringstrain_button.getP1().getX() <= graph_click.getX() <= hamstringstrain_button.getP2().getX() and \
                                    hamstringstrain_button.getP1().getY() <= graph_click.getY() <= hamstringstrain_button.getP2().getY():  # if the mouse click is within the hamstring strain button and the selected injury is not hamstring strain
                                filename_with_stacked = f"{filename.replace('.png', '_stacked.png')}"  # create a file name for a graph with hamstring strain and the selected injury data
                                save_plot(lambda injury: RehabProgram(injury, df, ham=True), selected_injury, filename_with_stacked)  # save the graph with hamstring strain and the selected injury data
                                img.undraw()  # remove the graph from the window
                                img = Image(Point(400, 250), filename_with_stacked)  # create a new graph with hamstring strain and the selected injury data
                                img.draw(win)  # draw the new graph
                                # remove all the buttons and the labels
                                acltear_button.undraw()
                                acltear_label.undraw()
                                anklesprain_button.undraw()
                                anklesprain_label.undraw()
                                kneeinjury_button.undraw()
                                kneeinjury_label.undraw()
                                shoulderdislocation_button.undraw()
                                shoulderdislocation_label.undraw()
                                hamstringstrain_button.undraw()
                                hamstringstrain_label.undraw()

                            if return_button.getP1().getX() <= graph_click.getX() <= return_button.getP2().getX() and \
                                    return_button.getP1().getY() <= graph_click.getY() <= return_button.getP2().getY():  # if the mouse click is within the return button
                                img.undraw()  # remove the grapg from the window
                                plt.close()  # close the plot
                                plt.close()  # close the plot
                                save_button.undraw()  # remove the save button
                                save_label.undraw()  # remove the save label
                                if trendline_button:  # if the trendline button exists
                                    trendline_button.undraw()  # remove the trendline button
                                    trendline_label.undraw()  # remove the trendline label
                                if acltear_button:  # if the acl tear button exists
                                    # remove all the buttons and the labels
                                    acltear_button.undraw()
                                    acltear_label.undraw()
                                    anklesprain_button.undraw()
                                    anklesprain_label.undraw()
                                    kneeinjury_button.undraw()
                                    kneeinjury_label.undraw()
                                    shoulderdislocation_button.undraw()
                                    shoulderdislocation_label.undraw()
                                    hamstringstrain_button.undraw()
                                    hamstringstrain_label.undraw()
                                return_button.undraw()  # remove th ereturn button
                                return_label.undraw()  # remove the return label
                                graph_background.undraw()  # remove rthe background

                                break  # exit the loop
                        break  # exit the loop for the graph window
        except GraphicsError:  # if there's a graphics error
            break  # break the loop
    win.close()  # close the window


main()  # run the main function