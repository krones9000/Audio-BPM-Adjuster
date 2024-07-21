# Audio BPM Adjuster

A Streamlit application to analyze and adjust the BPM (Beats Per Minute) of audio files in a given folder. This tool is useful for creating a consistent BPM playlist for activities such as running.

I listen to music when I run to pace me. However, a lot of music that is already at the BPM I prefer is also not music that I like. This app lets you provide your own music and a target BPM and it will adjust the files for you. Will they sound perfect? Hell no! Does it means you can listen to whatever you like instead of nothing but monotonous drum and base? Yes.

**I would not recommend trying to massively alter the BPM of tracks. If they're going to need to double in BPM to hit your target, they probably wont sound great. I've included an analysis step, so that you can check the BPM of your target songs before you alter the files.** 

## Features

- Analyze the BPM of audio files (.mp3, .wav) in a specified folder.
- Adjust the BPM of the audio files to a target value.
- Display the current and new BPM of each file.
- Reset functionality to start the process over.

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)
- FFmpeg (for audio processing with pydub)

### Step-by-Step Installation Guide

#### 1. Install Python and pip

If you don't have Python installed, download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions to install it. Make sure to check the box that says "Add Python to PATH" during installation.

#### 2. Open Command Prompt (Windows) or Terminal (Linux/Mac)

**Windows:**
- Press `Win + R` to open the Run dialog.
- Type `cmd` and press Enter to open the Command Prompt.

**Linux/Mac:**
- Open your Terminal application from your application menu.

#### 3. Install the Required Python Libraries

Type the following command in your Command Prompt or Terminal and press Enter:

```
pip install streamlit librosa numpy pydub pandas pyrubberband soundfile
```

This will install all the necessary libraries for the application.

#### 4. Install FFmpeg

**Windows:**
1. Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
2. Extract the downloaded archive and place the `ffmpeg` executable in a known location, for example, `C:\ffmpeg`.
3. Add FFmpeg to your system PATH:
   - Press `Win + R` to open the Run dialog.
   - Type `sysdm.cpl` and press Enter.
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, find and select the `Path` variable in the "System variables" section, then click "Edit".
   - Click "New" and add the path to the directory containing `ffmpeg.exe` (e.g., `C:\ffmpeg\bin`).
   - Click OK on all windows to close them.

**Linux:**
Open your Terminal and type the following command, then press Enter:

```
sudo apt-get install ffmpeg
```

**Mac:**
Open your Terminal and type the following command, then press Enter:

```
brew install ffmpeg
```

### Path Formatting

- When providing paths in the application on Windows, I've been told you may need to use double backslashes (`\\`) or forward slashes (`/`). For example: `C:\\Users\\YourUsername\\Music` or `C:/Users/YourUsername/Music`. I can't test this as I don't have a windows system. So you might need to experiment with the path inputs to get it working.

### PySoundFile Warning

The application uses `librosa` for BPM detection, which may produce a warning regarding PySoundFile. This warning can be safely ignored, as the application will fallback to `audioread` for loading audio files.

## Usage

1. **Clone the Repository**

   In your Command Prompt or Terminal, type the following commands and press Enter after each line:

```
git clone https://github.com/yourusername/audiobpmadjuster.git
cd audiobpmadjuster
```

2. **Run the Streamlit Application**

   In the same Command Prompt or Terminal, type the following command and press Enter:

```
streamlit run app.py
```

3. **Open the Application in Your Browser**

   After running the above command, Streamlit will automatically open a new tab in your default web browser with the application running.

4. **Use the Application**

   - Enter the path to your music folder in the text input field.
   - Click the "Analyze BPM" button to analyze the BPM of the audio files in the folder.
   - Enter the desired BPM in the input field.
   - Click the "Adjust BPM" button to adjust the BPM of the audio files.
   - The adjusted files will be saved in a new folder named `adjusted_bpm` within the specified music folder.
   - Use the "Reset" button to start the process over if needed.

## File Structure

- `app.py`: Main Streamlit application script.
- `requirements.txt`: List of dependencies (optional, if using for deployment).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements. I can't promise how long it will take to action though.

---

Happy adjusting!
