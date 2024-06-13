class GameResult:
    def __init__(self, solved, strikes, balls):
        self.__solved = solved
        self.__strikes = strikes
        self.__balls = balls

    def get_solved(self):
        return self.__solved

    def get_strikes(self):
        return self.__strikes

    def get_ball(self):
        return self.__balls