import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pytz import timezone
import pytz
from datetime import datetime
import random
import json

sys_random = random.SystemRandom()

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

points = client.open("IPL 2021").get_worksheet(0)
odds = client.open("IPL 2021").get_worksheet(1)
leaderboard = client.open("IPL 2021").get_worksheet(2)
bets = client.open("IPL 2021").get_worksheet(3)
timing = client.open("IPL 2021").get_worksheet(4)


def updateBet(team, name):
    """
    Given Team Name and Name of the person placing the bet, this function updates the google sheet "Bets"

    Args:
        team (string): Team Name
        name (string): User's Name

    Returns:
        boolean: Is the Team Name correct?
    """
    row = getCurrentMatch()
    col = getCol(name)
    if(bets.cell(row, 2).value.lower().find(team.lower()) == -1):  # Wrong Team Name
        return True
    else:
        bets.update_cell(row, col, team.upper())
        return False


def getCurrentMatch():
    """
    Calculates the Row number for the bets to be placed in

    Returns:
        int: Row Number for current match
    """
    with open("./match.json", "r+") as f:
        data = json.load(f)
        return int(data["Row"])


def getName(name):
    """
    Maps a name to every id

    Args:
        name (string): User discord ID

    Returns:
        string: User's name
    """
    if name == "Garg_Doppler#0732":
        return "Aaryan"
    elif name == "Anurag#4587":
        return "Fifi"
    elif name == "Aryan Bidani#3969":
        return "Gawd"
    elif name == "dhillo#6347":
        return "Simp"
    elif name == "dagar#0568":
        return "Qagar"
    elif name == "prajit_k#8574":
        return "Meena"
    elif name == "Pranav Gupta#5601":
        return "Pranav"
    elif name == "Rochak#4810":
        return "RRJ"
    elif name == "Saksham_2000#6650":
        return "Kholu"
    elif name == "shreyank#6297":
        return "Banakar Airlines"
    elif name == "DarthAmitesh#4268":
        return "Magar"
    elif name == "ashutoshsin#4206":
        return "Singla"


def getCol(name):
    """
    Maps a column number to every name

    Args:
        name (string): User Discord ID

    Returns:
        int: Column No. in Google Sheets
    """
    if name == "Garg_Doppler#0732":
        return 4
    elif name == "Anurag#4587":
        return 5
    elif name == "Aryan Bidani#3969":
        return 6
    elif name == "dhillo#6347":
        return 7
    elif name == "dagar#0568":
        return 8
    elif name == "prajit_k#8574":
        return 9
    elif name == "Pranav Gupta#5601":
        return 10
    elif name == "Rochak#4810":
        return 11
    elif name == "Saksham_2000#6650":
        return 12
    elif name == "shreyank#6297":
        return 13
    elif name == "DarthAmitesh#4268":
        return 14
    elif name == "ashutoshsin#4206":
        return 15


def getStats(name):
    """
    Fetches Stats from Spreadsheet

    Args:
        name (string): User's name

    Returns:
        string: Embed Description containing Points, Rank, Contribution and Profit
    """
    col = getCol(name)-2
    points = leaderboard.cell(2, col).value
    rank = leaderboard.cell(3, col).value
    contri = leaderboard.cell(4, col).value
    profit = int(leaderboard.cell(5, col).value)
    if profit >= 0:
        return "Points: {0}\nRank: {1}\nContri: {2}\nProfit: {3}\n".format(points, rank, contri, profit)
    else:
        return "Points: {0}\nRank: {1}\nContri: {2}\nLoss: {3}\n".format(points, rank, contri, str(0-profit))


def sorter(item):
    """
    sorter function key for sorted()

    """
    point = item[2]
    name = item[1]
    return (point, name)


def showLeaderboard():
    """
    Fetches the Leaderboard from Google Sheets and adds medals and stuff to make the embed interesting

    Returns:
        string: Leaderboard as it should look in the embed description
    """
    names = leaderboard.row_values(1)[1:]
    points = leaderboard.row_values(2)[1:]
    ranks = leaderboard.row_values(3)[1:]
    zipped = zip(ranks, names, points)
    sorted_zipped = sorted(zipped, key=sorter)
    lb = ""
    for element in sorted_zipped:
        if(element[0] == "1"):
            medal = "🥇"
        elif(element[0] == "2"):
            medal = "🥈"
        elif(element[0] == "3"):
            medal = "🥉"
        else:
            medal = ""
        lb += "{0:8}: {1:4} {2}\n".format(
            element[1], element[2], medal)

    return lb


def showBets():
    """
    Show all the bets for today

    Returns:
        string: Bets embed 
    """
    names = bets.row_values(1)[3:15]
    bet_list = bets.row_values(getCurrentMatch())[3:15]
    print(bet_list)
    zipped = zip(names, bet_list)
    bet_embed = ""
    for element in zipped:
        bet_embed += "{0}: {1}\n".format(element[0], element[1])

    teams = getMatch().split(" ")
    count1, count2 = 0, 0
    for bet in bet_list:
        if bet == teams[0]:
            count1 += 1
        elif bet == teams[2]:
            count2 += 1

    if count1 > count2+1 or count2 > count1+1:
        bet_embed += "\nDhyaan rakhna bhau aaj +2 wala panga pad sakta hai kyonki {0} ki {1} bets lagi hai aur {2} ki {3}.".format(
            teams[0], count1, teams[2], count2)
    else:
        bet_embed += "\nKaafi mast competition hoga aaj toh bets mai, dono ki lag bhag barabar bets hai"

    return bet_embed


