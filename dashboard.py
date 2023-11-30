import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *
import random 


def discussion_dashboard():
    clear()
    put_markdown("# Group Discussion Dashboard")

    # Add your PyWebIO components here if needed

    # Specify the path to your transcript file
    file_path = "/Users/norika_machome/Library/CloudStorage/OneDrive-UniversiteitLeiden/Semester1/4.MS_FRI/final_project/speechProcess/audio8.txt"

    # Read the transcript file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a list to store the timestamp, speaker, text, and word count information
    transcript = []

    # Get a list of all unique speakers
    all_speakers = set()

    # Iterate through the lines in the file and extract information
    for line in lines:
        # Assuming the speaker information is in a specific format, adapt as needed
        if line.startswith("[") and "]" in line:
            speaker = line.split(" ")[1]
            all_speakers.add(speaker)

    # Create initial dataframe with all speakers and zero cumulative word count
    initial_data = [{'timestamp': '', 'speaker': speaker, 'cumulative_word_count': 0} for speaker in all_speakers]
    df_initial = pd.DataFrame(initial_data)

    # Initialize variables for tracking word count over time for each speaker
    current_word_counts = {speaker: 0 for speaker in all_speakers}

    # Iterate through the lines in the file and extract information
    for line in lines:
        # Assuming the speaker information is in a specific format, adapt as needed
        if line.startswith("[") and "]" in line:
            timestamp = line.split("]")[0][1:]
            text = " ".join(line.split(" ")[2:]).strip()

            # Calculate word count
            word_count = len(text.split())

            # Update word count for each speaker
            for speaker in all_speakers:
                # Check if the current speaker matches the loop speaker
                if speaker in line:
                    # Update cumulative word count for the current speaker
                    current_word_counts[speaker] += word_count

                    # Append information to the transcript list
                    transcript.append({
                        "timestamp": timestamp,
                        "speaker": speaker,
                        "text": text,
                        "word_count": word_count,
                        "cumulative_word_count": current_word_counts[speaker]
                    })
                else:
                    # If the speaker doesn't match, use zero word count
                    transcript.append({
                        "timestamp": timestamp,
                        "speaker": speaker,
                        "text": "",
                        "word_count": 0,
                        "cumulative_word_count": current_word_counts[speaker]
                    })

    # Create a DataFrame from the transcript data
    df = pd.DataFrame(transcript)

    # Convert timestamp to datetime for better plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%M:%S.%f')

    # Convert the timestamp to string for animation
    df['timestamp_str'] = df['timestamp'].dt.strftime('%M:%S.%f')

    # Group by speaker and timestamp and concatenate the text
    full_text_df = df.groupby(['speaker', 'timestamp'])['text'].apply(lambda x: ' '.join(x)).reset_index()

    # Concatenate all text from different speakers and timestamps
    full_text = ' '.join(full_text_df['text'])

    # Create an animated bar plot with Plotly Express
    fig = px.bar(df, x='speaker', y='cumulative_word_count', color='speaker',
                animation_frame='timestamp_str',
                title='Cumulative Word Count Over Time for Each Speaker',
                labels={'timestamp_str': 'Timestamp', 'cumulative_word_count': 'Cumulative Word Count'},
                category_orders={'speaker': sorted(df['speaker'].unique())},
                )

    # Update layout for better readability
    fig.update_layout(xaxis=dict(title='Speaker'),
                    yaxis=dict(title='Cumulative Word Count', range=[0, 500]),
                    )

    html = fig.to_html(include_plotlyjs="require", full_html=False)
    put_html(html)

    # Show the full_text on the dashboard as markdown
    put_markdown(f"## Full Text\n{full_text}")

    