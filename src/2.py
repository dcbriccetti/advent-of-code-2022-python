from enum import Enum
from shared import get_string_groups

class Play(Enum):
    ROCK     = 'A'
    PAPER    = 'B'
    SCISSORS = 'C'

    @staticmethod
    def from_player_code(code: str) -> "Play":
        diff = ord('X') - ord('A')
        shifted_code = chr(ord(code) - diff)
        return Play(shifted_code)

class Outcome(Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN  = 'Z'

beats = {
    Play.ROCK:      Play.SCISSORS,
    Play.PAPER:     Play.ROCK,
    Play.SCISSORS:  Play.PAPER,
}

loses_to = {
    Play.ROCK:      Play.PAPER,
    Play.PAPER:     Play.SCISSORS,
    Play.SCISSORS:  Play.ROCK,
}

play_points_by_play = {
    Play.ROCK:      1,
    Play.PAPER:     2,
    Play.SCISSORS:  3,
}

win_points = 6
draw_points = 3

rounds: list[tuple[str, str]] = [(opponent_code, player_code)
        for opponent_code, player_code in get_string_groups('../data/2.txt')]

def part1():
    score = 0
    for opponent_code, player_code in rounds:
        opponent_play = Play(opponent_code)
        player_play = Play.from_player_code(player_code)
        score += compute_points(opponent_play, player_play)
    print(score)

def part2():
    score = 0
    for opponent_code, outcome_code in rounds:
        opponent_play = Play(opponent_code)
        match Outcome(outcome_code):
            case Outcome.DRAW:
                player_play = opponent_play
            case Outcome.WIN:
                player_play = loses_to[opponent_play]
            case Outcome.LOSE:
                player_play = beats[opponent_play]
        score += compute_points(opponent_play, player_play)
    print(score)

def compute_points(opponent_play: Play, player_play: Play) -> int:
    play_points: int = play_points_by_play[player_play]
    return play_points + \
        draw_points if opponent_play == player_play else \
        play_points + win_points if beats[player_play] == opponent_play else play_points

part1()
part2()
