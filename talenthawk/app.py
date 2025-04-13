import os
import io
import base64
from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from matplotlib.figure import Figure
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cosine

app = Flask(__name__)

# My sample data for soccer players
# I chose these players because they're well-known and have good stats to compare
players = {
    "messi": {
        "name": "Lionel Messi",
        "position": "Forward",
        "team": "Inter Miami",
        "age": 36,
        "stats": {
            "goals": 25,
            "assists": 18,
            "passing": 88,
            "shots": 62,
            "dribbles": 78
        }
    },
    "ronaldo": {
        "name": "Cristiano Ronaldo",
        "position": "Forward",
        "team": "Al Nassr",
        "age": 38,
        "stats": {
            "goals": 30,
            "assists": 5,
            "passing": 76,
            "shots": 75,
            "dribbles": 55
        }
    },
    "debruyne": {
        "name": "Kevin De Bruyne",
        "position": "Midfielder",
        "team": "Manchester City",
        "age": 32,
        "stats": {
            "goals": 10,
            "assists": 22,
            "passing": 92,
            "shots": 45,
            "dribbles": 70
        }
    }
}

def create_dataframe():
    """Convert my player dictionary into a pandas DataFrame
    This makes it easier to work with the data"""
    data = []
    for player_id, player in players.items():
        player_data = {
            'id': player_id,
            'name': player['name'],
            'position': player['position'],
            'team': player['team']
        }
        player_data.update(player['stats'])
        data.append(player_data)
    return pd.DataFrame(data)

def make_radar_chart(player_id):
    """Create a radar chart showing player stats
    I used matplotlib because it's simple and works well with Flask"""
    player = players[player_id]
    stats = player['stats']
    
    # These are the main stats I want to compare
    categories = ['goals', 'assists', 'passing', 'shots', 'dribbles']
    values = [stats[stat] for stat in categories]
    
    # Create the plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    
    # Plot the data
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values, [values[0]]))  # Close the polygon
    angles = np.concatenate((angles, [angles[0]]))  # Close the polygon
    
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    
    # Set the labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([cat.title() for cat in categories])
    
    plt.title(f"{player['name']} Stats")
    
    # Save to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plt.close()
    
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def home():
    """Show the main page with all players"""
    return render_template('index.html', players=players)

@app.route('/player/<player_id>')
def player_detail(player_id):
    """Show detailed stats for one player"""
    if player_id not in players:
        return "Player not found", 404
        
    player = players[player_id]
    chart = make_radar_chart(player_id)
    return render_template('player_detail.html', player=player, chart=chart)

@app.route('/compare')
def compare_players():
    """Let users compare two players"""
    player1_id = request.args.get('player1', 'messi')
    player2_id = request.args.get('player2', 'ronaldo')
    
    if player1_id not in players or player2_id not in players:
        return "Player not found", 404
        
    player1 = players[player1_id]
    player2 = players[player2_id]
    
    return render_template('comparison.html', 
                         player1=player1, 
                         player2=player2,
                         players=players)

if __name__ == '__main__':
    app.run(debug=True) 