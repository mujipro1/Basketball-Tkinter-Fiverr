from Teams import Teams
from Season import Session
class Association:
    def __init__(self):
        self.teams = Teams()
        self.session = Session()

if __name__ == '__main__':
    association = Association
