
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author 	: Patrick Pedersen <ctx.xda@gmail.com>
# Last updated  : 20:00 3/4/2017 CEST
# Description	: Simple greeter script

import random

def TimeFor(config, update, args) :
	bot = config.exportBot()
	
	# Check if parameter has been passed or not
	if len(args) > 1 :
		senderFirstName = args[1] # Greet given user
	else :
		senderFirstName = update.message.from_user.first_name # Greet sender
	
	# Greetings list
	greetings = ["Hey", "Hi", "Hello", "Welcome", "What's up", "Oi", "Sup", "Waddup", "Yo", "Ayy", "OMG it's", "Ello", "Holla", "Here comes"]

	# Select random greeting from greetings list
	bot.sendMessage(update.message.chat_id, greetings[random.randint(0, len(greetings))] + ' ' + senderFirstName)
