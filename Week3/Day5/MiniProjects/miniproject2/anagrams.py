from anagram_checker import AnagramChecker


class AnagramApp:

    def __init__(self):
        self.run = True

    def show_menu(self):
        print("Welcome to Anagram Checker!")
        user_input = input("Enter your word (enter 'quit_now' to quit):\n").strip().lower()
        return user_input

    def validator(self, text):
        if not text.isalpha():
            print("Please enter only letters! Only one word is allowed!")
            return False
        return True

    def main(self):
        while self.run:
            user_input = self.show_menu()
            if user_input == "quit_now":
                self.run = False
                print("Goodbye!")
                break

            if self.validator(user_input):
                checker = AnagramChecker()
                anagrams = checker.get_anagrams(user_input)
                if len(anagrams) == 0:
                    print("Please enter a valid word!")
                    continue

                anagrams.remove(user_input)

                print(f"YOUR WORD: {user_input.upper()}")
                print("This is a valid English word.")
                print(f"Anagrams for your word: {anagrams}")


if __name__ == "__main__":
    app = AnagramApp()
    app.main()