def getMatch():
    """
    Gets Current Match. For Eg: DC vs CSK, RCB vs SRH, etc

    Returns:
        string: match
    """
    row = getCurrentMatch()
    return bets.cell(row, 2).value


def monthMapper(num):
    """
    Maps a month to its index

    Args:
        num (int): Index of month

    Returns:
        string: Month Name
    """
    if num == 1:
        return "Jan"
    elif num == 2:
        return "Feb"
    elif num == 3:
        return "Mar"
    elif num == 4:
        return "Apr"
    elif num == 5:
        return "May"
    elif num == 6:
        return "Jun"
    elif num == 7:
        return "Jul"
    elif num == 8:
        return "Aug"
    elif num == 9:
        return "Sep"
    elif num == 10:
        return "Oct"
    elif num == 11:
        return "Nov"
    elif num == 12:
        return "Dec"


def getNumMatches():
    """
    Finds the number of matches being played today

    Returns:
        int: number of matches
    """
    match_no = int(getCurrentMatch())
    cur_match = bets.row_values(match_no)[:3]
    prev_match = bets.row_values(match_no-1)[:3]
    next_match = bets.row_values(match_no+1)[:3]
    if prev_match[0] == cur_match[0] or next_match[0] == cur_match[0]:
        return 2
    else:
        return 1


def getMatchEmbed(num):
    """
    Generates the Embed for today's matches

    Args:
        num (int): Number of Matches

    Returns:
        string: Match Embed
    """
    match_no = int(getCurrentMatch())
    cur_match = bets.row_values(match_no)[:3]
    prev_match = bets.row_values(match_no-1)[:3]
    next_match = bets.row_values(match_no+1)[:3]
    if num == 0:
        return (cur_match[1], "Time: 7:30 PM")
    if num == 1:
        if prev_match[0] == cur_match[0]:
            return (prev_match[1], "Time: {0}\nWinner: {1}".format("3:30 PM", prev_match[2]))
        else:
            return (cur_match[1], "Time: 3:30 PM")
    if num == 2:
        if next_match[0] == cur_match[0]:
            return (next_match[1], "Time: 7:30 PM")
        else:
            return (cur_match[1], "Time: 7:30 PM")


def id(name):
    """
    Returns user id in order to mention the user.

    Args:
        name (string): User name

    Returns:
        string: discord id for mentioning 
    """
    if name == "Aaryan":
        return '<@710197373745365072>'
    elif name == "Anurag":
        return '<@627135355182645249>'
    elif name == "Aryan":
        return '<@627061362761400323>'
    elif name == "Dheeraj":
        return '<@761830763519279124>'
    elif name == "Dagar":
        return '<@713363451640021034>'
    elif name == "Prajit":
        return '<@533712314797654017>'
    elif name == "Pranav":
        return '<@761604392344092673>'
    elif name == "Rochak":
        return '<@627136441125830657>'
    elif name == "Saksham":
        return '<@711233065698983946>'
    elif name == "Shreyank":
        return '<@627431599327150110>'
    elif name == "Amitesh":
        return '<@672888082244304959>'
    elif name == "Ashutosh":
        return '<@800752585983262740>'


def notBetted():
    """
    Detects the names of users who didn't bet

    Returns:
        list: IDs of users who didn't bet
    """
    names = bets.row_values(1)[3:15]
    bet_list = bets.row_values(getCurrentMatch())[3:15]
    not_betted = []
    zipped = zip(names, bet_list)
    for _, bet in zipped:
        if bet == '':
            not_betted.append(id(_))

    return not_betted


def allotPoints():
    """
    Allots Random Points to those who didn't bet

    Returns:
        dictionary: Keys->IDs, Values->Random Points
    """
    row = getCurrentMatch()
    names = bets.row_values(1)[3:15]
    bet_list = bets.row_values(getCurrentMatch())[3:15]
    allot = dict()
    for i, bet in enumerate(bet_list):
        if bet == '':
            point = (sys_random.randint(1, 4)) / 2
            points.update_cell(row, i+4, point)
            allot[id(names[i])] = point

    return allot


def fetchBetReminderTime(row):
    """
    Fetches the time when @IPL Better is to be reminded to place bets

    Args:
        row (int): Row number

    Returns:
        string: Bet Reminder Time
    """
    return timing.cell(row, 4).value


def fetchWarningTime(row):
    return timing.cell(row, 5).value


def fetchAllocationTime(row):
    return timing.cell(row, 6).value


def fetchDay(row):
    return timing.cell(row, 3).value


def updateRow():
    with open("./match.json", "r+") as f:
        data = json.load(f)
        data["Row"] += 1
        allocation_time = fetchAllocationTime(data["Row"])
        if len(allocation_time) == 4:
            allocation_time = "0" + allocation_time
        data["Time"] = allocation_time
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
