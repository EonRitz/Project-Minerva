# Project Minerva

Project Minerva is an artificial intelligence (AI) assistant designed to perform various tasks and provide assistance to the user. It is coded in Python and makes use of several libraries and packages to enable functionalities like speech recognition, text-to-speech, email sending, web browsing, system control, and more.

Here's a detailed breakdown of the key components and functionalities of Project Minerva:

1. **Voice Engine Setup:**
   - Project Minerva uses the `pyttsx3` library to handle text-to-speech synthesis. It initializes the engine, selects a voice, and sets it up to speak with the desired voice.

2. **Main Functions:**
   - The AI assistant provides various functions, including:
     - Telling the current time and date.
     - Greeting the user based on the time of the day (morning, afternoon, evening, night).
     - Recognizing and processing voice commands.
     - Sending emails.
     - Opening web pages in the Chrome browser.
     - Controlling the system (log out, shut down, restart).
     - Playing music.
     - Remembering user-inputted information.
     - Providing jokes.
     - Fetching weather information for a specified city.

3. **Voice Recognition:**
   - Speech recognition is achieved using the `speech_recognition` library, which listens for user commands and converts them into text.

4. **Text Analysis:**
   - The AI assistant uses the `wikipedia` library to perform searches on Wikipedia and summarize the results.

5. **Email Functionality:**
   - It has the capability to send emails through a specified SMTP server. Users can dictate the email content, and the assistant sends the email.

6. **Web Browsing:**
   - Users can command the assistant to open websites in Google Chrome. It does this using the `webbrowser` library.

7. **System Control:**
   - The assistant can perform system actions like logging out, shutting down, and restarting the computer. It uses the `os` library to execute these actions.

8. **Media Playback:**
   - Users can ask the assistant to play songs, and it opens the default media player for this task.

9. **Data Storage:**
   - The AI assistant can store and retrieve user-inputted information, allowing users to ask if it remembers certain details.

10. **System Monitoring:**
    - The assistant can check the CPU usage and battery percentage using the `psutil` library.

11. **Humor:**
    - The assistant can tell jokes using the `pyjokes` library.

12. **Weather Information:**
    - It fetches weather information for a specified city from the "wttr.in" website and provides the user with the weather report.

13. **User Interaction:**
    - The assistant interacts with the user through voice and text-to-speech, making it suitable for voice commands and responses.

14. **Initialization and Continuous Interaction:**
    - The assistant is initialized with a greeting and continuously listens for user commands, interacting with the user based on the voice commands it receives.

15. **Error Handling:**
    - The code includes basic error handling to deal with exceptions that might occur during execution.

Project Minerva is designed to serve as a voice-controlled AI assistant capable of performing a range of tasks, from providing information to controlling the computer. It can be extended and customized with additional functionalities based on the user's needs and preferences.
