# How to install Anaconda on Windows?

#### Go to https://www.anaconda.com/download/#windows and download Python 3.7 version. (The whole process takes around 30 minutes.)

Anaconda is a popular platform to *Python* (and *R*) data science. It comes with several IDEs (Integrated Development Environments, such as *Jupyter* and *Spyder*) and a package manager `conda` to allow user-friendly coding with *Python*.

*NOTE: To prevent permission errors, do not launch the installer from the Favorites folder.*

*NOTE: If you encounter issues during installation, temporarily disable your anti-virus software during install, then re-enable it after the installation concludes. If you installed for all users, uninstall Anaconda and re-install it for your user only and try again.*
<p align="center">
  <img src="./images/Anaconda_Windows.png" height="400px"/>
</p>

#### Choose the location to install *Anaconda*. 
<p align="center">
  <img src="./images/Anaconda_install-win-destination.png" height="400px"/>
</p>

#### You can continue with the default options. The installation takes around 20 minutes. 
<p align="center">
  <img src="./images/Anaconda_install-win-path.png" height="400px"/>
</p>


#### No need to install *Microsoft Visual Studio* at the end. We won't use it in this lab.
<p align="center">
  <img src="./images/No_VS_Windows.png" height="400px"/>
</p>

#### A successful installation displays the following screen:
<p align="center">
  <img src="./images/Anaconda_install_success_Windows.png" height="400px"/>
</p>

#### Now use the *Anaconda prompt* to verify installation and check the path of the required stuffs.
<p align="center">
  <img src="./images/conda_cmd_Windows.png" height="400px"/>
</p>

#### Type/copy the following commands into the *Anaconda prompt*:
```
where python conda jupyter spyder
```
As mentioned, `python` is the programming language and `conda` is the package manager. Here, `jupyter` and `spyder` are two IDEs that we will use.

#### You should see a path for each of them, e.g.
<p align="center">
  <img src="./images/Paths_Windows.png" height="400px"/>
</p>

## Install conda environment for extra packages
We will need some extra packages later when we deal with atmospheric data. Follow the guide below to install them into a "conda environment".

Download [environment.txt](https://raw.githubusercontent.com/joeylamcy/Python_tutorial/master/environment.txt) and save it on D:\ Drive. Execute the following command in the *Anaconda Prompt*: 
```bash
conda env create -vv -n earth -f D:\environment.txt
```
*Note: Feel free to change earth to other names.*

This will automatically install the relevant packages that you will need in this part and next part. This takes around 5 minutes. Make sure you have **internet connection** while you do this. 

Successful installation gives the following (or something similar):
```
#
# To activate this environment, use
#
#     $ conda activate earth
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Next part: [Python Introduction](./Part0_Introduction.md)
