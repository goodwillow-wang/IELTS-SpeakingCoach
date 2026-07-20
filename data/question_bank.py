"""
IELTS Speaking Test Question Bank
Based on Cambridge IELTS 9 & 13 authentic tests
"""

import json, os

IELTS_SPEAKING_QUESTIONS = {
    "Cambridge 9": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Games",
                "questions": [
                    "Do you like playing games? (Why/Why not?)",
                    "What games do you usually play?",
                    "Do you prefer to play games alone or with others?",
                    "What games did you enjoy playing when you were a child?",
                    "Do you still play the same games now that you are older?",
                    "How have the games children play changed since you were young?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person who has influenced you in your life.",
                "prompts": [
                    "Who this person is",
                    "How you know this person",
                    "What qualities this person has",
                    "And explain how this person has influenced you"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Influential People",
                "questions": [
                    "What kinds of people are considered influential in your country?",
                    "Do you think it's important for young people to have role models?",
                    "How do social media influencers affect young people today?",
                    "Do you think influence is always positive? Why or why not?"
                ]
            }
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Reading",
                "questions": [
                    "Do you like reading? (Why/Why not?)",
                    "What kind of books do you usually read?",
                    "Do you prefer to read at home or in a library?",
                    "Did you enjoy reading as a child?",
                    "What did you like to read when you were young?",
                    "Do you think reading habits have changed in recent years?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person that you like to spend time with.",
                "prompts": [
                    "Who this person is",
                    "How you know this person",
                    "What you usually do together",
                    "And explain why you like to spend time with this person"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Social Relationships",
                "questions": [
                    "How has the way people spend time with each other changed?",
                    "Do you think people spend enough time with their families?",
                    "What are the benefits of spending time with friends?",
                    "How important are social relationships for mental health?"
                ]
            }
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Flowers",
                "questions": [
                    "Do you like flowers? (Why/Why not?)",
                    "What kind of flowers do you know?",
                    "Do you think flowers are important?",
                    "When do people in your country give flowers to others?",
                    "Have you ever given flowers to someone?",
                    "Do you prefer to have flowers in your home or outside in a garden?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a journey you went on that you remember well.",
                "prompts": [
                    "Where you went",
                    "How you travelled",
                    "Why you went on this journey",
                    "And explain why you remember this journey well"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Travel and Transport",
                "questions": [
                    "How has air travel changed in recent decades?",
                    "Do you think people travel more now than in the past?",
                    "What are the environmental impacts of increased travel?",
                    "How do you think travel will change in the future?"
                ]
            }
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Happiness",
                "questions": [
                    "What makes you feel happy?",
                    "Do you think happiness is important?",
                    "Do you feel happy when you buy something new?",
                    "What do you think is the relationship between money and happiness?",
                    "Do you think people in your country are generally happy?",
                    "What do people in your country do to feel happy?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a gift you gave to someone.",
                "prompts": [
                    "What the gift was",
                    "Who you gave it to",
                    "Why you chose this gift",
                    "And explain how the person felt about this gift"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Gifts and Giving",
                "questions": [
                    "Do people in your country give gifts on special occasions?",
                    "What kinds of gifts are popular in your country?",
                    "Do you think it's the thought that counts when giving gifts?",
                    "How have gift-giving traditions changed in your country?"
                ]
            }
        }
    },
    "Cambridge 13": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Games",
                "questions": [
                    "Do you enjoy playing games? (Why/Why not?)",
                    "What games are popular in your country?",
                    "Do you prefer indoor or outdoor games?",
                    "Did you play any games when you were a child?",
                    "How often do you play games now?",
                    "Do you think games are important for children's development?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you started using a new technological device.",
                "prompts": [
                    "What device you started using",
                    "When you got it",
                    "What you used it for",
                    "And explain how you felt about using this new device"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Technology and Society",
                "questions": [
                    "How has technology changed the way people communicate?",
                    "Do you think technology has made life easier or more complicated?",
                    "What are the negative effects of technology on society?",
                    "How do you think technology will change in the next 10 years?"
                ]
            }
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Music",
                "questions": [
                    "Do you like music? (Why/Why not?)",
                    "What kind of music do you listen to?",
                    "Do you prefer listening to music alone or with others?",
                    "Have your music tastes changed as you've grown older?",
                    "Do you play any musical instruments?",
                    "Do you think children should learn to play an instrument?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person who you think is a good leader.",
                "prompts": [
                    "Who this person is",
                    "How you know them",
                    "What they do as a leader",
                    "And explain why you think they are a good leader"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Leadership",
                "questions": [
                    "What qualities make a good leader?",
                    "Do you think leaders are born or made?",
                    "How has leadership changed in modern workplaces?",
                    "Do you think everyone can learn to be a leader?"
                ]
            }
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Names",
                "questions": [
                    "Does your name have a special meaning?",
                    "Do you like your name? (Why/Why not?)",
                    "Who usually chooses names for babies in your country?",
                    "Do people in your country change their names?",
                    "Are there any naming traditions in your country?",
                    "Do you think names are important?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you received a good service from a company or shop.",
                "prompts": [
                    "What service you received",
                    "When and where you received it",
                    "Who helped you",
                    "And explain why you think it was good service"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Customer Service",
                "questions": [
                    "What do you think is good customer service?",
                    "How has customer service changed in recent years?",
                    "Do you think online shopping provides better service than physical stores?",
                    "What can companies do to improve their customer service?"
                ]
            }
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Concentration",
                "questions": [
                    "Can you concentrate easily? (Why/Why not?)",
                    "What do you do to help yourself concentrate?",
                    "Do you find it easier to concentrate in the morning or in the evening?",
                    "Do you think people's ability to concentrate has changed?",
                    "Is it important for children to learn to concentrate?",
                    "How can technology affect concentration?"
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you were very busy.",
                "prompts": [
                    "When this happened",
                    "What you had to do",
                    "How you managed the situation",
                    "And explain how you felt about being so busy"
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Two-way Discussion": {
                "topic": "Work-Life Balance",
                "questions": [
                    "Do you think people in your country work too hard?",
                    "How has the concept of work-life balance changed?",
                    "What are the effects of overworking on health?",
                    "How do you think working patterns will change in the future?"
                ]
            }
        }
    }
}


def get_all_topics():
    topics = []
    for book, tests in IELTS_SPEAKING_QUESTIONS.items():
        for test, parts in tests.items():
            topics.append({
                "book": book, "test": test,
                "part1_topic": parts["Part 1 - Introduction & Interview"]["topic"],
                "part2_topic": parts["Part 2 - Individual Long Turn"]["cue_card"][:50],
                "part3_topic": parts["Part 3 - Two-way Discussion"]["topic"]
            })
    return topics


def get_test(book_name, test_name):
    if book_name in IELTS_SPEAKING_QUESTIONS:
        if test_name in IELTS_SPEAKING_QUESTIONS[book_name]:
            return IELTS_SPEAKING_QUESTIONS[book_name][test_name]
    return None


# ---- Custom Questions Support ----
CUSTOM_QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "custom_questions.json")


def _init_custom():
    """Load custom questions from JSON file into IELTS_SPEAKING_QUESTIONS."""
    global IELTS_SPEAKING_QUESTIONS
    if "Custom Questions" not in IELTS_SPEAKING_QUESTIONS:
        IELTS_SPEAKING_QUESTIONS["Custom Questions"] = {}
    if CUSTOM_QUESTIONS_FILE and os.path.exists(CUSTOM_QUESTIONS_FILE):
        try:
            with open(CUSTOM_QUESTIONS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data:
                IELTS_SPEAKING_QUESTIONS["Custom Questions"].update(data)
        except Exception:
            pass


def add_custom_test_set(test_name, part1_data=None, part2_data=None, part3_data=None, questions_data=None):
    """Add a new custom test set and save to JSON file."""
    global IELTS_SPEAKING_QUESTIONS
    data = {}
    if questions_data:
        data = questions_data
    else:
        if part1_data:
            data["Part 1 - Introduction & Interview"] = part1_data
        if part2_data:
            data["Part 2 - Individual Long Turn"] = part2_data
        if part3_data:
            data["Part 3 - Two-way Discussion"] = part3_data
    if not data:
        return False
    # Load existing
    existing = {}
    if os.path.exists(CUSTOM_QUESTIONS_FILE):
        try:
            with open(CUSTOM_QUESTIONS_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            pass
    existing[test_name] = data
    with open(CUSTOM_QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    # Update in-memory
    if "Custom Questions" not in IELTS_SPEAKING_QUESTIONS:
        IELTS_SPEAKING_QUESTIONS["Custom Questions"] = {}
    IELTS_SPEAKING_QUESTIONS["Custom Questions"][test_name] = data
    return True


def delete_custom_test_set(test_name):
    """Delete a custom test set from JSON file and in-memory dict."""
    global IELTS_SPEAKING_QUESTIONS
    if not os.path.exists(CUSTOM_QUESTIONS_FILE):
        return False
    try:
        with open(CUSTOM_QUESTIONS_FILE, "r", encoding="utf-8") as f:
            existing = json.load(f)
        if test_name in existing:
            del existing[test_name]
            with open(CUSTOM_QUESTIONS_FILE, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
        if "Custom Questions" in IELTS_SPEAKING_QUESTIONS:
            if test_name in IELTS_SPEAKING_QUESTIONS["Custom Questions"]:
                del IELTS_SPEAKING_QUESTIONS["Custom Questions"][test_name]
            if not IELTS_SPEAKING_QUESTIONS["Custom Questions"]:
                del IELTS_SPEAKING_QUESTIONS["Custom Questions"]
        return True
    except Exception:
        return False


def get_custom_test_names():
    """Return list of custom test set names."""
    if "Custom Questions" in IELTS_SPEAKING_QUESTIONS:
        return list(IELTS_SPEAKING_QUESTIONS["Custom Questions"].keys())
    return []


# Initialize custom questions on module load
_init_custom()
