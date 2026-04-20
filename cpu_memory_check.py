 cpu_memory_check.py
# Author: Tejaswi Hanvate
# Description: Monitors CPU and Memory usage
# and alerts if usage exceeds safe threshold

import psutil
import datetime

# -------- SETTINGS --------
CPU_THRESHOLD = 80      # Alert if CPU > 80%
MEMORY_THRESHOLD = 80   # Alert if Memory > 80%
# --------------------------

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    status = "🔴 HIGH - ALERT!" if cpu > CPU_THRESHOLD else "✅ OK"
    return cpu, status

def check_memory():
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    status = "🔴 HIGH - ALERT!" if mem_percent > MEMORY_THRESHOLD else "✅ OK"
    return mem_percent, status

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*50}")
    print(f"   SERVER HEALTH CHECK REPORT")
    print(f"   Time : {now}")
    print(f"{'='*50}")

    cpu, cpu_status    = check_cpu()
    mem, mem_status    = check_memory()

    print(f"   CPU Usage    : {cpu}%    {cpu_status}")
    print(f"   Memory Usage : {mem}%    {mem_status}")
    print(f"{'='*50}\n")

    if "ALERT" in cpu_status or "ALERT" in mem_status:
        print("⚠️  WARNING: System resources are critically high!")
        print("   ACTION : Investigate running processes immediately.\n")
    else:
        print("✅  All systems are healthy and running normally.\n")

if _name_ == "_main_":
    main()
