@echo off
:: fade out total time, fade out last part
:: st=22: Sets the start time of the fade out to 22 seconds. Adjust this value based on when you want the fade out to begin.
:: d=3: Sets the duration of the fade out to 3 seconds. Adjust this value to control how long the fade out lasts.
:: ffmpeg -i final.mp4 -af "afade=t=out:st=70:d=14" -c:v copy final_fade.mp4

:: ffmpeg -i final.mp4 -af "afade=t=out:st=25:d=9:curve=exp" -c:v copy final_fade.mp4
ffmpeg -i final.mp4 -af "afade=t=out:st=25:d=9:curve=tri" -c:v copy final_fade.mp4
:: ffmpeg -i final.mp4 -af "afade=t=out:st=70:d=14:curve=log" -c:v copy final_fade.mp4
