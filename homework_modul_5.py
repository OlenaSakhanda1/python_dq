from datetime import datetime

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

def save_record_to_file(record):
    with open('News_feeds.txt', "a") as file:
        file.write(record.publish() + "\n")

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
