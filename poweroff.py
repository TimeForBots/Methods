import os

def TimeFor(cfg, update, args) :
	if update.message.from_user.id in cfg.masters :
		cfg.exportBot().sendMessage(update.message.chat_id, "Shutting down, bye")
		os.system("pkill -f TimeForUpdates.py") # Commits suicide
	else :
		cfg.exportBot().sendMessage(update.message.chat_id, "You do not have rights to shut me down")