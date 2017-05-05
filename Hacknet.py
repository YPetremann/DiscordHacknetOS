import discord
import asyncio
import Computers
import Commands
import Programs
import Daemons

computers = {
	"lobby":{
		"links":["trial_head"],
	},
	"trial_head":{
		'vm':True,
		"links":["trial_chain"],
		"filesystem":{
			"home":{},
			"bin":{},
			"sys":{
				"init":"TXT:authd\nsshd\nftpd\nhttpd\nsmtpd",
				"passwd":"admin:rosebud",
				"authd":"DEM:AUTHD"
			}
		}
	},
	"trial_chain":{
		'vm':True,
		"links":["trial_tail"],
		"filesystem":{
			"home":{
				"readme.txt":"TXT:connect to 192.168.9.55"
			},
			"bin":{
				"SSHCrack.exe":"EXE:SSHCrack"
			},
			"sys":{
				"init":"TXT:authd\nsshd\nftpd\nhttpd\nsmtpd",
				"passwd":"admin:rosebud",
				"sshd":"DEM:SSHD",
				"ftpd":"DEM:FTPD",
				"httpd":"DEM:HTTPD",
				"smtpd":"DEM:SMTPD",
				"authd":"DEM:AUTHD"
			}
		}
	},
	"trial_tail":{
		'vm':True,
		"links":["irc"],
		"ports":[],
		"porttohack":0,
	}
}

async def execute(client,message):
	if message.channel.name in computers:
		if message.content.lower() == "scan":
			tmp = await client.send_message(message.channel, "```\nScanning...\n```")
			await asyncio.sleep(1)
			for terminal in computers[message.channel.name]["links"]:
				tmp = await client.edit_message(tmp, tmp.content[:-3]+"Found Terminal : {}```".format(terminal))
				for role in message.server.roles:
					if role.name == terminal:
						await client.add_roles(message.author, role)
				await asyncio.sleep(0.1)
			return tmp
		elif message.content.lower() == "scan":
			tmp = await client.send_message(message.channel, "```\nScanning...\n```")
			await asyncio.sleep(1)
			for terminal in computers[message.channel.name]["links"]:
				tmp = await client.edit_message(tmp, tmp.content[:-3]+"Found Terminal : {}```".format(terminal))
				for role in message.server.roles:
					if role.name == terminal:
						await client.add_roles(message.author, role)
				await asyncio.sleep(0.1)
			return tmp
