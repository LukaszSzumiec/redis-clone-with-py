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
