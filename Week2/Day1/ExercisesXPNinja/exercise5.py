score = 0
run = True


while run:
    sentence = input("Enter the longest sentence without the character 'a': ").lower()

    if sentence == "quit":
        run = False
        break

    if not "a" in sentence:
        if len(sentence) > score:
            score = len(sentence)
            print(f"Congratulations! The new sentence just set a new record!\nThe new record is {len(sentence)}")
    else:
        print("Your input contains 'a'. Try again...")
