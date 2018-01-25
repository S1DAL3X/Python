import os

class Computer():
    ''' Class to create our computer '''
    def __init__(self, pc_name, cpu, videoCard, hdd, ssd, ram, user):
        ''' Initiate datails our PC '''
        self.pc_name = pc_name
        self.cpu = cpu
        self.videoCard = videoCard
        self.hdd = hdd
        self.ssd = ssd
        self.ram = ram
        self.user = user
        self.pc_name = pc_name

    def show_pc(self):
        ''' Print pc details '''
        print(str(self.pc_name) +
             '\n{}'.format(str(self.cpu)) +
             '\n{}'.format(str(self.videoCard)) +
             '\n{}'.format(str(self.hdd)) +
             '\n{}'.format(str(self.ssd)) +
             '\n{}'.format(str(self.ram)) +
             '\n{}'.format(str(self.user))+
             '\n{}'.format(str(self.pc_name)))

class UpgradePC(Computer):
    ''' Class ours new pc '''
    def __init__(self, pc_name, cpu, videoCard, hdd, ssd, ram, user, superSkill):
        ''' PC has some super skill '''
        super().__init__(pc_name, cpu, videoCard, hdd, ssd, ram, user)
        self.superSkill = superSkill

    def function(self):
        ''' Print super skill '''
        print(self.superSkill)

user = os.getlogin()
pc_name = os.environ['COMPUTERNAME']
cpu = os.environ['PROCESSOR_IDENTIFIER']

myPC = Computer(str(pc_name), str(cpu), 'NVIDIA GeForce GTX 1050Ti', '1TB', '500GB', '16GB', str(user))
#myPC.show_pc()

myNewPC = UpgradePC(str(pc_name), str(cpu), 'NVIDIA GeForce GTX 1070Ti', '1TB', '1TB', '32GB', str(user), 'Some skill')
#myNewPC.function()
myNewPC.show_pc()
