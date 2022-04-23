import json
from util import l


class Typonista():
    def __init__(self, letters: list = l, special_chars: list = [], word_length: int = 3, words_per_line: int = 5):
        self.letters = letters
        self.special_chars = special_chars
        self.word_length = word_length
        self.words_per_line = words_per_line

    @classmethod
    def fromfile(cls, path_to_file):
        with open(path_to_file, encoding="UTF-8") as file:
            json_dict = json.load(file)
            letters = json_dict["letters"]
            word_length = json_dict["word_length"]
            words_per_line = json_dict["words_per_line"]
            special_chars = json_dict["special_chars"]
            return cls(letters=letters, special_chars=special_chars, word_length=word_length,
                       words_per_line=words_per_line)

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def saveJSON(self, name: str = "config") -> None:
        with open(f'{name}.json', 'w') as outfile:
            json.dump(self.__dict__, outfile, indent=2, ensure_ascii=False)
