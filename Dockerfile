FROM python:3.10.11
WORKDIR /app

COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
# Install required system packages
RUN apt-get update && apt-get install -y espeak libespeak-dev alsa-utils portaudio19-dev
RUN pip install pipwin
RUN pipwin install pyaudio
# Install additional audio-related packages
RUN apt-get install -y alsa-utils


# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run script.py when the container launches
CMD ["python", "minerva.py"]