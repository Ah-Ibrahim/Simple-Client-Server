# Python Socket Server-Client Communication

This project implements a simple client-server communication system using Python sockets. The client sends a randomly generated string to the server, and the server processes the string based on a specified prefix before sending back a response.

## Features

- Uses TCP sockets for communication.
- The client generates and sends a random string with a prefix.
- The server processes the message and returns a response based on the prefix:
  - **"A"**: Sorts the string in descending order.
  - **"C"**: Sorts the string in ascending order.
  - **"D"**: Converts the string to uppercase.
  - Any other prefix returns an error message.
- Uses `colorama` for colored console output.

## Installation

1. Clone this repository or download the files.
2. Install the required dependencies:
   ```sh
   pip install colorama
   ```

## Usage

1. **Run the server**:

   ```sh
   python server.py
   ```

   The server starts listening on `localhost:9999`.

2. **Run the client**:
   ```sh
   python client.py
   ```
   The client generates a random string prefixed with `"C"` and sends it to the server. The server processes the string and returns the sorted result.

## File Structure

- `server.py`: Handles client connections and processes messages.
- `client.py`: Connects to the server and sends a message.

## Requirements

- Python 3.x
- `colorama` library

## Author

Developed by Ahmed Ibrahim. Contributions and feedback are welcome!
