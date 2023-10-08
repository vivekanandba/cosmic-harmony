import pandas as pd
import numpy as np
import struct
import io

# Load your data
data = pd.read_csv('data/meteorite_landings_clean-top-100-2023-10-08-13-59-29.csv')  # Replace with your file path

# Normalize year and mass for MIDI representation
min_year, max_year = data['year'].min(), data['year'].max()
data['midi_time'] = ((data['year'] - min_year) / (max_year - min_year) * 1000).astype(int)

# Apply logarithmic scaling to mass and normalize for pitch and velocity
data['log_mass'] = np.log(data['mass'])
min_log_mass, max_log_mass = data['log_mass'].min(), data['log_mass'].max()
data['midi_pitch'] = 127 - ((data['log_mass'] - min_log_mass) / (max_log_mass - min_log_mass) * 127).astype(int)
data['midi_velocity'] = ((data['log_mass'] - min_log_mass) / (max_log_mass - min_log_mass) * 127).astype(int)

# Function to convert value to MIDI variable length format
def write_varlen(value):
    value = int(value)
    chr_array = []
    chr_array.append(value & 0x7F)
    value >>= 7
    while value:
        chr_array.append(0x80 | (value & 0x7F))
        value >>= 7
    return bytes(chr_array[::-1])

# Function to create a simple MIDI file with the provided notes
def create_midi(notes):
    delta_time = 1024
    output = io.BytesIO()
    output.write(b'MThd')
    output.write(struct.pack('>L', 6))
    output.write(struct.pack('>H', 1))
    output.write(struct.pack('>H', 1))
    output.write(struct.pack('>H', delta_time))
    output.write(b'MTrk')
    track_data = io.BytesIO()
    for note in notes:
        track_data.write(write_varlen(note[0]))
        track_data.write(struct.pack('>BBB', 0x90, note[1], note[2]))
        track_data.write(write_varlen(1))
        track_data.write(struct.pack('>BBB', 0x80, note[1], note[2]))
    track_data.write(write_varlen(0))
    track_data.write(b'\xff\x2f\x00')
    output.write(struct.pack('>L', len(track_data.getvalue())))
    output.write(track_data.getvalue())
    return output.getvalue()

# Create notes data: [(time, pitch, velocity), ...]
notes_data = [(row['midi_time'], row['midi_pitch'], row['midi_velocity']) for _, row in data.iterrows()]

# Create MIDI file
midi_data = create_midi(notes_data)

# Save MIDI file
file_path = "output/audio"
with open(f'{file_path}/meteorite_melody_gpt4.mid', 'wb') as f:
    f.write(midi_data)
