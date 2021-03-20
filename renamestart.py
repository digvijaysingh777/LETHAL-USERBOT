#!/bin/bash


_get_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $LETHAL_REPO == "🇱 ETHAL 🇺 SERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $LETHAL_REPO == "🇱ETHAL 🇺SERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $LETHAL =~ $regex ]]
    then
        if [[ $LETHAL_REPO_BRANCH ]]
        then
            echo "${LETHAL_REPO}/archive/$LETHAL_REPO_BRANCH}.zip"
        else
            echo "${LETHAL_REPO}/archive/master.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    fi
}


_set_bot () {
    local zippath
    zippath="Lethaluserbot.zip"
    echo "  Downloading source code ..."
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    LETHALPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    sleep 5
    cd $LETHALPATH
    echo "    Starting LETHAL Bot    "
    echo "🇱ETHAL    🇺SERBOT
    
                              "

    python3 ../setup/updater.py ../requirements.txt requirements.txt
    python3 -m userbot
}

_set_bot
