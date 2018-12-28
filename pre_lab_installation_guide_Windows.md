# How to install Anaconda on Windows?

#### Go to https://www.anaconda.com/download/#windows and download Python 3.7 version. (The whole process takes around 20 minutes.)

Anaconda is a popular platform to *Python* (and *R*) data science. It comes with several IDEs (Integrated Development Environments, such as *Jupyter* and *Spyder*) and a package manager `conda` to allow user-friendly coding with *Python*.

*NOTE: To prevent permission errors, do not launch the installer from the Favorites folder.*

*NOTE: If you encounter issues during installation, temporarily disable your anti-virus software during install, then re-enable it after the installation concludes. If you installed for all users, uninstall Anaconda and re-install it for your user only and try again.*
<p align="center">
  <img src="./images/Anaconda_Windows.png" height="400px"/>
</p>

#### Choose the location to install *Anaconda*. Copy the path and save it. 
<p align="center">
  <img src="./images/Anaconda_install-win-destination.png" height="400px"/>
</p>

#### You can continue with the default options. The installation takes around 10 minutes. 
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

#### Remember you have saved a path? Now you need to tell Windows where to find *Anaconda*.
Windows 10 and Windows 8
1. In **Search**, search for and then select: **Edit the system environment variables**
1. Click **Environment Variables**. 
1. In the section **System Variables**, find the **Path** environment variable and select it. Click **Edit**.
1. Click **New** and paste your **saved path** *your_path*\Anaconda and another path *your_path*\Anaconda\Scripts.

<p align="center">
  <img src="./images/Env_vars_Windows.png" height="400px"/>
</p>

Windows 7
1. From the desktop, right click the Computer icon.
1. Choose **Properties** from the context menu.
1. Click the **Advanced system settings** link.
1. Click **Environment Variables**. 
1. In the section **System Variables**, find the **Path** environment variable and select it. Click **Edit**.
1. Click **New** and paste your saved path *your_path*\Anaconda and another path *your_path*\Anaconda\Scripts.

#### Now use the *Anaconda prompt* (or *command prompt*) to verify installation and check the path of the required stuffs.
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
