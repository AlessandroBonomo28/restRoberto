# restRoberto
[![Go Report Card](https://goreportcard.com/badge/github.com/TheTipo01/restRoberto)](https://goreportcard.com/report/github.com/TheTipo01/restRoberto)

restRoberto - Simple HTTP API that generates audio file with the (not so) famous Roberto voice.

## Endpoints

### GET `/audio`

Generates audio from the provided text and replies with status code 202 and the audio as raw PCM.

Query parameters:

- `token`: the authorization token
- `text`: the text used to generate the audio
- `voice`: the voice to use (Roberto or Paola). Default is Roberto.

Example query: `GET https://rest.roberto.site/audio?token=valid_token&text=nyanpasu`

# Docker
There's now a working image deployed. Take a look [here](https://github.com/TheTipo01/restRoberto/pkgs/container/restRoberto) for the image

### Docker Compose
To run restRoberto with Docker Compose, first copy `example_config.yml` to `config.yml` and edit it with your tokens, then run:

```
docker compose up -d
```
# Clients

### Rust
A synchronous client using ureq is available in the repository under `rust-client` folder.
### Python 
Use the python client under the `python-client` folder to perform a GET request and save the response content to an output.wav file. It requires request library. 

```
pip install requests
```
### curl
```
curl -o output.wav "http://localhost:8087/audio?token=your_token&text=ciao"
```