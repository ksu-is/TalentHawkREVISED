# TalentHawk - Simple Soccer Player Analytics

A beginner-friendly web application for comparing soccer player statistics. Built with Python, Flask, and basic HTML/CSS.

## What This App Does

- View a list of soccer players and their basic stats
- Compare two players side by side
- See detailed player statistics with visual charts
- Find players with similar performance

## How to Run the App

1. Install Python (version 3.8 or newer)
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python run.py
   ```
4. Open your web browser and go to: `http://localhost:5000`

## Project Structure

```
talenthawk/
├── app.py              # Main application file
├── templates/          # HTML files
│   ├── index.html     # Home page
│   ├── player_detail.html    # Player stats page
│   ├── comparison.html      # Compare players page
│   └── analytics.html       # Statistics page
├── static/            # For CSS and images (empty for now)
└── data/             # For player data (empty for now)
```

## Technologies Used

- Python: Main programming language
- Flask: Web framework
- Pandas: Data handling
- Matplotlib: Creating charts
- HTML/CSS: Web pages

## Sample Players

The app comes with sample data for these players:
- Lionel Messi
- Cristiano Ronaldo
- Erling Haaland
- Kylian Mbappé
- Kevin De Bruyne
- Mohamed Salah

## License

This project is licensed under the MIT License.
