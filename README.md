# python-project-1
## Project Overview
This project demonstrates how to create a python package ,build a wheel file and install.

## Prequisities
   1. Any IDE (ex: Visual Studio code,Pycharm)
   2. Python(Greater than 3.6 and pip installed)

## Steps:
  1. Run **pip install setuptools wheel** command to install required setup tools.
  2. Run **python setup.py bdist_wheel** command to create wheel file.
  3. Wheel file with **my_project-0.1.0-py3-none-any.whl** created under dist folder.
  4. Once the wheel file is created ,we can copy this file to anywhere and install and run the code without copying orginal code.

## Testing :
  1. Create a new project with name my_project_1.
  2. Copy wheel file my_project-0.1.0-py3-none-any.whl which was created in my_project to my_project_1.
  3. Install pip using **python -m ensurepip --default-pip** using command if not installed.
  4. Install file pip install my_project-0.1.0-py3-none-any.whl using command.
  5. Type **Python** in Visual Studio commmand line, it will open python shell. Run python application using below code.
     
         from my_package import module_1,module_2
         module_1.function1()
     **Output:**
         Response from Module1
     
         module_2.function2()
     **Output:**
          Response from module2

     


       

