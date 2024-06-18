# --------------------------------------------------------------------------
# Football Simulation Game
# Author: Arunim Guchait
# Version: 0.0
# Date: 2024-JUN-18
# --------------------------------------------------------------------------

import random
import time

# --------------------------------------------------------------------------
# Manchester City Squad
# --------------------------------------------------------------------------
man_city_squad = ["Ederson", "Walker", "Dias", "Laporte", "Cancelo", "De Bruyne", "Rodri", "Gundogan", "Mahrez",
                  "Sterling", "Foden"]

# --------------------------------------------------------------------------
# Real Madrid Squad
# --------------------------------------------------------------------------
real_madrid_squad = ["Courtois", "Carvajal", "Militao", "Alaba", "Mendy", "Modric", "Casemiro", "Kroos", "Benzema",
                     "Vinicius Jr", "Asensio"]


# --------------------------------------------------------------------------
# Function to print the available teams
# --------------------------------------------------------------------------
def show_teams():
    print("Available teams:")
    print("1. Manchester City F.C.")
    print("2. Real Madrid CF")


# --------------------------------------------------------------------------
# Function to get the team based on the user choice
# --------------------------------------------------------------------------
def get_team(choice):
    if choice == 1:
        return "Manchester City F.C.", man_city_squad
    elif choice == 2:
        return "Real Madrid CF", real_madrid_squad


# --------------------------------------------------------------------------
# Function to simulate a goal event
# --------------------------------------------------------------------------
def simulate_goal(minute, team_name, squad):
    goal_scorer = random.choice(squad[1:])  # Excluding the goalkeeper
    print(f"{minute}': {team_name} scores! {goal_scorer} with the goal!")
    time.sleep(2)
    return goal_scorer


# --------------------------------------------------------------------------
# Function to simulate a random event
# --------------------------------------------------------------------------
def simulate_event(minute, home_team, home_squad, away_team, away_squad):
    events = [
        "a dangerous tackle by",
        "a beautiful pass by",
        "a missed opportunity by",
        "a corner kick taken by",
        "a free kick taken by"
    ]
    goalkeepers = {"Manchester City F.C.": home_squad[0], "Real Madrid CF": away_squad[0]}
    event_team = random.choice([home_team, away_team])
    if random.random() > 0.8:  # 20% chance for a great save event
        print(f"{minute}': {event_team}: great save by {goalkeepers[event_team]}")
    else:
        event = random.choice(events)
        player = random.choice(home_squad if event_team == home_team else away_squad)
        print(f"{minute}': {event_team}: {event} {player}")
    time.sleep(1)


# --------------------------------------------------------------------------
# Function to simulate the football match
# --------------------------------------------------------------------------
def simulate_match(home_team, home_squad, away_team, away_squad):
    home_score = 0
    away_score = 0
    home_goal_scorers = []
    away_goal_scorers = []
    random_time = random.randint(6, 10)  # Random event increment time between 6 and 10 minutes

    for minute in range(1, 90, random_time):  # Simulating events between 6 and 10 minutes
        if random.random() > 0.7:  # 30% chance of a goal event
            if random.random() > 0.5:  # 50% chance for either team to score
                goal_scorer = simulate_goal(minute, home_team, home_squad)
                home_score += 1
                home_goal_scorers.append(goal_scorer)
                print("--------------------------------------------")
                print(f"{minute}': SCORE:", home_team, home_score, "-", away_score, away_team)
                print("--------------------------------------------")
            else:
                goal_scorer = simulate_goal(minute, away_team, away_squad)
                away_score += 1
                away_goal_scorers.append(goal_scorer)
                print("--------------------------------------------")
                print(f"{minute}': SCORE:", home_team, home_score, "-", away_score, away_team)
                print("--------------------------------------------")
        else:
            simulate_event(minute, home_team, home_squad, away_team, away_squad)

    print("\n90': Full-time!")
    print("--------------------------------------------")
    print("FINAL SCORE:")
    print(f"{home_team} {home_score} - {away_score} {away_team}")
    print(f"{home_team} goal scorers: {', '.join(home_goal_scorers)}")
    print(f"{away_team} goal scorers: {', '.join(away_goal_scorers)}")
    print("--------------------------------------------")

# --------------------------------------------------------------------------
# Main program
# --------------------------------------------------------------------------
def main():
    print("Welcome to the Football Simulation Game!")
    show_teams()
    home_choice = int(input("Choose the home team (1 or 2): "))
    away_choice = int(input("Choose the away team (1 or 2): "))

    if home_choice == away_choice:
        print("Home and away teams cannot be the same.")
        return

    home_team, home_squad = get_team(home_choice)
    away_team, away_squad = get_team(away_choice)

    print(f"\nStarting match: {home_team} vs {away_team}\n")
    simulate_match(home_team, home_squad, away_team, away_squad)

    # --------------------------------------------------------------------------
    # Play the game again
    # --------------------------------------------------------------------------
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        main()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
