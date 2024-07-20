# Audio BPM Adjuster

A Streamlit application to analyze and adjust the BPM (Beats Per Minute) of audio files in a given folder. This tool is useful for creating a consistent BPM playlist for activities such as running.

I listen to music when I run to pace me. However, a lot of music that naturally falls at the BPM I like sounds horrible to my ears. This app lets you provide your own music and a target BPM and it will adjust the files for you. Will they sound perfect? Hell no! Does it means you can listen to whatever you like instead of nothing but monotonous drum and base? Yes.

**I would not recommend trying to massively alter the BPM of tracks. If they're going to need to double in BPM to hit your target, they probably wont sound great. I've included an analysis step, so that you can check this before you alter the files. 

## Features

- Analyze the BPM of audio files (.mp3, .wav) in a specified folder.
- Adjust the BPM of the audio files to a target value.
- Display the current and new BPM of each file.
- Reset functionality to start the process over.

## Installation

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)
- FFmpeg (for audio processing with pydub)

### Dependencies

Install the required Python dependencies using pip:

```
pip install streamlit librosa numpy pydub pandas pyrubberband soundfile
```

### Setting up FFmpeg

#### Linux

1. Install FFmpeg using your package manager. For example, on Debian-based systems (like Ubuntu):

```
sudo apt-get install ffmpeg
```

#### Windows

1. Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
2. Extract the downloaded archive and place the `ffmpeg` executable in a known location.
3. Add the location of the `ffmpeg` executable to your system PATH:
   - Open the Start Search, type in "env", and select "Edit the system environment variables".
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, select the "Path" variable in the "System variables" section and click "Edit".
   - Click "New" and add the path to the directory containing `ffmpeg.exe`.
   - Click OK on all windows to close them.

### Path Formatting

- When providing paths in the application, use double backslashes (`\\`) or forward slashes (`/`) in the input field on Windows. For example: `C:\\Users\\YourUsername\\Music` or `C:/Users/YourUsername/Music`.

### PySoundFile Warning

The application uses `librosa` for BPM detection, which may produce a warning regarding PySoundFile. This warning can be safely ignored, as the application will fallback to `audioread` for loading audio files.

## Usage

1. Clone the repository:

```
git clone https://github.com/yourusername/audiobpmadjuster.git
cd audiobpmadjuster
```

2. Run the Streamlit application:

```
streamlit run app.py
```

3. Enter the path to your music folder in the text input field.
4. Click the "Analyze BPM" button to analyze the BPM of the audio files in the folder.
5. Enter the desired BPM in the input field.
6. Click the "Adjust BPM" button to adjust the BPM of the audio files.
7. The adjusted files will be saved in a new folder named `adjusted_bpm` within the specified music folder.
8. Use the "Reset" button to start the process over if needed.

## File Structure

- `app.py`: Main Streamlit application script.
- `requirements.txt`: List of dependencies (optional, if using for deployment).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements. I can't promise how long it will take to action though.

---

Happy adjusting!
