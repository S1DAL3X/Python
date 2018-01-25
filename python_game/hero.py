class Hero():
    ''' Class to create hero for our game '''
    def __init__(self, name, level, race, health):
        ''' Initiate out hero '''
        self.name = name
        self.level = level
        self.race = race
        self.health = health
        
    def level_up(self):
        ''' Set new level '''
        self.level += 1
        
    def show_hero(self):
        ''' Print hero description '''
        message = 'Name : {}'.format(self.name) + '\nLevel : {}'.format(str(self.level)) + '\nRace : {}'.format(self.race) + '\nHealth : {}'.format(str(self.health))
        print(message + '\n')
        
    def set_health(self, new_value):
        ''' Set new health '''
        self.health = new_value
        
    def moving(self):
        ''' Start moving '''
        print(self.name + ' is moving ...')