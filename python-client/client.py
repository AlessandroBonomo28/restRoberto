import requests

# Configuration
URL = "http://localhost:8087/audio"
PARAMS = {
    "token": "token1",
    "text": "Ciao, sono Roberto. Attenzione! allontanarsi dalla linea gialla!"
}
FILENAME = "output.wav"

def download_audio():
    print(f"--> Request in progress...")
    try:
        # Perform the GET request
        response = requests.get(URL, params=PARAMS, timeout=30)
        
        # Accept both 200 and 202, since the server responds with these codes
        if response.status_code in [200, 202]:
            print(f"--> Received {len(response.content)} bytes. Saving to {FILENAME}...")
            
            # Write the binary content to the file
            with open(FILENAME, "wb") as f:
                f.write(response.content)
            
            print(f"--> DONE! You can now open the {FILENAME} file.")
        else:
            print(f"Server error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    download_audio()