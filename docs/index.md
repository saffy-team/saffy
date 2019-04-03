# Saffy

<img src="https://res.cloudinary.com/ppierzc/image/upload/v1554243272/saffy_logo_hc4atf.png" width="250px" alt="Saffy Logo" />


## A High-Level Signal Analysis Framework

A simple signal analysis framework, which aims at clarity of code and reproducibility of solutions. The plugin architecture
aims to encourage building modular code among scientists and data analysts. It provides a basic structure for signal
storage and a pipeline for analysis.

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

## Contributing
If you like the project and want to add something to it then please create a pull request.
- The title should shortly summarize the goal of your addition
- In the description go in depth with the changes you have made and why.
