from datetime import datetime
import json
import smtplib
import os
import random
import time
import config

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

year = str(datetime.now().year)

# Send the message to the recipient.
def send(message, phone_number, carrier):
	phone_number = str(phone_number) + "{}"
	to_number = phone_number.format(carriers[carrier])
	auth = (config.EMAIL, config.APP_PASSWORD)

	domain = "smtp." + str(config.EMAIL[config.EMAIL.index('@') + 1 : ])
	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP(domain, 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)

# Check if the list of names is good.
def check_good_list(list):
	for person in list:
		if person["assignment"] in person["no list"]:
			return False
		
	return True

# Load the data.
f = open("members.json")
data = json.load(f)
participants = data["people"]

# Write to the log with each person and who they are assigned to.
def write_log():
	f = open("christmasNamesLog.txt", "w")
	f.write("Christmas Names " + year + "\n\n")
	f.write("program ran on " + str(datetime.now()))
	f.write("\n|Giver|\t\t\t\t|Receiver|\n")
	f.write("=============================================\n\n\n")

	names = ""
	tabs = "\t\t\t\t"

	for person in participants:
		assignment = participants[person["assignment"] - 1]
		if len(person["name"]) <= 3:
			tabs = "\t\t\t\t\t"
		elif len(person["name"]) > 7:
			tabs = "\t\t\t"
		else:
			tabs = "\t\t\t\t"
		line = person["name"] + tabs + assignment["name"] + "\n"
		names = names + line
	f.write(names)
	f.close

# Randomize the list of participants.
def randomize_list(patricipants):
	participant_list = []
	for person in participants:
			participant_list.append(person["id"])

	good_list = False

	while good_list == False:
		random_list = participant_list
		random.shuffle(random_list)

		count = 0
		for person in participants:
			person["assignment"] = random_list[count]
			count += 1
		
		good_list = check_good_list(participants)


# Do all the stuffs
randomize_list(participants)
write_log()


# Compose message and send to users
for person in participants:
	name = str(person["name"])
	number = person["number"]
	carrier = person["carrier"]

	assignment = participants[person["assignment"] - 1]
	assignmentName = str(assignment["name"])
	giftIdeas = assignment["gift ideas"]
	
	if config.TEST_MODE:
		message = (f"Secret Santa {year}\n\nThis automated message is a test to make sure {name.upper()} can recieve messages for Secret Santa. Please contact support if you have any questions.")
	else:
		message = (f"Secret Santa {year}\n\nThis is an automated message. {name.upper()}, your assignment is {assignmentName.upper()}.")
		if config.GIFT_IDEAS:
			message = message + (f" Some gift ideas are:\n {giftIdeas}")

	send(message,number,carrier)
	time.sleep(3)