#!/bin/bash
echo -e "Выберите нужный вариант сборки:\n\
         1. Автоматическая сборка\n\
         2. Полуавтоматическая сборка\n"

read var

if [[ $var -eq 1 ]] ; then
    rm -f Vagrantfile;
    ln -s Vagrantfile_auto Vagrantfile;
    vagrant up;
    sleep 5;
    python start_smoke_test.py;
elif [[ $var -eq 2 ]]; then
    rm -f Vagrantfile;
    ln -s Vagrantfile_manual Vagrantfile;
    vagrant up;
    sleep 5;
    ansible-playbook zookeeper_build.yml -e "{'hostname':'zookeeper-manual'}";
    sleep 5;
    python  start_smoke_test.py;
else 
   echo  "Выбран неверный вариант сборки";
   exit 1;
fi


           

