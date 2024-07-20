import os
import librosa
import numpy as np
from pydub import AudioSegment
import streamlit as st
import pandas as pd
import pyrubberband as pyrb
import soundfile as sf
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, message="PySoundFile failed. Trying audioread instead.")

def get_bpm(file_path):
    y, sr = librosa.load(file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(tempo, 2)

def adjust_tempo(input_file, output_file, target_bpm, current_bpm):
    audio = AudioSegment.from_file(input_file)
    
    if current_bpm == 0:
        st.warning(f"Could not detect BPM for {input_file}. Skipping.")
        return
    
    speed_factor = target_bpm / current_bpm
    adjusted_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed_factor)
    })
    adjusted_audio = adjusted_audio.set_frame_rate(audio.frame_rate)
    
    adjusted_audio.export(output_file, format=os.path.splitext(input_file)[1][1:])

def main():
    st.title("Audio BPM Adjuster")

    if 'file_df' not in st.session_state:
        st.session_state.file_df = None
    if 'folder_path' not in st.session_state:
        st.session_state.folder_path = ""

    # Step 1: Select folder
    folder_path = st.text_input("Enter the path to your music folder:", value=st.session_state.folder_path)
    st.session_state.folder_path = folder_path
    
    if folder_path and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]
        st.write(f"Found {len(files)} audio files in the folder.")
        
        # Step 2: Analyze BPM
        if st.button("Analyze BPM"):
            progress_bar = st.progress(0)
            file_data = []
            for i, file in enumerate(files):
                file_path = os.path.join(folder_path, file)
                bpm = get_bpm(file_path)
                file_data.append({"File": file, "Current BPM": bpm, "New BPM": None})
                progress_bar.progress((i + 1) / len(files))
            
            st.session_state.file_df = pd.DataFrame(file_data)
        
        # Step 3: Set desired BPM
        target_bpm = st.number_input("Enter the desired BPM:", min_value=1.0, value=120.0, step=0.1)
        
        # Step 4: Process files
        if st.button("Adjust BPM") and st.session_state.file_df is not None:
            output_folder = os.path.join(folder_path, "adjusted_bpm")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            progress_bar = st.progress(0)
            for i, row in st.session_state.file_df.iterrows():
                input_file = os.path.join(folder_path, row['File'])
                file_name, file_ext = os.path.splitext(row['File'])
                output_file = os.path.join(output_folder, f"{file_name}_{int(target_bpm)}{file_ext}")
                adjust_tempo(input_file, output_file, target_bpm, row['Current BPM'])
                st.session_state.file_df.at[i, 'New BPM'] = target_bpm
                progress_bar.progress((i + 1) / len(st.session_state.file_df))
            
            st.success(f"BPM adjustment complete. Adjusted files are in: {output_folder}")
        
        # Always display the updated DataFrame
        st.write(st.session_state.file_df)
        
        # Step 5: Reset button
        if st.button("Reset"):
            st.session_state.file_df = None
            st.session_state.folder_path = ""
            st.experimental_rerun()

if __name__ == "__main__":
    main()
