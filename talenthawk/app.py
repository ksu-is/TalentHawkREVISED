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

# Sample player data
players = {
    "player1": {
        "name": "Lionel Messi",
        "position": "Forward",
        "team": "Inter Miami",
        "age": 36,
        "nationality": "Argentina",
        "market_value": "$35 million",
        "contract": "2025",
        "stats": {
            "goals": 25,
            "assists": 18,
            "minutes_played": 2100,
            "passing_accuracy": 88,
            "shots_on_target": 62,
            "duels_won": 55,
            "successful_dribbles": 78,
            "tackles": 24,
            "interceptions": 12,
            "distance_covered": 210,
            "sprint_speed": 28,
            "aerial_duels_won": 22
        }
    },
    "player2": {
        "name": "Cristiano Ronaldo",
        "position": "Forward",
        "team": "Al Nassr",
        "age": 38,
        "nationality": "Portugal",
        "market_value": "$20 million",
        "contract": "2024",
        "stats": {
            "goals": 30,
            "assists": 5,
            "minutes_played": 2250,
            "passing_accuracy": 76,
            "shots_on_target": 75,
            "duels_won": 60,
            "successful_dribbles": 55,
            "tackles": 18,
            "interceptions": 8,
            "distance_covered": 225,
            "sprint_speed": 31,
            "aerial_duels_won": 65
        }
    },
    "player3": {
        "name": "Kevin De Bruyne",
        "position": "Midfielder",
        "team": "Manchester City",
        "age": 32,
        "nationality": "Belgium",
        "market_value": "$70 million",
        "contract": "2025",
        "stats": {
            "goals": 10,
            "assists": 22,
            "minutes_played": 1950,
            "passing_accuracy": 92,
            "shots_on_target": 45,
            "duels_won": 65,
            "successful_dribbles": 70,
            "tackles": 35,
            "interceptions": 28,
            "distance_covered": 260,
            "sprint_speed": 29,
            "aerial_duels_won": 30
        }
    },
    "player4": {
        "name": "Virgil van Dijk",
        "position": "Defender",
        "team": "Liverpool",
        "age": 32,
        "nationality": "Netherlands",
        "market_value": "$45 million",
        "contract": "2025",
        "stats": {
            "goals": 3,
            "assists": 2,
            "minutes_played": 2340,
            "passing_accuracy": 89,
            "shots_on_target": 10,
            "duels_won": 85,
            "successful_dribbles": 25,
            "tackles": 65,
            "interceptions": 70,
            "distance_covered": 220,
            "sprint_speed": 27,
            "aerial_duels_won": 90
        }
    },
    "player5": {
        "name": "Kylian Mbappé",
        "position": "Forward",
        "team": "Paris Saint-Germain",
        "age": 24,
        "nationality": "France",
        "market_value": "$180 million",
        "contract": "2024",
        "stats": {
            "goals": 35,
            "assists": 12,
            "minutes_played": 2200,
            "passing_accuracy": 80,
            "shots_on_target": 70,
            "duels_won": 62,
            "successful_dribbles": 85,
            "tackles": 15,
            "interceptions": 10,
            "distance_covered": 235,
            "sprint_speed": 36,
            "aerial_duels_won": 25
        }
    },
    "player6": {
        "name": "N'Golo Kanté",
        "position": "Midfielder",
        "team": "Al-Ittihad",
        "age": 32,
        "nationality": "France",
        "market_value": "$30 million",
        "contract": "2026",
        "stats": {
            "goals": 2,
            "assists": 8,
            "minutes_played": 2400,
            "passing_accuracy": 85,
            "shots_on_target": 15,
            "duels_won": 90,
            "successful_dribbles": 65,
            "tackles": 95,
            "interceptions": 90,
            "distance_covered": 290,
            "sprint_speed": 32,
            "aerial_duels_won": 40
        }
    }
}

# Helper functions
def create_player_df():
    """Create a pandas DataFrame from player data"""
    data = []
    for player_id, player in players.items():
        player_data = {'id': player_id, 'name': player['name'], 
                       'position': player['position'], 'team': player['team']}
        player_data.update(player['stats'])
        data.append(player_data)
    return pd.DataFrame(data)

def find_similar_players(player_id, n=3):
    """Find the most similar players to a given player"""
    df = create_player_df()
    stats_cols = list(players['player1']['stats'].keys())
    
    # Create a feature vector for the target player
    target_vector = df[df['id'] == player_id][stats_cols].values[0]
    
    # Calculate similarity for all other players
    similarities = {}
    for pid, p_data in df[df['id'] != player_id].iterrows():
        player_vector = p_data[stats_cols].values
        # Using cosine similarity (1 - cosine distance)
        similarity = 1 - cosine(target_vector, player_vector)
        similarities[p_data['id']] = similarity
    
    # Sort by similarity and get top n
    similar_players = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:n]
    return similar_players

