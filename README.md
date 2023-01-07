![Maintaner](https://img.shields.io/badge/maintainer-Thorsten_Mueller-blue)
<a href="https://twitter.com/intent/follow?screen_name=ThorstenVoice">
        <img src="https://img.shields.io/twitter/follow/ThorstenVoice?style=social&logo=twitter"
            alt="follow on Twitter"></a>
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

# cTTS
A super simple Python module for synthesizing voice using a Coqui TTS server.

## Requirements
Access to a running Coqui TTS server with a loaded model is required (eg: http://localhost:5002).

## How to use
First install module with `pip install cTTS`.

Run a simple Python code like this:
```python
import cTTS

cTTS.synthesizeToFile("output.wav", "This is a test.")
```

 Short video on how to use it: [Watch me](https://www.youtube.com/watch?v=hRoPIKRkERw)

### Arguments
* filename: Path, filename, .wav suffix of output file with synthesized voice.
* text: Text to be synthesized.
* url (optional): Protocol, server name/ip and port of Coqui TTS server (default: http://localhost:5002)
* addStopChar (optional): If "text" doesn't end with a dot, question or exclamation mark a dot is added as last character to avoid MAX_DECODER_STEPS issue (default: True). 

## Thanks
Thanks to all open voice communities for their effort for open voice and to the creator of gTTS package for name inspiration :-).
