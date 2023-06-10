#!/bin/bash
# sudo apt update; sudo apt upgrade -y; sudo apt autoremove -y; sudo apt install sysbench -y
# ctrl+z; bg; disown -h

for _ in {1..230}; do
    # log the time to file and terminal
    date | tee -a "$1".txt
    # run sysbench
    sysbench cpu --threads=8 --time=60 --rand-seed=99 --verbosity=3 run | tee -a "$1".txt
done

