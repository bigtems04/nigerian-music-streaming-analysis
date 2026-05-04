import os
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "song": ["Calm Rise", "Lagos Nights", "Rush Again", "Soft Life", "City Boys II"],
    "artist": ["Rema", "Asake", "Ayra Starr", "Omah Lay", "Burna Boy"],
    "streams": [750000, 600000, 700000, 360000, 850000],
    "unique_listeners": [400000, 310000, 280000, 250000, 500000],
    "saves": [60000, 55000, 84000, 20000, 75000],
    "skips": [90000, 72000, 56000, 70000, 110000],
    "completed_plays": [570000, 450000, 595000, 230000, 650000],
    "playlist_reach": [900000, 1200000, 700000, 400000, 1500000],
    "playlist_streams": [180000, 210000, 175000, 60000, 300000]
}

df = pd.DataFrame(data)

df
df["streams_per_listener"] = df["streams"] / df["unique_listeners"]

df["save_rate_percent"] = (df["saves"] / df["unique_listeners"]) * 100

df["skip_rate_percent"] = (df["skips"] / df["streams"]) * 100

df["completion_rate_percent"] = (df["completed_plays"] / df["streams"]) * 100

df["playlist_conversion_percent"] = (
    df["playlist_streams"] / df["playlist_reach"]
) * 100

df
df_rounded = df.copy()

kpi_columns = [
    "streams_per_listener",
    "save_rate_percent",
    "skip_rate_percent",
    "completion_rate_percent",
    "playlist_conversion_percent"
]

df_rounded[kpi_columns] = df_rounded[kpi_columns].round(2)

df_rounded
df_rounded.sort_values("save_rate_percent", ascending=False)

print(df_rounded.sort_values("save_rate_percent", ascending=False))

investment_ready = df_rounded[
    (df_rounded["save_rate_percent"] > 20) &
    (df_rounded["skip_rate_percent"] < 10) &
    (df_rounded["completion_rate_percent"] > 80)
]

investment_ready

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["streams"])
plt.title("Streams by Song")
plt.xlabel("Song")
plt.ylabel("Streams")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["save_rate_percent"])
plt.title("Save Rate by Song")
plt.xlabel("Song")
plt.ylabel("Save Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["skip_rate_percent"])
plt.title("Skip Rate by Song")
plt.xlabel("Song")
plt.ylabel("Skip Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["completion_rate_percent"])
plt.title("Completion Rate by Song")
plt.xlabel("Song")
plt.ylabel("Completion Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["playlist_conversion_percent"])
plt.title("Playlist Conversion by Song")
plt.xlabel("Song")
plt.ylabel("Playlist Conversion (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["playlist_conversion_percent"])
plt.title("Playlist Conversion by Song")
plt.xlabel("Song")
plt.ylabel("Playlist Conversion (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 13: Export the cleaned dataset
base_folder = os.path.dirname(os.path.dirname(__file__))

dataset_path = os.path.join(base_folder, "dataset", "music_kpi_analysis_output.csv")

df_rounded.to_csv(dataset_path, index=False)

print("CSV file created successfully:", dataset_path)



# Step 14: Save charts into the visuals folder
visuals_folder = os.path.join(base_folder, "visuals")
os.makedirs(visuals_folder, exist_ok=True)
# Chart 1: Streams by Song
plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["streams"])
plt.title("Streams by Song")
plt.xlabel("Song")
plt.ylabel("Streams")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "streams_by_song.png"))
plt.close()


# Chart 2: Save Rate by Song
plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["save_rate_percent"])
plt.title("Save Rate by Song")
plt.xlabel("Song")
plt.ylabel("Save Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "save_rate_by_song.png"))
plt.close()

# Chart 3: Skip Rate by Song
plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["skip_rate_percent"])
plt.title("Skip Rate by Song")
plt.xlabel("Song")
plt.ylabel("Skip Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "skip_rate_by_song.png"))
plt.close()

# Chart 4: Completion Rate by Song
plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["completion_rate_percent"])
plt.title("Completion Rate by Song")
plt.xlabel("Song")
plt.ylabel("Completion Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "completion_rate_by_song.png"))
plt.close()

# Chart 5: Playlist Conversion by Song
plt.figure(figsize=(10, 5))
plt.bar(df_rounded["song"], df_rounded["playlist_conversion_percent"])
plt.title("Playlist Conversion by Song")
plt.xlabel("Song")
plt.ylabel("Playlist Conversion (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "playlist_conversion_by_song.png"))
plt.close()

print("Charts saved successfully in the visuals folder:", visuals_folder)