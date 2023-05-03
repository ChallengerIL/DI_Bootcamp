# 1. Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# 2. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# 3. Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# 4. Call the function make_great().
# 5. Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(names_list: list):
    return [print(name) for name in names_list]


def make_great():
    global magician_names
    # return [name + "the Great" for name in names_list]

    for name in magician_names:
        idx = magician_names.index(name)
        name += " the Great"
        magician_names[idx] = name


if __name__ == '__main__':
    show_magicians(magician_names)
    print("\n")
    make_great()
    show_magicians(magician_names)
