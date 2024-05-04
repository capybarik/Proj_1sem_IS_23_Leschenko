class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_res):
        self.resolution = new_res

    def title_upper(self):
        self.title = self.title.upper()

my_image1 = Image("1920x1080", "Портрет", "jpg")
my_image2 = Image("360x240", "Иконка", "png")
print(my_image1.__dict__)
print(my_image2.__dict__)

my_image1.resize("1280x720")
print(my_image1.resolution)

my_image2.resize("16x16")
print(my_image2.resolution)

my_image2.title_upper()
print(my_image2.__dict__)