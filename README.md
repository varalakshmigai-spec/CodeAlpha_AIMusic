# 🎵 AI Music Generator

## Overview

AI Music Generator is a deep learning project that generates new musical sequences from a collection of MIDI files. The system uses an LSTM (Long Short-Term Memory) neural network to learn musical patterns and create original melodies.

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

---

## Features

* Collects and processes MIDI music files.
* Extracts musical notes using the `music21` library.
* Trains an LSTM-based neural network on note sequences.
* Generates new music based on learned patterns.
* Converts generated note sequences into MIDI files.
* Converts MIDI output into WAV audio format using FluidSynth.
* Provides a simple Streamlit web interface for music generation.

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* music21
* PrettyMIDI
* FluidSynth
* Streamlit

---

## Project Workflow

1. Collect MIDI music files.
2. Preprocess and extract note sequences.
3. Train an LSTM neural network on the dataset.
4. Generate new music sequences.
5. Convert generated sequences to MIDI format.
6. Render MIDI into playable audio (WAV).
7. Play generated music through the web interface.

---

## Project Structure

```text
Task3/
│
├── app.py
├── preprocess.py
├── train.py
├── generate.py
├── notes.pkl
├── music_model.h5
├── requirements.txt
├── dataset/
│   └── *.mid
└── README.md
```

---

## Installation

Clone the repository;

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

## Usage

### Preprocess Dataset

```bash
python preprocess.py
```

### Train the Model

```bash
python train.py
```

### Generate Music

```bash
python generate.py
```

### Run the Web Application

```bash
streamlit run app.py
```

---

## Output

The generated music is saved as:

* `generated_music.mid`
* `generated_music.wav`

These files can be played using any MIDI or audio player.

---

## Future Improvements

* Support multiple music genres.
* Improve melody quality using advanced architectures.
* Add real-time music generation.
* Deploy the application online.
* Add multiple instrument support.