def generate_radar_chart(player_id):
    """Generate a radar chart for a player"""
    player = players[player_id]
    stats = player['stats']
    
    # Select stats to display
    display_stats = ['goals', 'assists', 'passing_accuracy', 'shots_on_target', 
                     'duels_won', 'successful_dribbles', 'tackles']
    
    # Get values
    values = [stats[stat] for stat in display_stats]
    
    # Create radar chart
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, polar=True)
    
    # Number of variables
    N = len(display_stats)
    
    # What will be the angle of each axis in the plot
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Add the first value again to close the circle
    values += values[:1]
    
    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], [stat.replace('_', ' ').title() for stat in display_stats])
    
    # Draw the chart
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.1)
    
    # Add title
    plt.title(f"{player['name']} - Performance Profile", size=15, y=1.1)
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def generate_comparison_chart(player1_id, player2_id):
    """Generate a comparison chart for two players"""
    player1 = players[player1_id]
    player2 = players[player2_id]
    
    # Select stats to display
    display_stats = ['goals', 'assists', 'passing_accuracy', 'shots_on_target', 
                     'duels_won', 'successful_dribbles', 'tackles']
    
    # Get values
    values1 = [player1['stats'][stat] for stat in display_stats]
    values2 = [player2['stats'][stat] for stat in display_stats]
    
    # Number of variables
    N = len(display_stats)
    
    # What will be the angle of each axis in the plot
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Add the first value again to close the circle
    values1 += values1[:1]
    values2 += values2[:1]
    
    # Create figure
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, polar=True)
    
    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], [stat.replace('_', ' ').title() for stat in display_stats])
    
    # Draw the two players
    ax.plot(angles, values1, linewidth=2, linestyle='solid', label=player1['name'])
    ax.fill(angles, values1, alpha=0.1)
    
    ax.plot(angles, values2, linewidth=2, linestyle='solid', label=player2['name'])
    ax.fill(angles, values2, alpha=0.1)
    
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    # Add title
    plt.title(f"Player Comparison: {player1['name']} vs {player2['name']}", size=15, y=1.1)
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def perform_pca():
    """Perform PCA on player stats"""
    df = create_player_df()
    stats_cols = list(players['player1']['stats'].keys())
    
    # Standardize the data
    X = df[stats_cols].values
    X_std = StandardScaler().fit_transform(X)
    
    # Perform PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_std)
    
    # Create PCA chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Define colors for positions
    position_colors = {
        'Forward': 'red',
        'Midfielder': 'blue',
        'Defender': 'green'
    }
    
    # Plot each player
    for i, (_, row) in enumerate(df.iterrows()):
        position = row['position']
        color = position_colors.get(position, 'gray')
        ax.scatter(X_pca[i, 0], X_pca[i, 1], c=color, s=100, alpha=0.7)
        ax.annotate(row['name'], (X_pca[i, 0] + 0.05, X_pca[i, 1] + 0.05))
    
    # Add legend
    for position, color in position_colors.items():
        ax.scatter([], [], c=color, label=position)
    
    ax.legend()
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of Player Statistics')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def generate_correlation_chart():
    """Generate a correlation heatmap of player stats"""
    df = create_player_df()
    stats_cols = list(players['player1']['stats'].keys())
    
    # Calculate correlation matrix
    corr_matrix = df[stats_cols].corr()
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    im = ax.imshow(corr_matrix, cmap='coolwarm')
    
    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    
    # Set ticks
    ax.set_xticks(np.arange(len(stats_cols)))
    ax.set_yticks(np.arange(len(stats_cols)))
    
    # Label ticks
    ax.set_xticklabels([stat.replace('_', ' ').title() for stat in stats_cols], rotation=45, ha='right')
    ax.set_yticklabels([stat.replace('_', ' ').title() for stat in stats_cols])
    
    # Loop over data to create text annotations
    for i in range(len(stats_cols)):
        for j in range(len(stats_cols)):
            text = ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                          ha="center", va="center", color="black" if abs(corr_matrix.iloc[i, j]) < 0.7 else "white")
    
    ax.set_title("Correlation of Player Statistics")
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def generate_distribution_chart(stat):
    """Generate a distribution chart for a specific stat by position"""
    df = create_player_df()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get unique positions
    positions = df['position'].unique()
    
    # Plot distribution for each position
    for position in positions:
        position_data = df[df['position'] == position]
        ax.hist(position_data[stat], alpha=0.5, label=position, bins=5)
    
    ax.set_xlabel(stat.replace('_', ' ').title())
    ax.set_ylabel('Number of Players')
    ax.set_title(f'Distribution of {stat.replace("_", " ").title()} by Position')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def generate_position_chart(position):
    """Generate a chart showing average stats for a specific position"""
    df = create_player_df()
    stats_cols = list(players['player1']['stats'].keys())
    
    # Filter by position
    position_df = df[df['position'] == position]
    
    # Calculate averages
    avg_stats = position_df[stats_cols].mean()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create bar chart
    ax.bar(range(len(avg_stats)), avg_stats.values, color='skyblue')
    ax.set_xticks(range(len(avg_stats)))
    ax.set_xticklabels([stat.replace('_', ' ').title() for stat in avg_stats.index], rotation=45, ha='right')
    
    ax.set_ylabel('Average Value')
    ax.set_title(f'Average Statistics for {position}s')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Save to in-memory file
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img

