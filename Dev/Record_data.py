import pylsl
import datetime
import csv

from pylsl import StreamInlet, resolve_stream

prev_time = 0
classification_segment = []

streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])



while True:
    sample, timestamp = inlet.pull_sample()
    # timestamp transformed into seconds
    current_time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    # print(current_time, sample)
    if current_time == prev_time:
        classification_segment.append(sample)
    else:
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(classification_segment)
        classification_segment = []
        prev_time = current_time

