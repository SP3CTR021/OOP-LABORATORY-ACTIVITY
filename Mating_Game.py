class FlamesGame:
    def __init__(self, name1, name2):
        self.original_name1 = name1.strip()
        self.original_name2 = name2.strip()
        self.name1 = name1.replace(" ", "").lower()
        self.name2 = name2.replace(" ", "").lower()
        self.result = None

    def remove_common_letters(self):
        name1, name2 = self.name1, self.name2
        for ch in name1[:]:
            if ch in name2:
                name1 = name1.replace(ch, "", 1)
                name2 = name2.replace(ch, "", 1)
        return len(name1) + len(name2)

    def calculate(self):
        total_count = self.remove_common_letters()

        if total_count == 0:
            self.result = "Not compatible! Single forever </3"
            return

        flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
        index = 0

        while len(flames) > 1:
            index = (index + total_count - 1) % len(flames)
            flames.pop(index)

        self.result = flames[0]

    def get_result(self):
        if self.result is None:
            self.calculate()
        return f"{self.original_name1} ❤️ {self.original_name2} → {self.result}"



game1 = FlamesGame("Maria Lopez", "Juan Cruz")
print(game1.get_result())

game2 = FlamesGame("Robert", "Jessica")
print(game2.get_result())

game3 = FlamesGame("Anna", "Anna")
print(game3.get_result())

game4 = FlamesGame("Christopher", "Angelica")
print(game4.get_result())

game5 = FlamesGame("Michael", "Sarah")
print(game5.get_result())
