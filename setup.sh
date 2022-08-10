#!/usr/bin/env bash

if [ $(pwd) != "/home/ubuntu/ld-apm-simulation" ]
then
  echo "This script should only be run from the root of the project! Exiting"
  exit 1
fi

# Including this step because hostname shows up in New Relic
# Change this if you prefer something else
echo "Setting hostname..."
host_name = "LaunchDarkly-NewRelic-App"
hostnamectl set-hostname $host_name

echo "Installing dependencies..."
sudo apt update
sudo apt install python3-pip
pip3 install newrelic virtualenv
virtualenv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

echo "Setting up systemd service..."
sudo cp ./setup/ld-apm-simulation.service /etc/systemd/system
sudo systemctl daemon-reload
echo "Starting the application..."
sudo systemctl start ld-apm-simulation.service

cat << EOM
Done! But there are still a few things you must do manually:
  - Add a new application on New Relic One
    - In the top menu bar, go to Explorer > Add More Data and select Python as the application type
  - Give the application a name in New Relic
  - Download your newrelic.ini file and place it in the root of this project directory
  - Optional: Configure log and infrastructure metrics
    - Instructions and a command to do this will be provided on the New Relic application setup page
EOM