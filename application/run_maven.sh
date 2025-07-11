#!/bin/bash
chmod +x install_maven.sh
./install_maven.sh
source /etc/profile.d/maven.sh
mvn clean install -e -DskipTests