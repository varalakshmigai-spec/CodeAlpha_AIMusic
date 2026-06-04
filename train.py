import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
from tensorflow.keras.utils import to_categorical

# =========================
# LOAD DATA
# =========================
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

print("Total notes loaded:", len(notes))

# Optional: reduce dataset for faster training
notes = notes[:50000]

# =========================
# UNIQUE NOTES
# =========================
pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

note_to_int = {note: number for number, note in enumerate(pitchnames)}
int_to_note = {number: note for number, note in enumerate(pitchnames)}

# =========================
# CREATE SEQUENCES
# =========================
sequence_length = 50

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in seq_in])
    network_output.append(note_to_int[seq_out])

n_patterns = len(network_input)

# reshape for LSTM
X = np.reshape(network_input, (n_patterns, sequence_length, 1))
X = X / float(n_vocab)

y = to_categorical(network_output)

# =========================
# BUILD MODEL
# =========================
model = Sequential([
    Input(shape=(X.shape[1], X.shape[2])),
    LSTM(128, return_sequences=True),
    Dropout(0.3),
    LSTM(128),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dense(n_vocab, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

# =========================
# TRAIN MODEL
# =========================
model.fit(X, y, epochs=10, batch_size=32)

# =========================
# SAVE MODEL
# =========================
model.save("music_model.h5")

print("Training complete. Model saved as music_model.h5")