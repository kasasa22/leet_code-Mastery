import numpy as np
import librosa
import matplotlib.pyplot as plt

# Load the audio file
audio_path = r'C:\Users\x1carbon\Desktop\music\song.mp3'
y, sr = librosa.load(audio_path, sr=None)

# Plot the original sound waveform
plt.figure(figsize=(14, 5))
plt.plot(y, label='Original Waveform')
plt.title('Original Sound Waveform')
plt.legend()
plt.show()

# Sort the waveform
sorted_y = np.sort(y)

# Plot the sorted sound waveform
plt.figure(figsize=(14, 5))
plt.plot(sorted_y, label='Sorted Waveform')
plt.title('Sorted Sound Waveform')
plt.legend()
plt.show()
