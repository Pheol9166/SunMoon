class Gamepack():
    def __init__(self, name: str) -> None:
        # game title
        self.name = name

    # read text and print it 
    def read(scene: str) -> None:
        import time


        for word in scene:
            print(word, end = '', flush = True)
            time.sleep(0.1)
        time.sleep(0.5)