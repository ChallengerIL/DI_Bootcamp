from game import Game


def get_user_menu_choice():
    print("Menu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit\n")

    try:
        user_choice = str(input()).lower()[0]
    except ValueError:
        print("Only letters are allowed")
    else:
        if user_choice == "g":
            return "new_game"
        else:
            return "exit"


def print_results(results):
    print("Game results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("\nThank you for playing!")


def main():
    active = True
    score = {
        "win": 0,
        "loss": 0,
        "draw": 0,
    }

    while active:
        if get_user_menu_choice() == "exit":
            active = False
            print_results(score)
            break

        new_game = Game()
        score[new_game.play()] += 1


if __name__ == "__main__":
    main()
