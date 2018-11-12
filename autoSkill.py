import pyautogui as pad
import time
import csv
from datetime import datetime

SLEEP = 0.9
pad.FAILSAFE = True

change_list = []
change_dict = dict()
startTime = datetime.now()
adding = 0
removing = 0
changing = 0
errors = 0

#Compiles queue changes needed into a dictionary data structure for use later
with open('audit.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		change_list.append(row)
		
del change_list[0]	

for list in change_list:
	try:
		change_dict[list[0]].update({list[1]:(list[2], list[3])})
	except KeyError:
		change_dict[list[0]] = {list[1]:(list[2], list[3])}

pad.click(pad.center(pad.locateOnScreen('search.png')))

for extension in change_dict:

	while True:

		try:

			pad.typewrite(extension)
			time.sleep(SLEEP)
			pad.click(pad.center(pad.locateOnScreen('at.png')))
			time.sleep(SLEEP)
			pad.click(pad.center(pad.locateOnScreen('attributes.png')))
			time.sleep(SLEEP)
			pad.click(pad.center(pad.locateOnScreen('add.png')))
			time.sleep(SLEEP)
			
			for queue in change_dict[extension]:

				pad.typewrite(queue)

				if change_dict[extension][queue][0] == 'NULL':

					time.sleep(SLEEP)
					pad.click(pad.center(pad.locateOnScreen('addQueue.png')))
					pad.click(pad.center(pad.locateOnScreen('dropdown.png')))
					pad.typewrite(change_dict[extension][queue][1])
					pad.press('enter')
					pad.click(pad.center(pad.locateOnScreen('queueSearch.png')))
					pad.keyDown('ctrl')
					pad.keyDown('a')
					pad.keyUp('a')
					pad.keyUp('ctrl')
					pad.press('delete')
					adding+=1

				elif change_dict[extension][queue][1] == 'NULL':

					time.sleep(SLEEP)
					pad.click(pad.center(pad.locateOnScreen('remove.png')))
					pad.click(pad.center(pad.locateOnScreen('queueSearch.png')))
					pad.keyDown('ctrl')
					pad.keyDown('a')
					pad.keyUp('a')
					pad.keyUp('ctrl')
					pad.press('delete')
					removing+=1

				else:

					time.sleep(SLEEP)
					pad.click(pad.center(pad.locateOnScreen('dropdown.png')))
					pad.typewrite(change_dict[extension][queue][1])
					pad.press('enter')
					pad.click(pad.center(pad.locateOnScreen('queueSearch.png')))
					pad.keyDown('ctrl')
					pad.keyDown('a')
					pad.keyUp('a')
					pad.keyUp('ctrl')
					pad.press('delete')
					changing+=1
			
			pad.click(pad.center(pad.locateOnScreen('close.png')))
			pad.click(pad.center(pad.locateOnScreen('save.png')))
			time.sleep(5)
			pad.press('tab')
			
		except TypeError:
		
			pad.hotkey('ctrl', 'r')
			time.sleep(10)
			errors+=1
			pad.press('tab')
			continue
			
		break
	
print('Skilling Complete!')
print(str(adding) + ' queues added')
print(str(removing) + ' queues removed')
print(str(changing) + ' queues changed')
print(str(errors) + ' errors encountered')
print('Time elapsed: ' + str(datetime.now()-startTime))
