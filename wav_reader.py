import matplotlib.pyplot as plot
import numpy as np
import wave


def print_plot(data, frame_rate_in):
    record_time = np.linspace(0, len(data) / frame_rate_in, num=len(data))

    plot.figure(1)
    plot.title("Signal Wave...")
    plot.plot(record_time, data)
    plot.show()


def read_wave_file(name):
    with wave.open(name, "rb") as file_in:
        file_in_content = file_in.readframes(1024 * 1024)
        content = np.fromstring(file_in_content, "Int16")
        f_rate = file_in.getframerate()
        n_channels = file_in.getnchannels()
        s_width = file_in.getsampwidth()
    return content, f_rate, n_channels, s_width


def write_wave_file(name, content, f_rate, n_channels, s_width):
    with wave.open(name, "wb") as file_out:
        file_out.setnchannels(n_channels)
        file_out.setsampwidth(s_width)
        file_out.setframerate(f_rate)
        file_out.writeframes(content)


def cut_noises(content_in):
    content_out = []
    for sample in content_in:
        if 0 < abs(sample) < 3000:
            content_out.append(sample)
    content_out = np.array(content_out)
    return content_out


data_in, FRAME_RATE, CHANNELS, SAMPLE_WIDTH = read_wave_file("sample.wav")
data_out = cut_noises(data_in)
write_wave_file("output.wav", data_out, FRAME_RATE, CHANNELS, SAMPLE_WIDTH)
print_plot(data_out, FRAME_RATE)
