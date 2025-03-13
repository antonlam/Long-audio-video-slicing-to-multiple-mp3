import subprocess
import math
import os
import sys
from datetime import datetime, timedelta

ffmpeg = os.path.join(os.getcwd(), "tools", "ffmpeg.exe")
ffplay = os.path.join(os.getcwd(), "tools", "ffplay.exe")
ffprobe = os.path.join(os.getcwd(), "tools", "ffprobe.exe")

def runErrorCheck(cmd):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print('FFmpeg output:', result.stdout)
    except subprocess.CalledProcessError as e:
        print('FFmpeg error:', e.stderr)

def convert_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return float(h * 3600 + m * 60 + s)

def get_audio_duration(file_path):
    try:
        ffprobe_cmd = [ffprobe, '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
        result = subprocess.check_output(ffprobe_cmd).decode('utf-8').strip()
        duration = float(result)
        return duration
    except subprocess.CalledProcessError as e:
        print(f"Error while running ffprobe: {e}")
    except Exception as e:
        print(f"An error occurred: {e}\nCurrent file: {file_path}")
        sys.exit()

def split_audio(input_file, timeslotArray, nameArray):
    duration = get_audio_duration(input_file)
    try:
        for i in range(len(timeslotArray)-1):
            start_time = convert_to_seconds(timeslotArray[i])
            end_time = convert_to_seconds(timeslotArray[i + 1])
            output_file = f"{nameArray[i]}.mp3"
                
            ffmpeg_cmd = [
                ffmpeg, '-i', input_file, '-ss', str(start_time), '-t', str(end_time - start_time), '-c', 'copy', output_file
            ]
            subprocess.run(ffmpeg_cmd)
    except subprocess.CalledProcessError as e:
        print(f"Error while running ffmpeg: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def ifExists(file):
    if os.path.exists(file):
        os.remove(file)
        
def removeAllFile(name):
    input_audio_file = os.path.join(os.getcwd(), f"{name}.mp3")
    muted_file = os.path.join(os.getcwd(), f"{name}.mp4")
    export_audio_file = os.path.join(os.getcwd(),"output.mp3")
    export_file = os.path.join(os.getcwd(),"output.mp4")
    ifExists(input_audio_file)
    ifExists(muted_file)
    ifExists(export_audio_file)
    ifExists(export_file)

if __name__== "__main__":
    timeslotArray = ['0:00:00', '0:04:13','0:10:11','0:19:03']
    nameArray = ['item1','item2','item3']
    fileName = "music"
    input_audio_file = os.path.join(os.getcwd(), f"{fileName}.mp3")
    split_audio(input_audio_file, timeslotArray, nameArray)



