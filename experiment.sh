#!/bin/bash
# tracing overhead experiment

# pull from git
git pull

# functin to reset
resetExperiment() {
    killall -q python3
    killall -q bpftrace
    truncate -s 0 trace_log.txt
}

# function to run experiment
runExperiment() {
    resetExperiment
    # TODO: finish experiment
    
}

