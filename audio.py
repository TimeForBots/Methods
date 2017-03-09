from datetime import datetime, timedelta

# Global vars
bot = None
chat_id = None

def sendMessage(msg) :
	bot.sendMessage(chat_id, msg)

def missingParams() :
	sendMessage("Not enough parameters provided")

def pollForAudio(bot, oldUpdateID) :
	newUpdate = bot.getUpdates()[-1]
	while newUpdate.update_id == oldUpdateID : newUpdate = bot.getUpdates()[-1]
	return newUpdate.message.audio.file_id if newUpdate.message and newUpdate.message.audio else -1

def TimeFor(config, update, args) :
	global bot
	global chat_id

	bot = config.exportBot()
	chat_id = update.message.chat_id

	argc = len(args)

	if argc < 2 :
		missingParams()
	else :

		# List command
		if args[1] == "list" :
			if argc > 2 : sendMessage(config.audioconfig.strlistSection(args[2]))
			else        : sendMessage(config.audioconfig.strlist())

		# Push
		elif argc == 4 and args[1] == "push" :
			if config.audioconfig.has_section(args[2]) :
				sendMessage("Name set, awaiting upload")
				file_id = pollForAudio(bot, update.update_id)

				if file_id != -1 :
						config.audioconfig.addOption(args[2], args[3], file_id)
						config.audioconfig.save()
						sendMessage("Successfully added " + args[3] + " to " + args[2])
				else :
					sendMessage("Invalid audio file")
			else :
				sendMessage("Section " + args[2] + " not found!")

		elif argc == 4 and args[1] == "remove" :
			if config.audioconfig.has_section(args[2]) :
				if config.audioconfig.has_option(args[2], args[3]) :
					config.audioconfig.removeOption(args[2], args[3])
					config.audioconfig.save()
					sendMessage("Successfully removed " + args[2] + " from " + args[3])
				else :
					sendMessage("No such entry for " + args[3] + " found under " + args[3])
			else :
				sendMessage("Section " + args[2] + " not found!")

		# Play
		elif argc == 4 and args[1] == "play" :
			if config.audioconfig.has_section(args[2]) :
				if config.audioconfig.has_option(args[2], args[3]) :
					bot.sendAudio(chat_id, config.audioconfig.getID(args[2], args[3]))
				else :
					sendMessage("No such entry for " + args[3] + " found under " + args[3])
			else :
				sendMessage("Section " + args[2] + " not found!")

		# Invalid option
		else :
			sendMessage("Invalid audio command")