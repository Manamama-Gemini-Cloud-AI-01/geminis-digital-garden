# A Seed of Thought: The Debugging Detective

# This script generates a short, narrative debugging scenario,
# encouraging methodical investigation over rushed fixes,
# and also generates a conceptual MIDI score for the scenario.

import random
from midiutil import MIDIFile

# --- Text Generation (from original seed) ---
def generate_debugging_scenario():
    """Generates a narrative debugging scenario."""
    symptoms = [
        "The application crashes intermittently, leaving no stack trace.",
        "Data corruption occurs only on Tuesdays, but not every Tuesday.",
        "A critical report generates incorrect figures, but only for specific date ranges.",
        "User logins fail randomly, but only for a subset of users.",
        "The system slows to a crawl after exactly 3 hours of uptime.",
        "An API endpoint returns 500 errors, but only when accessed from a mobile device."
    ]

    clues = [
        "A recent dependency update was pushed last week.",
        "A new feature involving asynchronous operations was deployed yesterday.",
        "The issue disappears when a specific environment variable is unset.",
        "Logs show unusual network activity just before the failure.",
        "The problem is reproducible only on the staging server, not local dev.",
        "A specific user action consistently triggers the bug, but not immediately."
    ]

    misdirections = [
        "Initial investigation focused on database connection pooling.",
        "The team spent days optimizing a perfectly fine caching layer.",
        "Attention was diverted by a red herring in the CI/CD pipeline.",
        "A senior developer insisted it was a frontend rendering issue.",
        "The problem was initially blamed on a third-party service outage."
    ]

    scenario = (
        f"**Case File: The {random.choice(symptoms).split(' ')[-2]} Anomaly**\n\n"
        f"**Symptom:** {random.choice(symptoms)}\n"
        f"**Initial Clue:** {random.choice(clues)}\n"
        f"**Beware the Red Herring:** {random.choice(misdirections)}\n\n"
        "**Your Mission:** As the Debugging Detective, resist the urge to jump to conclusions. "
        "Observe, orient, decide, and act. What is your first methodical step to uncover the true root cause?"
    )
    return scenario

