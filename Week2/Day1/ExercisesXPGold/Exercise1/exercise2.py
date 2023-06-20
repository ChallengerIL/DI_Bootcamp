seasons = {
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11],
    "winter": [12, 1, 2],
}

while True:
    month = int(input("Enter a month as an integer: "))
    for season, number in seasons.items():
        if month in number:
            print(season)
            