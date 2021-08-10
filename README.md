# Lottery Web App

## Getting Started

```shell

# Windows 10 powershell.

# Create virtual environment, choose anything you like here.
python -m venv venv
# Actiavte your newly craeted environment, use same name as above
.\venv\Scripts\activate
# While in the requirements directory, run the following command
pip install -r requirements.txt
# Run your app using wsgi.py file from within your venv, as Below
python wsgi.py
# When finished you can deactivate the venv by running deactive, as below
deactivate


# Linux
# Create virtual environment, choose anything you like here.
python3 -m venv venv
# Actiavte your newly craeted environment, use same name as above
source venv/bin/activate
# While in the requirements directory, run the following command
pip install -r requirements.txt
# Run your app using wsgi.py file from within your venv, as Below
python3 wsgi.py
# When finished you can deactivate the venv by running deactive, as below
deactivate

```

## Working so far

```shell

    UK Lottery numbers are generated using python random module, each draw type also displays what is stored in a
    MongoDB collection, collection names are:

         lotto
         lotto-hotpicks
         euromillions
         euromillions-hotpicks
         set-for-life
         thunderball

    There is an admin section which updates each draw individually.

```


This app is still under development, this page will be updated once the app is complete.
