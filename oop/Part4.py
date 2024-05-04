class Comment:
    count = 0
    def __init__(self, text):
        self.text = text

    def upcount(self):
        self.count += 1

my_comment = Comment("My comment")

my_comment.upcount()
print(my_comment.count)

my_comment.count = 17
print(my_comment.__dict__)
print(Comment.count)