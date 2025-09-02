# run_demo.py
import subprocess, time, sys, os

# Choose a start time a little in the future so both scripts can be ready
T0 = time.time() + 3.0
env = os.environ.copy()
env["DEMO_T0"] = str(T0)

spike = subprocess.Popen(
    ["pybricksdev", "run", "ble", "hub_program.py", "--name", "SPIKEHub-A"],
    env=env
)
create3 = subprocess.Popen(
    [sys.executable, "create3_script.py"],
    env=env
)

# Optional: wait & propagate exit codes
ret1 = spike.wait()
ret2 = create3.wait()
sys.exit(ret1 or ret2)
