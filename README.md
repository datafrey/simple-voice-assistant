# Simple voice assistant

A simple voice assistant created with Python. The linux system was used so it have to be a little modified for running in Windows or Mac. Determines the type of user request by keyword/keyphrase (the command is triggered when a keyword or keyphrase sounds).

Assistant can:

- speak the current time (keyword: *time*);
- speak the current date (keyword: *date*);
- make Wikipedia requests (keyword: *wikipedia*);
- send emails (keyword: *email*);
- search something in browser (keyword: *browser*);
- play music (keyword: *music*);
- save some info to a file (keyword: *remember*) and read it (keyphrase: *what do you know*);
- make a screenshot (keyword: *screenshot*);
- check the current CPU usage (keyword: *cpu*);
- check how much battery is left (keyword: *battery*);
- shutdown/restart/logout from the system (keywords: *shutdown*/*restart*/*logout*);
- joke (keyword: *joke*).

The list of used Python libraries:

1. **gtts** - can be installed using pip;
2. **speechrecognition** - can be installed using pip/conda;
3. **wikipedia** - can be installed using pip/conda;
4. **pyautogui** - can be installed using pip/conda;
5. **psutil** - can be installed using pip/conda;
6. **pyjokes** - can be installed using pip/conda;
7. **pyaudio** - can be installed using pip/conda;

You may also need to install **mpg123**, **espeak** and **scrot** packages if run it in linux.
