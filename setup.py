import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="cTTS",
    version="0.0.2",
    author="Thorsten Müller",
    author_email="tm@thorsten-voice.de",
    packages=["cTTS"],
    description="Python module for using a Coqui TTS server",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/thorstenMueller/cTTS",
    license='Mozilla Public License Version 2.0',
    python_requires='>=3.4',
    install_requires=[
        "setuptools>=42",
        "wheel",
        "response"
]
)