
import csv 

def league_builder():
    #reads in the starting csv document
    with open('soccer_players.csv', newline='') as csvfile:
        soccer_reader = csv.reader(csvfile)
        rows = list(soccer_reader)
    del(rows[0])
        
    #The LISTS! 
    the_best_players = []
    the_okiest_players = [] #They still are the best players to me
    Sharks = []
    Dragons = []
    Raptors = []

    #Seperates the YES from the NO players, puts them into seperate lists
    for players in rows:
        if players[2]=='YES':
            the_best_players.append(players)
        else:
            the_okiest_players.append(players)

    #builds team lists for writing purposes
    shark_list = the_best_players[:3] + the_okiest_players[:3]
    dragon_list = the_best_players[3:6] + the_okiest_players[3:6]
    raptor_list = the_best_players[6:] + the_okiest_players[6:]
    
    #Admittedly, I had to do some research for this.
    #It joins EACH individual item of a list, by access specific items. Its a for loop in one sentence
    Sharks = "Sharks" + "\n" + "\n".join([', '.join(x) for x in shark_list])
    Dragons = "Dragons" + "\n" + "\n".join([', '.join(x) for x in dragon_list])
    Raptors = "Raptors" + "\n" + "\n".join([', '.join(x) for x in raptor_list])

    #Function to write teams to 'teams.txt' file
    def team_writer(team):

        for players in team:
            with open("teams.txt", "a") as file:
                file.write(players)
        with open("teams.txt", "a") as file:
            file.write("\n" * 2)

    #Writes out individual team letters
    #Captures player names, parent names and list_names
    #While I don't think it's...eloquent, it works!
    def team_letters(team):
        count = 0
        player_letters = []
        player_parents = []
        seperator = "_"
        name = ''
        title = ''
        team_name = ''

        if team == shark_list:
            team_name = "Sharks"
        if team == dragon_list:
            team_name = "Dragons"
        if team == raptor_list:
            team_name = "Raptors"

        
        while count <= len(team) - 1:
            for players in team:                 
                player_letters = (team[count][0])
                player_parents = (team[count][3])
                count += 1
                player = player_letters.split()
                name = seperator.join(player)
                title = name + ".txt"
                           
                with open(title, "a") as file:
                        file.write("Dear, " + player_parents + ", " + player_letters + " will start playing for the " + team_name + " with the starting date of 10/10/3021")
                        


    
    #function calls
    team_writer(Sharks)
    team_writer(Dragons)
    team_writer(Raptors)

    team_letters(shark_list)
    team_letters(dragon_list)
    team_letters(raptor_list)





    







if __name__ == '__main__':
    league_builder()