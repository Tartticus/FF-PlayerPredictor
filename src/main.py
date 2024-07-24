import requests

def get_league_users(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/users"
    response = requests.get(url)
    return response.json()

def get_rosters(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = requests.get(url)
    return response.json()

def get_players(player_ids):
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)
    all_players = response.json()
    return [all_players[player_id] for player_id in player_ids if player_id in all_players]

def main():
    league_id = "your_league_id_here"  # Replace with your actual league ID
    users = get_league_users(league_id)
    rosters = get_rosters(league_id)

    for roster in rosters:
        user_id = roster['owner_id']
        user = next((user for user in users if user['user_id'] == user_id), {})
        player_ids = roster.get('players', [])
        players = get_players(player_ids)

        print(f"User: {user.get('display_name', 'Unknown')}")
        for player in players:
            print(f"  - {player['full_name']} ({player['team']})")

if __name__ == "__main__":
    main()
