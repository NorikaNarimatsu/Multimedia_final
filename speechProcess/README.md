# Speech Recognition and Analysis for Group Discussion

## Description:


## Installation:
Requirements:
* `python3`
* `pyannote-audio`

You can install `whisper-timestamped` either by using pip:
```bash
pip3 install git+https://github.com/linto-ai/whisper-timestamped
```

or by cloning this repository and running installation:
```bash
git clone https://github.com/linto-ai/whisper-timestamped
cd whisper-timestamped/
python3 setup.py install
```

## Usage:
### Backend Part
Place the audio file you want to process in the root directory. (Remember the file should be '.wav'. If not, please use `ffmpeg` to transfer.)
To run the program, simply run `python3 speechProcess.py`. The program will first output two UserWarning. The last line would be `  torchaudio.set_audio_backend("soundfile")`. After these finished, input the audio file's name in the command line.
### Example Output
The program will create two .vtt intermediate files that you can ignore. The ultimate output file will be a .txt file, which includes the start time, speaker and content of each sentences in the audio file. Here is an example output file:
```bibtex
[00:00.220] SPEAKER_02: Hi, this is Bill Wale in the Host of Good Fellows. 
[00:02.440] SPEAKER_02: Thanks for listening to the audio version of the show, 
[00:04.480] SPEAKER_02: but we want to let you know that Good Fellows
[00:05.980] SPEAKER_02: is primarily a video production,
[00:08.040] SPEAKER_02: and you're missing a lot of extra features
[00:09.620] SPEAKER_02: by only listening to our show.
```