import os, re, csv, string, json
from homework_modul_4_2 import normalizing_letter_cases_in_text
from collections import Counter
from datetime import datetime, timedelta

class Record:
    def __init__(self, text):
        self.text = text
        self.date_published = datetime.now()

class News(Record):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city

    def publish(self):
        return f"{self.__class__.__name__}-------------------------\n {self.text}\n {self.city},  {self.date_published}\n"

class Private_ad(Record):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        self.days_left = (self.expiration_date - datetime.now().date()).days

    def publish(self):
        return f"{self.__class__.__name__}-------------------------\n {self.text}\n Actual until: {self.expiration_date}, {self.days_left} days left\n"

class Tasks(Record):
    def __init__(self, text, group, priority, story_points):
        super().__init__(text)
        self.group = group
        self.priority = priority
        self.story_points = story_points

    def publish(self):
        return f"{self.__class__.__name__}-------------------------\n {self.text}\n group: {self.group}\n priority: {self.priority}\n story_points: {self.story_points}\n"

class Records_from_file:
    def __init__(self, file_path, num_records):
        self.file_path = file_path
        self.num_records = num_records

    def read_write_records(self):
        records = []
        record_section = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        record_section.append(normalizing_letter_cases_in_text(line))
                    else:
                        if record_section:
                            records.append(record_section)
                        record_section = []

                if record_section:
                    records.append(record_section)

            #os.remove(self.file_path)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

        if self.num_records >= len(records):
            self.num_records = len(records)
        records = records[:self.num_records]
        for i in range(len(records)):
            if records[i][0] == 'News-------------------------':
                text = records[i][1]
                city = records[i][2][0:records[i][2].find(',')]
                news = News(text, city)
                news.publish()
                save_record_to_file(news)
            elif records[i][0] == 'Private_ad-------------------------':
                text = records[i][1]
                expiration_date_str = datetime.strptime(records[i][2][14:24], '%Y-%m-%d').date()
                days_to_subtract = int(records[i][2][26:records[i][2].rfind("'") - 9])
                new_expiration_datetime = datetime.combine(expiration_date_str, datetime.min.time()) - timedelta(days=days_to_subtract)
                expiration_date = str(new_expiration_datetime.date())
                private_ad = Private_ad(text, expiration_date)
                private_ad.publish()
                save_record_to_file(private_ad)
            elif records[i][0] == 'Tasks-------------------------':
                text = records[i][1]
                group = records[i][2][7::]
                priority = records[i][3][10::]
                story_points = records[i][4][14::]
                task = Tasks(text, group, priority, story_points)
                task.publish()
                save_record_to_file(task)
        return records

class Records_from_file_json:
    def __init__(self, file_path, num_records):
        self.file_path = file_path
        self.num_records = num_records

    def read_records(self):
        try:
            with open(self.file_path, "r") as f:
                my_dict = json.load(f)

        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return []
        return my_dict

    def write_records_to_json(self, my_dict, file_path):
        try:
            with open(output_file, "a") as file:
                for i, (key, value) in enumerate(my_dict.items()):
                    if i >= self.num_records or self.num_records >= len(my_dict):
                        break
                    if key.startswith('News'):
                        text = value['text']
                        city = value['city']
                        news = News(text, city)
                        news.publish()
                        file.write(news.publish() + "\n")
                    elif key.startswith('Private_ad'):
                        text = value['text']
                        expiration_date = value['expiration_date']
                        private_ad = Private_ad(text, expiration_date)
                        private_ad.publish()
                        file.write(private_ad.publish() + "\n")
                    elif key.startswith('Tasks'):
                        text = value['text']
                        group = value['group']
                        priority = value['priority']
                        story_points = value['story_points']
                        task = Tasks(text, group, priority, story_points)
                        task.publish()
                        file.write(task.publish() + "\n")
            print(f"Records written to {output_file} successfully!")
            # os.remove(self.file_path)
        except Exception as e:
            print(f"An error occurred while writing to the file: {str(e)}")

def save_record_to_file(record):
    with open('News_feeds1.txt', "a") as file:
        file.write(record.publish() + "\n")
    count_records('News_feeds1.txt')

def count_records(file_path):
    records = []
    record_section = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                record_section.append(line)
            else:
                if record_section:
                    records.append(record_section)
                record_section = []

        if record_section:
            records.append(record_section)

    dict_words = []
    dict_words1 = []
    for i in range(len(records)):
        for j in range(len(records[i])):
            temp_word = records[i][j].split()
            for k in range(len(temp_word)):
                translator = str.maketrans("", "", string.punctuation)
                result = temp_word[k].translate(translator)
                dict_words.append(result)
                dict_words1.append(result.lower())

    word_counts = Counter(dict_words1)
    word_counts_dict = dict(word_counts)
    total_letters = sum(len(word) for word in dict_words)
    uppercase_letters = sum(1 for letter in ''.join(dict_words) if letter.isupper())
    percentage_uppercase = round((uppercase_letters / total_letters) * 100, 2) if total_letters > 0 else 0

    letter_counts = {}
    for word in dict_words:
        for letter in word:
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

    csv_filename = 'word_counts.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Word', 'Count'])
        for word, count in word_counts_dict.items():
            csv_writer.writerow([word, count])
        csv_writer.writerow([])
        csv_writer.writerow(['Letter', 'Count'])
        for letter, count in letter_counts.items():
            csv_writer.writerow([letter, count])
        csv_writer.writerow([])
        csv_writer.writerow(['All letters (upper and lower cases): ' + str(total_letters)])
        csv_writer.writerow(['All letters in upper case): ' + str(uppercase_letters)])
        csv_writer.writerow(['Percentage letters in upper case to all letters: ' + str(percentage_uppercase)])

output_file = 'News_feeds1.txt'
file_path = input("Enter the txt file's path for rewriting records: ")
if len(file_path) < 1:
    file_path = 'News_feeds.txt'
num_records = int(input("Choose how many records from txt file do you want to write in the constant file: "))
r = Records_from_file(file_path, num_records)
r.read_write_records()

file_path_json = input("Enter the file's path for rewriting records from json: ")
if len(file_path_json) < 1:
    file_path_json = 'News_feeds.json'
num_records_json = int(input("Choose how many records from json file do you want to write in the constant file: "))
r = Records_from_file_json(file_path_json, num_records_json)
records = r.read_records()
r.write_records_to_json(records, output_file)

while True:
    print("Choose the record type:")
    print("1. News")
    print("2. Private Ad")
    print("3. Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter news text: ")
        city = input("Enter city: ")
        news = News(text, city)
        news.publish()
        save_record_to_file(news)
        print("News published successfully!")
    elif choice == "2":
        text = input("Enter ad text: ")
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        private_ad = Private_ad(text, expiration_date)
        private_ad.publish()
        save_record_to_file(private_ad)
        print("Private Ad published successfully!")
    elif choice == "3":
        text = input("Enter task text: ")
        group = input("Enter group for the task: ")
        priority = input("Enter priority for the task: ")
        story_points = input("Enter story_points for the task: ")
        task = Tasks(text, group, priority, story_points)
        task.publish()
        save_record_to_file(task)
        print("Task published successfully!")
    elif choice == "4":
        count_records('News_feeds1.txt')
        break
    else:
        print("Invalid choice. Please choose a valid option.")
    count_records('News_feeds1.txt')




