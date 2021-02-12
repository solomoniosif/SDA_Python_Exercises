
# TODO: Write a Python class to reverse a string word by word.
# * Input string : 'hello .py'
# * Expected Output : '.py hello'


class ReverseWords:
    def __call__(self, phrase):
        if isinstance(phrase, str):
            return self.reverse_words(phrase)
        return 'Input argument must be a string'

    @staticmethod
    def reverse_words(phrase):
        return ' '.join(reversed(phrase.split()))


if __name__ == '__main__':
    reverse_words = ReverseWords()

    print(reverse_words('hello .py'))
    print(reverse_words('My name is Joe'))