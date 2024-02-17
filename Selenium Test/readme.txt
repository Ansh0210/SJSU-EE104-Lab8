1) First ensure that python is installed in your computer/laptop. Add it to the $PATH 

2) Download selenium IDE extension on google chrome. 

3) Download the latest WebDriver for google chrome from: https://googlechromelabs.github.io/chrome-for-testing/#stable  
	* Check your chrome version before downloading. 

4) add the destination folder of WebDriver to $PATH.

5) create a .env file in your project folder to store passwords and licenses. 

6) Record a new test in a new project using the selenium IDE extension on google chrome. 

7) Provide the project name and the project's base url that you want to test. This is the base link: https://eprint.com.hr/demo/addauser.php

8) Once clicked on start recording, a new window will open up where you can put in the username and password information to be recorded by selenium. Click on login page to open the login window and type the username and password again. 'Successful Login' will show up if successfully logged in. 

9) Go back to your selenium IDE and stop the recording. Give a name to your test such as "My Login Test" and save it. 

10) You will see the recorded steps in the IDE. (Optional) Press the play button to run the test. Can change the execution speed as well. 

11) Export the test to a Python code and place it in your project folder. Save the Project as 'My Automation Test.side' in your project folder as well. 

12) Modify the python file to add the executable path for the WebDriver

13) Then open terminal and change directory (cd) to your project directory. Pip install selenium and pytest. 

14) run the following commands after to install selenium side runner: 
	npm install -g selenium-side-runner
		
* make sure that you have node.js installed on your system before running the npm command or else you will encounter an error. 

15) run the following command to run the test using terminal:
	selenium-side-runner <ProjectName>.side