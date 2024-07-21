from pydub import AudioSegment

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

input_file = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3.mp3"
output_file = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3_speedup2.mp3"

sound = AudioSegment.from_file(input_file)
speeded_up_sound = speed_change(sound, speed=4.0)
speeded_up_sound.export(output_file, format="mp3")
