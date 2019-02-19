if ! [ $(which pip) ]; then
  echo "Installing pip with sudo"
  #curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python 
  sudo apt install python-pip
  if ! [ $? -eq 0 ]; then
    exit 1
  fi
fi

if ! [ $(which virtualenv) ]; then
  echo "Installing virtualenv with sudo"
  sudo -H pip install virtualenv
  if ! [ $? -eq 0 ]; then
    exit 2
  fi
fi

sudo apt-get install xvfb firefox

virtualenv $(pwd)/py_env
source $(pwd)/py_env/bin/activate
pip install -r requirements.txt
echo "0-5 7 * * 3 $(pwd)/run_footy.sh" > tmp
echo "56-59 6 * * 3 $(pwd)/run_footy.sh" >> tmp
crontab tmp
rm tmp
