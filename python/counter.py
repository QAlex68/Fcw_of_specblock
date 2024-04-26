import csv


class Counter:
    def __init__(self, file_name):
        self.file_name = file_name

    def count_rows(self):
        try:
            with open(self.file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                row_count = sum(1 for row in reader)
                return row_count
        except FileNotFoundError:
            return 0
