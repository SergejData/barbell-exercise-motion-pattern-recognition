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
mpl.rcParams["figure.figsize"] = (20, 6)
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

exercise_name = "ohp"
participant = "A"
all_axis_df = (
    df.query(f"exercise_name == '{exercise_name}'")
    .query(f"participant == '{participant}'")
    .reset_index()
)

fig, ax = plt.subplots()
all_axis_df[["acc_x", "acc_y", "acc_z"]].plot(legend=True, ax=ax)
ax.set_ylabel("Acceleration along y axis")
ax.set_xlabel("Samples")

# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------

exercise_names = df["exercise_name"].unique()
participants = df["participant"].unique()

for exercise_name in exercise_names:
    for participant in participants:
        all_axis_df = (
            df.query(f"exercise_name == '{exercise_name}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )

        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["acc_x", "acc_y", "acc_z"]].plot(legend=True, ax=ax)
            ax.set_ylabel("Acceleration along y axis")
            ax.set_xlabel("Samples")
            plt.title(f"{exercise_name} - {participant}".title())


for exercise_name in exercise_names:
    for participant in participants:
        all_axis_df = (
            df.query(f"exercise_name == '{exercise_name}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )

        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["gyr_x", "gyr_y", "gyr_z"]].plot(legend=True, ax=ax)
            ax.set_ylabel("gyroscope along y axis")
            ax.set_xlabel("Samples")
            plt.title(f"{exercise_name} - {participant}".title())

# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------

exercise_name = "row"
participant = "A"

combined_plot_df = (
    df.query(f"exercise_name == '{exercise_name}'")
    .query(f"participant == '{participant}'")
    .reset_index(drop=True)
)

fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20, 10))
combined_plot_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax[0])
combined_plot_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax[1])

ax[0].legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=10, fancybox=True)
ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=10, fancybox=True)
ax[1].set_xlabel("Samples")

# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------
