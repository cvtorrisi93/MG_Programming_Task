"""
Mantel Group Programming Task
Christian Torrisi
Log Analyser
"""
import os.path


def main():
    file_name = "programming-task-example-data.log"
    logs = load_log_file(file_name)
    data = gather_data(logs)
    create_report(data, file_name)


def create_report(data, log_file_name):
    new_file_name = "log_report.txt"
    count = 1

    while os.path.exists(new_file_name):
        new_file_name = "log_report_{}.txt".format(count)
        count += 1

    new_file = open(new_file_name, "w+")
    new_file.write("Log Report for file: \"{}\"\n\n".format(log_file_name))
    new_file.write("Number of Unique IP Addresses: {}\n\n".format(len(data[0])))
    new_file.write("Top 3 Active IP Addresses:\n")
    for i in range(0, 3):
        new_file.write("{}: {}   ->   Count: {}\n".format(i+1, data[0][i][0], data[0][i][1]))

    new_file.write("\nTop 3 Visited URLs:\n")
    for i in range(0, 3):
        new_file.write("{}: {}   ->   Count: {}\n".format(i+1, data[1][i][0], data[1][i][1]))


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
def load_log_file(file_name):
    # Try/except to check if the file can be loaded correctly
    try:
        with open(file_name) as file_logs:
            file_logs = file_logs.readlines()
    except OSError as e:
        print("Could not open or read file: {}\n{}".format(file_name, e))
    # Catch all/different exceptions could be placed here for better error handling

    return file_logs


main()
