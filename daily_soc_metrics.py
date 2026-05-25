import csv

critical = 0
high = 0
medium = 0
low = 0

with open('alerts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        severity = row['Severity']

        if severity == 'Critical':
            critical += 1
        elif severity == 'High':
            high += 1
        elif severity == 'Medium':
            medium += 1
        elif severity == 'Low':
            low += 1

print("Daily SOC Metrics")
print("-----------------")
print(f"Critical Alerts: {critical}")
print(f"High Alerts: {high}")
print(f"Medium Alerts: {medium}")
print(f"Low Alerts: {low}")
