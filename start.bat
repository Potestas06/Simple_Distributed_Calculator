cd backend
start cmd /k python netNode.py
start cmd /k python spooler.py
start cmd /k python logger.py

cd calc
for /L %%i in (1,1,5) do start cmd /k python calc%%i.py
