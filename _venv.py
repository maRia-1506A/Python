# 1) pip intsall virtualenv (packege)
# 2) virtualenv env (setup isolated environment: env)
# 3) .\env\Scripts\activate.ps1 (environment activation)
# 4) pip freeze > requirements.txt (after install packeges, returns all the package installed in a file)
# 5) pip install –r requirements.txt (install same packages from one env to another)
# type "deactivate" (environment deactivation)

'''‘pip freeze’ 
returns all the package installed in a given python environment along with the versions.
(pip freeze > requirements .txt)
The above command creates a file named ‘requirements.txt’ in the same directory containing the output of ‘pip freeze’.
We can distribute this file to other users, and they can recreate the same environment using:
(pip install –r requirements.txt)'''
