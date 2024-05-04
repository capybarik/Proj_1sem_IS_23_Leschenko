class Comment:
    def __init__(self, text):
        self.text = text


    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

m_1 = Comment.merge_comments("Hello", "world!")
print(m_1)