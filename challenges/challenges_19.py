# Challenge #1
# Consider this text file that contains multiple duplicate MAC addresses.
# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.

with open('challenges/files/macs.txt', 'r') as file:
    content = file.read().splitlines()
    unique_macs = set(content)
    seperated_macs = []
    for line in unique_macs:
        seperated_macs.extend(line.split(' '))
    
    with open('challenges/files/unique_macs.txt', 'w') as f:
        for mac in seperated_macs:
            f.write(mac + '\n')
