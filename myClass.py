class Course:
    def __init__(self, name:str, price:int) -> None:
        self.name = name
        self.price = price
    def upload(self):
        return f"{self.name} is uploaded"
    def download(self):
        return f"{self.name} is downloaded"