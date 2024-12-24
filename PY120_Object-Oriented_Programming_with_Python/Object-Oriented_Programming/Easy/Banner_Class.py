class Banner:
        
    def __init__(self, message):
        self._message = message
        self._length = len(message)

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        empty_string = ' ' * self._length
        return f'| {empty_string} |'

    def _horizontal_rule(self):
        border = '-'* self._length
        return f'+-{border}-+'
    
    @property
    def message(self):
        return self._message

    def _message_line(self):
        return f"| {self.message} |"
    
    
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+