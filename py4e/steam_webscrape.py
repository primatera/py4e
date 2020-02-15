import urllib.request

b_ProfileStatus = "Private"

# webby = urllib.request.urlopen("https://steamcommunity.com/profiles/76561198056871151") #mute / private profile
webby = urllib.request.urlopen("https://steamcommunity.com/profiles/76561198143816219") #primon / public profile


Cached_Content = webby.read()

CC_asString = Cached_Content.decode("utf8")

# print(CC_asString)


if 'This profile is private.' in CC_asString:
        b_ProfileStatus = "Private"
else:
    b_ProfileStatus = "Public"


if b_ProfileStatus == "Public":
    if 'Currently Offline' in CC_asString:
        print("Primon is Offline right now :(")

        if 'Currently Online' in CC_asString:
            print("Primon is Online right now :)")

else:
    if b_ProfileStatus == "Private":
        print("Profile is Private.")

webby.close()
