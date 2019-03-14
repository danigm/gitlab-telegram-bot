# gitlab webhook telegram bot

Simple gitlab telegram bot that listen to gitlab webhooks and send each event
to the authenticated chats

https://core.telegram.org/bots

Create a new bot https://core.telegram.org/bots#create-a-new-bot
and then copy the token to the token file.

# Requirements 
Only work with python3

# How to use

1. Change the authmsg file with some secret keyworld
1. Run the app.py in your server
1. Create a webhook in your gitlab project that points to
   http://yourserver:10111/
1. Talk to your bot and write only the keyworld
1. You will receive each event in your repo

# FAQ

## Q. How can I stop receiving messages
R. Write "shutupbot" in your conversation and the bot won't talk to you anymore

## Q. How can I enable the bot in group chats
R. Write /keyworld instead of keyworld

# Interesting files

 * chats, the json with all the chats to send notifications
 * token, the bot token
 * offset, the last msg id received from telegram api

# Docker
## build
```shell
$ docker build -t bot .
```
## run
```shell
$ docker run -d -p 10111:10111 --name bot -e AUTHMSG="XXX" -e TOKEN="XXX:XXX" bot
```