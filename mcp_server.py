import sys
import json

def handle_request(request):
    # Parse the JSON-RPC request
    method = request.get("method")
    params = request.get("params", {})
    req_id = request.get("id")

    # For demo: just echo back the text sent
    if method == "echo":
        result = {"echo": params.get("text", "")}
    else:
        result = {"error": "Unknown method"}

    # Build JSON-RPC response
    response = {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": result
    }
    return response

if __name__ == "__main__":
    for line in sys.stdin:
        request = json.loads(line)
        response = handle_request(request)
        print(json.dumps(response), flush=True)
