linebreak = "----------------------------------------"
l = ["a", "s", "d", "f", "j", "k", "l", "ö"]
exit_words = {"exit", "quit", "exit()", "quit()"}


def evaluate_input(user_input: str) -> str:
    if user_input in exit_words:
        exit(0)
    else:
        return user_input