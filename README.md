# img2music is a Python tool convert image to music
# Current Status (Jul 2024): Convert image to Piano song
## Require Libs
1. Pydub
```
   pip install pydub
```
2. ffmpeg

   Install Windows
   - Download ffmpeg https://www.ffmpeg.org/download.html
   - Extract to a folder, for example C:/ffmpeg
   - Open Environment Variables and add C:/ffmpeg/bin to PATH
   - Check again by using command
     ```
     ffmpeg -version
     ```

## Using
1. Convert image to pixels
   - Go to folder **src/common/process-img**
   - Execute **pixel-converter.py** to convert an image to pixels, store in a txt file
   - Go to folder **src/no-lyrics/piano/src**
   - Execute **main.py** to convert pixels file to mp3
   - [Options] Speed up mp3 file by using **speed-up.py**
