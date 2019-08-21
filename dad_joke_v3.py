import requests
import ascii_art
from random import choice


def dad_joke():
    ascii_art.print_art("DAD JOKE INITIALIZED", choice(ascii_art.valid_colors))
    print("Write \"quit\" to exit.")
    while True:
        search = input("What kind of joke do you want? ")
        if search == "quit":
            break
        else:
            print(search_joke(search))


def search_joke(st):
    url = "https://icanhazdadjoke.com/search"
    try:
        response = requests.get(
            url, headers={"Accept": "application/json"},
            params={"term": st, "limit": 30})
        data = response.json()
        joke_count = len(data["results"])
        joke_list = [data["results"][var]["joke"]
                     for var in range(0, joke_count)]
        the_joke = choice(joke_list)

        return f"{joke_count} jokes found. Here is one:\n{the_joke}"

    except IndexError:
        print(
            "I haven't found any joke with that term.\nHere is a random joke:")
        response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"})
        data = response.json()
        return data["joke"]


dad_joke()
