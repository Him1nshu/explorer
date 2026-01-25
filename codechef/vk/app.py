import pandas as pd


# 1. Load Virat Match Data
def load_data(filename):
    """
    Load Virat Kohli match-wise performance data and parse dates.
    """
    try:
        # TODO: Load the CSV file using Pandas
        df = pd.read_csv(filename)

        # TODO: Convert 'match_date' column to datetime objects
        # Use this format="%Y-%m-%d"
        __________
        
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
    except Exception:
        print(f"Error loading data.")
        return pd.DataFrame()


# 2. Load Opponent Mapping Data
def load_opponent_data(filename):
    try:
        # TODO: Load the CSV file using Pandas
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 3. Merge Match + Opponent Data
def merge_match_opponent(match_df, opponent_df):
    """
    Merge match data with opponent full names.
    """

    if "opponent" not in match_df.columns or "opponent" not in opponent_df.columns:
        print("Error: 'opponent' column missing in one of the datasets.")
        return match_df

    # TODO: Merge the two dataframes on the "opponent" column using a left join
    merged_df = __________
    
    return merged_df


# 4. Analysis Functions
def total_runs(df):
    """
    Calculate total runs scored by Virat Kohli.
    """
    runs_column = df["runs"]
    
    # TODO: Calculate total runs scored by Virat Kohli
    total = __________
    
    return total


def average_runs(df):
    """
    Calculate the average runs per match scored by Virat Kohli.
    """
    runs_column = df["runs"]
    
    # TODO: Calculate the average runs per match
    average = __________
    
    # TODO: Round the average to 2 decimal places
    average_rounded = __________
    
    return average_rounded


def runs_by_opponent(df):
    """
    Calculate total runs scored against each opponent.
    """
    # TODO: Group the data by "opponent" full name
    grouped_data = __________

    # TODO: Sum the runs for each opponent
    total_runs = __________
    
    # TODO: Sort the total runs in descending order
    sorted_runs = __________
    
    return sorted_runs


def count_fifties(df):
    """
    Count the number of matches where Virat Kohli scored fifty or more runs (but less than 100 runs).
    """
    # TODO: Find the number of matches with 50-99 runs
    total_fifties = __________

    return total_fifties


def count_centuries(df):
    """
    Count the number of matches where Virat Kohli scored a century or more runs.
    """
    # TODO: Find the number of matches with 100 or more runs
    total_centuries = __________

    return total_centuries


def career_run_progression(df):
    """
    Calculate cumulative career runs over time.
    """
    # TODO: Sort the dataframe by "match_date"
    df_sorted = __________

    # TODO: Calculate cumulative sum of "runs"
    # Hint: Use .cumsum() to calculate the cumulative sum of runs
    cumulative_runs = __________

    # TODO: Create a new column for career total runs with name "career_runs"
    __________

    # TODO: Select only the required columns for output
    result = __________

    return result


def consistency_matches(df):
    """
    Count the number of matches where Virat Kohli scored at least 30 runs.
    """
    # TODO: Filter matches where runs are >= 30
    total_consistent_matches = __________

    return total_consistent_matches


def not_out_innings(df):
    """
    Count the number of innings where Virat Kohli remained Not Out.
    """
    # TODO: Find the number of innings where Virat Kohli remained Not Out
    total_not_out = __________

    return total_not_out


def best_venue(df):
    """
    Find the venue where Virat Kohli has scored the most runs.
    """
    # TODO: Find the venue where Virat Kohli has scored the most runs
    best_venue = __________

    return best_venue


if __name__ == "__main__":
    print("### Virat Kohli Career Analysis ###")

    # Load Data
    virat_df = load_data("ipl_matches.csv")
    opponent_df = load_opponent_data("opponents.csv")

    if not virat_df.empty:
        # Merge if opponent data exists
        if not opponent_df.empty:
            df = merge_match_opponent(virat_df, opponent_df)
        else:
            df = virat_df
            print("Warning: Opponent data missing, proceeding with match data only.")

        # 1. Total runs
        print(f"\nTotal Career Runs: {total_runs(df)}")

        # 2. Average runs
        print(f"Average Runs Per Match: {average_runs(df)}")

        # 3. Runs against each opponent
        print("\nRuns Against Each Opponent (Top 3):")
        print(runs_by_opponent(df).head(3))

        # 4. Fifty counts
        print(f"\nNumber of 50s: {count_fifties(df)}")

        # 5. Century counts
        print(f"Number of Centuries: {count_centuries(df)}")

        # 6. Career progression
        print("\nCareer Run Progression (First 5 matches):")
        print(career_run_progression(df).head())

        # 7. Consistency (30+ runs)
        print(f"\nNumber of Consistent Matches (30+ runs):")
        print(f"{consistency_matches(df)}")

        # 8. Not Out Innings
        print(f"Number of Not Out Innings:")
        print(f"{not_out_innings(df)}")

        # 9. Best Venue
        best = best_venue(df)
        print(f"\nBest Venue: {best.index[0]} with {best.values[0]} runs")


