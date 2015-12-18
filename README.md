# gitlab webhook telegram bot

Simple gitlab telegram bot that listen to gitlab webhooks and send each event
to the authenticated chats

https://core.telegram.org/bots

Create a new bot https://core.telegram.org/bots#create-a-new-bot
and then copy the token to the token file.

# How to use

1. Change the app.py AUTHMSG to some secret
1. Run the app.py in your server
1. Create a webhook in your gitlab proyect that points to
   http://yourserver:10111/
1. Talk to your bot and write only the AUTHMSG
1. You will receive each event in your repo

# FAQ

## Q. How can I stop receiving messages
R. Write "shutupbot" in your conversation and the bot won't talk to you anymore

## Q. How can I enable the bot in group chats
R. Write /AUTHMSG instead of AUTHMSG

# Interesting files

 * chats, the json with all the chats to send notifications
 * token, the bot token
 * offset, the last msg id received from telegram api
