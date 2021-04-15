import sheets
import discord
import movie

def updateBet(message):
    """
    Updates User's Bet

    Args:
        message (object): discord message that prompts this action

    Returns:
        boolean:
    """
    content = message.content.lower().split(" ")
    team = content[content.index("pe") - 1].lower()
    status = sheets.updateBet(team, str(message.author))

    return status


def getMyPointsEmbed(message):
    embed = discord.Embed(title="{0} ke stats".format(sheets.getName(str(message.author))),
                          description=sheets.getStats(str(message.author)),
                          color=0xFF5733)
    return embed


def getPointsEmbed(message):
    embed = discord.Embed(title="Sabke Stats",
                    description="Ye lo bhau, jin jinke bole aapne un sabke stats dikha derela mai",
                    color=0xFF5733)
    for user in message.mentions:
        embed.add_field(name=sheets.getName(str(user)),
                    value=sheets.getStats(str(user)),
                    inline=False)
    return embed


def getLeaderboard(message):
    embed = discord.Embed(title="Leaderboard",
                          description=sheets.showLeaderboard(),
                          color=0xFF5733)
    return embed


def getCommands():
    embed = discord.Embed(
        title="Bunty ka skillset",
        description="Bhau aapko jo bhi karana hai isme se, uske liye ek line likho bas jisme uss kaam ke saare keyword aa rhe ho.\n\nKuchh words ke aage change bhi kar sakte ho aap, jaise lag ek keyword hai toh lag ka lagana, lagaio, lagade kuchh bhi bana sakte ho. Upar se line mai words ka order bhi matter nahi karta.",
  		    color=0xFF5733)

    embed.add_field(name="Bet lagana",
                    value='Keywords: bunty, pe, bet, lag',
                    inline=False)
    embed.add_field(name="Apne points dikhana",
                    value='Keywords: bunty, points, mere',
                    inline=False)
    embed.add_field(name="Dusro ke points dikhana",
                    value='Keywords: bunty, points',
                    inline=False)
    embed.add_field(name="Leaderboard dikhana",
                    value='Keywords: bunty, leaderboard, dikh',
                    inline=False)
    embed.add_field(name="Bets dikhana",
                    value='Keywords: bunty, bets, dikh',
                    inline=False)
    embed.add_field(name="Matches dikhana",
                    value='Keywords: bunty, kisk, match',
                    inline=False)
    embed.add_field(name="Movie ki list banana",
                    value='bhau isme movie ka naam \"\" mai dalna hoga\nKeywords: bunty, daal, list',
                    inline=False)
    embed.add_field(name="Movie ki list dikhana",
                    value='Keywords: bunty, dikh, list, movie',
                    inline=False)
    return embed


def showBets():
    embed = discord.Embed(title="Aaj ki Bets for {0}".format(sheets.getMatch()),
                          description=sheets.showBets(),
                          color=0xFF5733)
    return embed


def getMatches():
    num_matches = sheets.getNumMatches()
    if num_matches == 1:
        embed = discord.Embed(title="Aaj ka match:", color=0xFF5733)
        embed.add_field(name=sheets.getMatchEmbed(0)[0],
                        value=sheets.getMatchEmbed(0)[1],
                        inline=False)
    elif num_matches == 2:
        embed = discord.Embed(title="Aaj ke matches:", color=0xFF5733)
        embed.add_field(name=sheets.getMatchEmbed(1)[0],
                        value=sheets.getMatchEmbed(1)[1],
                        inline=False)
        embed.add_field(name=sheets.getMatchEmbed(2)[0],
                        value=sheets.getMatchEmbed(2)[1],
                        inline=False)
    return embed


def warning():
    people = sheets.notBetted()
    notif = ""
    for tag in people:
        notif += str(tag)
    return notif


def showMovieList():
    embed = discord.Embed(title="Movies ki list", 
                        description=movie.showMovie(), 
                        color=0xFF5733)
    return embed

def showMovieInfo(message):
    embed = discord.Embed(title=movie.fetchMovieTitle(message.content), 
						description=movie.get_imd_summary(movie.findLink(movie.fetchMovieName(message.content))), 
						color=0xFF5733)
    embed.set_thumbnail(url=movie.fetchPosterUrl(message.content))
    return embed