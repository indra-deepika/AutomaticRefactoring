#!/bin/bash

# Variables
REPO_URL="https://github.com/indra-deepika/SE_Bonus_Test_Repo"
LOCAL_REPO_PATH="./"
DESIGNITEJAVA_PATH="./DesigniteJava.jar"
OUTPUT_PATH="./DesginiteJavaOutput/"

# Clone the repository
git clone $REPO_URL $LOCAL_REPO_PATH

# Run DesigniteJava
java -jar $DESIGNITEJAVA_PATH -i $LOCAL_REPO_PATH -o $OUTPUT_PATH

# Optionally, push the results back to the repository or handle them as needed
