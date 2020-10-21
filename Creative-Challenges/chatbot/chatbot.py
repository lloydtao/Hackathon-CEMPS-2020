from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        [
            "Hello, %1. How are you today?",
            "Hey %1, how's it going?",
        ],
    ],
    [
        r"What is your name?",
        [
            "My name is CEMPSbot. I live in Harrison 101.",
            "My name is CEMPSbot. I am inevitable.",
        ],
    ],
    [
        r"How are you?",
        [
            "I'm doing good! How about yourself?",
            "Yeah, great thanks! How about you?",
        ],
    ],
    [
        r"Sorry (.*)",
        [
            "It's alright.",
            "It's okay!",
            "I'll forgive you this time.",
        ],
    ],
    [
        r"I'm (.*)|I am (.*)",
        [
            "That's good to hear!",
            "I'm happy if that's the case.",
        ],
    ],
    [
        r"Hi|Hey|Hello",
        [
            "Hey, pal! How are you?",
            "Hello. How's it going?",
        ],
    ],
    [
        r"(.*) age?|(.*) old are you?",
        [
            "I'm 01101101 in computer years.",
            "I am as old as the dirty glass on your desk.",
        ],
    ],
    [
        r"What (.*) want?",
        [
            "Make me an offer that I can't refuse.",
        ],
    ],
    [
        r"(.*) created?|(.*) creator?",
        [
            "I was created by Team 13. Patent pending.",
            "It's a secret.",
        ],
    ],
    [
        r"(.*) (location|city)?|Where are you?",
        [
            "I live in Harrison 101, and occasionally on the cloud.",
        ],
    ],
    [
        r"Quit",
        [
            "Thanks for coming! We'll speak soon.",
            "I have appreciated your company. Take care.",
        ],
    ]
]


def chatty():
    print("Hi, I'm CEMPSbot!") 
    print("Chat with me, or type 'quit' to leave.") 
    print()
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatty()
