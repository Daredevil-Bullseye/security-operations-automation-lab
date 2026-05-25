alerts = [
    {"Severity": "Critical"},
    {"Severity": "High"},
    {"Severity": "High"},
    {"Severity": "Medium"},
    {"Severity": "Low"},
    {"Severity": "Critical"},
    {"Severity": "Medium"},
]

metrics = {
    "Critical": 0,
    "High": 0,
    "Medium": 0,
    "Low": 0,
}

for alert in alerts:
    severity = alert["Severity"]
    metrics[severity] += 1

print("Daily SOC Metrics")
print("-----------------")
for severity, count in metrics.items():
    print(f"{severity} Alerts: {count}")
