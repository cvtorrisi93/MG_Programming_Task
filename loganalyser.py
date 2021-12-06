"""
Mantel Group Programming Task
Christian Torrisi
Log Analyser
"""


def main():
    filename = "programming-task-example-data.log"
    load_log_file(filename)


# Function to load the data into from the log file
def load_log_file(filename):
    try:
        with open(filename) as file_logs:
            file_logs = file_logs.readlines()
    except OSError as e:
        print("Could not open or read file: {}\n{}".format(filename, e))

    for line in file_logs:
        print(line, end='')


main()
