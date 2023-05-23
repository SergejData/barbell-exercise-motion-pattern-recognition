import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

df = pd.read_pickle("../../data/interim/01_data_processed.pkl")

# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------

set_df = df[df["set"] == 1]

plt.plot(set_df["acc_y"].reset_index(drop=True))

# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------


for exercise in df["exercise_name"].unique():
    subset = df[df["exercise_name"] == exercise]
    fig, ax = plt.subplots()
    plt.plot(subset[:100]["acc_y"].reset_index(drop=True), label=exercise)
    plt.legend()
    plt.show()


# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------

mpl.style.use("seaborn")
mpl.rcParams["figure.figsize"] = (30, 5)
mpl.rcParams["figure.dpi"] = 100

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------

category_df = df.query("exercise_name == 'squat' & participant == 'A'").reset_index()

fig, ax = plt.subplots()
category_df.groupby("exercise_difficulty")["acc_y"].plot(legend=True)
ax.set_ylabel("Acceleration along y axis")
ax.set_xlabel("Samples")


# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------

participant_df = (
    df.query("exercise_name == 'ohp'").sort_values("participant").reset_index()
)


fig, ax = plt.subplots()
participant_df.groupby("participant")["acc_y"].plot(legend=True)
ax.set_ylabel("Acceleration along y axis")
ax.set_xlabel("Samples")

# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------
