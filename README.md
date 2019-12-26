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

Monte Carlo is a family of numerical simulation technique extensively used in statistical physics and mathematical finance. It has historically proven records of being one of the most reliable technique addressing vital problems in industry and academics. A Monte Carlo simulation predicts the outcome of functions which are inherently indeterministic. A system simulated with MC performs a random walk within all possible states it can evolve. An ensemble average determined from all the states gives an estimate of the mathematical quantity of interest. 
# Natural Algorithm
Now let's quickly peep in the general procedure for an MC simulation. A natural algorithm is executed n times to generate n number of random samples. The probability of finding the average value of a state variable within a specified range of tolerance scales directly with the square of variance and inversely with the square of tolerance and number of samples. The value of n is kept sufficiently large enough to obtain a probability above 99%. 
The algorithm is computationally expensive because of the quadratic dependence of probability on the number of trials O(N2). The fact has severely limited it's application to small-scale systems with few data sets. Recently researchers have come across ways to speed up the MC simulation with the use of quantum algorithms. Quantum algorithms are analogous to classical algorithms expect that their design is to find implementation on a quantum architecture. It poses several advantages over its classical counterpart, imparting enhanced speed and realistic randomness. Quantum walks are a quantum analogue to random walks and have substantially reduced the time-consumption in MC simulations for mixing of Markov chains as reported by Ashley Montanaro(2015). Several algorithms are developed so far to encompass the need to accelerate the classical deterministic and randomised algorithms with rigorous performance bounds — the error rates of outcome benchmark the effectiveness of these algorithms. 
The line of research on performing quantum integration algorithms started from Abrams and Williams (1999), who established the foregrounds which finally helped in the development of parallel computation of high dimensional integrals by Heinrich et al. (2001). 
The measurement on an n qubit system with all the qubits initialised to state |0>...|0> operated by a Walsh-Hadamard transform gives a random outcome |i> with probability 2-n. Thus, a quantum computer implements Monte Carlo with real physical randomness. Now lets define a quantum query given by a unitary map

Qf: |i>|y>→|i>|y + f(i)> (0 ≤ i < 2n-1)

If we set the last qubit as zero, then Qf acts as a subroutine which will update the last entry with function output. In an MC simulation, the f(i) can be the integration function.
A practical implementation of some of these algorithms on a hypothetical quantum computer and its betterment is the original motto of this project. We specifically focus on MC pricing of financial derivatives and how the arrangement of probability distributions can leverage the advantages of quantum superposition and thus accelerate the simulation. The prices of derivatives are extracted through quantum measurements with high confidence. We expect a quadratic speed up as reported in recent literature (Patrick Rebentrost, (2018)). 

After the financial crisis of 2008-2009, it's essential for the government and banks to estimate the risk exposure of the financial institutions. Such risks follow the nomenclature XVA where X stands for the type of risk associated and VA for value adjustment.  Different MC simulations performed overnight assesses the risk under different scenarios. Reducing the time-consumption of these overnight calculations facilitates the institutions to take actions following the changing market conditionsVoice-based analytics help enterprises to search for data and generate reports. This solution is based on speech recognition. The reports and results can be presented in different formats as per commands. The voice commands are based on natural language and keyword-based queries. The text-based queries are typically different from voice query length. Voice queries may not be questions but more as commands to search and generate results. The speech recognition and processing happen in steps like coding, synthesis, and recognition. The speech-based queries and commands can be connected or isolated words. The speech can be continuous and spontaneous. The speaker models help in identifying person-specific speech patterns. Speaker specific speech models are accurate and precise for voice-based analytics. Diarisation helps in partitioning the speech into homogeneous segments specific to speaker. 


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
