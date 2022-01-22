class Student:
    def __init__(self, name, model, cpu, ram):
        self.name = name
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.notebook = self.Notebook(self.model, self.cpu, self.ram)

    def print_info(self):
        print(self.name, end=' ')
        self.notebook.print_info()

    class Notebook:
        def __init__(self, model, cpu, ram):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def print_info(self):
            print(f'=> {self.model}, {self.cpu}, {self.ram}')


st = Student('Roman', 'HP', 'i7', '16')
st2 = Student('Vladimir', 'HP', 'i7', '16')
st.print_info()
st2.print_info()
