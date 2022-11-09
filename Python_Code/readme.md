## How to use

```
# First, install pdm, it's a modern Python package and dependency manager, like npm
# https://pdm.fming.dev/latest/#recommended-installation-method

# change working directory to Python_Code, where the pyproject.toml file is and run this command to install all dependencies
pdm install

# with these commands you can start different programms
pdm run python3 main.py # starts all componends combined in two threads to serve the frontend with the image and to recognize people on the cam
pdm run python3 Recognizer.py # just recognizes people on the people.png
pdm run python3 MqttSender.py # sends test string to mqtt broker

```


## Class Diagram

```mermaid
classDiagram
	class MqttSender
	class Logger
	class Recognizer
	class HttpStreamer
```