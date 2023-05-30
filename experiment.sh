#!/bin/bash
# start overhead
# git pull
# echo "$2" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor # powersave or performance
# define experiment
experiment() {
  # setup
  killall -q python3
  killall -q bpftrace
  truncate -s 0 raw.txt
  sleep 1 # wait for 1 second
  # run tracing if necessary
  if [ "$2" == "X" ]; then
    sudo bpftrace overhead.bt >>raw.txt & # begin tracing
  fi
  # run the workload and measure how long it took
  stress-ng --cpu 1 --cpu-load 50 --timeout 10s --metrics --no-rand-seed | tee Logs/log_"$1".txt
  # end tracing
  killall -q bpftrace
  # update logs
  outputSize=$(wc -l raw.txt) # context switches recorded
  echo "$outputSize" >>Logs/log_"$1".txt
}
# run experiment
echo "Starting experiment ${1}"
iterationCounter=0
for _ in {1..5}; do # number of iterations
  sleep 1
  # experiment phase
  iterationCounter=$((iterationCounter + 1)) && printf "\t---------Run %s---------\n" "$iterationCounter"
  experiment "$1" X # base run
  experiment "$1" 1 # 1 context switch
done
# git pull
git add .
git commit -m "add and process experiment $1"
# git push # add to git
