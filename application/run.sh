pip install pylint
pip install -r application/requirements.txt
pylint --fail-under=8 application/
if [ $? -ne 0 ]; then
echo "Pylint failed with exit code $?"
exit 1
fi