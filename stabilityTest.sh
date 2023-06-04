  for _ in {1..1500}; do
    # log the time
    date >> Logs/Stability/test1.txt
    # run stress-ng
    stress-ng --cpu 1 --cpu-load 80 --timeout 60 --metrics --no-rand-seed >> Logs/Stability/test1.txt 2>&1
  done