import pandas as pd   #import library for loading data, https://pypi.org/project/pandas/
import matplotlib.pylab as plt  #import library for plotting, https://pypi.org/project/matplotlib/
import numpy as np  #import numerical python library
from audiolazy import midi2str,str2midi
from midiutil import MIDIFile #import library to make midi file, https://midiutil.readthedocs.io/en/1.2.1/
from PIL import Image #import library to load image



data_filename = 'lunarCraterAges'

degrees_per_beat = 4 #set conversion factor
bpm = 90  #if bpm = 60, 1 beat = 1 sec

scale_start_note = 'C3'
scale_octaves = 3
scale = 'lydian'


vel_min,vel_max = 35,110   #minimum and maximum note velocity

#https://professionalcomposers.com/midi-cc-list/
controller_number_pan = 10
controller_number_mod = 1
controller_number_cutoff = 74


#moon texture map: https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720
image_file = './data/moon_surface.jpg'

cc_min,cc_max = 63 -35, 63 + 35 #midpoint between 0-127 plus or minus

single_note_name = 'C4' #name of note that will be modified by control changes
chord_note_names = ['C2','C3','G3','E4']  # C major chord, chord that will be modified by control changes
################################################
def map_value(value, min_value, max_value, min_result, max_result, power=1):
    '''maps value(s) from one range to another

    Args:
        value: input value (int, float, list, or array)
        min_value,max_value: input value range
        min_result,max_result: output value range
        power: scaling parameter, linear mapping if set to 1
    Returns:
        int if both min_result and max_result are int, otherwise float
        list of int or float if value is a list
        array of int or float if value is an array'''
    value_input = value

    if isinstance(value_input, list): value = np.array(value_input) #convert list to array

    #validation
    if np.any(value < min_value) or np.any(value > max_value):
        raise ValueError(f'one or more values is outside of range [{min_value},{max_value}]!')

    #mapping
    result = min_result + ((value - min_value)/(max_value - min_value))**power*(max_result - min_result)

    #rounding
    if isinstance(min_result*max_result, int):
        if isinstance(value_input, int) or isinstance(value_input, float):
            result = round(result)
        if isinstance(value_input, list) or isinstance(value_input, np.ndarray):
            result = np.round(result).astype(int)

    if isinstance(value_input, list): result = result.tolist() #convert array back to list (if input value was list)

    return result


def get_scale_notes(start_note, octaves, scale):
    '''returns scale note names'''

    scales = {
    'major':[2,2,1,2,2,2,1],
    'minor':[2,1,2,2,1,2,2],
    'harmonicMinor':[2,1,2,2,1,3,1],
    'melodicMinor':[2,1,2,2,2,2,1],

    'ionian':[2,2,1,2,2,2,1],
    'dorian':[2,1,2,2,2,1,2],
    'phrygian':[1,2,2,2,1,2,2],
    'lydian':[2,2,2,1,2,2,1],
    'mixolydian':[2,2,1,2,2,1,2],
    'aeolian':[2,1,2,2,1,2,2],
    'lochrian':[1,2,2,1,2,2,2],

    'majorPent':[2,2,3,2,3],
    'minorPent':[3,2,2,3,2],

    'wholetone':[2,2,2,2,2,2],
    'diminished':[2,1,2,1,2,1,2,1]
    }

    if type(scale) is str:
        scale_steps = scales[scale]
    if type(scale) is list:
        scale_steps = scale

    note_names = []
    for octave in range(octaves):
        note_number = str2midi(start_note) + (12*octave)

        for step in scale_steps:
            note_names.append(midi2str(note_number))
            note_number = note_number + step

    #add root as last note
    last_midi_note = str2midi(start_note) + (octaves*12)
    note_names.append(midi2str(last_midi_note))

    #could alter function to return midi note numbers instead
    #note_numbers = [str2midi(n) for n in note_names]

    return note_names


