# Secret Santa Names Picker #

This program will randomize all of your participants for secret santa. It will also send everyone a text messgae with who their person is. You can add in funtionality to send gift ideas.

### Setup ###

To make this work, you will need to copy the `example.config.py` and `example.members.json` files and remove the "example.". Then add your email and password to `config.py` and decide if you would like to send gift ideas. In the `members.json` file, add in each participant's: 

* name 
* phone number
* phone carrier

If you want to control who doesn't get who (for example, you don't want to assign someone themselves and if you don't want to have someone get the same person 2 years in a row) then put that id in the "no list".

Make sure to __give each participant a unique id__ when adding more people to the list. 

The program sends texts through your email provider so people will get a message from you, but you won't see it. This helps with the anonimity. If someone forgets or you need to debug, a list is generated named `christmasNames.txt` that has everyone's name and assignment. 

Have Fun!