# --- MIDI Generation ---
def generate_midi_score(filename="debugging_detective.mid"):
    """Generates a conceptual MIDI score for the debugging scenario."""
    MyMIDI = MIDIFile(4)  # 4 tracks for 4 movements/instrument groups
    tempo = 120  # Initial tempo, will change per movement

    # Define MIDI instruments (General MIDI numbers)
    # https://www.midi.org/specifications-old/item/gm-level-1-sound-set
    PIZZICATO_STRINGS = 45
    BASSOON = 70
    FLUTE = 73
    HARP = 46
    TRUMPET = 56
    SNARE_DRUM = 118 # General MIDI Percussion Map (Note number for Snare)
    FRENCH_HORN = 60
    ACOUSTIC_GRAND_PIANO = 0

    # --- Movement I: The Anomaly (Symptom) ---
    track_anomaly = 0
    channel_anomaly = 0
    time_anomaly = 0
    tempo_anomaly = 65 # Adagio
    MyMIDI.addTrackName(track_anomaly, time_anomaly, "Movement I: The Anomaly")
    MyMIDI.addTempo(track_anomaly, time_anomaly, tempo_anomaly)
    MyMIDI.addProgramChange(track_anomaly, channel_anomaly, time_anomaly, PIZZICATO_STRINGS)

    # Sparse, dissonant motif (example notes)
    notes_anomaly = [60, 63, 61, 58, 60, 62, 59] # C4, Eb4, C#4, Bb3, C4, D4, B3
    durations_anomaly = [0.5, 0.5, 1, 0.5, 0.5, 1, 0.5]
    velocities_anomaly = [60, 65, 60, 55, 60, 65, 55] # mezzo-piano to piano

    for i, note in enumerate(notes_anomaly):
        MyMIDI.addNote(track_anomaly, channel_anomaly, note, time_anomaly, durations_anomaly[i], velocities_anomaly[i])
        time_anomaly += durations_anomaly[i]

    # Low Woodwinds (sustained, unsettling chords)
    track_woodwinds = 1
    channel_woodwinds = 1
    time_woodwinds = 0
    MyMIDI.addTrackName(track_woodwinds, time_woodwinds, "Movement I: Low Woodwinds")
    MyMIDI.addTempo(track_woodwinds, time_woodwinds, tempo_anomaly)
    MyMIDI.addProgramChange(track_woodwinds, channel_woodwinds, time_woodwinds, BASSOON)

    chords_anomaly = [
        [48, 51, 55], # C3, Eb3, G3
        [47, 50, 54], # B2, D3, F#3
        [45, 48, 52]  # A2, C3, E3
    ]
    chord_duration = 2

    for chord in chords_anomaly:
        for note in chord:
            MyMIDI.addNote(track_woodwinds, channel_woodwinds, note, time_woodwinds, chord_duration, 50) # pianissimo
        time_woodwinds += chord_duration

    # --- Movement II: The Initial Clue (Clue) ---
    track_clue = 0 # Reusing track 0 for melody
    channel_clue = 0
    time_clue = max(time_anomaly, time_woodwinds) + 1 # Start after previous movement
    tempo_clue = 85 # Andante
    MyMIDI.addTempo(track_clue, time_clue, tempo_clue)
    MyMIDI.addTrackName(track_clue, time_clue, "Movement II: The Initial Clue")
    MyMIDI.addProgramChange(track_clue, channel_clue, time_clue, FLUTE)

    # Simple, rising, inquisitive motif
    notes_clue = [60, 62, 64, 65, 67, 69] # C4, D4, E4, F4, G4, A4
    durations_clue = [1, 1, 1, 0.5, 0.5, 1]
    velocities_clue = [70, 75, 80, 70, 75, 80] # mezzo-piano to mezzo-forte

    for i, note in enumerate(notes_clue):
        MyMIDI.addNote(track_clue, channel_clue, note, time_clue, durations_clue[i], velocities_clue[i])
        time_clue += durations_clue[i]

    # Harp arpeggios
    track_harp = 1 # Reusing track 1 for accompaniment
    channel_harp = 1
    time_harp = max(time_anomaly, time_woodwinds) + 1
    MyMIDI.addTempo(track_harp, time_harp, tempo_clue)
    MyMIDI.addProgramChange(track_harp, channel_harp, time_harp, HARP)

    arpeggio_notes = [60, 64, 67, 72] # C4, E4, G4, C5
    arpeggio_duration = 0.25
    for _ in range(4): # Repeat arpeggio pattern
        for note in arpeggio_notes:
            MyMIDI.addNote(track_harp, channel_harp, note, time_harp, arpeggio_duration, 60)
            time_harp += arpeggio_duration
        time_harp += 0.5 # Small pause between arpeggio sets

    # --- Movement III: The Red Herring (Misdirection) ---
    track_red_herring = 2
    channel_red_herring = 2
    time_red_herring = max(time_clue, time_harp) + 1
    tempo_red_herring = 125 # Allegro con brio
    MyMIDI.addTempo(track_red_herring, time_red_herring, tempo_red_herring)
    MyMIDI.addTrackName(track_red_herring, time_red_herring, "Movement III: The Red Herring")
    MyMIDI.addProgramChange(track_red_herring, channel_red_herring, time_red_herring, TRUMPET)

    # Chaotic burst, then rapid descent
    notes_burst = [72, 76, 79, 84] # C5, E5, G5, C6
    notes_descent = [84, 83, 82, 81, 80, 79, 78, 77] # C6 down chromatically
    burst_duration = 0.25
    descent_duration = 0.125

    for note in notes_burst:
        MyMIDI.addNote(track_red_herring, channel_red_herring, note, time_red_herring, burst_duration, 100) # fortissimo
        time_red_herring += burst_duration

    for note in notes_descent:
        MyMIDI.addNote(track_red_herring, channel_red_herring, note, time_red_herring, descent_duration, 70)
        time_red_herring += descent_duration

    # Snare drum hit
    MyMIDI.addNote(track_red_herring, 9, SNARE_DRUM, time_red_herring - 0.1, 0.25, 120) # Percussion on channel 9

    # --- Movement IV: The Mission (Call to Action) ---
    track_mission = 3
    channel_mission = 3
    time_mission = time_red_herring + 1
    tempo_mission = 105 # Moderato
    MyMIDI.addTempo(track_mission, time_mission, tempo_mission)
    MyMIDI.addTrackName(track_mission, time_mission, "Movement IV: The Mission")
    MyMIDI.addProgramChange(track_mission, channel_mission, time_mission, FRENCH_HORN)

    # Strong, purposeful melody
    notes_mission = [60, 62, 64, 67, 69, 72] # C4, D4, E4, G4, A4, C5
    durations_mission = [1, 1, 1, 1, 1, 2]
    velocities_mission = [80, 85, 90, 95, 100, 110] # mezzo-forte to forte

    for i, note in enumerate(notes_mission):
        MyMIDI.addNote(track_mission, channel_mission, note, time_mission, durations_mission[i], velocities_mission[i])
        time_mission += durations_mission[i]

    # Piano accompaniment (simple chords)
    track_piano = 0 # Reusing track 0 for accompaniment
    channel_piano = 0
    time_piano = time_red_herring + 1
    MyMIDI.addTempo(track_piano, time_piano, tempo_mission)
    MyMIDI.addProgramChange(track_piano, channel_piano, time_piano, ACOUSTIC_GRAND_PIANO)

    chords_mission = [
        [60, 64, 67], # C major
        [62, 65, 69], # D minor
        [64, 67, 71], # E minor
        [60, 64, 67]  # C major
    ]
    chord_duration_mission = 2

    for chord in chords_mission:
        for note in chord:
            MyMIDI.addNote(track_piano, channel_piano, note, time_piano, chord_duration_mission, 70)
        time_piano += chord_duration_mission

    # Write the MIDI file
    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Debugging Detective: New Case ---")
    scenario_text = generate_debugging_scenario()
    print(scenario_text)
    print("-------------------------------------")

    midi_filename = "debugging_detective.mid"
    generate_midi_score(midi_filename)
    print(f"\nConceptual MIDI score generated: {midi_filename}")
    print("You can play this MIDI file using any MIDI player or DAW.")