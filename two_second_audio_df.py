duration_and_non_null_mask = pd.notna(data.audio_filename) & (data.duration >= 2)
two_second_audio_df = data[duration_and_non_null_mask]
two_second_audio_df.describe()