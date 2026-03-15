from fuzzywuzzy import fuzz


def fuzzy_match_names(unique_names_1, unique_names_2, threshold=90):
    """
    Perform fuzzy matching between two lists of player names.
    """

    match_map = {}

    for name1 in unique_names_1:

        best_score = 0
        best_match = None

        for name2 in unique_names_2:

            score = fuzz.token_sort_ratio(name1, name2)

            if score > best_score:
                best_score = score
                best_match = name2

        if best_score >= threshold:
            match_map[name1] = best_match
        else:
            match_map[name1] = name1

    return match_map


def apply_name_matching(df, column1, column2):

    unique1 = df[column1].unique()
    unique2 = df[column2].unique()

    match_map = fuzzy_match_names(unique1, unique2)

    df[column1] = df[column1].map(match_map)

    return df