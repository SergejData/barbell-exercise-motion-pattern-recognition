import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# --------------------------------------------------------------
# Load data, create plot settings
# --------------------------------------------------------------

df = pd.read_pickle("../../data/interim/01_data_processed.pkl")

mpl.style.use("seaborn")
mpl.rcParams["figure.figsize"] = (20, 6)
mpl.rcParams["figure.dpi"] = 100


# --------------------------------------------------------------
# Loop over all plot combinations and export for both sensors
# --------------------------------------------------------------

# Get unique exercise names and participants from the df
exercise_names = df["exercise_name"].unique()
participants = df["participant"].unique()

# Loop over each unique exercise
for exercise_name in exercise_names:
    # Loop over each unique participant
    for participant in participants:
        # Filter the df for only this exercise and participant
        combined_plot_df = (
            df.query(f"exercise_name == '{exercise_name}'")
            .query(f"participant == '{participant}'")
            .reset_index()
        )

        # Proceed if there are rows in the filtered df
        if len(combined_plot_df) > 0:
            # Create subplot with 2 rows, sharing the same x-axis
            fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20, 10))

            # Plot accelerometer data on the first subplot
            combined_plot_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax[0])
            ax[0].set_title(
                f"Accelerometer Data for {exercise_name.title()}, participant {participant}"
            )  # Add title to the first subplot
            ax[0].set_ylabel("g")  # Add y label to the first subplot
            ax[0].legend(loc="upper right", ncol=1, fancybox=True)

            # Plot gyroscope data on the second subplot
            combined_plot_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax[1])
            ax[1].set_title(
                f"Gyroscope Data for {exercise_name.title()}, participant {participant}"
            )  # Add title to the second subplot
            ax[1].set_ylabel("deg/s")  # Add y label to the second subplot
            ax[1].legend(loc="upper right", ncol=1, fancybox=True)
            ax[1].set_xlabel("Samples")

            # Display plots to check
            plt.show()

            # Save plots as a PNG file with e.g. filename "Row (A).png")
            plt.savefig(
                f"../../reports/figures/{exercise_name.title()} ({participant}).png"
            )
