#!/bin/bash


_get_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $HELL_REPO == "🇱 ETHAL 🇺 SERBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $HELL_REPO == "🇱 ᴇᴛʜᴀʟ 🇺 ꜱᴇʀʙᴏᴛ" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    elif [[ $HELL_REPO =~ $regex ]]
    then
        if [[ $HELL_REPO_BRANCH ]]
        then
            echo "${HELL_REPO}/archive/${HELL_REPO_BRANCH}.zip"
        else
            echo "${HELL_REPO}/archive/master.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZVZhZGVycy9WYWRlci9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
    fi
}


_set_bot () {
    local zippath
    zippath="hellbot.zip"
    echo "  Downloading source code ..."
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    HELLPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    sleep 5
    cd $HELLPATH
    echo "    Starting HellBot    "
    echo "🇱 ᴇᴛʜᴀʟ 	🇺 ꜱᴇʀʙᴏᴛ
    
                              "

    python3 ../setup/updater.py ../requirements.txt requirements.txt
    python3 -m userbot
}

_set_bot