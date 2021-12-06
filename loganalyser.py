"""
Mantel Group Programming Task
Christian Torrisi
Log Analyser
"""


def main():
    filename = "programming-task-example-data.log"
    logs = load_log_file(filename)

    visited_urls = get_urls(logs)


def get_urls(logs):
    all_urls = {}
    for log in logs:
        log_data = log.split("\"-\"", 1)[0]
        url_data = log_data.split("GET ", 1)[1]
        url = url_data.split(" ")[0]
        if url in all_urls:
            all_urls[url] += 1
        else:
            all_urls[url] = 1
    return all_urls


# Function to load the data into from the log file
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
