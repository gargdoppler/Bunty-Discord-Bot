import json
import sheets

def addEvent():
	with open('./events.json', 'r+') as f:
		data = json.load(f)
		weekday = sheets.fetchDay(sheets.get_current_match())
		data[weekday] = {"00:00":["Set Reminders", ""]}
		matches = sheets.getNumMatches()
		if matches == 1:
			bet_reminder_time = sheets.fetchBetReminderTime(sheets.get_current_match())
			warning_time = sheets.fetchWarningTime(sheets.get_current_match())
			allocation_time = sheets.fetchAllocationTime(sheets.get_current_match())
			if len(bet_reminder_time)==4:
				bet_reminder_time = "0"+bet_reminder_time
			if len(warning_time)==4:
				warning_time = "0"+warning_time
			if len(allocation_time)==4:
				allocation_time = "0"+allocation_time
			data[weekday][bet_reminder_time] = ["Bet Reminder", "<@&767098701104939038> Bets lagado"]
			data[weekday][warning_time] = ["Warning", " Bets lagado nahi toh mai fir random bet laga dunga tumhari"]
			data[weekday][allocation_time] = ["Allocate", ""]
		elif matches == 2:
			bet_reminder_time1 = sheets.fetchBetReminderTime(sheets.get_current_match())
			warning_time1 = sheets.fetchWarningTime(sheets.get_current_match())
			allocation_time1 = sheets.fetchAllocationTime(sheets.get_current_match())
			if len(bet_reminder_time1)==4:
				bet_reminder_time1 = "0"+bet_reminder_time1
			if len(warning_time1)==4:
				warning_time1 = "0"+warning_time1
			if len(allocation_time1)==4:
				allocation_time1 = "0"+allocation_time1
			bet_reminder_time2 = sheets.fetchBetReminderTime(sheets.get_current_match()+1)
			warning_time2 = sheets.fetchWarningTime(sheets.get_current_match()+1)
			allocation_time2 = sheets.fetchAllocationTime(sheets.get_current_match()+1)
			if len(bet_reminder_time2)==4:
				bet_reminder_time2 = "0"+bet_reminder_time2
			if len(warning_time2)==4:
				warning_time2 = "0"+warning_time2
			if len(allocation_time2)==4:
				allocation_time2 = "0"+allocation_time2
			data[weekday][bet_reminder_time1] = ["Bet Reminder", "<@&767098701104939038> Bets lagado"]
			data[weekday][warning_time1] = ["Warning", " Bets lagado nahi toh mai fir random bet laga dunga tumhari"]
			data[weekday][allocation_time1] = ["Allocate", ""]
			data[weekday][bet_reminder_time2] = ["Bet Reminder", "<@&767098701104939038> Bets lagado"]
			data[weekday][warning_time2] = ["Warning", " Bets lagado nahi toh mai fir random bet laga dunga tumhari"]
			data[weekday][allocation_time2] = ["Allocate", ""]

		f.seek(0)
		json.dump(data, f, indent = 4)
		f.truncate() 
	