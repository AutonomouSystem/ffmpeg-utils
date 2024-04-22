@echo off

:: set input files
set video=upscale.mp4
set audio=combined.mp3

:: set output file
set output=final.mp4

:: volume levels (range from 0 to 1)
set video_volume=1
set audio_volume=0.20

:: combine video and audio
ffmpeg -i "%video%" -i "%audio%" -c:v copy -filter_complex "[0:a]volume=%video_volume%[v_audio];[1:a]volume=%audio_volume%[m_audio];[v_audio][m_audio]amix=inputs=2[aout]" -map 0:v -map "[aout]" -c:a aac -shortest "%output%"

:: pause to show output
pause
