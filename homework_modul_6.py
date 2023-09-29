from datetime import datetime, timedelta
import os, re
from homework_modul_4_2 import normalizing_letter_cases_in_text

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
            if self.num_records > 0 and self.num_records >= len(records):
                records = records[:self.num_records]
            print(records)

            #os.remove(self.file_path)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

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

def save_record_to_file(record):
    with open('News_feeds1.txt', "a") as file:
        file.write(record.publish() + "\n")

file_path = input("Enter the file's path for rewriting records: ")
if len(file_path) < 1:
    file_path = 'News_feeds.txt'
num_records = int(input("Choose how many records from old file do you want to write in the constant file: "))
r = Records_from_file(file_path, num_records)
r.read_write_records()

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
        break
    else:
        print("Invalid choice. Please choose a valid option.")
