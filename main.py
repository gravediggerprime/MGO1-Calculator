import requests, dictionlib, funclib

id_obtained = False

while not id_obtained:

    user_name = input("Enter Display Name > ")

    print("Please Wait...")

    user_id = funclib.display_to_id(user_name)

    if isinstance(user_id, int):

        id_obtained = True

        print("User Found")
        print("Importing User's Stats...")

    elif len(user_id) != 0:

        print("Exact match not found, did you mean any of the follow]ing?\n", user_id)

    else:

        print("No matches found, please try again")

url = "https://api.mgo1.savemgo.com/api/v1/user/{user}/stats".replace("{user}", str(user_id))

response = requests.get(url=url)
response.raise_for_status()

response = response.json()["data"]

for i in range(funclib.apilen(url)):

    if response[i]["period"] == 1 or response[i]["period"] == 2:
        continue

    dictionlib.true_all_time["Kills"] += response[i]["kills"]

    dictionlib.true_all_time["Deaths"] += response[i]["deaths"]

    dictionlib.true_all_time["Stuns Received"] += response[i]["stuns_received"]

    dictionlib.true_all_time["Stuns"] += response[i]["stuns"]

    dictionlib.true_all_time["Headshots"] += response[i]["head_shots"]

    dictionlib.true_all_time["Headshots received"] += response[i]["head_shots_received"]

    dictionlib.true_all_time["Team Kills"] += response[i]["team_kills"]

    dictionlib.true_all_time["Team Stuns"] += response[i]["team_stuns"]

    dictionlib.true_all_time["Rolls"] += response[i]["rolls"]

    if response[i]["mode_string"] == "deathmatch":

        dictionlib.true_all_time["Deathmatch Plays"] += response[i]["rounds_played"]

    elif response[i]["mode_string"] == "team deathmatch":

        dictionlib.true_all_time["TDM Plays"] += response[i]["rounds_played"]

        dictionlib.true_all_time["TDM Wins"] += response[i]["team_wins"]

    elif response[i]["mode_string"] == "capture":

        dictionlib.true_all_time["Capture Plays"] += response[i]["rounds_played"]

        dictionlib.true_all_time["Capture Wins"] += response[i]["team_wins"]

    elif response[i]["mode_string"] == "sneaking":

        dictionlib.true_all_time["Sneaking Plays"] += response[i]["rounds_played"]

        dictionlib.true_all_time["Sneaking Wins"] += response[i]["team_wins"]

        dictionlib.true_all_time["Survived Sneaking"] += response[i]["rounds_no_death"]

    elif response[i]["mode_string"] == "rescue":

        dictionlib.true_all_time["Rescue Plays"] += response[i]["rounds_played"]

        dictionlib.true_all_time["Rescue Wins"] += response[i]["team_wins"]

        dictionlib.true_all_time["Survived Rescue"] += response[i]["rounds_no_death"]

print(funclib.stat_disp(user_name))
