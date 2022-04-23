import random


class Dictation():
    def __init__(self, letters, special_chars):
        self.letters = letters
        self.special_chars = special_chars
    def generate_line(self)->str:
        line=""
        for i in range(15):
            line = f"{line}{random.choice(tuple(self.letters))}"
        line = f"{line}{random.choice(tuple(self.special_chars))}"
        return line

    def generate_dictation(self)->None:
        with open("dictation.txt","w",encoding="UTF-8") as f:
            for i in range(15):
                f.write(f"{self.generate_line()}\n")