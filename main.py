import typonista
import dictation

from util import linebreak, evaluate_input


if __name__ == '__main__':
    print("Welcome to typonista")
    print(linebreak)
    print("Instructions: This is a program \n"
          "to strengthen your keyboard knowledge.\n"
          "The algorithm will display a letter \n"
          "or series of letters you need to hit.\n"
          "\n"
          "Once you are finished the program will\n"
          "display your accuracy.\n"
          "GL&HF")
    print(linebreak)
    print("Confirm with enter")
    input()

    typonist = typonista.Typonista().fromfile("config.json")
    dictat = dictation.Dictation(typonist.letters)

    while True:
        nextline = dictat.generate_line()
        print(linebreak)
        print(nextline)
        user_in = input()
        user_in = evaluate_input(user_input=user_in)



