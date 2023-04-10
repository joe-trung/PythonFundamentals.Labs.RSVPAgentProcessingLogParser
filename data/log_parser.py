import re

with open('/Users/trung/Python Projects/PythonFundamentals.Labs.RSVPAgentProcessingLogParser/data/rsvp_agent_log.dat', 'r') as f:
    line = f.readlines()

warnings = "WARNINGS: \n"
for x in line:
    if 'WARNING' in x.upper():
        datetime = re.search('\d{2}/\d{2} \d{2}:\d{2}:\d{2}', x)
        error = x.split(': ')[1]
        warnings = warnings + datetime.group(0) +" -- " + error


print(warnings)
