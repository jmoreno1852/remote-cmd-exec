# Remote Code Execution (RCE) in Python

This project demonstrates a **Remote Code Execution (RCE) server** implemented in Python, allowing a client to send and execute commands on a remote machine. The execution results are then sent back to the client over a TCP socket.

🚨 **Security Warning:** This project is for educational purposes only. Running an RCE server without proper security measures can expose the system to critical vulnerabilities, including unauthorized access and command injection.

## Features

- **Remote command execution:** Clients can send shell commands to be executed on the remote machine.
- **Socket-based communication:** Uses Python's `socket` module to establish a TCP connection.
- **Simple two-way communication:** The client sends a command, and the server responds with the output.
- **Lightweight implementation:** Minimal dependencies, works on any system with Python installed.

## Security Concerns

⚠️ **WARNING: Running an unrestricted RCE server can lead to complete system compromise.**  
- The current implementation does **not** include authentication or input validation.
- Any connected client can execute arbitrary commands.
- A malicious user could run destructive commands like `rm -rf /` or `shutdown -h now`.
- **DO NOT expose this server on public networks without adding security measures** like authentication, input sanitization, and command whitelisting.

## Reference

This project is based on an article by **Yash Salvi**, available at:  
🔗 [Execute Commands Remotely on Machine Using Python](https://medium.com/@yash.salvi/execute-commands-remotely-on-machine-using-python-efc865697122)

## File Structure
```plaintext
📁 remote-cmd-exec/
│── 📁 src/
│   │── server.py   # Contains the main server logic
│   │── client.py   # Contains the client logic
│── main.py         # Listens for incoming connections and executes commands
│── requirements.txt
│── README.md       # Project documentation
```
