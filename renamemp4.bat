@echo off
:: renames .mp4s in directory giving them numbers 1.mp4, 2.mp4, 3.mp4 
etc.
:: rencode different mp4 types to match

setlocal EnableDelayedExpansion

set counter=1

for %%f in (*.mp4) do (
    ffmpeg -i "%%f" -c:v libx265 -crf 17 -preset slower -c:a aac -b:a 128k -ar 48000 -s 1920x1080 -r 120 -pix_fmt yuv420p -f mp4 -y "!counter!.mp4"
    set /a counter+=1
)

echo "Jobs Done!"
pause
endlocal