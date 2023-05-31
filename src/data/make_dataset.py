import pandas as pd
from glob import glob
from typing import List

# --------------------------------------------------------------
# Loading and extracting data from files,
# transforming and merging the datasets
# --------------------------------------------------------------


# Create a list of all file paths in the MetaMotion folder
files = glob("../../data/raw/MetaMotion/*.csv")


def data_from_files(files: List[str]) -> pd.DataFrame:
    # Initialize two empty dfs for accelerometer and gyroscope data
    acc_df = pd.DataFrame()
    gyr_df = pd.DataFrame()

    # Initialize set counters for accelerometer and gyroscope data
    acc_set = 1
    gyr_set = 1

    # Loop over all file paths
    for f in files:
        # Extract metadata (participans, exercise name and its difficulty) from the filename
        participant = f.split("-")[0].replace("../../data/raw/MetaMotion/", "")
        exercise_name = f.split("-")[1]
        exercise_difficulty = f.split("-")[2].split("_")[0].rstrip("123")

        # Read the current file into a df
        df = pd.read_csv(f)

        # Add metadata to the df
        df["participant"] = participant
        df["exercise_name"] = exercise_name
        df["exercise_difficulty"] = exercise_difficulty

        # Check if current file is accelerometer data
        # !(Note that "if" conditions below are case sensitive. Not a problem in this project)
        if "Accelerometer" in f:
            # If so, increment the accelerometer set counter and add it to the df
            df["set"] = acc_set
            acc_set += 1
            # Add the current df to the accelerometer master df
            acc_df = pd.concat([acc_df, df])

        # Check if current file is gyroscope data
        if "Gyroscope" in f:
            # If so, increment the gyroscope set counter and add it to the df
            df["set"] = gyr_set
            gyr_set += 1
            # Add the current df to the gyroscope master df
            gyr_df = pd.concat([gyr_df, df])

    # Convert the 'epoch (ms)' column to datetime and set as index for both df
    acc_df.index = pd.to_datetime(acc_df["epoch (ms)"], unit="ms")
    gyr_df.index = pd.to_datetime(gyr_df["epoch (ms)"], unit="ms")

    # Remove unneeded columns from both dfs
    columns_to_remove = ["epoch (ms)", "time (01:00)", "elapsed (s)"]
    for column in columns_to_remove:
        del acc_df[column]
        del gyr_df[column]

    # Return the final accelerometer and gyroscope dfs
    return acc_df, gyr_df


# Use the function to process the files and get the dfs
acc_df, gyr_df = data_from_files(files)


# Merge  columnwise first three columns of accelerometer df with gyroscope df
data_merged = pd.concat([acc_df.iloc[:, :3], gyr_df], axis=1)

# Rename columns
data_merged.columns = [
    "acc_x",
    "acc_y",
    "acc_z",
    "gyr_x",
    "gyr_y",
    "gyr_z",
    "participant",
    "exercise_name",
    "exercise_difficulty",
    "set",
]

# --------------------------------------------------------------
# Resampling and exporting the dataset
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# Define the columns that will take mean aggregation, last value aggregation.
mean_cols = ["acc_x", "acc_y", "acc_z", "gyr_x", "gyr_y", "gyr_z"]
last_cols = ["participant", "exercise_name", "exercise_difficulty", "set"]

# Create a dictionary that maps the column names to the respective aggregation
sampling = {column: "mean" for column in mean_cols}
sampling.update({column: "last" for column in last_cols})

# Split the df into a list of dfs, each containing data from a single day (This will
# save a lot of time and computational resources!)
days = [g for n, g in data_merged.groupby(pd.Grouper(freq="D"))]

# For each df in 'days', resample it at 200ms intervals,
# apply sample aggregations and generate a singe df,
# remove missing values that have been created during resampling
data_resampled = pd.concat(
    [df.resample(rule="200ms").apply(sampling).dropna() for df in days]
)

# Convert the 'set' column from float to integer
data_resampled["set"] = data_resampled["set"].astype(int)


# Export dataset
data_resampled.to_pickle("../../data/interim/01_data_processed.pkl")
