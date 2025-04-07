from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample player data
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
            "dribbles_completed": 95
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
            "dribbles_completed": 65
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
            "dribbles_completed": 70
        }
    }
}

@app.route('/')
def index():
    """Home page with player list"""
    return render_template('basic_index.html', players=SAMPLE_PLAYERS)

@app.route('/api/players')
def get_players():
    """API endpoint to get all players"""
    return jsonify(SAMPLE_PLAYERS)

if __name__ == '__main__':
    app.run(debug=True) 