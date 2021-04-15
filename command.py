updateBet_key = ["pe", "bet", "lag", "bunty"]
showMyPoints_key = ["mere", "points", "bunty"]
showMentionPoints_key = ["points", "bunty"]
leaderboard_key = ["leaderboard", "bunty", "dikh"]
showBets_key = ["bets", "dikh", "bunty"]
showMatch_key = ["kisk", "match", "bunty"]
addMovie_key = ["bunty", "da", "list"]
showMovie_key = ["bunty", "dikh", "list", "movie"]
showMovieInfo_key = ["bunty", "imdb"]

def recUpdateBet(message):
	for key in updateBet_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowMyPoints(message):
	for key in showMyPoints_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowMentionPoints(message):
	for key in showMentionPoints_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowLeaderboard(message):
	for key in leaderboard_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowBets(message):
	for key in showBets_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowMatch(message):
	for key in showMatch_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recAddMovie(message):
	for key in addMovie_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowMovie(message):
	for key in showMovie_key:
		if message.lower().find(key) == -1:
			return False
	return True

def recShowMovieInfo(message):
	for key in showMovieInfo_key:
		if message.lower().find(key) == -1:
			return False
	return True