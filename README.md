# Redis Clone: Building a Simple In-Memory Key-Value Store

## Overview
This project is a simplified implementation of Redis, an in-memory data store, built from scratch to understand its internal workings. The clone includes basic features like key-value operations, data persistence, and support for multiple clients.

---

## Features
1. **Persistent Connections**: Clients can maintain open connections for multiple commands.
2. **Basic Commands**:
   - `SET key value`: Stores a key-value pair.
   - `GET key`: Retrieves the value for a given key.
   - `DEL key`: Deletes a key.
3. **Support for Structures**:
   - Strings
   - Lists (`LPUSH`, `RPUSH`, `LPOP`, `RPOP`)
   - Sets (`SADD`, `SMEMBERS`)
   - Hashmaps (`HSET`, `HGET`, `HDEL`)
4. **Protocol Support**: Implements RESP (Redis Serialization Protocol) for communication.
5. **Multithreading/Asynchronous**: Handles multiple clients simultaneously.
6. **Persistence**:
   - Saves data to disk in JSON format.
   - Loads data back into memory at startup.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Basic understanding of socket programming and Python threading or asyncio.

### Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/redis-clone.git
cd redis-clone
```

### Running the Server
To start the server, run:
```bash
python server.py
```

The server will start listening on `localhost:6379`.

### Testing with a Client
You can test the server using tools like `telnet` or `redis-cli`:
```bash
telnet localhost 6379
```

Example commands:
```plaintext
SET mykey myvalue
GET mykey
DEL mykey
```

---

## Project Structure
```
redis-clone/
├── server.py        # Main server logic
├── data_store.py    # In-memory data structures and persistence
├── protocol.py      # Implementation of the RESP protocol
├── README.md        # Documentation
```

---

## Development Plan

The project is structured into the following stages:

### **1. Basic TCP Server**
- Set up a TCP server that handles incoming connections and simple commands.

### **2. Parsing and Executing Commands**
- Implement command parsing and execution for `SET`, `GET`, and `DEL`.

### **3. Supporting Multiple Clients**
- Add multithreading or asyncio for handling multiple connections simultaneously.

### **4. Adding Data Structures**
- Extend support to Lists, Sets, and Hashmaps.

### **5. RESP Protocol**
- Parse and handle Redis Serialization Protocol (RESP) commands.

### **6. Data Persistence**
- Save in-memory data to disk and reload it at startup.

### **7. Advanced Features**
- Implement expiration (`EXPIRE`) and publish/subscribe (`PUB/SUB`).

---

## How to Contribute
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a clear description of changes.

---

## Learning Resources
- [Redis Documentation](https://redis.io/docs/)
- [Redis Serialization Protocol (RESP)](https://redis.io/docs/reference/protocol-spec/)
- [Build Your Own X - Redis](https://github.com/codecrafters-io/build-your-own-x)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
