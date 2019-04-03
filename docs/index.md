# Saffy

<img src="https://res.cloudinary.com/ppierzc/image/upload/v1554243272/saffy_logo_hc4atf.png" width="250px" alt="Saffy Logo" />


## A High-Level Signal Analysis Framework

Ever too often in signal analysis is time wasted on the repetitive tasks, which are very similar across projects. You promise yourself
to build a code base for your solutions, but end up just copy pasting whole chunks of code. Starting each project you hope that this time you will
have good structure and it will be awesome to work with. But it most often fails.
Probably because your on a deadline or building sustainable data architectures is not your thing, you just wanted to do some analysis.

Rightfully so! That's why saffy was created, so that you don't have to come up with a data structure and architecture.
So that you can concentrate on the fun and important part which is the analysis! When you come up with a solution you like,
you already have it as part of the framework, so it is easy to use in the future.

## Features
- Write 50% less code than before
- You concentrate on the fun logic stuff and let saffy do the boring repetetive tasks.
- Lost in variables and data? Saffy provides a data architecture to keep it clean. 
- Quick prototyping of signal analysis algorithms
- Reproducibility of solutions
- Clean, readable and organized code
- Your code-base can easily expand over multiple projects
- A clean pipline from modeled signals to real-world data
- Less simple and repetitive work

## Install

`pip3 install saffy`

###### From Source
Using a virtualenv is recommended! 

`!pip3 install -U https://api.github.com/repos/saffy-team/saffy/zipball/master`

or if you want the source code

Download the package to your project directory

`git clone https://github.com/saffy-team/saffy.git`

Install dependencies

`pip3 install -r ./saffy/requirements.txt`

## Usage
```python
import saffy
sig = saffy.SignalManager(filename="path/to/file")
```

## Example
A short example of how to use saffy for EEG data analysis.
```python
EEG = saffy.SignalManager(filename="path/to/file")

EEG.extract_channels(['C3', 'C4', 'trig'])

EEG.set_tags_from_channel('trig')

EEG.remove_channel('trig')

EEG.butter_highpass_filter(cutoff=1, order=2)
EEG.cheb2_notch_filter(cutoff=50, order=1, rs=3, width=0.3, btype='bandstop')

PRE_EEG = EEG.copy('pre')
PRE_EEG.set_epochs_from_tags(-4, -2)

PRE_EEG.welch_mean_spectrum()

POST_EEG = EEG.copy('post')
POST_EEG.set_epochs_from_tags(0.5, 2.5)

POST_EEG.welch_mean_spectrum()
```
With just this code we managed to calculate the mean spectrum using Welch's method for the signal before and after the trigger.
In plain numpy and scipy this would take much longer, would be less readable and probably would be much more error prone.
For comparison you can see the attached [solution](https://github.com/saffy-team/saffy/blob/master/examples/plain_numpy_scipy_EEG_example.py) in plain numpy and scipy.

## Contributing
If you like the project and want to add something to it then please create a pull request.
- The title should shortly summarize the goal of your addition
- In the description go in depth with the changes you have made and why.
