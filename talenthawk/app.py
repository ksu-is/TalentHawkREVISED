import os
import json
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify
import plotly
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

app = Flask(__name__)

# Sample player data - in a real application, this would come from a database
# Each player has various statistical attributes
SAMPLE_PLAYERS = {
    "player1": {
        "name": "Lionel Messi",
        "team": "Inter Miami",
        "position": "Forward",
        "age": 35,
        "stats": {
            "goals": 25,
            "assists": 15,
            "pass_accuracy": 88,
            "shots_on_target": 65,
            "dribbles_completed": 95,
            "tackles": 45,
            "interceptions": 30,
            "distance_covered": 320,
            "sprint_speed": 32,
            "stamina": 85
        }
    },
    "player2": {
        "name": "Cristiano Ronaldo",
        "team": "Al-Nassr",
        "position": "Forward",
        "age": 38,
        "stats": {
            "goals": 22,
            "assists": 8,
            "pass_accuracy": 80,
            "shots_on_target": 70,
            "dribbles_completed": 65,
            "tackles": 40,
            "interceptions": 35,
            "distance_covered": 345,
            "sprint_speed": 35,
            "stamina": 90
        }
    },
    "player3": {
        "name": "Kevin De Bruyne",
        "team": "Manchester City",
        "position": "Midfielder",
        "age": 31,
        "stats": {
            "goals": 12,
            "assists": 20,
            "pass_accuracy": 92,
            "shots_on_target": 55,
            "dribbles_completed": 70,
            "tackles": 60,
            "interceptions": 65,
            "distance_covered": 380,
            "sprint_speed": 30,
            "stamina": 88
        }
    },
    "player4": {
        "name": "Virgil van Dijk",
        "team": "Liverpool",
        "position": "Defender",
        "age": 31,
        "stats": {
            "goals": 5,
            "assists": 3,
            "pass_accuracy": 86,
            "shots_on_target": 30,
            "dribbles_completed": 40,
            "tackles": 85,
            "interceptions": 92,
            "distance_covered": 360,
            "sprint_speed": 33,
            "stamina": 86
        }
    },
    "player5": {
        "name": "Kylian Mbappé",
        "team": "PSG",
        "position": "Forward",
        "age": 24,
        "stats": {
            "goals": 28,
            "assists": 12,
            "pass_accuracy": 82,
            "shots_on_target": 72,
            "dribbles_completed": 88,
            "tackles": 35,
            "interceptions": 25,
            "distance_covered": 340,
            "sprint_speed": 38,
            "stamina": 89
        }
    },
    "player6": {
        "name": "Erling Haaland",
        "team": "Manchester City",
        "position": "Forward",
        "age": 22,
        "stats": {
            "goals": 32,
            "assists": 7,
            "pass_accuracy": 78,
            "shots_on_target": 80,
            "dribbles_completed": 60,
            "tackles": 30,
            "interceptions": 20,
            "distance_covered": 330,
            "sprint_speed": 36,
            "stamina": 87
        }
    },
    "player7": {
        "name": "Joshua Kimmich",
        "team": "Bayern Munich",
        "position": "Midfielder",
        "age": 28,
        "stats": {
            "goals": 6,
            "assists": 14,
            "pass_accuracy": 90,
            "shots_on_target": 40,
            "dribbles_completed": 55,
            "tackles": 75,
            "interceptions": 78,
            "distance_covered": 390,
            "sprint_speed": 31,
            "stamina": 92
        }
    },
    "player8": {
        "name": "Jude Bellingham",
        "team": "Real Madrid",
        "position": "Midfielder",
        "age": 19,
        "stats": {
            "goals": 15,
            "assists": 10,
            "pass_accuracy": 84,
            "shots_on_target": 50,
            "dribbles_completed": 75,
            "tackles": 65,
            "interceptions": 60,
            "distance_covered": 370,
            "sprint_speed": 34,
            "stamina": 91
        }
    }
}

# Create a dataframe for analysis
def create_player_df():
    data = []
    for player_id, player_info in SAMPLE_PLAYERS.items():
        player_data = {
            'id': player_id,
            'name': player_info['name'],
            'team': player_info['team'],
            'position': player_info['position'],
            'age': player_info['age']
        }
        # Add all stats to the player data
        for stat, value in player_info['stats'].items():
            player_data[stat] = value
        data.append(player_data)
    return pd.DataFrame(data)

# Helper function to run PCA on player stats
def perform_pca(df, features, n_components=2):
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    
    # Create a DataFrame with principal components
    pca_df = pd.DataFrame(
        data=principal_components,
        columns=[f'PC{i+1}' for i in range(n_components)]
    )
    
    # Add player information
    pca_df['id'] = df['id']
    pca_df['name'] = df['name']
    pca_df['team'] = df['team']
    pca_df['position'] = df['position']
    
    # Calculate explained variance
    explained_variance = pca.explained_variance_ratio_
    
    return pca_df, explained_variance, pca

