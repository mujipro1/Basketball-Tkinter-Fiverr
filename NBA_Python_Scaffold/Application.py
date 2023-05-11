'''
Main application file for the NBA League application.
This file contains the Application class for the NBA League application.
'''
from tkinter import *
from tkinter import ttk
from Teams import Teams
from PIL import ImageTk, Image
from Validator import Validator
from Player import Player

class Application:
    '''Main Tkinter Application class'''
    root = Tk()

    def __init__(self) -> None:
        '''Initialize the application'''
        root = self.root
        root.title("Basketball League")
        root.geometry("800x600+300+50")
        root.resizable(False, False)
        # png icon for window
        root.iconbitmap('images/nba.ico')
        root.configure(background='#0f0f0f')

        # Load images
        self.img = PhotoImage(file='images/NBA_Back.png')
        self.img2 = PhotoImage(file='images/nba.png')
        self.img3 = PhotoImage(file='images/error.png')
        self.img4 = PhotoImage(file='images/edit.png')

        # reduce image size using PIL resize
        img = Image.open('images/NBA_Back.png')
        img = img.resize((600, 300))
        self.reducedImg = ImageTk.PhotoImage(img)

        self.main_menu()
        self.run()

    def ButtonStyle(self, width, height):
        '''Create a custom style for buttons'''
        # Global style for Buttons
        self.globalButtonStyle = {'font': ('Arial', 13),
                            'bg': '#2b2b2b', 'fg': 'white',
                            'relief': 'flat',
                            'cursor': 'hand2'
                            }

        buttonStyle = self.globalButtonStyle
        buttonStyle['width'] = width
        buttonStyle['height'] = height
        return buttonStyle

    def main_menu(self) -> None:
        '''Main menu screen'''
        root = self.root

        # PlayOff Image Frame
        frameTop = Frame(root, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)
        imgLabel = Label(frameTop, image=self.img, bg='#0f0f0f')
        imgLabel.pack()

        # Options Frame
        frameBottom = Frame(root, bg='#0f0f0f')
        frameBottom.pack(side=TOP, fill=BOTH, expand=True)

        # Buttons
        # Teams, New Session, Exit Game Buttons
        teamsButton = Button(frameBottom, text='Explore the Teams', command=self.TeamsMenu)
        teamsButton.pack(side=LEFT, padx=10, pady=5, expand=True)
        newSeasonButton = Button(frameBottom, text='Arrange a new Season', command=self.SeasonMenu)
        newSeasonButton.pack(side=LEFT, padx=10, pady=5, expand=True)
        exitButton = Button(frameBottom, text='Exit Game', command=exit)
        exitButton.pack(side=LEFT, padx=10, pady=5, expand=True)

        # apply the custom style to buttons
        teamsButton.configure(self.ButtonStyle(20, 4))
        newSeasonButton.configure(self.ButtonStyle(20, 4))
        exitButton.configure(self.ButtonStyle(20, 4))

    def SeasonMenu(self):
        '''New Season screen'''

        root2 = Toplevel(self.root)
        root2.title("New Season")
        root2.geometry("600x600+400+50")
        root2.resizable(False, False)
        # png icon for window
        root2.iconbitmap('images/nba.ico')
        root2.configure(background='#0f0f0f')

        # PlayOff Image Frame
        frameTop = Frame(root2, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)

        imgLabel = Label(frameTop, image=self.reducedImg, bg='#0f0f0f')
        imgLabel.pack()

        # Options Frame
        frameBottom = Frame(root2, bg='#0f0f0f')
        frameBottom.pack(side=TOP, fill=BOTH, expand=True)
        # Buttons
        # Round, Current, Game, Result, Close Buttons

        roundButton = Button(frameBottom, text='Round')
        roundButton.pack(side=TOP, padx=10, pady=4)
        currentButton = Button(frameBottom, text='Current')
        currentButton.pack(side=TOP, padx=10, pady=4)
        gameButton = Button(frameBottom, text='Game')
        gameButton.pack(side=TOP, padx=10, pady=4)
        resultButton = Button(frameBottom, text='Result')
        resultButton.pack(side=TOP, padx=10, pady=4)
        closeButton = Button(frameBottom, text='Close', command=root2.destroy)
        closeButton.pack(side=TOP, padx=10, pady=4)


        # apply the custom style to buttons
        roundButton.configure(self.ButtonStyle(25, 2))
        currentButton.configure(self.ButtonStyle(25, 2))
        gameButton.configure(self.ButtonStyle(25, 2))
        resultButton.configure(self.ButtonStyle(25, 2))
        closeButton.configure(self.ButtonStyle(25, 2))


    def TeamsMenu(self) -> None:
        '''Teams screen'''

        root3 = Toplevel(self.root)
        root3.title("Teams Menu")
        root3.geometry("600x600+400+50")
        root3.resizable(False, False)
        # png icon for window
        root3.iconbitmap('images/nba.ico')
        root3.configure(background='#0f0f0f')

        # Label stating All teams
        label = Label(root3, text='All Teams', font=('Arial', 16), bg='#0f0f0f', fg='white')
        label.pack(side=TOP, pady=10)

        # treeview Frame
        frameTop = Frame(root3, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)

        # treeview
        self.tree = ttk.Treeview(frameTop, columns=(1, 2, 3, 4), show='headings', height=20)
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frameTop, orient=VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure columns
        self.tree.column(1, width=130, anchor='c')
        self.tree.column(2, width=130, anchor='c')
        self.tree.column(3, width=150, anchor='c')
        self.tree.column(4, width=150, anchor='c')

        # Configure headings
        self.tree.heading(1, text='Team Name')
        self.tree.heading(2, text='Number Of Players')
        self.tree.heading(3, text='Average Player Credit')
        self.tree.heading(4, text='Average Age')

        # Insert data into treeview
        self.teams = Teams()
        allTeams = self.teams.getTeams()
        for team in allTeams:
            teamName = team.getName()
            teamPlayers = team.getPlayers()
            teamPlayersCount = len(teamPlayers)
            teamAvgCredit = team.getCurrentList().CountAvgCredit()
            teamAvgAge = team.getCurrentList().CountAvgAge()
            self.tree.insert('', 'end', values=(teamName, teamPlayersCount, teamAvgCredit, teamAvgAge))

        # Options Frame
        frameBottom = Frame(root3, bg='#0f0f0f')
        frameBottom.pack(side=TOP, fill=BOTH, expand=True)

        # Buttons
        # Add, Manage, Delete, Close Buttons
        addButton = Button(frameBottom, text='Add', command=self.addNewTeamScreen)
        addButton.pack(side=LEFT, padx=10, pady=5, expand=True)
        manageButton = Button(frameBottom, text='Manage',command=self.ManageTeam)
        manageButton.pack(side=LEFT, padx=10, pady=5, expand=True)
        deleteButton = Button(frameBottom, text='Delete',command=self.deleteTeam)
        deleteButton.pack(side=LEFT, padx=10, pady=5, expand=True)
        closeButton = Button(frameBottom, text='Close', command=root3.destroy)
        closeButton.pack(side=LEFT, padx=10, pady=5, expand=True)

        # apply the custom style to buttons
        addButton.configure(self.ButtonStyle(12, 3))
        manageButton.configure(self.ButtonStyle(12, 3))
        deleteButton.configure(self.ButtonStyle(12, 3))
        closeButton.configure(self.ButtonStyle(12, 3))

        # Disable manage and delete buttons initially
        manageButton.config(state="disabled")
        deleteButton.config(state="disabled")

        # Disable manage and delete buttons on selection
        def selectItem(a):
            curItem = self.tree.focus()
            if curItem:
                manageButton.config(state="normal")
                deleteButton.config(state="normal")
                addButton.config(state="disabled")
        
        # Bind selectItem function to self.treeview
        self.tree.bind('<<TreeviewSelect>>', selectItem)

        # If clicked on anywhere other than the rows(even the tree) disable manage and delete buttons
        def deselectItem(a):
            manageButton.config(state="disabled")
            deleteButton.config(state="disabled")
            addButton.config(state="normal")
        
        # Bind deselectItem function to self.treeview
        self.tree.bind('<Button-1>', deselectItem)


    def addNewTeamScreen(self):
        '''Add New Team Screen'''
        root4 = Toplevel(self.root)
        root4.title("Adding New Team")
        root4.geometry("500x300+450+150")    
        root4.resizable(False, False)

        root4.iconbitmap('images/nba.ico')
        root4.configure(background='#0f0f0f')

        #frame for window
        frameTop = Frame(root4, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)

        Label(frameTop, text='Team Details', font=('Arial', 20, 'bold'), bg='#0f0f0f', fg='white').pack(side=TOP, pady=20)
        Label(frameTop, text='Name', font=('Arial', 15), bg='#0f0f0f', fg='white').pack(side=TOP, pady=5)

        # New Team Entry
        self.newTeam = Entry(frameTop, font=('Arial', 12))
        self.newTeam.pack(side=TOP, pady=5)

        # Add Team Button
        addButton = Button(frameTop, text='Add', command=self.addTeam)
        addButton.pack(side=LEFT, padx=10, pady=10, expand=True)
        addButton.configure(self.ButtonStyle(15, 2))


    def addTeam(self):
        '''Add Team to Teams Array'''

        data = self.newTeam.get()
        if data == '':
            self.errorScreen("Please Enter Data")
            return

        allTeams = self.teams.getTeams()
        for team in allTeams:
            teamName = team.getName()
            if data == teamName:
                errorMessage = f"Team {teamName} already exists! "
                self.errorScreen(errorMessage)
                break


    def deleteTeam(self):
        '''Delete Team from Teams Array and treeview'''

        #get selected Team
        allTeams = self.teams.getTeams()
        curItem = self.tree.focus()
        if curItem:
            teamName = self.tree.item(curItem)['values'][0]
            for team in allTeams:
                if teamName == team.getName():
                    allTeams.remove(team)
                    self.tree.delete(curItem)
                    break
    
    def ManageTeam(self):
        '''Manage Team Screen'''
        root = Toplevel(self.root)
        root.geometry("600x600+400+50")
        root.resizable(False, False)
        root.iconbitmap('images/edit.ico')
        root.focus()

        #get team name
        curItem = self.tree.focus()
        teamName = self.tree.item(curItem)['values'][0]
        root.title(f"Managing Team {teamName}")

        # Team Name Frame
        frameTop = Frame(root, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)

        # Label stating Team Name
        Label(frameTop, text='Team Name', font=('Arial', 16), bg='#0f0f0f', fg='white').pack(side=LEFT, padx=20, pady=5)
        
        #Entry displaying Team Name
        self.teamNameEntry = Entry(frameTop, font=('Arial', 12))
        self.teamNameEntry.insert(0, teamName)
        self.teamNameEntry.pack(side=LEFT, padx=15, pady=5)
        
        # treeview Frame
        frameMid = Frame(root, bg='#0f0f0f')
        frameMid.pack(side=TOP, fill=BOTH)

        # treeview
        self.tree2 = ttk.Treeview(frameMid, columns=(1, 2, 3, 4), show='headings', height=20)
        self.tree2.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frameMid, orient=VERTICAL, command=self.tree2.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure scrollbar
        self.tree2.configure(yscrollcommand=scrollbar.set)

        # Configure columns
        self.tree2.column(1, width=160, anchor='c')
        self.tree2.column(2, width=160, anchor='c')
        self.tree2.column(3, width=120, anchor='c')
        self.tree2.column(4, width=120, anchor='c')

        # Configure headings
        self.tree2.heading(1, text='Player Name')
        self.tree2.heading(2, text='Player Credit')
        self.tree2.heading(3, text='Player Age')
        self.tree2.heading(4, text='Player No.')

        # Insert data into treeview
        allTeams = self.teams.getTeams()
        for team in allTeams:
            if teamName == team.getName():
                teamPlayers = team.getPlayers()
                for player in teamPlayers:

                    playerName = player.getName()
                    playerCredit = player.getCredit()
                    playerAge = player.getAge()
                    playerNo = player.getNo()
                    self.tree2.insert('', 'end', values=(playerName, playerCredit, playerAge, playerNo))

        # Options Frame
        frameBottom = Frame(root, bg='#0f0f0f')
        frameBottom.pack(side=TOP, fill=BOTH, expand=True)

        # Buttons
        # Add, Update, Delete, Save and Close Buttons
        addButton = Button(frameBottom, text='Add',command=lambda:self.updatePlayerRecord(1)) 
        addButton.pack(side=LEFT, padx=5, pady=5, expand=True)
        updateButton = Button(frameBottom, text='Update', command=lambda:self.updatePlayerRecord(0))
        updateButton.pack(side=LEFT, padx=5, pady=5, expand=True)
        deleteButton = Button(frameBottom, text='Delete', command=self.deletePlayer)
        deleteButton.pack(side=LEFT, padx=5, pady=5, expand=True)
        saveandcloseButton = Button(frameBottom, text='Save and Close',
                                     command=lambda: self.saveAndCloseFunctionality(root))
        saveandcloseButton.pack(side=LEFT, padx=5, pady=5, expand=True)

        # apply the custom style to buttons
        addButton.configure(self.ButtonStyle(14, 3))
        updateButton.configure(self.ButtonStyle(14, 3))
        deleteButton.configure(self.ButtonStyle(14, 3))
        saveandcloseButton.configure(self.ButtonStyle(14, 3))

        # Disable update and delete buttons initially
        updateButton.config(state="disabled")
        deleteButton.config(state="disabled")

        # Disable update and delete buttons on selection
        def selectItem(a):
            curItem = self.tree2.focus()
            if curItem:
                updateButton.config(state="normal")
                deleteButton.config(state="normal")
                addButton.config(state="disabled")

        # Bind selectItem function to self.treeview
        self.tree2.bind('<<TreeviewSelect>>', selectItem)

        # If clicked on anywhere other than the rows(even the tree) disable update and delete buttons
        def deselectItem(a):
            updateButton.config(state="disabled")
            deleteButton.config(state="disabled")
            addButton.config(state="normal")

        # Bind deselectItem function to self.treeview
        self.tree2.bind('<Button-1>', deselectItem)

    def saveAndCloseFunctionality(self, root):
        '''Save and Close Button Functionality'''

        #update the team name       
        allTeams = self.teams.getTeams()
        curItem = self.tree.focus()
        prevName = self.tree.item(curItem)['values'][0]

        for team in allTeams:
            if team.getName() == prevName:
                team.setName(self.teamNameEntry.get())
                self.tree.item(curItem, values=(self.teamNameEntry.get(), len(team.getPlayers()),
                        team.getCurrentList().CountAvgCredit(), team.getCurrentList().CountAvgAge()))
        root.destroy()


    def updatePlayerRecord(self, flag):
        '''Update Player Record Screen'''
        root = Toplevel(self.root)
        root.geometry("600x400+400+100")
        root.resizable(False, False)
        root.iconbitmap('images/edit.ico')
        root.focus()

        #get player name
        curItem = self.tree2.focus()
        if flag == 0:
            playerName = self.tree2.item(curItem)['values'][0]
            root.title(f"Updating Player: {playerName}")
        else:
            root.title(f"Adding Player")

        # Player Name Frame
        frameTop = Frame(root, bg='#0f0f0f')
        frameTop.pack(side=TOP, fill=BOTH)

        Label(frameTop, text="Player Details", font=('Arial', 18), bg='#0f0f0f', fg='white').pack(side=LEFT, padx=40, pady=20)

        def makeFrame(name):
            nameframe = Frame(root, bg='#0f0f0f')
            nameframe.pack(side=TOP, fill=BOTH)
            
            # Label stating Player Name
            Label(nameframe, text=name, font=('Arial', 13), width=20 ,bg='#0f0f0f', fg='white').pack(side=LEFT, padx=40, pady=10)
            playerNameEntry = Entry(nameframe, font=('Arial', 13))
            playerNameEntry.pack(side=TOP, pady=10)

            return playerNameEntry

        self.PNameEntry = makeFrame('Player Name')
        self.PCredEntry = makeFrame('Player Cred')
        self.PAgeEntry = makeFrame('Player Age')
        self.PNoEntry = makeFrame('Player No.')
        
        if flag == 0:
            playerName = self.tree2.item(curItem)['values'][0]
            playerCred = self.tree2.item(curItem)['values'][1]
            playerAge = self.tree2.item(curItem)['values'][2]
            playerNo = self.tree2.item(curItem)['values'][3]

            self.PNameEntry.insert(0, playerName)
            self.PCredEntry.insert(0, playerCred)
            self.PAgeEntry.insert(0, playerAge)
            self.PNoEntry.insert(0, playerNo)
        else:
            #get latest player no
            allTeams = self.teams.getTeams()
            curItem = self.tree.focus() 
            teamName = self.tree.item(curItem)['values'][0]
            for team in allTeams:
                if team.getName() == teamName:
                    teamPlayers = team.getPlayers()
                    playerNo = teamPlayers[-1].getNo()
                    break

            self.PNameEntry.insert(0, "")
            self.PCredEntry.insert(0, "0.0")
            self.PAgeEntry.insert(0, "0")
            self.PNoEntry.insert(0, playerNo+1)

        #Options frame
        frameBottom = Frame(root, bg='#0f0f0f')
        frameBottom.pack(side=TOP, fill=BOTH, expand=True)

        # Buttons
        # Update, Add and Close Buttons
        updateButton = Button(frameBottom, text='Update', command=lambda:self.updateRecord(flag))
        updateButton.pack(side=LEFT, padx=5, pady=5, expand=True)
        addButton = Button(frameBottom, text='Add', command=lambda:self.updateRecord(flag)) 
        addButton.pack(side=LEFT, padx=5, pady=5, expand=True)
        closeButton = Button(frameBottom, text='Close', command=root.destroy) 
        closeButton.pack(side=LEFT, padx=5, pady=5, expand=True)

        # apply the custom style to buttons
        updateButton.configure(self.ButtonStyle(14, 3))
        addButton.configure(self.ButtonStyle(14, 3))
        closeButton.configure(self.ButtonStyle(14, 3))

        # Disable update and delete buttons for add player
        if flag == 1:
            updateButton.config(state="disabled")

        else:
            addButton.config(state="disabled")

    
    def updateRecord(self, flag):
        '''Update Player Record'''
        #get player name
        curItem = self.tree2.focus()
        if flag == 0:
            playerNameOld = self.tree2.item(curItem)['values'][0]

        #get team name
        curItem = self.tree.focus()
        teamName = self.tree.item(curItem)['values'][0]

        curPlayer = self.tree2.focus()

        #get player details
        playerName = self.PNameEntry.get()
        playerCred = self.PCredEntry.get()
        playerAge = self.PAgeEntry.get()
        playerNo = self.PNoEntry.get()

        #check if cred, age and no are numbers
        checkEngine = Validator()
        err = checkEngine.checkAllErrors(playerName, playerCred, playerAge, playerNo)
        if len(err) > 0:
            self.errorScreen(err[0])
            return

        if flag == 0:
            #update player details
            allTeams = self.teams.getTeams()
            for team in allTeams:
                if team.getName() == teamName:
                    teamPlayers = team.getPlayers()
                    for player in teamPlayers:
                        if player.getName() == playerNameOld:
                            self.tree2.item(curPlayer, values=(playerName, playerCred, playerAge, playerNo))
                            player.update(playerName, float(playerCred), int(playerAge), int(playerNo))
                            self.errorScreen("Player Updated!", 1)
                            break

        else:
            #add player details
            allTeams = self.teams.getTeams()
            for team in allTeams:
                if team.getName() == teamName:
                    teamPlayers = team.getPlayers()
                    self.tree2.insert('', 'end', values=(playerName, playerCred, playerAge, playerNo))
                    teamPlayers.append(Player(playerName, float(playerCred), int(playerAge), int(playerNo)))
                    self.errorScreen("Player Added!", 1)
                    break
    
    def deletePlayer(self):
        '''Delete Player from Teams Array and treeview'''

        #get selected Team
        allTeams = self.teams.getTeams()
        curItem = self.tree.focus()
        teamName = self.tree.item(curItem)['values'][0]

        #get selected Player
        curPlayer = self.tree2.focus()
        playerName = self.tree2.item(curPlayer)['values'][0]

        for team in allTeams:
            if team.getName() == teamName:
                teamPlayers = team.getPlayers()
                for player in teamPlayers:
                    if player.getName() == playerName:
                        teamPlayers.remove(player)
                        self.tree2.delete(curPlayer)
                        self.errorScreen("Player Deleted!", 1)
                        break


    def errorScreen(self, msg, idx=0):
        '''Display Error Message'''

        root = Toplevel(self.root)
        root.focus()
        root.title("Error")
        root.geometry("300x250+550+200")    
        root.resizable(False, False)
        root.configure(background='#0f0f0f')
        root.iconbitmap('images/error.ico')

        if idx == 1:
            root.title("Success")
            root.iconbitmap('images/success.ico')

        Label(root, text='Message', font=('Arial', 18, 'bold'), bg='#0f0f0f', fg='white').pack(side=TOP, pady=20)
        Label(root, text=msg, font=('Arial', 13), bg='#0f0f0f', fg='white').pack(side=TOP, pady=10)

        # OK Button
        addButton = Button(root, text='Ok', command=root.destroy)
        addButton.pack(side=LEFT, padx=10, pady=10, expand=True)
        addButton.configure(self.ButtonStyle(15, 2))


    def run(self) -> None:
        '''Run the application'''
        self.root.mainloop()


if __name__ == '__main__':
    app = Application()
