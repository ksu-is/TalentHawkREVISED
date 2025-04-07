# TalentHawk - Soccer Talent Scouting & Analytics Platform

TalentHawk is a simple web-based soccer talent scouting and analytics platform built on Python, Flask, and Pandas. It helps soccer coaches, scouts, and analysts identify and evaluate talent efficiently through data visualization and player comparisons. This project is designed as a beginner-friendly college-level application.

## Features

- **Player Profiles**: Detailed statistical profiles of players with key performance metrics
- **Performance Visualization**: Visual representation of player statistics through radar charts
- **Player Comparison**: Side-by-side comparison of players on selected statistics
- **Similar Player Analysis**: Find players with similar statistical profiles
- **Basic Analytics**: Analyze player data with visual charts and statistics
- **Position-Based Analysis**: View statistics grouped by player positions

## Technologies Used

- **Backend**: Python, Flask
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Visualization**: Matplotlib
- **Frontend**: Bootstrap (CSS only)

## Installation & Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/talenthawk.git
   cd talenthawk
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python run.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
talenthawk/
│
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
├── run.py                # Script to run the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Key Implementation Details

- **Pure Server-Side Rendering**: All views are rendered on the server using Flask templates
- **No JavaScript Dependencies**: The application functions without client-side JavaScript
- **Matplotlib Integration**: Charts are generated on the server and served as images
- **Sample Data**: Uses built-in sample data for demonstration purposes
- **Simple Interface**: Clean, responsive UI using Bootstrap CSS

## Future Enhancements

1. **Database Integration**: Move from sample data to a real database backend
2. **Additional Metrics**: Add more advanced player performance metrics
3. **User Authentication**: Add login system for scouts and analysts
4. **Custom Reports**: Generate PDF reports for scouted players
5. **Data Import/Export**: Allow users to upload/download player data

## License

This project is licensed under the MIT License - see the LICENSE file for details.
