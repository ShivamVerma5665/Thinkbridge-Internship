# Thinkbridge Internship

##--> This is a development branch


## Description

This repository consists of modules of python programs that will get completed during the internship period at ThinkBridge Software Pvt. Ltd. under the guidance of Sai Ganesh Sir.  

## Prerequisites

This program is entirely developed using Python3. So, installing a python compiler would help you not only to run the code easily but also will help you to make required changes. I personally use **Microsoft Visual Studio Code (https://code.visualstudio.com/)** which is one of the best compilers available for all operating systems and which also includes extensions of all the other languages apart from python e.g. java, cpp, ruby, etc. You can also use other compilers such as **Atom (https://atom.io/)**, **Eclipse (https://www.eclipse.org/downloads/)** and **PyScripter (https://sourceforge.net/projects/pyscripter/)**, **Pycharm (https://www.jetbrains.com/pycharm/)**.

# Installation Instructions

Below are the guidelines on how to install **Microsoft Visual Studio Code** for your Operating System

![Screenshot at 2020-06-19 10-17-39](https://user-images.githubusercontent.com/43331648/85097621-97c42f80-b1e7-11ea-8b9d-0b598e23f43d.png)

## For Windows
   * Goto https://code.visualstudio.com/download
   * Click on the **windows download button** and your download will start automatically(if applicable, provide the appropriate path where the executable file must get downloaded.
   * Once downloaded, double click the executable file and complete the installation.

## For Linux
Note : If you don't know whether your distribution is debian or RPM-based, then you can find your distro in the list given in the following link https://en.wikipedia.org/wiki/List_of_Linux_distributions. If you know that then please ignore.

   * If you have a _debian distribution or Ubuntu_, then download the **.deb** file by clicking on the **.deb download button**
     1. Using
        `sudo dpkg -i /path/to/deb/file`
        `sudo apt-get install -f`
     2. Using
        `sudo apt install ./name.deb`
        OR
        `sudo apt install /path/to/package/name.deb`
        With old apt-get versions you must first move your deb file to `/var/cache/apt/archives/` directory. For both, after executing this command, it will automatically download its dependencies.
     3. First installing `gdebi` and then opening your .deb file using it (Right-click -> Open with). It will install your .deb package with all its dependencies.
        **Note:** APT maintains the package index which is a database of available packages available in repo defined in `/etc/apt/sources.list` file and in the `/etc/apt/sources.list.d` directory. All these methods will fail to satisfy the software dependency if the dependencies required by the deb is not present in the package index.

   * If your distribution is RPM-based, then download the .rpm package by clicking the .rpm  download button
     
     1. Log in as root, or use the su command to change to the root user at the workstation on which you want to install the software.
     2. Download the package you wish to install. The package will be named something like DeathStar0_42b.rpm.
     3. To install the package, enter the following command at the prompt:

        `rpm -i code-version_number.rpm`
   
     4. If you are upgrading from an earlier version of the software package, run RPM in upgrade mode, as in the following example:

        `rpm -U code-version_number.rpm`
        
## For MacOS
   
   1. Download Visual Studio Code for Mac.
   2. Double-click on the downloaded archive to expand the contents.
   3. Drag Visual Studio Code.app to the Applications folder, making it available in the Launchpad.
   4. Add VS Code to your Dock by right-clicking on the icon and choosing Options, Keep in Dock.
   
**Alternative option** 
   * You can also download Microsoft Visual Studio Code from **snapstore**. In order to install go to https://snapcraft.io/code
   
![vscode_snapstore](https://user-images.githubusercontent.com/43331648/85097834-4d8f7e00-b1e8-11ea-95e7-0f7876ff15e2.png)

Note : If you want to install compiler other than vscode then you can go to the links mentioned in prerequisites and if the compiler name is not mentioned over there, then the web is open for you, just google it!

## _Latest Commit_

* A currency converter program that will convert the given integer amount(e.g. 212.45) into words(e.g. Two hundred and Twelve 45/100) written in python3.

## How to run - currency_to_text.py
 
### _For both Linux and windows users_

### Running the program on Vscode
  * If you have followed the instructions and installed Vscode on your machine, then you can simply install python extension from the extension market place.
  
![python-extension-marketplace](https://user-images.githubusercontent.com/43331648/85097259-84fd2b00-b1e6-11ea-81fa-581e6857316b.png)

  
  * Now, you can simply run the code or `Right-click` and select `Run in terminal` and the you will have the program running in your vscode window.
  
  ![code_in_vscode](https://user-images.githubusercontent.com/43331648/85097731-f1c4f500-b1e7-11ea-8d66-89f90a7612eb.png)

### Running the program on Command Prompt / Terminal

1. **Clone the repository** either pressing the green clone button present at the homepage of the repository or running the following command in your command prompt/terminal - `git clone https://github.com/ShivamVerma5665/Thinkbridge-Internship.git`
   * Note : Assuming your pc has git already installed on it. If you don't have git installed on your system then you can follow the steps given on **https://git-scm.com/book/en/v2/Getting-Started-Installing-Git**.
2. Extract the zip file in your home folder(or any folder of your choice)
3. Open command prompt/terminal in the same directory where you have extracted the zip file and goto modules folder.
4. You can run the program by typing **`python3 currency_to_word.py`** in your command prompt / terminal.
    * Note : Assuming you have python3 installed correctly on your system and if not then download it from             
      **https://www.python.org/downloads/** based on your OS.
5. Congratulations! you have run the program successfully

### **Alternative method for Linux users**
Type the following commands
   * **`sudo chmod 777 run.sh`**
   * **`./run.sh`**
### Now you can convert you integer input into words. Enjoy!

**Output**

![currency_to_text_output](https://user-images.githubusercontent.com/43331648/85097504-40be5a80-b1e7-11ea-8fc5-2d21d2f11475.png)


