## Gold-Ninja-Game

📖 Project Overview
Ninja Gold is a simple web-based mini game where players take on the role of a ninja trying to collect gold. The player starts with 0 gold and can visit different locations such as the farm, cave, house, or quest to earn—or sometimes lose—gold.
Each action updates the total gold count and logs the activity, creating a running history of the player’s journey.


## ✨ Features
•	🎮 Interactive gameplay with multiple locations 
•	💰 Earn or lose gold depending on the location 
•	📊 Real-time gold counter 
•	📝 Activity log tracking all actions 
•	🎲 Randomized outcomes for dynamic gameplay 
•	🔄 Reset option to start over 


## 📸 Screenshots
Main Game Interface
Activity Log


## 🛠️ Tech Stack
•	Frontend: HTML, CSS
•	Backend: Django (Python) 
•	Database: SQLite (default) 


## ⚙️ Installation & Setup
1. Clone repo
git clone https://github.com/Majd-Kawa/Gold-Ninja-Game.git
cd ninja_gold
2. Create virtual environment
python -m venv env

# Windows
call env\Scripts\activate

# Mac/Linux
source env/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Start server
python manage.py runserver
5. Visit in browser
http://127.0.0.1:8000


## 🚀 How to Play
1.	Start the game by setting your ‘Goal Gold’ and ‘Number of Moves’
2.	Click ‘Let’s Start’ to begin
3.	Choose a location: 
  o	🌾 Farm → earn 10–20 gold
  o	🕳️ Cave → earn 10–20 gold
  o	🏠 House → earn 10–20 gold
  o	❓ Quest → earn or lose 0-50 gold (high risk, high reward) 
4.	Each action reduces your available moves
5.	Try to reach your goal before you run out of moves
6.	Check the ‘Activities log’ to see your progress
7.	The game ends when:
  - You reach the goal → 🎉 You win
  - Moves run out → 💀 Game over
8.	Click ‘Reset Game’ to play again


## 📌 Future Improvements
•	Add animations and sound effects 
•	Add leaderboard functionality 
•	Store data in a persistent database 

