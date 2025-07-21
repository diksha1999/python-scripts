import subprocess
import json

# Start the server as a subprocess
proc = subprocess.Popen(
    ["python3", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

# Prepare a JSON-RPC request
request = {
    "jsonrpc": "2.0",
    "method": "echo",
    "params": {"text": "Hello, MCP! This is test MCP client"},
    "id": 1
}

# Send the request to the server
proc.stdin.write(json.dumps(request) + "\n")
proc.stdin.flush()

# Read the response from the server
response_line = proc.stdout.readline()
response = json.loads(response_line)
print("Server response:", response)

# Optional: terminate the server process
proc.terminate()
