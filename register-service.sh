#!/bin/bash
# Creates periodic-sync-service

default_workers=3
directory=$(dirname -- $(readlink -fn -- "$0"))

printf "This script will setup the periodic-sync as a service\n"
printf "Are you ok with this?\n"

select yn in "Yes" "No"; do
    case $yn in
        Yes )

            break;;

        No )

            # Exit script
            exit 0;;
    esac
done

printf "How many workers would you like to assign to pinion.weather?\n"
printf "recommended formula (2 x number_of_cores) + 1\n"
read -p "(DEFAULT=3)" workers

if [ -z "$workers" ]
  then
    workers=$default_workers
fi

printf "Using $workers workers\n"

cat >> periodic-sync.service <<EOF
[Unit]
Description=periodic-sync service
Requires=memcached.service
After=memcached.service
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=${USER}
ExecStart=${directory}/pipenv run python main.py

[Install]
WantedBy=multi-user.target
EOF

sudo mv periodic-sync.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start periodic-sync.service
sudo systemctl enable periodic-sync.service