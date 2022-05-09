class Pilot:
    def __init__(self, name, positions):
        """
        constructor of the Pilot class
        """
        self.name = name
        self.positions = positions

    def getNbStart(self):
        """
        allows to obtain the number of starts taken by the pilot
        """
        return sum([len(i) for i in self.positions])

    def getNbPolePosition(self):
        """
        allows to obtain the number of pole position realized by the pilot
        """
        return len(self.positions[0])

    def getNbWin(self):
        """
        allows you to obtain the number of Grand Prix won by the pilot
        """
        return sum([i.count(0) for i in self.positions])

    def getNbPodium(self):
        """
        allows to obtain the number of podium realized by the pilot
        """
        return sum([i.count(0) + i.count(1) + i.count(2) for i in self.positions])

    def winRate(self):
        """
        allows to obtain the win rate
        """
        return self.getNbWin()/self.getNbStart()
        
    def podiumRate(self):
        """
        allows to obtain the podium rate
        """
        return self.getNbPodium()/self.getNbStart()