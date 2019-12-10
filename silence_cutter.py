from scipy.io import wavfile as wav
import numpy as np


def categorize(out_array, in_value):
    if in_value < 0.2:
        out_array["0"] += 1
    elif in_value < 0.4:
        out_array["1"] += 1
    elif in_value < 0.6:
        out_array["2"] += 1
    elif in_value < 0.8:
        out_array["3"] += 1
    else:
        out_array["4"] += 1


samples_rate, samples = wav.read(filename="sample.wav", mmap=True)
samples_max = np.iinfo(samples.dtype).max

array = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0
}

print(array["0"])

print(samples.shape)
size, axis = samples.shape
i = 0
for sample in samples[:, 0]:
    value = abs(sample/samples_max)
    categorize(array, value)
    i += 1
    print(str(int((i/size)*100)) + "%")
#    print(value > 0.5)

print(array)
print(dir(samples))
print(axis)
