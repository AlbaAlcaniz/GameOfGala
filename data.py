image_paths = {
    'audio/castle.wav': [],
    'figures/0_2_miguelina.png': [
        "\nPrincess Miguelina doesn't wake up",
        'Her teenager dreams are deep, but this is too much.',
        "Let's ask Alcañiz family, maybe they know what's going on."
    ],
    'figures/0_3_alcanicil.png': [
        'The telepathic network of the brothers Alcañiz informs us that...',
        'The princess has been bewitched!\n',
        'We need to find the spell to wake her up.\n'
    ],
    'figures/0_4_letsgo.png': [
        'The brothers Alcañiz will help us.\n',
        'Through the network, they will guide us in this adventure over the kingdom.',
        "We'll have to visit all the family members...\n",
        'in exchange for helping them in small missions, they will give us parts of the spell',
        "\nLET'S GO!"
    ],
    'move0': [],
    'audio/1_1_explanation.wav': [],
    'figures/1_1_explanation.png': [
        'Teresa has entered a photography contest at VillaFoto ',
        'But her photo is full of cards! \n',
        'Remove the cards from the photo so that she can participate.',
        'To do this, you have to find the pair of each of the cards...',
        'If you touch two cards in a row with the same number, they will disappear.'
    ],
    'memory_game': [],
    'figures/1_3_congrats.png': [
        "Well done!\nYou've removed all the cards from the photo.",
        'Thanks to you,\nTeresa has won the contest!'
    ],
    'move1': [],
    'audio/2_1_explanation.wav': [],
    'figures/2_1_explanation.png': [
        'Héctor and María want to know the soccer classification.',
        'To know the teams position, they need to solve some sums.',
        'Can you help them? \n'
    ],
    'futbol_game': [],
    'figures/2_3_congrats.png': [
        'Well done! \n',
        'Of course, Valencia goes first. \n',
        "And Barça doesn't even appear in the classification due to its bad results..."
    ],
    'move2': [],
    'audio/3_1_explanation.wav': [],
    'figures/3_1_explanation.png': [
        'The kingdom train is broken, and Paco and Mari have decided to fix it. ',
        "But they are having trouble understanding the train's instructions.",
        'Complete the numerical series to help them. \n',
        'Associating each number you find with its letter of the alphabet ...',
        'You will be able to find the next part of the spell. \n'
    ],
    'series_game': [],
    'figures/3_3_congrats.png': [
        'Achieved! Now the kingdom train works perfectly again.',
        "A very beautiful train, don't you think?\n"
    ],
    'move3': [],
    'audio/4_1_explanation.wav': [],
    'figures/4_1_explanation.png': [
        'Some of the kingdom road signs are misplaced.\n',
        "The grandpas didn't know this, and have decided not to use the GPS",
        "And now they're lost! \n",
        "They have ended up in a labyrinth and they can't find the exit.",
        'Get them out of there and pick up the letters that you find on the way'
    ],
    'labyrinth_game': [],
    'figures/4_3_congrats.png': [
        'Well done!\n',
        'You took the grandpas out of the labyrinth.\n',
        "Good news! With the letters you found on the way, we've deciphered the spell!"
    ],
    'move4': [],
    'audio/castle2.wav': [],
    'figures/5_1_miguelina.png': [
        "Let's say the spell and see if the princess wakes up",
        '\n¡FERNANDUCHO ES UN MIEDICA!',
        "PD: Fernando is my uncle's name. Fernanducho is how we tickle him. Miedica means chicken",
        '\n...',
        '\n...',
        "Uhm...\nIt looks like the princess doesn't wake up...",
        'Have we done something wrong?\n',
        "Houston! You need to see this, I think that I've found the problem..."
        ],
    'figures/5_2_blai.png': [
        '¡Oh no!\n',
        'Blai was distracting Fernando and gave us wrong directions.',
        "We shouldn't have gone to the labyrinth...\n",
        "At least we've helped the grandpas!\n",
        "Let's keep looking!.\n"
    ],
    'move5': [],
    'audio/6_1_explanation.wav': [],
    'figures/6_1_explanation.png': [
        "It looks like there's been a water leak in your home.",
        'The green pipes are misplaced so the circuit is not closed.',
        'Place them correctly until the two round valves are connected.',
        "You'll need to use all the pipes!\n"
    ],
    'pipelines_game': [],
    'figures/6_3_congrats.png': [
        'Done!\n',
        'Now your parents can relax in the swimming pool.'
    ],
    'move6': [],
    'audio/7_1_explanation.wav': [],
    'figures/7_1_explanation.png': [
        'Teresina and Jordi want to expand the business by flying their balloon in the kingdom.',
        'But they are having trouble filling in the permits.\n',
        'Can you help them by solving the crossword? \n'
    ],
    'crossword_game': [],
    'figures/7_3_congrats.png': [
        "Now Teresina and Jordi's balloon can fly through the kingdom.",
        'And by helping them,\nwe have deciphered the spell!',
        "Let's hope we did it correctly this time...\n",
        "Let's go back to the castle to check if we can wake up the princess."
    ],
    'move7': [],
    'audio/castle3.wav': [],
    'figures/8_1_miguelina.png': [
        "Let's say the spell to see if the princess wakes up this time",
        '\n¡FERNANDUCHO ES UN MEDIAS NOCHES!',
        "PD: I don't know what 'medias noches' means, but it's how we tickle my uncle xD",
        '\n...',
        '\n...'],
    'audio/princessrescued.wav': [],
    'figures/8_2_success.png': [
        '\nWE DID IT!',
        "\nWe've woken up the princess.",
        "Thank you, Houston\n Without you, it wouldn't have been possible"
    ]
}

destinations = [
    ['castle', "Let's go first to VillaFoto, el village of the photography", 'fernando'],
    ['photo_village', "Next step: uncle's house", 'antonio'],
    ['hector', 'Hurry! To the train station', 'paco'],
    ['train_station', 'We enter the labyrinth...', 'fernando'],
    ['labyrinth', 'We have it! Back to the castle', 'paco'],
    ['castle', "Let's head to your house", 'antonio'],
    ['sofi', "It's time to fly!", 'fernando'],
    ['balloon', 'Last trip! Towards the castle', 'paco'],
    ['castle','aux']
]