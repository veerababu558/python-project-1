# python-project-1
## Project Overview
This project demonstrates how to create a python package ,build a wheel file and install on it on another project.

## Prequisities
   1. Any IDE (ex: Visual Studio code,PyCharm).
   2. Python(version 3.6 or higher) and pip installed.

## Steps:
  1. Run the following command to install the necessary python setup tools.
  2. 
          pip install setuptools wheel
  3. Run the following command to create wheel file.
     
          python setup.py bdist_wheel
  5. Wheel file with **my_project-0.1.0-py3-none-any.whl** created under dist folder.
  6. Once the wheel file is created ,we can copy it to any location and install it and run without needing the original source code.

## Testing :
  1. Create a new project with name my_project_1.
  2. Copy the wheel file my_project-0.1.0-py3-none-any.whl which was created in my_project to my_project_1.
  3. Install pip using **python -m ensurepip --default-pip**  if not installed in my_project_1 project.
  4. Install the wheel file in my_project_1 by running following command.

        pip install my_project-0.1.0-py3-none-any.whl
  6. Type **Python** in Visual Studio IDE terminal and run the following python code.
     
         from my_package import module_1,module_2
         module_1.function1()
     **Output:**
         Response from Module1
     
         module_2.function2()
     **Output:**
          Response from module2

     


       

