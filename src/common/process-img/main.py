import os

path = "E:/thac-si-cntt-TLU/final-project/img2music/src/no-lyrics/piano/asset/mp3"
dir_list = os.listdir(path)

out_file_path = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/piano.txt"
f = open(out_file_path, "a")
for i in dir_list:
    f.write("@E:/thac-si-cntt-TLU/final-project/img2music/src/no-lyrics/piano/asset/mp3/" + str(i) + "@")
    f.write('\n')
f.close()