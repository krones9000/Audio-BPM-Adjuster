import os  # For file and directory operations
import librosa  # For audio analysis and feature extraction
import numpy as np  # For numerical operations (not used directly here)
from pydub import AudioSegment  # For audio file manipulation
import streamlit as st  # For creating the web application
import pandas as pd  # For data handling and manipulation
import pyrubberband as pyrb  # For time-stretching and pitch-shifting (not used directly here)
import soundfile as sf  # For reading and writing audio files (not used directly here)
import warnings  # For handling warnings

# Suppress specific warnings related to audio file reading issues
warnings.filterwarnings("ignore", category=UserWarning, message="PySoundFile failed. Trying audioread instead.")

def get_bpm(file_path):
    """
    Calculate the BPM (Beats Per Minute) of an audio file.
    
    Args:
    - file_path (str): Path to the audio file
    
    Returns:
    - float: BPM of the audio file rounded to two decimal places
    """
    y, sr = librosa.load(file_path)  # Load the audio file with librosa
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)  # Estimate the tempo (BPM)
    return round(tempo, 2)  # Return BPM rounded to two decimal places

def adjust_tempo(input_file, output_file, target_bpm, current_bpm):
    """
    Adjust the tempo of an audio file to a target BPM.
    
    Args:
    - input_file (str): Path to the input audio file
    - output_file (str): Path to save the adjusted audio file
    - target_bpm (float): Desired BPM
    - current_bpm (float): Current BPM of the audio file
    """
    audio = AudioSegment.from_file(input_file)  # Load the audio file using pydub

    if current_bpm == 0:
        st.warning(f"Could not detect BPM for {input_file}. Skipping.")  # Warn if BPM detection failed
        return

    speed_factor = target_bpm / current_bpm  # Calculate the speed factor for tempo adjustment
    adjusted_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed_factor)  # Adjust the frame rate
    })
    adjusted_audio = adjusted_audio.set_frame_rate(audio.frame_rate)  # Reset the frame rate to original

    adjusted_audio.export(output_file, format=os.path.splitext(input_file)[1][1:])  # Export the adjusted audio

def main():
    """
    Main function to run the Streamlit app for BPM adjustment.
    """
    st.title("Audio BPM Adjuster")  # Set the title of the app

    # Initialize session state variables
    if 'file_df' not in st.session_state:
        st.session_state.file_df = None
    if 'folder_path' not in st.session_state:
        st.session_state.folder_path = ""

    # Step 1: Select folder
    folder_path = st.text_input("Enter the path to your music folder:", value=st.session_state.folder_path)
    st.session_state.folder_path = folder_path  # Store the folder path in session state

    if folder_path and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]  # List audio files
        st.write(f"Found {len(files)} audio files in the folder.")  # Display the number of files

        # Step 2: Analyze BPM
        if st.button("Analyze BPM"):
            progress_bar = st.progress(0)  # Initialize a progress bar
            file_data = []
            for i, file in enumerate(files):
                file_path = os.path.join(folder_path, file)
                bpm = get_bpm(file_path)  # Get BPM of each file
                file_data.append({"File": file, "Current BPM": bpm, "New BPM": None})
                progress_bar.progress((i + 1) / len(files))  # Update progress bar

            st.session_state.file_df = pd.DataFrame(file_data)  # Store file data in session state

        # Step 3: Set desired BPM
        target_bpm = st.number_input("Enter the desired BPM:", min_value=1.0, value=120.0, step=0.1)  # Input desired BPM

        # Step 4: Process files
        if st.button("Adjust BPM") and st.session_state.file_df is not None:
            output_folder = os.path.join(folder_path, "adjusted_bpm")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)  # Create output folder if it doesn't exist

            progress_bar = st.progress(0)  # Initialize a progress bar
            for i, row in st.session_state.file_df.iterrows():
                input_file = os.path.join(folder_path, row['File'])
                file_name, file_ext = os.path.splitext(row['File'])
                output_file = os.path.join(output_folder, f"{file_name}_{int(target_bpm)}{file_ext}")  # Define output file path
                adjust_tempo(input_file, output_file, target_bpm, row['Current BPM'])  # Adjust BPM
                st.session_state.file_df.at[i, 'New BPM'] = target_bpm  # Update DataFrame with new BPM
                progress_bar.progress((i + 1) / len(st.session_state.file_df))  # Update progress bar

            st.success(f"BPM adjustment complete. Adjusted files are in: {output_folder}")  # Notify completion

        # Always display the updated DataFrame
        st.write(st.session_state.file_df)  # Display DataFrame with current BPM info

        # Step 5: Reset button
        if st.button("Reset"):
            st.session_state.file_df = None  # Clear DataFrame
            st.session_state.folder_path = ""  # Clear folder path
            st.experimental_rerun()  # Rerun the app to refresh

if __name__ == "__main__":
    main()  # Run the main function to start the Streamlit app
