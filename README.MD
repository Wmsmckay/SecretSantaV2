# Secret Santa Names Picker #

This program will randomize all of your participants for secret Santa. It will also send everyone a text message with who their person is. You can add in functionality to send gift ideas.

### Setup ###

To make this work, you will need to copy the `example.config.py` and `example.members.json` files and remove the "example.". Then add your email and password to `config.py` and decide if you would like to send gift ideas. In the `members.json` file, add in each participant's: 

* name 
* phone number
* phone carrier

If you want to control who doesn't get who (for example, you don't want to assign someone themselves and if you don't want to have someone get the same person 2 years in a row) then put that id in the "no list".

Make sure to __give each participant a unique id__ when adding more people to the list. 

The program sends texts through your email provider so people will get a message from you, but you won't see it. This helps with the anonymity. If someone forgets or you need to debug, a list is generated named `christmasNames.txt` that has everyone's name and assignment. 

### Test mode ###

To make sure you setup everything correctly, you can run the program in `test_mode`. This setting is found in the `config.py` file. To use it, set it to true and then run the program. This will send everyone an automated message with their name to make that their name, number and carrier is correct. Sometime it can take a few minutes for the messages to be sent so be aware of that. When you are ready for the full program to be ran, turn this mode off and everyone will receive their assignment. 

Have Fun!
