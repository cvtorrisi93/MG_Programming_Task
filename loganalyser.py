"""
Mantel Group Programming Task
Christian Torrisi
Log Analyser
"""


def main():
    filename = "programming-task-example-data.log"
    logs = load_log_file(filename)
    visited_urls = get_urls(logs)
    ip_addresses = get_ip_addresses(logs)


# Function to get all of the IP Addresses that visited each URL
# and count the number of times they occurred
def get_ip_addresses(logs):
    all_ip_addresses = {}
    for log in logs:
        # Split method below is under the assumption that all log files are formatted in this way.
        ip_address = log.split(" ")[0]
        if ip_address in all_ip_addresses:
            all_ip_addresses[ip_address] += 1  # Add one IP address to an existing dictionary item (IP Address)
        else:
            all_ip_addresses[ip_address] = 1  # Create new dictionary item for "new" IP address
    # Sort from highest to lowest (number of occurrences)
    return sorted(all_ip_addresses.items(), key=lambda x: x[1], reverse=True)


# Function to get all urls that were visited in the logged data
# and count each time the site was visited
def get_urls(logs):

    all_urls = {}
    for log in logs:
        # Split method below is under the assumption that all log files are formatted in this way.
        url = log.split("\"-\"", 1)[0].split("GET ", 1)[1].split(" ")[0]
        if url in all_urls:
            all_urls[url] += 1  # Add one visit to an existing dictionary item (url)
        else:
            all_urls[url] = 1  # Create new dictionary item for "new" url
    # Sort from highest to lowest (number of occurrences)
    return sorted(all_urls.items(), key=lambda x: x[1], reverse=True)


# Function to load the data from the log file
def load_log_file(filename):
    # Try/except to check if the file can be loaded correctly
    try:
        with open(filename) as file_logs:
            file_logs = file_logs.readlines()
    except OSError as e:
        print("Could not open or read file: {}\n{}".format(filename, e))
    # Catch all/different exceptions could be placed here for better error handling

    return file_logs


main()
