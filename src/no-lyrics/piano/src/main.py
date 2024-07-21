from pydub import AudioSegment
from mp3lst import PIANO_MP3_LST
import math
import re

def concat_mp3_files(mp3_lst, output_file):
    combined = AudioSegment.empty()
    for mp3_file in mp3_lst:
        audio = AudioSegment.from_mp3(mp3_file)
        combined += audio
    combined.export(output_file, format='mp3')

mp3_files = []
input_file = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3.txt"
output_file = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3.mp3"

f = open(input_file, "r")
lines = f.readlines()
for line in lines:
    do_line = line.replace("[", "")
    do_line = do_line.replace("]", "")
    do_line = re.sub("\s+", " ", do_line)
    rgb = list(filter(None, do_line.split(" ")))
    average = (int(rgb[0]) + int(rgb[1]) + int(rgb[2]))/3
    index = math.floor(average % 89)
    mp3_files.append("E:/thac-si-cntt-TLU/final-project/img2music/src/no-lyrics/piano/asset/mp3/" + PIANO_MP3_LST[index])

concat_mp3_files(mp3_files, output_file)
