import requests, dictionlib


def apilen(url):
    try:
        check = requests.get(url=url)
        check.raise_for_status()

        counter = 0

        while True:

            check.json()["data"][counter]

            counter += 1

    except:

        return counter


def display_to_id(user_input_for_search):

    counter = apilen(f"https://api.mgo1.savemgo.com/api/v1/user/search/{user_input_for_search}")

    potential_names = ""

    for i in range(counter):

        name_search = requests.get(url=f"https://api.mgo1.savemgo.com/api/v1/user/search/{user_input_for_search}")

        if name_search.json()["data"][i]["display_name"] == user_input_for_search:

            return name_search.json()["data"][i]["id"]

        name_search = name_search.json()["data"][i]["display_name"]

        if len(name_search) > 0:

            potential_names += f"{name_search}\n"

    return potential_names


def kd_calc():
    kd_ratio = (dictionlib.true_all_time["Kills"] + dictionlib.true_all_time["Stuns"]) / (
            dictionlib.true_all_time["Deaths"] +
            dictionlib.true_all_time[
                "Stuns Received"])

    kd_ratio = round(kd_ratio, 2)

    return kd_ratio


def hs_percent():

    headshot = dictionlib.true_all_time["Headshots"] / dictionlib.true_all_time["Kills"]

    return headshot


def stat_disp(display_name):

    stats = f"""
Username: {display_name}

Kills: {dictionlib.true_all_time["Kills"]}

Deaths: {dictionlib.true_all_time["Deaths"]}

Stuns: {dictionlib.true_all_time["Stuns"]}

Stuns Received: {dictionlib.true_all_time["Stuns Received"]}

K/D Ratio: {kd_calc()}

Head Shots: {dictionlib.true_all_time["Headshots"]}

Head Shots Received: {dictionlib.true_all_time["Headshots received"]}

Head Shots Percentage: {round(hs_percent() * 100, 2)}%

Team Kills: {dictionlib.true_all_time["Team Kills"]}

Team Stuns: {dictionlib.true_all_time["Team Stuns"]}

Rolls: {dictionlib.true_all_time["Rolls"]}

Sneaking Rounds: {dictionlib.true_all_time["Sneaking Plays"]}

Sneaking Wins: {dictionlib.true_all_time["Sneaking Wins"]}

Sneaking Rounds Without Dying: {dictionlib.true_all_time["Survived Sneaking"]}

Rescue Rounds: {dictionlib.true_all_time["Rescue Plays"]}

Rescue Wins: {dictionlib.true_all_time["Rescue Wins"]}

Rescue Rounds Without Dying: {dictionlib.true_all_time["Survived Rescue"]}

Team Deathmatch Rounds: {dictionlib.true_all_time["TDM Plays"]}

Team Deathmatch Wins: {dictionlib.true_all_time["TDM Wins"]}

Capture Rounds: {dictionlib.true_all_time["Capture Plays"]}

Capture Wins: {dictionlib.true_all_time["Capture Wins"]}

Deathmatch Rounds: {dictionlib.true_all_time["Deathmatch Plays"]}"""

    return stats
