import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast


def load_processed_data():
    ms = pd.read_csv("data/processed/ms_clean.csv")
    md = pd.read_csv("data/processed/md_clean.csv")
    return ms, md


############################################################
# 1. Who is the most dominant singles player?
############################################################

def dominant_singles_player(ms):

    match_counts = (
        ms.groupby("team_one_players").size() +
        ms.groupby("team_two_players").size()
    )

    eligible_players = match_counts[match_counts >= 100].index

    ps1 = ms[ms["team_one_players"].isin(eligible_players)]
    ps2 = ms[ms["team_two_players"].isin(eligible_players)]

    total_match_as_team1 = ps1.groupby("team_one_players").size()
    total_match_as_team2 = ps2.groupby("team_two_players").size()

    match_won_as_team1 = ps1[ps1["winner"] == 1]["team_one_players"].value_counts()
    match_won_as_team2 = ps2[ps2["winner"] == 2]["team_two_players"].value_counts()

    total_matches = total_match_as_team1 + total_match_as_team2
    matches_won = match_won_as_team1 + match_won_as_team2

    win_rate = (matches_won / total_matches) * 100

    return win_rate.sort_values(ascending=False).head(5)


############################################################
# 2. Which country dominates doubles tournaments?
############################################################

def dominant_doubles_country(md):

    country_pairs = md.groupby(
        ["team_one_player_one_nationality", "team_two_player_one_nationality"]
    ).size()

    return country_pairs.sort_values(ascending=False).head(10)


############################################################
# 3. Does tournament level affect match intensity?
############################################################

def tournament_intensity(md):

    avg_sets = md.groupby("tournament_type")["nb_sets"].mean()

    return avg_sets.sort_values(ascending=False)


############################################################
# 4. Do retired matches skew results?
############################################################

def retirement_analysis(md):

    retired = md[md["retired"] == True]

    retirement_rate = (
        retired.groupby("tournament_type").size() /
        md.groupby("tournament_type").size()
    ) * 100

    return retirement_rate.sort_values(ascending=False)


############################################################
# 5. Who scores the most consecutive points?
############################################################

def most_consecutive_points(md):

    team1 = md.groupby(
        ["team_one_player_one", "team_one_player_two"]
    )["team_one_most_consecutive_points"].max()

    team2 = md.groupby(
        ["team_two_player_one", "team_two_player_two"]
    )["team_two_most_consecutive_points"].max()

    combined = pd.concat([team1, team2])

    return combined.sort_values(ascending=False).head(10)


############################################################
# 6. How often does the team with fewer points win?
############################################################

def losing_team_more_points(md):

    win_pair_2 = md[
        (md["team_one_total_points"] > md["team_two_total_points"]) &
        (md["winner"] == 2)
    ]

    win_pair_1 = md[
        (md["team_one_total_points"] < md["team_two_total_points"]) &
        (md["winner"] == 1)
    ]

    total_cases = win_pair_1.shape[0] + win_pair_2.shape[0]

    percent = (total_cases / md.shape[0]) * 100

    return percent


############################################################
# 7. How common are straight-set wins?
############################################################

def straight_set_wins(md):

    straight_sets = md[md["nb_sets"] == 2].shape[0]
    three_sets = md[md["nb_sets"] == 3].shape[0]

    return {
        "Straight Sets": straight_sets,
        "Three Sets": three_sets
    }


############################################################
# 8. Are certain months more intense?
############################################################

def matches_by_month(md):

    md["month"] = pd.to_datetime(md["date"], format="%d-%m-%Y").dt.month

    return md.groupby("month").size()


############################################################
# 9. Which players improve in later rounds?
############################################################

def performance_by_round(md):

    avg_points = md.groupby(
        ["team_one_player_one", "team_one_player_two", "round"]
    )["team_one_total_points"].mean()

    return avg_points.sort_values(ascending=False).head(10)


############################################################
# 10. Visualize match momentum
############################################################

def visualize_match_momentum(md):

    final_match = md[
        (md["round"] == "Final") &
        (md["nb_sets"] == 3)
    ].iloc[0]

    score_list = ast.literal_eval(final_match["game_3_scores"])

    x_coords = []
    y_coords = []

    for score in score_list:
        x, y = score.split("-")
        x_coords.append(int(x))
        y_coords.append(int(y))

    plt.figure(figsize=(10,6))

    plt.plot(x_coords, y_coords, marker="o")

    plt.xlabel("Team 1 Score")
    plt.ylabel("Team 2 Score")
    plt.title("Match Momentum")

    plt.grid()

    plt.show()


############################################################
# Run the analysis
############################################################

def run_analysis():

    ms, md = load_processed_data()

    print("\n1. Dominant Singles Players")
    print(dominant_singles_player(ms))

    print("\n2. Dominant Doubles Countries")
    print(dominant_doubles_country(md))

    print("\n3. Tournament Intensity")
    print(tournament_intensity(md))

    print("\n4. Retirement Analysis")
    print(retirement_analysis(md))

    print("\n5. Most Consecutive Points")
    print(most_consecutive_points(md))

    print("\n6. Losing Team Scoring More Points (%)")
    print(losing_team_more_points(md))

    print("\n7. Straight Set Wins")
    print(straight_set_wins(md))

    print("\n8. Matches by Month")
    print(matches_by_month(md))

    print("\n9. Performance by Round")
    print(performance_by_round(md))

    visualize_match_momentum(md)


if __name__ == "__main__":
    run_analysis()