import random

# Lists of words or phrases to generate headlines
#past
florida_man_verbs = ["arrested", "attacked", "ate", "rescued", "stole", "fought"]

#present
florida_man_verbs_present = ["arrest", "attack", "eat", "rescue", "steal", "fight"]

#neither
florida_man_nouns = ["alligator", "panther", "beachgoer", "police car", "burrito", "shark"]
florida_man_adjectives = ["drunk", "naked", "masked", "disguised", "confused", "crazy"]

# Generate a random headline
verb = random.choice(florida_man_verbs)
verb_present = random.choice(florida_man_verbs_present)
noun = random.choice(florida_man_nouns)
adjective = random.choice(florida_man_adjectives)

#sentence formats
florida_man_sentence_format = [f"florida man {verb} {adjective} {noun}!", f"{adjective} florida man {verb} {noun}", f"florida man attempts to {verb_present} {adjective} {noun}!"]

#random sentence formats
headline = random.choice(florida_man_sentence_format)

print(headline.capitalize())