def prepare_comparison_stats(player1_id, player2_id):
    """Prepare comparison statistics for two players"""
    player1 = players[player1_id]
    player2 = players[player2_id]
    
    comparison = {}
    for stat, value in player1['stats'].items():
        p1_value = value
        p2_value = player2['stats'][stat]
        
        # Determine which player is better (higher value is assumed to be better for all stats)
        p1_better = p1_value > p2_value
        p2_better = p2_value > p1_value
        
        comparison[stat] = {
            'p1_value': p1_value,
            'p2_value': p2_value,
            'p1_better': p1_better,
            'p2_better': p2_better
        }
    
    return comparison

# Routes
@app.route('/')
def index():
    """Home page - show player list"""
    return render_template('index.html', players=players)

@app.route('/player/<player_id>')
def player_detail(player_id):
    """Player detail page"""
    if player_id not in players:
        return redirect('/')
    
    # Find similar players
    similar_players = find_similar_players(player_id)
    
    return render_template('player_detail.html', 
                           player=players[player_id],
                           player_id=player_id,
                           players=players,
                           similar_players=similar_players)

@app.route('/radar_chart/<player_id>')
def radar_chart(player_id):
    """Generate and serve a radar chart for a player"""
    if player_id not in players:
        return redirect('/')
    
    img = generate_radar_chart(player_id)
    return send_file(img, mimetype='image/png')

@app.route('/comparison')
def comparison():
    """Player comparison page"""
    # Get selected players
    player1_id = request.args.get('player1')
    player2_id = request.args.get('player2')
    
    comparison_stats = None
    if player1_id and player2_id and player1_id in players and player2_id in players:
        comparison_stats = prepare_comparison_stats(player1_id, player2_id)
    
    return render_template('comparison.html', 
                          players=players,
                          selected_player1=player1_id,
                          selected_player2=player2_id,
                          comparison_stats=comparison_stats)

@app.route('/comparison_chart')
def comparison_chart():
    """Generate and serve a comparison chart for two players"""
    player1_id = request.args.get('player1')
    player2_id = request.args.get('player2')
    
    if not player1_id or not player2_id or player1_id not in players or player2_id not in players:
        # Return a placeholder image if players are not selected
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        ax.text(0.5, 0.5, 'Please select two players to compare', 
                ha='center', va='center', fontsize=14)
        ax.axis('off')
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return send_file(img, mimetype='image/png')
    
    img = generate_comparison_chart(player1_id, player2_id)
    return send_file(img, mimetype='image/png')

@app.route('/analytics')
def analytics():
    """Analytics dashboard page"""
    # Get stats and positions
    stats = list(players['player1']['stats'].keys())
    positions = list(set(p['position'] for p in players.values()))
    
    # Get selected stat and position (or default)
    selected_stat = request.args.get('stat', 'goals')
    if selected_stat not in stats:
        selected_stat = 'goals'
        
    selected_position = request.args.get('position', 'Forward')
    if selected_position not in positions:
        selected_position = 'Forward'
    
    return render_template('analytics.html',
                          stats=stats,
                          positions=positions,
                          selected_stat=selected_stat,
                          selected_position=selected_position)

@app.route('/pca_chart')
def pca_chart():
    """Generate and serve a PCA chart"""
    img = perform_pca()
    return send_file(img, mimetype='image/png')

@app.route('/correlation_chart')
def correlation_chart():
    """Generate and serve a correlation heatmap"""
    img = generate_correlation_chart()
    return send_file(img, mimetype='image/png')

@app.route('/distribution_chart')
def distribution_chart():
    """Generate and serve a distribution chart for a specific stat"""
    stat = request.args.get('stat', 'goals')
    stats = list(players['player1']['stats'].keys())
    if stat not in stats:
        stat = 'goals'
    
    img = generate_distribution_chart(stat)
    return send_file(img, mimetype='image/png')

@app.route('/position_chart')
def position_chart():
    """Generate and serve a chart for a specific position"""
    position = request.args.get('position', 'Forward')
    positions = list(set(p['position'] for p in players.values()))
    if position not in positions:
        position = 'Forward'
    
    img = generate_position_chart(position)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True) 