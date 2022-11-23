# HESP Pipeline
This repo hosts the pipeline for HESP echelle spectrograph. 
## Installation
The repo can be cloned using git clone
`git clone https://github.com/arunsurya77/hesp_pipeline/`

it has following files

* bin ​ directory with the source files and supportfiles
* req.txt​ which has the list of python packages required for the installation
* hesp.config ​the config file for the pipeline

Make sure you have pip installed in your system. You can install it in ubuntu by

`sudo apt-getinstall python-pip`

or in Fedora by,

`yum install python-pip`

Use pip to installthe packages listed in req.txt

`sudo pip install -r req.txt`

Once the packages are installed copy the bin directory to a location in your home
directory. 
This could be inside a subdirectory also.
Copy hesp.config to your home directory. 
hesp.config has to be directly in your home directory and notinside any subdirectories .

Edit your hesp.config and give the exact path to the bin directory in the `path=` line in
Config subsection of hesp.config.

Now to make the python scripts inside the bin directory executable. Go to the bin
directory and use the command

`sudo chmod a+x hesp_*`

In Fedora one can accomplish the same using chmod command in root #.
Now the bin directory has to be added to the linux environment variable $PATH to be
accessible at differentlocations .

For this edit your .bash_profile or .bashrc file to add
`PATH=$PATH:~/hesp/bin
export PATH`

where `~/hesp/bin​` is the path ofthe hesp source files.
Depending on .bashrc or .bash_profile you used you will need to open a new terminal or
login again for the PATH variable to be active.
## Routines
`hesp_createlist` : Create the files.txt with the list of files and related info used for reduction.

`hesp_preproc` : Preprocessing of the files including, Bias Subtraction, Overscan Correction, Trimming and Cosmic Ray Correction

`hesp_extract`: Extract the orders from the processed files. This command will extract all the files listed in files.txt

`hesp_extract_file` : Extract only a single file given as argument ofthe command

`hesp_traceview`: View the trace overplotted on the image file given as the argument.

`hesp_traceshift` : Adjustthe trace by shifting interactively and update the global traces in the bin directory.

`hesp_addwave`: Create wavelength calibrated spectra for a list of files given as argument.

`hesp_recalib`: Find outthe global shifts in ThAr spectra and adjust and re-calibrate the wavelength solution accordingly

`hesp_view` : Interactive viewing ofthe wavelength calibrated spectra
## Manual
Hesp pipeline tutorial is available in link below

https://docs.google.com/document/d/1ImKAY45-Qm9kQ6Pytp7kDOZUo9PFYn-xKFlCleR-VgQ/edit?usp=sharing
