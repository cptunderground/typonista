import typonista
import dictation
from util import l

if __name__ == '__main__':
    print("testing")

    typonist_fromfile = typonista.Typonista.fromfile("config.json")
    typonist_fromconst = typonista.Typonista()
    print(typonist_fromfile)
    print(typonist_fromconst)
    _dictation = dictation.Dictation(typonist_fromfile.letters, typonist_fromfile.special_chars)
    _dictation.generate_dictation()