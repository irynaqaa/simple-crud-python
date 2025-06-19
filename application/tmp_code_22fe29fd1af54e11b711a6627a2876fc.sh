#!/bin/bash
pip install pylint
pip install -r requirements.txt
pylint --fail-under=8 .