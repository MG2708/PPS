#OOPs in Python
#Using Class
#Date : 27/12/2021

class Room:
	door = 1
	walls = 4
	window = 1
	curtains = 2
	light = 1
	chair = 0
	name = ""

	def __init__(self,name):
		self.name = name

	def open_door(self):
		print(f'I have opened the door for {self.name}')

	def switch_on_light(self):
		print(f'Switched on {self.light} lights for {self.name}')

	def switch_off_light(self):
		print(f'Leaving the {self.name}, switched off {self.light} lights')

	def switch_on_fan(self):
		print(f'Switched on {self.fans} fans for {self.name}')

	def switch_off_fan(self):
		print(f'Leaving the {self.name}, switched off {self.fans} fans')

bedroom = Room('bedroom')
bedroom.window = 3
bedroom.curtains = 6
bedroom.light = 3
bedroom.fans = 1
bedroom.open_door()
bedroom.switch_on_light()
bedroom.switch_on_fan()
bedroom.switch_off_light()
bedroom.switch_off_fan()
print()

studyroom = Room('studyroom')
studyroom.light = 4
studyroom.chair = 1
studyroom.table = 1
studyroom.fans = 1
studyroom.open_door()
studyroom.switch_on_light()
studyroom.switch_on_fan()
studyroom.switch_off_light()
studyroom.switch_off_fan()
print()

kitchen = Room('kitchen')
kitchen.door = 1
kitchen.window = 3
kitchen.curtains = 1
kitchen.light = 3
kitchen.open_door()
kitchen.switch_on_light()


