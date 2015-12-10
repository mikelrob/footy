virtualenv $(pwd)/py_env
source $(pwd)/py_env/bin/activate
pip install -r requirements.txt
echo "0-5 7 * * 3 $(pwd)/run_footy.sh" > tmp
crontab tmp
rm tmp
