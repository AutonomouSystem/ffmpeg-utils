@echo off

:: TO-DO: handle transitions 
rem (echo file '1.mp4' & echo file '2.mp4' )>list.txt
rem ffmpeg -safe 0 -f concat -i list.txt -c copy output.mp4

:: Create File List
for %%i in (*.mp4) do echo file '%%i'>> mylist.txt

:: Concatenate Files
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4

:: handle transitions between .mp4s
:: https://romander.github.io/ffmpeg-script-generator/
:: ffmpeg -vsync 0 -c:v h264_cuvid -i 1.mp4 -i 2.mp4 -filter_complex "[0]settb=AVTB[0:v]; [1]settb=AVTB[1:v]; [0]aresample=async=1:first_pts=0,apad,atrim=0:271[0:a]; [1]aresample=async=1:first_pts=0,apad,atrim=0:177[1:a]; [0:v][1:v]xfade=transition=fade:duration=0.1:offset=270.9,format=yuv420p[video]; [0:a][1:a]acrossfade=d=0.1:c1=tri:c2=tri[audio]" -c:v h264_nvenc -map "[audio]" -ar 48000 -b:a 96k -map "[video]" -rc vbr -cq 30 -qmin 30 -qmax 30 out.mp4

echo "Jobs Done!"
:: cleanup
del mylist.txt
pause
