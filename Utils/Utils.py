class Utils:
    @staticmethod
    def searching_equal_games(list_of_names, first_game, second_game):
        first_game_num = second_game_num = 0
        for i, j in enumerate(list_of_names):
            if first_game == j:
                first_game_num = i
            if second_game == j:
                second_game_num = i
        return first_game_num, second_game_num
