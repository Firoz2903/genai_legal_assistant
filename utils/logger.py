import json, datetime

def log_action(action):
    log = {
        "action": action,
        "time": str(datetime.datetime.now())
    }
    with open("data/audit_logs.json", "a") as f:
        json.dump(log, f)
        f.write("\n")
