This is a python program that allow me to slice multiple audio tracks from a audio tracks by time division

step 1. installation requirement: https://www.ffmpeg.org/download.html 
1. ffmpeg.exe
2. ffplay.exe
3. ffprobe.exe
   
![image](https://github.com/user-attachments/assets/5a60b120-7a02-4a99-a3dd-69d8d6683043)

step 2. unzip the file and put all 3 items in the file named "tools"

![image](https://github.com/user-attachments/assets/9e93b737-2bc0-4b7c-920f-528ad0295822)
![image](https://github.com/user-attachments/assets/022b8238-0880-4470-b35b-9996ca2d2bd0)

step 3: rename your designated audio as "music.mp3" and keep it with the same level of the tools file

![image](https://github.com/user-attachments/assets/a5a00525-254e-4daa-8b04-25d6421ea346)

step 4: adjust the timeslotArray and nameArray inside the python program

![image](https://github.com/user-attachments/assets/3dcf0621-efd2-4299-a176-cc26b58b2d2c)

timeslotArray should have an extra end duration about the audio

e.g. 
> nameArray: 3 elements    
> timeslotArray: 4 elements and the last one is the time end of the video
