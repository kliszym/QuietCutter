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


def replace_max1(out_maxim, new_max, new_index):
    out_maxim["max1"] = new_max
    out_maxim["index1"] = new_index


def replace_max2(out_maxim, new_max, new_index):
    out_maxim["max2"] = new_max
    out_maxim["index2"] = new_index


def find_highest_index(in_array):
    maxim = {
        "max1": 0,
        "index1": 0,
        "max2": 0,
        "index2": 0
    }

    for max_iterator in range(5):
        if in_array[str(max_iterator)] > maxim["max1"]:
            replace_max2(maxim, maxim["max1"], maxim["index1"])
            replace_max1(maxim, in_array[str(max_iterator)], max_iterator)
        elif in_array[str(max_iterator)] > maxim["max2"]:
            replace_max2(maxim, in_array[str(max_iterator)], max_iterator)

    if maxim["index2"] > 1:
        if maxim["index1"] < maxim["index2"]:
            return maxim["index1"]
    return maxim["index2"]


samples_rate, samples = wav.read(filename="sample_small.wav", mmap=True)
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

print(array)
print(dir(samples))
print(axis)
