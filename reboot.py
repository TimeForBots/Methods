import os

def TimeFor(cfg, update, args) :
	if update.message.from_user.id in cfg.masters :
		if cfg.execPath :
			cfg.exportBot().sendMessage(update.message.chat_id, "Rebooting")
			os.system('sh ' + cfg.execPath + ' restart')
		else :
			cfg.exportBot().sendMessage(update.message.chat_id, "No execution script path defined in bot configuration. Unable to restart")
	else :
		cfg.exportBot().sendMessage(update.message.chat_id, "You do not have rights to restart me")