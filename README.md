**Hello. I am a beginner Python developer. This is my graduation project. Its development and support I will continue in the future.
<br>
This is currently a raw alpha version. The code is in the public domain, if you want to help me in the development, all the information below.**


# PC Constructor

This project helps to assemble the computer in a user-friendly form of a consistent selection of components.

## What do we need to install the application?

1. We need [Python3](https://www.python.org)
    - Install Python 3 on Windows:
      - **First step**:
        - Open a browser window and go to the [Download](https://www.python.org/downloads/windows/) for Windows page on [python.org](https://www.python.org);
        - Under the top heading where Python Releases for Windows is written, click on the link to the latest version of Python 3.x.x .;
        - Scroll down and select the Windows x86-64 installation file for the 64-bit version of the operating system or the Windows x86 file for the 32-bit
      - **Second step**:
        - Run the installation file
        ---
    - Install Python 3 on Linux([Ubuntu](https://ubuntu.com/))
      - Depending on the version of Ubuntu you're working with, Python installation instructions will vary. You can determine your local version of Ubuntu by running the following command:
        ```shell
          $ lsb_release -a
          No LSB modules are available.
          Distributor ID: Ubuntu
          Description:    Ubuntu 16.04.4 LTS
          Release:        16.04
          Codename:       xenial
        ```
        *Follow the instructions below depending on the version number that is visible under the Release label in the console output:*
        
        
        **Ubuntu 17.10**, **Ubuntu 18.04** and later provides Python 3.x by default. You can invoke it with the ``` $python3 ``` command.
        <hr>
        
        **Ubuntu 16.10** and **Ubuntu 17.04** are not introduced by Python 3.6 by default, however it is available in the Universe repository. You can install it by running the following commands:
        ```shell
        $ sudo apt-get update
        $ sudo apt-get install python3.x
        ```
        ---
     - Install Python 3 on Mac OS X:
        - **First step Install Homebrew**:
            - Open the browser and go to the page http://brew.sh/. After the page has finished loading, select the boot code under Install Homebrew. Next, press Cmd + C to copy it to the clipboard. Make sure that you completely select the text of the command, as otherwise the installation will fail.
            - Next, you need to open the **Terminal.app** window, insert the Homebrew boot code, then press Enter. After that, the Homebrew installation will begin.
            - If you do this on a fresh version of macOS, you may receive a warning prompting you to install Apple’s developer command-line tools. This is necessary in order to complete the installation, so confirm the dialog by clicking install.
            - We confirm the dialog *"Software was installed"* of the installation file of the developer tools;
            - Return to the terminal, press Enter to continue the installation of Homebrew;
            - Homebrew will ask you to enter your password to complete the installation. Enter your user password and press Enter to continue;
            - Depending on your internet connection, Homebrew will take several minutes to download the necessary files. After the installation is complete, you will need to return to the terminal window.
        - **Second step Install Python**:
            - After Homebrew is installed, go back to the terminal and execute the following command:
                ```$ brew install python3```
            - Check whether python is installed or not with the command: 
                ```$ python3```
2. We need IDE for Python:
    - I use PyCharm. You can download Pycharm from this [link](https://www.jetbrains.com/ru-ru/pycharm/download/)

## Built With

* [Python](https://www.python.org/) - Programming language.
* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
* [Beautiful Soup 4.9.0](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parser for parsing HTML / XML 
* [Requests](https://requests.readthedocs.io/en/master/)

## Deployment

I will describe it later

## Authors

* **Yura Aronov** - *Initial work* - [gYliasH](https://github.com/aronovY)
