# VoicePowerBI
Voice Powered reporting

Reports can be launched using voice input. Voice-based analytics and business intelligence solution helps enterprises search databases and create reports and charts. Speech recognition is the user interface for this solution. The speech-based commands lookup for queries with predefined database searches with report variables

![alt text](https://github.com/bhagvank/arc/blob/master/speech-icon-2797263_640.png)

# Feature

1.Signup

2.Login

3.Profile

4.Voice Recognition

5.Voice Powered reports

6. Dialog Flow integration

# VoicePowerBI

Voice-based analytics help enterprises to search for data and generate reports. This solution is based on speech recognition. The reports and results can be presented in different formats as per commands. The voice commands are based on natural language and keyword-based queries. The text-based queries are typically different from voice query length. Voice queries may not be questions but more as commands to search and generate results. The speech recognition and processing happen in steps like coding, synthesis, and recognition. The speech-based queries and commands can be connected or isolated words. The speech can be continuous and spontaneous. The speaker models help in identifying person-specific speech patterns. Speaker specific speech models are accurate and precise for voice-based analytics. Diarisation helps in partitioning the speech into homogeneous segments specific to speaker. 


# Instructions 
1. Ensure that mysql is installed, python3 and django

  * [Python3](https://www.python.org/downloads/)

  * [Django](https://docs.djangoproject.com/en/2.0/topics/install/#installing-official-release)

  * [MySql](https://www.mysql.com/downloads/)
  
  
2.git clone this repository
```
git clone https://github.com/bhagvank/voicepowerBI.git

```
   
3. Pipenv install : install the packages required
```
pipenv install
```

4. Pipenv shell : Run the virtual env 
```
pipenv shell
```  
   
5. run locally using settings (update the database username and password)
```
python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py runserver

```

6. Exit the shell
```
exit
```  
