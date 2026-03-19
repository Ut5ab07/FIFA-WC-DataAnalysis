def calculate_forward_score(df):
    return (
        0.30 * df["goals_per90"] +
        0.20 * df["assists_per90"] +
        0.25 * df["npxg_per90"] +
        0.15 * df["xg_assist_per90"] +
        0.10 * df["goals_assists_per90"]
    )


def calculate_midfielder_score(df):
    return (
        0.20 * df["assists_per90"] +
        0.20 * df["chance_created_per90"] +
        0.20 * df["xg_assist_per90"] +
        0.15 * df["pass_per90"] +
        0.15 * df["tackles_per90"] +
        0.10 * df["successful_dribbles"]
    )


def calculate_defender_score(df):
    return (
        0.40 * df["success_tackles_per90"] +
        0.30 * df["clearance_per90"] +
        0.20 * df["pass_success"] +
        0.10 * df["chance_created_per90"]
    )


def calculate_goalkeeper_score(df):
    return (
        0.30 * df["save_percentage"] +
        0.30 * df["saves"] +
        0.25 * df["Clean_s"] -
        0.15 * df["goals_conceded_per90"]
    )