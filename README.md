# Chat-Application
A simple tool for real-time communication.

This application consists of two main components: the server (`server.py`) and the client (`client.py`). The server handles incoming connections and relays messages between clients, while the client provides an interface for users to connect to the server, send, and receive messages. Inluded is a DOCX report of the lab, written in french (`CEG3585 – Lab1.docx`).

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:
   ```
   git clone https://your-repository-url.git
   ```
2. Navigate to the project directory:
   ```
   cd path-to-your-project
   ```

## Running the Server

To start the server, run the following command in your terminal:

```
python server.py
```

By default, the server listens on `localhost` and port `8080`. You can change these settings by editing the `server.py` file.

## Running the Client

To connect to the server, open a new terminal window and run:

```
python client.py
```

The client will prompt you to enter the server's IP address and port. Use `localhost` and `8080` if you are running the server on the same machine with default settings.

## Features

- **Real-Time Communication**: Send and receive messages instantly with multiple users.
- **Simple User Interface**: Easy-to-use interface for all interactions.
- **Server Settings**: Ability to change server IP and port as needed.
