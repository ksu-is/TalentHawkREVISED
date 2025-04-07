# TalentHawk Documentation

Welcome to the TalentHawk documentation. TalentHawk is a web-based platform for soccer talent scouting and analytics.

## Overview

TalentHawk helps professional soccer scouts, coaches, and analysts identify and evaluate talent efficiently through data analytics and player comparisons.

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/talenthawk.git
cd talenthawk

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Running the Application

```bash
python run.py
```

Then open your browser and navigate to `http://localhost:5000`.

## Features

- **Player Profiles**: Detailed statistical profiles of players with key performance metrics
- **Performance Visualization**: Visual representation of player statistics through radar charts
- **Player Comparison**: Side-by-side comparison of multiple players on selected statistics
- **Similar Player Analysis**: Find players with similar statistical profiles
- **Advanced Analytics**: Utilize Principal Component Analysis (PCA) to identify player clusters and patterns
- **Position-Based Filtering**: Filter and analyze players by position

## Screenshots

(Coming soon)

## User Guide

### Home Page

The home page displays a list of all players in the database. You can click on any player to view their detailed profile.

### Player Detail Page

The player detail page shows:
- Basic player information (name, team, position, age)
- A radar chart visualizing the player's performance metrics
- A list of similar players based on statistical profile

### Player Comparison Page

The comparison page allows you to:
- Select multiple players (up to 4) for comparison
- Filter players by position
- Choose which statistics to compare
- View a radar chart comparison of the selected players
- See a detailed table of the selected statistics

### Analytics Page

The analytics page provides:
- Principal Component Analysis (PCA) visualization of all players
- Options to customize which statistics to include in the analysis
- Insights about player clustering and statistical patterns

## API Reference

TalentHawk provides the following API endpoints:

- `/api/players` - Returns all player data
- `/api/comparison_chart` - Generates comparison charts for selected players
- `/api/pca` - Performs PCA analysis on selected statistics

## Contributing

See the [Contributing Guide](../CONTRIBUTING.md) for more information on how to contribute to TalentHawk. 