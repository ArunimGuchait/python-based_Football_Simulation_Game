# Python-based Football Simulation Game
---
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

---

## How to Play
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/football-simulation-game.git
    cd football-simulation-game
    ```

2. **Run the Game**:
    Make sure you have Python installed. Run the game using the following command:
    ```sh
    python football_simulation_game.py
    ```

3. **Follow the Prompts**:
    - Choose the home and away teams by entering the corresponding numbers.
    - Watch the match unfold with random events and commentary.
    - At the end of the match, you can choose to play again.

---

## Code Structure
- `man_city_squad` and `real_madrid_squad`: Lists containing the squad players for Manchester City and Real Madrid.
- `show_teams()`: Function to display the available teams.
- `get_team(choice)`: Function to get the team name and squad based on the user choice.
- `simulate_goal(minute, team_name, squad)`: Function to simulate a goal event.
- `simulate_event(minute, home_team, home_squad, away_team, away_squad)`: Function to simulate a random football event.
- `simulate_match(home_team, home_squad, away_team, away_squad)`: Function to simulate the entire match.
- `main()`: Main function to start the game, handle user inputs, and control the game flow.

---

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## Project Information
This project is my final project for Code in Place 2024. This project is for my learning purposes.

## Acknowledgements
Special thanks to the teachers and TAs of Code in Place 2024 for their support and guidance.

## Credits
Icons by Flaticon and images by Freepik. 

## License
This project is licensed under the  Apache-2.0 license. See the `LICENSE` file for more details.