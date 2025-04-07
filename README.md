# TalentHawk - Soccer Talent Scouting & Analytics Platform

TalentHawk is a web-based soccer talent scouting and analytics platform built on Python and Flask. It helps professional soccer scouts, coaches, and analysts identify and evaluate talent efficiently through data analytics and player comparisons.

## Features

- **Player Profiles**: Detailed statistical profiles of players with key performance metrics
- **Performance Visualization**: Visual representation of player statistics through radar charts
- **Player Comparison**: Side-by-side comparison of multiple players on selected statistics
- **Similar Player Analysis**: Find players with similar statistical profiles
- **Advanced Analytics**: Utilize Principal Component Analysis (PCA) to identify player clusters and patterns
- **Position-Based Filtering**: Filter and analyze players by position

## Technologies Used

- **Backend**: Python, Flask
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly, Bootstrap
- **Frontend**: HTML/CSS, JavaScript

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
   python talenthawk/app.py
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
│   ├── app.py            # Flask application
│   ├── templates/        # HTML templates
│   │   ├── base.html     # Base template with common layout
│   │   ├── index.html    # Home page with player list
│   │   ├── player_detail.html  # Player profile page
│   │   ├── comparison.html     # Player comparison page
│   │   └── analytics.html      # Advanced analytics page
│   │
│   ├── static/           # Static files (CSS, JS, images)
│   └── data/             # Data files
│
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Future Enhancements

1. **Video Analysis**: Integration with SportslabKit's tracking capabilities to analyze player movement from match footage
2. **Database Integration**: Move from sample data to a real database backend
3. **Predictive Modeling**: Implement machine learning models to predict player performance
4. **User Authentication**: Add login system for scouts and analysts
5. **Custom Reports**: Generate PDF reports for scouted players
6. **Mobile App**: Develop a companion mobile application for on-the-go scouting

## Acknowledgements

This project is based on the [SportsLabKit](https://github.com/AtomScott/sportslabkit) repository, an open-source toolkit for sports analytics.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