# Helper function to find similar players
def find_similar_players(df, player_id, features, n_similar=3):
    # Extract features for analysis
    X = df[features].values
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Get the index of the selected player
    player_idx = df[df['id'] == player_id].index[0]
    
    # Calculate Euclidean distances to all other players
    distances = np.sqrt(np.sum((X_scaled - X_scaled[player_idx])**2, axis=1))
    
    # Get indices of the most similar players (excluding the player itself)
    similar_indices = np.argsort(distances)[1:n_similar+1]
    
    # Return the similar players
    return df.iloc[similar_indices]

# Routes
@app.route('/')
def index():
    """Home page with player list"""
    return render_template('index.html', players=SAMPLE_PLAYERS)

@app.route('/player/<player_id>')
def player_detail(player_id):
    """Player detail page"""
    if player_id not in SAMPLE_PLAYERS:
        return redirect(url_for('index'))
    
    player = SAMPLE_PLAYERS[player_id]
    
    # Create radar chart for the player's stats
    stats = player['stats']
    categories = list(stats.keys())
    values = list(stats.values())
    
    # Radar chart
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=player['name']
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False
    )
    
    radar_chart = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Find similar players
    player_df = create_player_df()
    stat_columns = list(SAMPLE_PLAYERS['player1']['stats'].keys())
    similar_players = find_similar_players(player_df, player_id, stat_columns)
    
    return render_template(
        'player_detail.html', 
        player=player, 
        player_id=player_id, 
        radar_chart=radar_chart,
        similar_players=similar_players.to_dict('records')
    )

@app.route('/comparison')
def player_comparison():
    """Page for comparing multiple players"""
    player_df = create_player_df()
    positions = player_df['position'].unique().tolist()
    return render_template('comparison.html', players=SAMPLE_PLAYERS, positions=positions)

@app.route('/api/comparison_chart', methods=['POST'])
def comparison_chart():
    """API endpoint to generate comparison charts"""
    player_ids = request.json.get('player_ids', [])
    stats = request.json.get('stats', [])
    
    if not player_ids or not stats:
        return jsonify({'error': 'Missing required parameters'})
    
    # Create dataframe of selected players
    selected_players = []
    for player_id in player_ids:
        if player_id in SAMPLE_PLAYERS:
            player = SAMPLE_PLAYERS[player_id]
            player_stats = {
                'id': player_id,
                'name': player['name'],
                'team': player['team']
            }
            for stat in stats:
                player_stats[stat] = player['stats'].get(stat, 0)
            selected_players.append(player_stats)
    
    df = pd.DataFrame(selected_players)
    
    # Create comparison chart
    fig = go.Figure()
    for _, row in df.iterrows():
        values = [row[stat] for stat in stats]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=stats,
            fill='toself',
            name=row['name']
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True
    )
    
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return jsonify({'chart': chart_json})

@app.route('/analytics')
def analytics():
    """Advanced analytics page"""
    player_df = create_player_df()
    stat_columns = list(SAMPLE_PLAYERS['player1']['stats'].keys())
    
    # Perform PCA
    pca_df, explained_variance, _ = perform_pca(player_df, stat_columns)
    
    # Create scatter plot with PCA results
    fig = px.scatter(
        pca_df, x='PC1', y='PC2', 
        color='position',
        hover_data=['name', 'team'],
        labels={
            'PC1': f'Principal Component 1 ({explained_variance[0]:.2%})',
            'PC2': f'Principal Component 2 ({explained_variance[1]:.2%})'
        },
        title='Player Clustering by Statistical Profile'
    )
    
    pca_chart = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template(
        'analytics.html', 
        pca_chart=pca_chart,
        stats=stat_columns
    )

@app.route('/api/pca', methods=['POST'])
def pca_api():
    """API endpoint to generate PCA based on selected features"""
    selected_stats = request.json.get('stats', [])
    
    if not selected_stats:
        return jsonify({'error': 'No stats selected'})
    
    player_df = create_player_df()
    
    # Perform PCA with selected stats
    pca_df, explained_variance, _ = perform_pca(player_df, selected_stats)
    
    # Create scatter plot with PCA results
    fig = px.scatter(
        pca_df, x='PC1', y='PC2', 
        color='position',
        hover_data=['name', 'team'],
        labels={
            'PC1': f'Principal Component 1 ({explained_variance[0]:.2%})',
            'PC2': f'Principal Component 2 ({explained_variance[1]:.2%})'
        },
        title='Player Clustering by Selected Statistics'
    )
    
    pca_chart = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return jsonify({'chart': pca_chart})

if __name__ == '__main__':
    app.run(debug=True) 