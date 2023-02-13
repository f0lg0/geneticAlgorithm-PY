# geneticAlgorithm-1
Application of a Genetic Algorithm to the "Infinite monkey theorem"

## Description
### What is the Genetic Algorithm?
According to the MathWorks website (https://www.mathworks.com/help/gads/what-is-the-genetic-algorithm.html),
<pre> 	The genetic algorithm is a method for solving both constrained and unconstrained optimization problems
	that is based on natural selection, the process that drives biological evolution.</pre>
In the most basic sense, the Genetic Algorithm is an algorithm that attempts to mimic the idea of biological
evolution in order to solve optimization problems. More information on the specifics of the algorithm can be
found in the documentation folder.

### What is the Infinite Monkey Theorem?
The Infinite Monkey Theorem is the idea that if you give a monkey infinite time in front of a typewriter, the
monkey will eventually produce a specified work (the most common example is a work of Shakespeare).

### What does the project do?
The project essentially combines these two concepts in order to produce a specified string. The program is given
a target string and starts the algorithm by producing random letters. It continually runs the algorithm, giving 
each string a fitness rating until a generation produces a string with a fitness of 1.0, meaning an exact match
to the target has been found.

## How to Run

### Installation
Before continuing, make sure you have the latest version of python installed.

To install, you must clone the repository to your PC using the following command in a CLI (Command line interface)
<pre>	git clone https://github.com/f0lg0/geneticAlgorithm-PY.git <i>directory</i></pre>
where <i>directory</i> is the file path where you want the installation to download on your computer.

### Run
To run, first navigate to the installation in the CLI using the command
<pre>	cd <i>directory</i> </pre>
where <i>directory</i> is the file path where you previously installed the repository to your computer.\
Then, type in the CLI
<pre>	python3 main.py </pre>
which should start running the program.\
If this does not work, try replacing "python3" with "python" or "py".
If it still does not work, double check your installation of Python.

### Example
If ran correctly, the output in the terminal should look something like this:
<pre>
Generation # 1456 | Fittest individual fitness:  0.9411764705882353
Target phrase: genetic algorithm
==========================================================
Individual # 0 : genetic algorithv | Fitness:  0.9411764705882353
Individual # 1 : genetic algorithv | Fitness:  0.9411764705882353
Individual # 2 : genetic algorithb | Fitness:  0.9411764705882353
Individual # 3 : genetic algorithv | Fitness:  0.9411764705882353
Individual # 4 : genetic algorithb | Fitness:  0.9411764705882353
Individual # 5 : genetic algorithv | Fitness:  0.9411764705882353
Individual # 6 : genetic algorithv | Fitness:  0.9411764705882353
Individual # 7 : genetic algorithv | Fitness:  0.9411764705882353
</pre>
Note: This is not the entire output, just a small portion.\
This particular example shows the algorithm nearing completion, as it is very close to getting 
the target phrse "genetic algorithm".

## Info
This python code was written in a Linux environment, so it may not work with Windows.

Feel free to play with this code and to criticize my work by giving me advice. Just please don't be rude.

## Tips
Resize your terminal window to a pretty big size, output is going to occupy a lot of space.

## Thanks to
Daniel Shiffman and his amazing "The Nature of Code" (chapter 9) book!