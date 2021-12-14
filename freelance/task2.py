class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return " ".join([str(i) for i in self.data])

    def to_file_string(self):
        return ",".join([str(i) for i in self.data])


class Manager:
    def __init__(self):
        self.q = Queue()

    def run(self):
        # run the menu log N times until the False
        # is returned (when the "q" is pressed by the logic)
        while self.log_menu() != False:
            pass

    def log_menu(self):
        menu_text = """
Press 1: enqueue a word
Press 2: dequeue a word
Press 3: Show the Queue
Press 4: Save to the file
Press r: Read the queue file
Press q: exit
Select an option: """
        res = input(menu_text).lower()
        # specify and parse the actions below.
        available = ('1', '2', '3', '4', 'r', '4d', 'q')
        while res not in available:
            res = input(menu_text).lower()

        # process each of the parts
        if res == '1':
            self.add_word()
        elif res == '2':
            if self.delete_word():
                return True
        elif res == '3':
            print(self.q)
        elif res == '4':
            if self.save_q():
                return True
        elif res == 'r':
            if self.read_q():
                return True
        else:
            print("Exit...")
            return False

    def add_word(self):
        word = input("Enter the word to add to the queue: ")
        self.q.enqueue(word)

    def delete_word(self):
        if len(self.q) < 1:
            print("WARNING! The queue is empty")
            return True
        self.q.dequeue()
        print("The word was deleted from a queue")

    def save_q(self):
        file = input("Enter file name to save the queue: ")
        if file == 'q':
            return True
        with open(file, 'w', encoding='utf-8') as f:
            f.write(self.q.to_file_string())

    def read_q(self):
        file = input("Enter file name to read the queue: ")
        if file == 'q':
            return True
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read().split(",")
            print("Reading data...")
            self.q = Queue()
            for word in data:
                self.q.enqueue(word)


if __name__ == '__main__':
    Manager().run()
