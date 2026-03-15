import pandas as pd
from src.entity_matching import apply_name_matching


def load_raw_data():
    """
    Load raw badminton datasets.
    """

    ms = pd.read_csv("data/raw/ms.csv")
    md = pd.read_csv("data/raw/md.csv")

    return ms, md


def normalize_names(df, column):
    """
    Standardize player names by converting to lowercase
    and removing spaces.
    """

    df[column] = df[column].str.lower().str.replace(" ", "", regex=False)

    return df


def clean_singles_dataset(ms):
    """
    Clean singles dataset and resolve inconsistent player names.
    """

    # Normalize player names
    ms = normalize_names(ms, "team_one_players")
    ms = normalize_names(ms, "team_two_players")

    # Apply fuzzy entity matching
    ms = apply_name_matching(ms, "team_one_players", "team_two_players")
    ms = apply_name_matching(ms, "team_two_players", "team_one_players")

    return ms


def clean_doubles_dataset(md):
    """
    Clean doubles dataset and resolve inconsistent player names.
    """

    # Normalize player names
    md = normalize_names(md, "team_one_player_one")
    md = normalize_names(md, "team_two_player_one")

    # Apply fuzzy matching to resolve duplicates
    md = apply_name_matching(md, "team_one_player_one", "team_two_player_one")
    md = apply_name_matching(md, "team_two_player_one", "team_one_player_one")

    return md


def save_processed_data(ms_clean, md_clean):
    """
    Save cleaned datasets to processed layer.
    """

    ms_clean.to_csv("data/processed/ms_clean.csv", index=False)
    md_clean.to_csv("data/processed/md_clean.csv", index=False)

    print("Processed datasets saved to data/processed/")


def run_data_cleaning_pipeline():
    """
    Full data cleaning pipeline.
    """

    print("Loading raw datasets...")

    ms, md = load_raw_data()

    print("Cleaning singles dataset...")
    ms_clean = clean_singles_dataset(ms)

    print("Cleaning doubles dataset...")
    md_clean = clean_doubles_dataset(md)

    print("Saving processed datasets...")
    save_processed_data(ms_clean, md_clean)

    print("Data cleaning pipeline completed successfully.")


if __name__ == "__main__":
    run_data_cleaning_pipeline()