class AutoCompleteData:
    def __init__(self, completed, source_text, offset, score):
        self.completed = completed
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def get_completed(self):
        return self.completed

    def set_completed(self, completed):
        self.completed = completed

    def get_source_text(self):
        return self.source_text

    def set_source_text(self, source_text):
        self.source_text = source_text

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
