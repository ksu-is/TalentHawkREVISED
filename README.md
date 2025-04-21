# TalentHawk - Simple Soccer Player Analytics

A beginner-friendly web application for comparing soccer player statistics. Built with Python, Flask, and HTML/CSS.

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
├── talenthawk/           # Main application folder
│   ├── app.py            # Flask application with all functionality
│   ├── templates/        # HTML templates
│   │   ├── index.html    # Home page with player list
│   │   ├── player_detail.html  # Player profile page
│   │   ├── comparison.html     # Player comparison page
│   │   └── analytics.html      # Analytics dashboard page
│   │
│   ├── static/           # For static files (currently empty)
│   └── data/             # For data files (currently contains sample data)
│
├── presentations/        # Project presentations
│   └── Talent Hawk PP (2).pptx  # Final project presentation
│
├── run.py                # Script to run the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## How It Works

1. **Python (app.py)**
   - Handles all the data processing
   - Creates the charts and statistics
   - Connects to the web pages

2. **HTML Templates**
   - `index.html`: Shows a grid of player cards
   - `player_detail.html`: Shows one player's stats and charts
   - `comparison.html`: Shows two players side by side
   - `analytics.html`: Shows charts and statistics

3. **Data Flow**
   - Python reads player data
   - Processes it with Pandas
   - Creates charts with Matplotlib
   - Sends everything to HTML templates
   - Shows the result in your browser

## Technologies Used

- **Python**: The main programming language
- **Flask**: Makes the web application
- **HTML**: Creates the web pages
- **CSS**: Makes the pages look nice
- **Pandas**: Handles the player data
- **Matplotlib**: Creates the charts

## Sample Players

The app comes with sample data for these players:
- Lionel Messi
- Cristiano Ronaldo
- Erling Haaland
- Kylian Mbappé
- Kevin De Bruyne
- Mohamed Salah

## Testing

To run the tests:
```
pytest tests/test_app.py
```

## License

This project is licensed under the MIT License.
