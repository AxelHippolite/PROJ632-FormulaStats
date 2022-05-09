import ast
import pandas as pd
from Pilot import Pilot
from Grid import Grid 

if __name__ == '__main__':
    var = True
    print("##### Formula'Stats #####")
    while var:
        print("\nWhat do you want to do ?")
        choice = int(input("1 - Predicting Standings.\n2 - To Have Information on a Pilot.\n3 - Quit Program.\nChoice : ")) #menu creation
        while choice != 1 and choice != 2 and choice != 3:
            choice = int(input("1 - Predicting Standings.\n2 - To Have Information on a Pilot.\nChoice : "))
        if choice == 1:
            start_grid = Grid()
            print("\n1 - Predicting Standings.")
            print("You will be asked to fill in for each position of the starting grid,\nthe corresponding person in the form of name-lastname (EX : max-verstappen).")
            print("You will then get the predictions of the algorithm. Write -stop- to finish th grid.\n")
            start_grid.addPilot() #start grid creation
            print("\nGrid Finished.\nPrediction in Progress...\n")
            pred = start_grid.makePrediction() #final grid creation
            for i in range(len(pred)): print(str(i + 1) + '. ' + str(pred[i])) #print of the prediction
        elif choice == 2:
            print("\n2 - Information on a Pilot.")
            pilot_name = input("On which driver do you want information (EX : max-verstappen) ?\nPilot : ")
            pilot = Pilot(pilot_name, [ast.literal_eval(pd.read_csv('results/' + pilot_name + '_positions.csv')['End Position'][i]) for i in range(len(pd.read_csv('results/' + pilot_name + '_positions.csv')['End Position']))]) #creation of a Pilot object
            print('\n----- ' + pilot.name + ' -----') #displaying driver information
            print('Stats Since 2000 :')
            print('Number of Starts :', pilot.getNbStart())
            print('Number of Pole Position:', pilot.getNbPolePosition())
            print('Number of Wins :', pilot.getNbWin())
            print('Number of Podiums :', pilot.getNbPodium())
            print('Win Rate (%) :', round(pilot.winRate(), 4)*100)
            print('Podium Rate (%) :', round(pilot.podiumRate(), 4)*100)
            print('----------------------------')
        else:
            var = False #allows to end the program   
