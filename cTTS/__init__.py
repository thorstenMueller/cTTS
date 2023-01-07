import requests
import json
import logging

__version__ = '0.0.2'

# This module will not do any text cleaning (numbers, dates, ...)!

# Ideas for following versions:
# =============================
# Adding a function returning raw audio data instead saving to disk directly
# Adding librosa to offer functions for
# - getting samplerate
# - getting audio length

VALID_END_OF_PHRASE = ['.',';','!','?']

def prepareText(text,addStopChar):
    """Add a dot at the end of text if no valid end of phrase character is found.
    This will avoid "MAX_DECODER_STEP" error and generation of weird voice output.

    Args:
        text (string): Text to be checked for valid end of phrase char.
        addStopChar (boolean): Should line ending be checked.

    Returns:
        string: String with valid end of phrase character (.)
    """
    if addStopChar and text[-1] not in VALID_END_OF_PHRASE:
        text = text + "."
    return text

def synthesizeToFile(filename, text, url="http://localhost:5002", addStopChar=True):
    """Synthesize a text (no additional text cleaning!) using a Coqui TTS server.

    Args:
        filename (string): Path, filename and .wav extension where synthesized voice will be saved. 
        text (string): Text to be synthesized.
        url (string): URL of Coqui TTS server (default: http://localhost:5002)
        addStopChar (boolean): If true a dot will be added as last char if
            last char is not a common line ending character to avoid
            max_decoder_steps error. Defaults to true.

    Returns:
        boolean: "True" if audio could be retrieved from Coqui TTS server api. Otherwise "False"
    """
    if len(text) == 0:
        logging.error("No text has been specified.")
        return False

    try:
        req = requests.get(url + "/api/tts", params={'text': prepareText(text, addStopChar)})
    except Exception as e:
        logging.error("Error calling Coqui TTS server api")
        print(e)
        return False
    
    if req.status_code == 200 and req.headers['Content-Type'] == 'audio/wav':
        logging.info("Valid audio has been returned from Coqui TTS api.")
        #logging.info("Length of content {} bytes.", req.headers['Content-Length'])
        #logging.info("Request took {} microseconds.", req.elapsed)
        with open(filename, 'wb') as f:
            f.write(req.content)
        return True
    else:
        logging.warn("No audio has been returned from Coqui TTS server api")

    return False
