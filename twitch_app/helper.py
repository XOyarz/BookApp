from twitch import TwitchClient



# def get_twitch_user_bio(id):
#     client = TwitchClient(client_id='3xmckrtg57y9c26qxb51vby9hykgcw')
#
#     twitch_user = client.users.get_by_id(id)
#
#     return(twitch_user.bio)


def get_twitch_user(id):
    client = TwitchClient(client_id='3xmckrtg57y9c26qxb51vby9hykgcw')

    twitch_user = client.channels.get_by_id(id)

    return(twitch_user)