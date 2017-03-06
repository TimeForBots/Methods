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
# Author 	: Sebastian Holler <jaroomgtavhype@gmail.com>
# Last updated  : 17:22 3/4/2017 CEST
# Description	: Simple pong ping script (request with /pong)
def TimeFor(config, update, args) :
	config.exportBot().sendMessage(update.message.chat_id, "ping")

