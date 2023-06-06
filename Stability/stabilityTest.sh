#!/bin/bash
# note: sudo apt install sysbench

for _ in {1..1500}; do
    # log the time to file and terminal
    date | tee -a "$1".txt
    # run sysbench
    sysbench cpu --threads=1 --time=60 --rand-seed=99 --verbosity=3 run | tee -a "$1".txt
done

