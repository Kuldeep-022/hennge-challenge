# HENNGE Admission Challenge

This repository contains my solution for the HENNGE Admission Challenge.

## Files

- `main.py` - Main entry point (if used).
- `send_request.py` - Script to generate TOTP and send the challenge request.
- `generate_totp.py` - Function to generate TOTP (Time-based One-Time Password).
- `mission3.json` - JSON file containing submission data.

## How to Run

1. **Install requirements** (if any):
    ```sh
    pip install requests
    ```

2. **Run the solution**:
    ```sh
    python send_request.py
    ```

## Solution Details

- Generates a TOTP using your email and a fixed string.
- Encodes the credentials in Base64.
- Reads the submission data from `mission3.json`.
- Sends a POST request to HENNGE's endpoint.
- Prints the response containing the challenge result.

## Example Output

```
Generated TOTP: 0135730987
Base64 Auth: a3V...==
Headers: {'Content-Type': 'application/json', ...}
JSON Data: {...}
Status Code: 200
Response: {"message": "Congratulations! You have achieved mission 3"}
```

## Contact

- Author: Kuldeep-022
