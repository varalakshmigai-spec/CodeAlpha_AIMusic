import numpy as np
import pickle
from tensorflow.keras.models import load_model
import pretty_midi
import os

# Load data
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))

n_vocab = len(pitchnames)
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

model = load_model("music_model.h5")

sequence_length = 50

start = np.random.randint(0, len(notes) - sequence_length)
pattern = [note_to_int[n] for n in notes[start:start + sequence_length]]

output_notes = []

for _ in range(40):

    x = np.array(pattern).reshape(1, len(pattern), 1)
    x = x / float(n_vocab)

    prediction = model.predict(x, verbose=0)[0]

    temperature = 0.8

    prediction = prediction ** (1 / temperature)
    prediction = prediction / np.sum(prediction)

    index = np.random.choice(len(prediction), p=prediction)
    note = int_to_note[index]

    # convert safely
    try:
        pitch = int(note)
    except:
        pitch = 60
    # clamp to safe piano range
    pitch = max(36, min(84, pitch))

    output_notes.append(pitch)

    pattern.append(index)
    pattern = pattern[1:]
print("Generated notes:")
print(output_notes[:50])
# Convert to MIDI
midi = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=0)

start_time = 0
for note in output_notes:

    try:
        pitch = int(note)
    except:
        pitch = 60

    pitch = max(21, min(108, pitch))  # safe MIDI range

    new_note = pretty_midi.Note(
        velocity=127,
        pitch=pitch,
        start=start_time,
        end=start_time + 0.5
    )

    instrument.notes.append(new_note)
    start_time += 0.5

midi.instruments.append(instrument)
midi.write("generated_music.mid")

print("Music generated: generated_music.mid")
import os

os.system(
   fluidsynth -g 7 -r 22050 generated_music.mid -F generated_music.wav -ni /usr/share/sounds/sf2/FluidR3_GM.sf2
)

print("✅ WAV created: generated_music.wav")
   