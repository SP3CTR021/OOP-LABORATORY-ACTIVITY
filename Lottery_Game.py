import random

class LotteryGame:
    def __init__(self):
        self.winning_numbers = random.sample(range(1, 61), 6)
        self.player_numbers = []

    def get_player_numbers(self):
        for i in range(6):
            num = int(input(f"Enter number {i+1} (1-60): "))
            if 1 <= num <= 60:
                self.player_numbers.append(num)
            else:
                print("Invalid number, try again!")
                return False  # stop if invalid input
        return True

    def check_results(self):
        matches = set(self.player_numbers) & set(self.winning_numbers)
        match_count = len(matches)

        if match_count == 6:
            prize = 1_000_000
        else:
            prize = match_count * 1000

        print("\nWinning Numbers:", self.winning_numbers)
        print("Your Numbers:", self.player_numbers)
        print("Matched Numbers:", matches)
        print("Total Prize: ₱{:,.0f}".format(prize))

    def play(self):
        if self.get_player_numbers():
            self.check_results()


# Example usage
game = LotteryGame()
game.play()
