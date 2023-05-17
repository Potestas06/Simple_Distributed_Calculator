timeout /t 5 /nobreak
cd backend
set "current_path=%CD%"
wt -w 0 nt -d "%current_path%" -p "Command Prompt" --title netMode cmd /k python netNode.py
wt -w 0 nt -d "%current_path%" -p "Command Prompt" --title spooler cmd /k python spooler.py
wt -w 0 nt -d "%current_path%" -p "Command Prompt" --title logger cmd /k python logger.py

set "current_path=%CD%\calc"
for /L %%i in (1,1,5) do (
  wt -w 0 nt -d "%current_path%" -p "Command Prompt" --title calc%%i cmd /k python calc%%i.py
)
