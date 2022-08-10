#!/usr/bin/env bash

if [ $(pwd) != "/home/ubuntu/ld-new-relic-simulation" ]
then
  echo "This script should only be run from the root of the project! Exiting"
  exit 1
fi

echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-virtualenv
PATH="$PATH:/home/ubuntu/.local/bin" # Needed to run the virtualenv script below
pip3 install newrelic virtualenv==20.0.17
virtualenv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

echo "Setting up systemd service..."
sudo cp ./setup/ld-new-relic-simulation.service /etc/systemd/system
sudo systemctl daemon-reload

cat << EOM
*****************************************************************************************************
                          LaunchDarkly New Relic Simulation setup complete!
=====================================================================================================

Setup is done! But there are still a few things you must do manually:

  - Rename the .env.example file to .env and fill in your LaunchDarkly SDK key

  - Add a new application on New Relic One
    - In the top menu bar, go to Explorer > Add More Data and select Python as the application type

  - Give the application a name in New Relic

  - Download your newrelic.ini file and place it in the root of this project directory

  - Optional: Configure log and infrastructure metrics
    - Instructions and a command to do this will be provided on the New Relic application setup page

After you've completed these steps, you can start the service with this command:

    sudo systemctl start ld-new-relic-simulation

Have fun :)

=====================================================================================================
*****************************************************************************************************
EOM