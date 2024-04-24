@echo off
:: combines clips into one single video
:: TO-DO: handle transitions 
rem (echo file '1.mp4' & echo file '2.mp4' )>list.txt
rem ffmpeg -safe 0 -f concat -i list.txt -c copy output.mp4

:: create File List

setlocal EnableDelayedExpansion

:: Create File List with durations
set counter=0
(
    for %%f in (*.mp4) do (
        ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "%%f" > dur.txt
        set /p dur=<dur.txt
        echo file '%%f'
        echo duration !dur!
        del dur.txt
        set /a counter+=1
    )
) > mylist.txt

:: Concatenate Files
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4

echo "Jobs Done!"
del mylist.txt
pause
endlocal