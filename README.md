# Log-Aggregation
# Socket-Based Log Aggregation System

## Abstract
In modern distributed systems, logs are generated across multiple machines, making monitoring and debugging difficult. This project implements a Socket-Based Log Aggregation System to centralize log data using socket programming.

The system uses a client-server architecture where multiple clients send log messages to a central server using TCP sockets. The server listens for incoming connections, receives log data, and stores it in a file for further analysis.

This approach enables real-time log collection, improves system monitoring, and simplifies debugging. The project demonstrates the use of socket programming for communication between distributed components.

## Team Members
1. Nidhi Mallikarjuna - PES2UG24AM103
2. Riya Harugop - PES2UG24AM136
3. Rhea Nair - PES2UG24AM133
## GitHub Link
https://github.com/riyaharugop/Log-Aggregation
## How to Run

1. Run server:
python server.py

2. Run client:
python client.py
