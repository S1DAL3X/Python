from hero import *

        
hero1 = Hero('S1DAL3X', 1, 'Human', 100)
hero1.set_health(150)
hero1.level_up()
hero1.show_hero()

hero2 = SuperHero('GodFather', 5, 'Magician', 100, 10)
hero2.show_hero()
hero2.level_up()
hero2.level_magic()

hero2.makemagic()
hero2.makemagic()
hero2.makemagic()

hero2.show_hero()
hero2.set_health(200)
hero2.show_hero()

        
