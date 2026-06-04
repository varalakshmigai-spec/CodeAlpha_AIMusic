import pretty_midi
import glob
import os
import pickle

# -------------------------
# PATH
# -------------------------
DATASET_PATH = "dataset"

files = glob.glob(os.path.join(DATASET_PATH, "**/*.mid"), recursive=True)

print("MIDI files found:", len(files))

notes = []

# -------------------------
# EXTRACT NOTES
# -------------------------
for i, file in enumerate(files):
    print(f"Processing {i+1}/{len(files)}:", file)

    try:
        midi_data = pretty_midi.PrettyMIDI(file)

        for instrument in midi_data.instruments:
            for note in instrument.notes:
                notes.append(str(note.pitch))

    except Exception as e:
        print("Skipped:", file)

# -------------------------
# SAVE DATA
# -------------------------
with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("\nTotal Notes:", len(notes))