import matplotlib.pyplot as plot
import numpy as np
import wave

QUIET_TIME = 0.2
INTERRUPTION_TIME = 0


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


def cut_noises(content_in, quiet_const):
    content_out = []
    content_part = []
    quiet_actual = 0
    for sample in content_in:
        content_part.append(sample)
        if 300 < abs(sample) < 3000:
            if quiet_actual > quiet_const:
                content_part.clear()
            quiet_actual = 0
            content_part.append(sample)
            content_out += content_part
            content_part.clear()
        else:
            quiet_actual += 1
    content_out = np.array(content_out)
    return content_out


data_in, FRAME_RATE, CHANNELS, SAMPLE_WIDTH = read_wave_file("sample.wav")
QUIET_SAMPLES = QUIET_TIME * FRAME_RATE
print("FRAME RATE: " + str(FRAME_RATE))
print("SAMPLES LENGTH: " + str(QUIET_SAMPLES))

data_out = cut_noises(data_in, QUIET_SAMPLES)
write_wave_file("output.wav", data_out, FRAME_RATE, CHANNELS, SAMPLE_WIDTH)
print_plot(data_out, FRAME_RATE)
