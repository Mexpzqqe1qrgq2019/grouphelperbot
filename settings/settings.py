class Bot:
    token = '1145773465:AAFjC1aNg9EG5IlQHpNQgB-ENRrhtVje1-o'
    groupId = -476176949
    useStaffGroup = True
    staffGroupId = -476176949
    language = "en"


class Databases:
    admins = 'admins.json'
    users = 'users.json'


class Messages:
    welcome = "Hi, <b>{{name}}</b>!\nWelcome in the {{group_name}} group!"
    rules = ""


class Moderation:
    showWelcomeMessage = True
    deleteCommands = True
    spamDetect = True
    scanSendedFiles = True
    forwardSpamDetect = True
    detectPorn = True
    detectViolence = True
    mustHaveUsername = True
    controlUserName = True
    globalSilenceActive = False
    groupClosed = False
    maxWarns = 3
    userNameCharacterLimit = 32
    channelsWhitelist = ["durov", "telegram"]
    wordBlacklist = ["dick", "god"]


class BlockedMedia:
    text = False
    gif = False
    contact = True
    location = False
    document = False
    game = False
    audio = False


class virusTotal:
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class sightEngine:
    user = '1234567890'
    key = 'xxxxxxxxxxxxxxxxxxxx'
