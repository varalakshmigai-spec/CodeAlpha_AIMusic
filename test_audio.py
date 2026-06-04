import pretty_midi

midi = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=0)

notes = [60, 64, 67, 72, 67, 64, 60]

start = 0
for pitch in notes:
    instrument.notes.append(
        pretty_midi.Note(
            velocity=120,
            pitch=pitch,
            start=start,
            end=start + 1
        )
    )
    start += 1

midi.instruments.append(instrument)
midi.write("test.mid")