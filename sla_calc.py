import sys
from datetime import datetime, timedelta
SLA = {"P1": 4, "P2": 8, "P3": 24, "P4": 72}
def due(created, prio):
    return datetime.strptime(created, "%Y-%m-%d %H:%M") + timedelta(hours=SLA[prio])
def breached(created, prio, now):
    return now > due(created, prio)
if __name__ == "__main__":
    c, p = sys.argv[1], sys.argv[2]
    print(f"SLA due: {due(c, p).strftime('%Y-%m-%d %H:%M')} ({p}, {SLA[p]}h)")
