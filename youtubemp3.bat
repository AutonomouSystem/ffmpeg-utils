@echo off
:: use yt-dlp to download YouTube links into .mp3
:: recommend use chocolatey on Windows e.g. choco install yt-dlp
rem yt-dlp mp3 from link or playlist
rem TO-DO add playlist support 

set /p type=Enter 1 for single video or 2 for playlist:
set /p link=Enter link:

if "%type%" == "1" (
  yt-dlp -x --audio-format mp3 --audio-quality 0 -o "1.mp3" "%link%"
) else if "%type%" == "2" (
  yt-dlp -x --audio-format mp3 --audio-quality 0 -o "1.mp3" "%link%"
) else (
  echo Invalid option. Please enter 1 or 2.
)

pause
