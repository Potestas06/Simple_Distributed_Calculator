# Simple_Distributed_Calculator

## Table of contents

- Start
- Project file structure
- Components

## Start

### Installations

For running the Program it's necessary to install websockets

Command

```
pip install websockets
```

### Start batch file

To start the calculator follow these steps:

1. If you haven't already download Windows Terminal and go in the project folder.
2. Install Websockets like mentioned above.
3. Execute the start.bat file. <br>
   Like this: <br>
    ```
    ./start.bat
    ```
   You should see multiple new tabs open in your Terminal window. These are the different Programs. They are also
   labeled on the top in the title.
4. open the index.html and enjoy you calculator.

## Project file structure

### frontend

The Frontend is held simple with only 3 Files html, css, and js.

Structure:

```
index.html
script.js
style.css
```

### backend

The backend folder and file structure is more complex and consists of 8 Python scripts and one log file.

Structure:

```
spooler.py
netNode.py
logger.py
logs --------
     logfile.log
calc --------
     calc1.py
     calc2.py
     calc3.py
     calc4.py
     calc5.py
```

note: The logfile.log is auto generated and won't be there at the start.

## Components

Due to the clear function of the index.html and style.css only the javascript will be described separately.

### Calculators

The Calculators all have the same and very simple Task. They are receiving a calculation in json format from the
spooler. Then they will try to solve it.

#### Handling (outputs):

Calculation

```
SUCCESS:
{solution}
ERRORS:
- Invalid input
- Error: + {error}
```

Connection

```
1. Received message: {message} ----> One or more message/s have been received.
2. Sent reply: {reply} ----> The solution of the calculator got sent back.
3. Connection closed ----> Websocket closed.
```

### logger

The logger has the task to log calculations and their solution in the log file.
It logs the Time and Date when the calculation was made, the calculation itself, the answer to it, and if the two
calculator that calculate with it received the same answer.

#### Handling (outputs):

Logs

```
Format:
[{DateTime}] {"work":"{Calculation}"}{"result": "{result}"}{"checksum": true}
Example:
[2023-05-17 14:24:53] {"work":"7+7"}{"result": "14"}{"checksum": true}
```

Connection

```
1. Received message: {message} ----> One or more message/s have been received.
2. Received response: {response} ----> One or more message/s have been received.
3. Received checksum: {checksum} ----> One or more message/s have been received.
4. sent: {reply}
```

### netNode

NetNode is the intermediate piece of the client and the system.
NotNode Accepts the invoices and sends them to the spooler and also sends back the response given by the system.

#### Handling (outputs):

redirect

```
Sent: {message}
Result: {response}
```

Connection

```
1. Received message: {message}
2. Sent reply: {reply}
```

### Spooler

The spooler is responsible for receiving calculations in JSON format, forwarding them to the calculators, and returning
their solutions.

#### Handling (outputs):

```
Logger:
Sent "{message}" to logger
SUCCESS:
- Logged: {message}
ERRORS:
- Failed to log: {message}

Traffic
SUCCESS:
- {solution}
ERRORS:
- Invalid input
- Error: + {error}

Connection
- Received message: {message} ----> One or more message(s) have been received.
- Result: {response} -- sent back response
- Sent: {message} -- sent back message
- Sent reply: {reply} -- sent reply
- Connection closed ----> Websocket closed.
```

### calculator

This script sets up a WebSocket connection to a server running on localhost at port 8000. It handles the functionality
of a basic calculator interface on a web page. The script listens for button clicks on the calculator keys and performs
the corresponding actions such as clearing the display, evaluating the equation, appending operators and operands, etc.
When the equal button is clicked, the equation is sent to the server via the WebSocket connection for evaluation. The
server's response is then displayed on the calculator's display. Additionally, the script includes a theme switch
functionality that toggles between a dark and light theme based on user input. If the WebSocket connection is closed, a
message indicating the lost connection is displayed on the calculator's display.