def save_midi_cc(events, events_cc, out_filename, bpm=60):
    '''saves one track midi file with note events and control change events'''

    my_midi_file = MIDIFile(1) #one track
    my_midi_file.addTempo(track=0, time=0, tempo=bpm)

    for event in events:
        my_midi_file.addNote(track=0, channel=0, pitch=event['midi'], time=event['t'] , duration=event['dur'], volume=event['vel'])

    for event_cc in events_cc:
        my_midi_file.addControllerEvent(track=0, channel=0, time=event_cc['t'], controller_number=event_cc['controller_number'], parameter=event_cc['parameter'])

    with open(out_filename + '_cc.mid', "wb") as f:
        my_midi_file.writeFile(f)
    print('saved ' + out_filename + '_cc.mid')
####################################################


########## SECTION A (CRATER DATA) ##################
## Load data
df = pd.read_csv(data_filename+'.csv')  #load data as a pandas dataframe
n_craters = len(df)

longitudes = df['longitude'].values    #this is a numpy array (not a list), you can do mathematical operations directly on the object
latitudes = df['latitude'].values
diameters = df['diameter'].values


## Map longitude to time

duration = 360/degrees_per_beat
print('Duration:',duration,'beats')

sec_per_beat = 60/bpm
duration_sec = duration*sec_per_beat
print('Duration:',duration_sec,'seconds')

t_data =  map_value(longitudes, 0, 360, 0., duration)

## Map crater latitude to pitch, diameter to velocity
note_names = get_scale_notes(scale_start_note, scale_octaves, scale)
note_numbers = np.array([str2midi(n) for n in note_names]) #make it an array so we can use do indexing with an array
n_notes = len(note_numbers)
print('Resolution:',n_notes,'notes')


midi_data = note_numbers[map_value(latitudes, -90, 90, 0, n_notes-1)]
vel_data = map_value(diameters, min(diameters), max(diameters), vel_min, vel_max)

## Collect midi events
events = []
for i in range(n_craters):
    event = {}

    event['t'] = t_data[i]
    event['midi'] = midi_data[i]
    event['dur'] = 2
    event['vel'] = vel_data[i]
    events.append(event)


## Map longitude to stereo pandas
time_cc = np.linspace(0, duration, 100) #choose a time resolution for control change events

#simple left-to-right pan (same as mapping longitude to pan from left to right)
#pan_cc = map_value(time_cc, 0, duration, 0, 127)  #returns integers since 0 and 127 are integers

#sine wave pan (this follows the left-right position of craters as they sweep around the moon)
pan_cc = map_value(np.sin(2*np.pi*time_cc/duration), -1, 1, 0, 127)

events_cc=[]
for i in range(len(time_cc)):
    events_cc.append({'t':time_cc[i],'controller_number':controller_number_pan,'parameter':pan_cc[i]})

## Save events as MIDI file
save_midi_cc(events,events_cc, 'craters_pan', tempo=bpm)


########## SECTION B (IMAGE DATA) ##################

## Load Image
im = Image.open(image_file)
width, height = im.size

im_grey = im.convert('L') #convert to greyscale
im_grey = np.roll(im_grey, int(width/2)) #shift so that 0 longitude is on left side


## Get Average brightness
im_arr = np.array(im_grey) #convert image to an array

avg_brightness = np.mean(im_arr, axis=0) #average pixel value of each column

im_longitudes = np.linspace(0, 360, width) #array of each column's longitude

## Map brightness to control change
time_cc_im = np.linspace(0, duration, width)

brightness_cc = map_value(avg_brightness, min(avg_brightness), max(avg_brightness), cc_min, cc_max )

## Save CC events on single note:

events = [{'t': 0, 'midi': str2midi(single_note_name), 'vel': 100, 'dur': duration}] #make single long note

events_cc=[]
for i in range(len(time_cc_im)):
    events_cc.append({'t':time_cc_im[i], 'controller_number':controller_number_mod, 'parameter':brightness_cc[i]})

save_midi_cc(events, events_cc, 'brightness_note', tempo=bpm)


## Save CC events on chord

chord_note_numbers = [str2midi(c) for c in chord_note_names]

events=[]
for i in range(len(chord_note_numbers)):
    events.append({'t': 0, 'midi': chord_note_numbers[i], 'vel': 100, 'dur': duration})

events_cc=[]
for i in range(len(time_cc_im)):
    events_cc.append({'t':time_cc_im[i], 'controller_number':controller_number_cutoff, 'parameter':brightness_cc[i]})

save_midi_cc(events, events_cc, 'brightness_chord', tempo=bpm)
