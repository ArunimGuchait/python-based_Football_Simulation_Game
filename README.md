# Python-based Football Simulation Game

- Version: 0.0
- Date: 2024-JUN-18

## Overview
Welcome to the Football Simulation Game! This is a simple Python-based simulation game that allows you to simulate a football match between two of the world's top football clubs: Manchester City F.C. and Real Madrid CF. The game provides random events and commentary to give you a feel of a real-time football match.

## Features
- **Team Selection**: Choose between Manchester City F.C. and Real Madrid CF as the home or away team.
- **Real-time Simulation**: The game simulates various football events such as goals, tackles, passes, missed opportunities, and more.
- **Random Events**: Every 6 to 10 minutes of simulated match time, a random event occurs.
- **Commentary**: Each event is accompanied by commentary to enhance the match experience.
- **Score Updates**: The score is updated in real-time with detailed information on goal scorers.
- **Play Again Option**: After the match ends, you have the option to play again.



## How to Play
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/ArunimGuchait/python-based_Football_Simulation_Game.git
    cd football-simulation-game_0_0.py
    ```

2. **Run the Game**:
    Make sure you have Python installed. Run the game using the following command:
    ```sh
    python football-simulation-game_0_0.py
    ```

3. **Follow the Prompts**:
    - Choose the home and away teams by entering the corresponding numbers.
    - Watch the match unfold with random events and commentary.
    - At the end of the match, you can choose to play again.



## Code Structure
- `man_city_squad` and `real_madrid_squad`: Lists containing the squad players for Manchester City and Real Madrid.
- `show_teams()`: Function to display the available teams.
- `get_team(choice)`: Function to get the team name and squad based on the user choice.
- `simulate_goal(minute, team_name, squad)`: Function to simulate a goal event.
- `simulate_event(minute, home_team, home_squad, away_team, away_squad)`: Function to simulate a random football event.
- `simulate_match(home_team, home_squad, away_team, away_squad)`: Function to simulate the entire match.
- `main()`: Main function to start the game, handle user inputs, and control the game flow.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## Project Information
This project is my final project for Code in Place 2024. This project is for my learning purposes.

## Acknowledgements
Special thanks to the teachers and TAs of Code in Place 2024 for their support and guidance.

## Credits
Icons by Flaticon and images by Freepik. 

## License
This project is licensed under the Apache-2.0 license. See the `LICENSE` file for more details.

## Code Visualisation in Python Tutor
[Code Visualisation in Python Tutor](https://pythontutor.com/render.html#code=import%20random%0A%0Aman_city_squad%20%3D%20%5B%22Ederson%22,%20%22Walker%22,%20%22Dias%22,%20%22Laporte%22,%20%22Cancelo%22,%20%22De%20Bruyne%22,%20%22Rodri%22,%20%22Gundogan%22,%20%22Mahrez%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Sterling%22,%20%22Foden%22%5D%0A%0Areal_madrid_squad%20%3D%20%5B%22Courtois%22,%20%22Carvajal%22,%20%22Militao%22,%20%22Alaba%22,%20%22Mendy%22,%20%22Modric%22,%20%22Casemiro%22,%20%22Kroos%22,%20%22Benzema%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Vinicius%20Jr%22,%20%22Asensio%22%5D%0A%0Adef%20show_teams%28%29%3A%0A%20%20%20%20print%28%22Available%20teams%3A%22%29%0A%20%20%20%20print%28%221.%20Manchester%20City%20F.C.%22%29%0A%20%20%20%20print%28%222.%20Real%20Madrid%20CF%22%29%0A%0Adef%20get_team%28choice%29%3A%0A%20%20%20%20if%20choice%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20%22Manchester%20City%20F.C.%22,%20man_city_squad%0A%20%20%20%20elif%20choice%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20return%20%22Real%20Madrid%20CF%22,%20real_madrid_squad%0A%0Adef%20simulate_goal%28minute,%20team_name,%20squad%29%3A%0A%20%20%20%20goal_scorer%20%3D%20random.choice%28squad%5B1%3A%5D%29%20%20%23%20Excluding%20the%20goalkeeper%0A%20%20%20%20print%28f%22%7Bminute%7D'%3A%20%7Bteam_name%7D%20scores!%20%7Bgoal_scorer%7D%20with%20the%20goal!%22%29%0A%20%20%20%20return%20goal_scorer%0A%0Adef%20simulate_event%28minute,%20home_team,%20home_squad,%20away_team,%20away_squad%29%3A%0A%20%20%20%20events%20%3D%20%5B%0A%20%20%20%20%20%20%20%20%22a%20dangerous%20tackle%20by%22,%0A%20%20%20%20%20%20%20%20%22a%20beautiful%20pass%20by%22,%0A%20%20%20%20%5D%0A%20%20%20%20goalkeepers%20%3D%20%7B%22Manchester%20City%20F.C.%22%3A%20home_squad%5B0%5D,%20%22Real%20Madrid%20CF%22%3A%20away_squad%5B0%5D%7D%0A%20%20%20%20event_team%20%3D%20random.choice%28%5Bhome_team,%20away_team%5D%29%0A%20%20%20%20if%20random.random%28%29%20%3E%200.8%3A%20%20%23%2020%25%20chance%20for%20a%20great%20save%20event%0A%20%20%20%20%20%20%20%20print%28f%22%7Bminute%7D'%3A%20%7Bevent_team%7D%3A%20great%20save%20by%20%7Bgoalkeepers%5Bevent_team%5D%7D%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20event%20%3D%20random.choice%28events%29%0A%20%20%20%20%20%20%20%20player%20%3D%20random.choice%28home_squad%20if%20event_team%20%3D%3D%20home_team%20else%20away_squad%29%0A%20%20%20%20%20%20%20%20print%28f%22%7Bminute%7D'%3A%20%7Bevent_team%7D%3A%20%7Bevent%7D%20%7Bplayer%7D%22%29%0A%20%20%20%20%0A%0Adef%20simulate_match%28home_team,%20home_squad,%20away_team,%20away_squad%29%3A%0A%20%20%20%20home_score%20%3D%200%0A%20%20%20%20away_score%20%3D%200%0A%20%20%20%20home_goal_scorers%20%3D%20%5B%5D%0A%20%20%20%20away_goal_scorers%20%3D%20%5B%5D%0A%20%20%20%20%0A%20%20%20%20for%20minute%20in%20range%281,%2090,%2010%29%3A%20%20%0A%20%20%20%20%20%20%20%20if%20random.random%28%29%20%3E%200.7%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20random.random%28%29%20%3E%200.5%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20goal_scorer%20%3D%20simulate_goal%28minute,%20home_team,%20home_squad%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20home_score%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20home_goal_scorers.append%28goal_scorer%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22%7Bminute%7D'%3A%20SCORE%3A%22,%20home_team,%20home_score,%20%22-%22,%20away_score,%20away_team%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20goal_scorer%20%3D%20simulate_goal%28minute,%20away_team,%20away_squad%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20away_score%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20away_goal_scorers.append%28goal_scorer%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22%7Bminute%7D'%3A%20SCORE%3A%22,%20home_team,%20home_score,%20%22-%22,%20away_score,%20away_team%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20simulate_event%28minute,%20home_team,%20home_squad,%20away_team,%20away_squad%29%0A%0A%20%20%20%20print%28%22FINAL%20SCORE%3A%22%29%0A%20%20%20%20print%28f%22%7Bhome_team%7D%20%7Bhome_score%7D%20-%20%7Baway_score%7D%20%7Baway_team%7D%22%29%0A%0Adef%20main%28%29%3A%0A%20%20%20%20print%28%22Welcome%20to%20the%20Football%20Simulation%20Game!%22%29%0A%20%20%20%20show_teams%28%29%0A%20%20%20%20home_choice%20%3D%20int%28input%28%22Choose%20the%20home%20team%20%281%20or%202%29%3A%20%22%29%29%0A%20%20%20%20away_choice%20%3D%20int%28input%28%22Choose%20the%20away%20team%20%281%20or%202%29%3A%20%22%29%29%0A%0A%20%20%20%20if%20home_choice%20%3D%3D%20away_choice%3A%0A%20%20%20%20%20%20%20%20print%28%22Home%20and%20away%20teams%20cannot%20be%20the%20same.%22%29%0A%20%20%20%20%20%20%20%20return%0A%0A%20%20%20%20home_team,%20home_squad%20%3D%20get_team%28home_choice%29%0A%20%20%20%20away_team,%20away_squad%20%3D%20get_team%28away_choice%29%0A%0A%20%20%20%20print%28f%22%5CnStarting%20match%3A%20%7Bhome_team%7D%20vs%20%7Baway_team%7D%5Cn%22%29%0A%20%20%20%20simulate_match%28home_team,%20home_squad,%20away_team,%20away_squad%29%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)