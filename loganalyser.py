"""
Mantel Group Programming Task
Christian Torrisi
Log Analyser
"""


def main():
    filename = "programming-task-example-data.log"
    logs = load_log_file(filename)
    data = gather_data(logs)
    print(data)


# Gather all relevant data for analysis into an array
# The first element will contain an array of IP addresses
# The second array will contain an array of the visited URLs
def gather_data(logs):

    all_ip_addresses, all_urls = {}, {}
    for log in logs:
        # Split methods below is under the assumption that all log files are formatted in a consistent way.
        ip_address = log.split(" ")[0]
        url = log.split("\"-\"", 1)[0].split("GET ", 1)[1].split(" ")[0]

        all_ip_addresses = get_info(all_ip_addresses, ip_address)

        all_urls = get_info(all_urls, url)

    # Sort from highest to lowest based on value of each key (URL or IP Address occurrences)
    all_ip_addresses = sorted(all_ip_addresses.items(), key=lambda x: x[1], reverse=True)
    all_urls = sorted(all_urls.items(), key=lambda x: x[1], reverse=True)
    return [all_ip_addresses, all_urls]


# Get a stripped item, add to or check if it is an existing item in the dictionary
def get_info(item_dict, item):
    if item in item_dict:
        item_dict[item] += 1  # Add one to the value of an existing dictionary item
    else:
        item_dict[item] = 1  # Create new dictionary item

    return item_dict


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
