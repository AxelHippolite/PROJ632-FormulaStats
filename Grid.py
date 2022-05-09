import ast
import pandas as pd

class Grid():
    def __init__(self):
        """
        constructor of the Pilot class
        """
        self.grid = []

    def addPilot(self, pilot=None):
        """
        allows to add a pilot on the grid
        """
        count = 1
        while pilot != 'stop':
            pilot = input(str(count) + '. ')
            self.grid.append(pilot)
            count += 1
        self.grid = self.grid[:-1]

    def makePrediction(self):
        """
        return the prediction of the final grid
        """
        pred_grid = [None for i in self.grid]
        for i in range(len(self.grid)):
            df = pd.read_csv('results/' + self.grid[i] + '_positions.csv')
            end_pos = ast.literal_eval(df['End Position'][i])
            if len(end_pos) == 0:   #get the final position
                pos = i
            else:
                pos = max(set(end_pos), key=end_pos.count)

            while pos >= len(pred_grid):
                pos -= 1
            
            if pred_grid[pos] is None: #put the pilot on the final grid
                pred_grid[pos] = self.grid[i]
            else:
                if pred_grid[:pos].count(None) != 0 and pos < i:
                    while pred_grid[pos] is not None:
                        pos -= 1
                else:
                    while pred_grid[pos] is not None:
                        pos += 1
                pred_grid[pos] = self.grid[i]
        return pred_grid
