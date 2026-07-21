"""
IELTS Speaking Test Question Bank
Extracted from Cambridge IELTS 9-21 authentic tests
"""

import json, os


IELTS_SPEAKING_QUESTIONS = {

    "Cambridge 9": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Games",
                "questions": [
                    "What games are popular in your country? [Why?]",
                    "Do you play any games? [Why/Why not?]",
                    "How do people learn to play games in your country?",
                    "Do you think it\u2019s important for people to play games? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an open-air or street You will have to talk about the topic",
                "prompts": [
                    "market which you enjoyed visiting. for one to two minutes.",
                    "You have one minute to think about",
                    "what you are going to say.",
                    "You can make some notes to help",
                    "you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "clothes or old objects? Which type of market is more popular? Why?",
                    "Do you think markets are more suitable places for selling certain types of things? Which",
                    "ones? Why do you think this is?",
                    "Do you think young people feel the same about shopping at markets as older people?",
                    "What do you think are the advantages of buying things from shops rather than markets?",
                    "How does advertising influence what people choose to buy? Is this true for everyone?",
                    "shopping habits? Why is this?",
                    "To what extent do you agree or disagree?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Bicycles",
                "questions": [
                    "How popular are bicycles in your home town? [Why?]",
                    "How often do you ride a bicycle? [Why/Why not?]",
                    "Do you think that bicycles are suitable for all ages? [Why/Why not?]",
                    "What are the advantages of a bicycle compared to a car? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person who has done a lot of You will have to talk about the",
                "prompts": [
                    "work to help people. topic for one to two minutes.",
                    "You have one minute to think",
                    "about what you are going to",
                    "You can make some notes to",
                    "help you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are some of the ways people can help others in the community? Which is most",
                    "Why do you think some people like to help other people?",
                    "the past. Do you agree or disagree? Why?",
                    "who live in your area? Do you think there are enough of them?",
                    "Which groups of people generally need most support in a community? Why?",
                    "community? Should it be the government or individual people?",
                    "Which is the most suitable job for each person?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Telephoning",
                "questions": [
                    "How often do you make telephone calls? [Why/Why not?]",
                    "Who do you spend most time talking to on the telephone? [Why?]",
                    "When do you think you\u2019ll next make a telephone call? [Why?]",
                    "Do you sometimes prefer to send a text message instead of telephoning? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a journey [e.g. by car, You will have to talk about the topic",
                "prompts": [
                    "plane, boat] that you remember well. for one to two minutes.",
                    "You have one minute to think about",
                    "what you are going to say.",
                    "You can make some notes to help",
                    "you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why do people need to travel every day?",
                    "work or school? Why is this?",
                    "you agree or disagree? Why?",
                    "What do you think people can learn from travelling to other countries? Why?",
                    "Can travel make a positive difference to the economy of a country? How?",
                    "countries? In what ways?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Telephoning",
                "questions": [
                    "How often do you make telephone calls? [Why/Why not?]",
                    "Who do you spend most time talking to on the telephone? [Why?]",
                    "When do you think you\u2019ll next make a telephone call? [Why?]",
                    "Do you sometimes prefer to send a text message instead of telephoning? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a journey [e.g. by car, You will have to talk about the topic",
                "prompts": [
                    "plane, boat] that you remember well. for one to two minutes.",
                    "You have one minute to think about",
                    "what you are going to say.",
                    "You can make some notes to help",
                    "you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why do people need to travel every day?",
                    "work or school? Why is this?",
                    "you agree or disagree? Why?",
                    "What do you think people can learn from travelling to other countries? Why?",
                    "Can travel make a positive difference to the economy of a country? How?",
                    "countries? In what ways?",
                ]
            }
        },
    },

    "Cambridge 10": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Weekends",
                "questions": [
                    "How do you usually spend your weekends? [Why?]",
                    "Which is your favourite part of the weekend? [Why?]",
                    "Do you think your weekends are long enough? [Why/Why not?]",
                    "How important do you think it is to have free time at the weekends? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe someone you know who ~\u2014|_- You will have to talk about the topic for",
                "prompts": [
                    "does something well. | one to two minutes.",
                    ": Surin | You have one minute to think about",
                    "_ who this person is. ig | You can make some notes to help you",
                    "how you know this person if you wish.",
                    "what they do well",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What skills and abilities do people most want to have today? Why?",
                    "Which skills should children learn at school? Are there any skills which they should learn",
                    "at home? What are they?",
                    "Which skills do you think will be important in the future? Why?",
                    "Which kinds of jobs have the highest salaries in your country? Why is this?",
                    "Are there any other jobs that you think should have high salaries? Why do you think that?",
                    "you think about that? Why?",
                    "What is unusual about Brackenside pool?",
                    "What decision has not yet been made about the pool?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Music",
                "questions": [
                    "What types of music do you like to listen to? [Why?]",
                    "At what times of day do you like to listen to music? [Why?]",
                    "Did you learn to play a musical instrument when you were a child? [Why/Why not?]",
                    "Do you think all children should learn to play a musical instrument? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a shop near where you live You will have to talk about the topic for",
                "prompts": [
                    "that you sometimes use. one to two minutes.",
                    "You have one minute to think about",
                    "what sorts of product or You can make some notes to help you",
                    "service it sells if you wish.",
                    "what the shop looks like",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What types of local business are there in your neighbourhood? Are there any",
                    "restaurants, shops or dentists for example?",
                    "Do you think local businesses are important for a neighbourhood? In what way?",
                    "How do large shopping malls and commercial centres affect small local businesses?",
                    "Why do you think that is?",
                    "Why do some people want to start their own business?",
                    "Are there any disadvantages to running a business? Which is the most serious?",
                    "What are the most important qualities that a good business person needs? Why is that?",
                    "Which meal/s are required each day? 6",
                    "Which TWO things does Alice say about the Dolphin Conservation Trust?",
                    "13 Why is Alice so pleased the Trust has won the Charity Commission award?",
                    "Which dolphin does Alice make each of the following comments about?",
                    "Do you think this is a positive or negative development?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Travel",
                "questions": [
                    "Do you enjoy travelling? [Why/Why not?]",
                    "Have you done much travelling? [Why/Why not?]",
                    "Do you think it's better to travel alone or with other people? [Why?]",
                    "\u00a2 Where would you like to travel in the future? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a child that you know. You will have to talk about the",
                "prompts": [
                    "topic for one to two minutes.",
                    "who this child is and how often you about what you are going",
                    "see him or her to say.",
                    "how old this child is You can make some notes to",
                    "what he or she is like help you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "How much time do children spend with their parents in your country? Do you think that",
                    "parents and children? Why?",
                    "Have relationships between parents and children changed in recent years? Why do you",
                    "What are the most popular free-time activities with children today?",
                    "Do you think the free-time activities children do today are good for their health? Why is that?",
                    "How do you think children\u2019s activities will change in the future? Will this be a",
                    "positive change? 79",
                    "Why did a port originally develop at Manham?",
                    "What caused Manham\u2019s sudden expansion during the Industrial Revolution?",
                    "Why did rocks have to be sent away from Manham to be processed?",
                    "What happened when the port declined in the twentieth century?",
                    "What did the Manham Trust hope to do?",
                    "outweigh the disadvantages?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "School",
                "questions": [
                    "Did you go to secondary/high school near to where you lived? [Why/Why not?]",
                    "What did you like about your secondary/high school? [Why?]",
                    "Tell me about anything you didn\u2019t like at your school.",
                    "How do you think your school could be improved? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe something you don\u2019t have now but You will have to talk about the",
                "prompts": [
                    "would really like to own in the future. topic for one to two minutes.",
                    "You have one minute to think",
                    "what this thing is to say.",
                    "how long you have wanted to own it You can make some notes to",
                    "where you first saw it help you if you wish.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What types of things do young people in your country most want to own today?",
                    "Why do some people feel they need to own things?",
                    "Do you think that owning lots of things makes people happy? Why?",
                    "Do you think television and films can make people want to get new possessions?",
                    "Why do they have this effect?",
                    "Are there any benefits to society of people wanting to get new possessions?",
                    "Why do you think this is?",
                    "in the future? Why?",
                    "Do the following statements agree with the information given in the text on page 104?",
                    "Australian menu? Not only can you enjoy",
                    "leading Australian singer?",
                ]
            }
        },
    },

    "Cambridge 11": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Names",
                "questions": [
                    "\u00a2 How did your parents choose your name(s)?",
                    "Does your name have any special meaning?",
                    "Is your name common or unusual in your country?",
                    "If you could change your name, would you? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a TV documentary you watched You will have to talk about the",
                "prompts": [
                    "that was particularly interesting. topic for one to two minutes.",
                    "You have one minute to think",
                    "what the documentary was about You can make some notes to",
                    "why you decided to watch it help you if you wish.",
                    "what you learnt during the documentary",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular kinds of TV programmes in your country? Why is this?",
                    "Do you think there are too many game shows on TV nowadays? Why?",
                    "Do you think TV is the main way for people to get the news in your country? What other",
                    "What types of products are advertised most often on TV?",
                    "Do you think that people pay attention to adverts on TV? Why do you think that is?",
                    "How important are regulations on TV advertising?",
                ]
            }
        },
    },

    "Cambridge 12": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Health",
                "questions": [
                    "\u00a2 Is it important to you to eat healthy food? [Why?/Why not?]",
                    "\u00a2 If you catch a cold, what do you do to help you feel better? [Why?]",
                    "\u00a2 Do you pay attention to public information about health? [Why?/Why not?]",
                    "\u00ab What could you do to have a healthier lifestyle?",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an occasion when you had to wait You will have to talk about the",
                "prompts": [
                    "a long time for someone or something to topic for one to two minutes.",
                    "arrive. You have one minute to think",
                    "about what you are going to say.",
                    "who or what you were waiting for help you if you wish.",
                    "how long you had to wait",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "In what kinds of situations should people always arrive early?",
                    "How important it is to arrive early in your country?",
                    "How can modern technology help people to arrive early?",
                    "What kinds of jobs require the most patience?",
                    "ls it always better to be patient in work (or studies)?",
                    "Do you agree or disagree that the older people are, the more patient they are?",
                    "How much will they pay per night for a double room at the hotel?",
                    "What type of restaurant will they go to on Tuesday evening?",
                    "Who will they meet on Wednesday afternoon?",
                    "What does the man say about the play on each of the following days?",
                    "Do the advantages of this situation outweigh the disadvantages?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Songs and singing",
                "questions": [
                    "Did you enjoy singing when you were younger? [Why?/Why not?]",
                    "How often do you sing now? [Why?]",
                    "Do you have a favourite song you like listening to? [Why?/Why not?]",
                    "How important is singing in your culture? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a film/movie actor from your country | You will have to talk about the",
                "prompts": [
                    "who is very popular. topic for one to two minutes.",
                    "You have one minute to think",
                    "who this actor is You can make some notes to",
                    "what kinds of films/movies he/she acts in help you if you wish.",
                    "what you know about this actor\u2019s life",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular types of films in your country?",
                    "Do you think cinemas will close in the future?",
                    "How important is the theatre in your country\u2019s history?",
                    "How strong a tradition is it today in your country to go to the theatre?",
                    "Do you think the theatre should be run as a business or as a public service?",
                    "Which TWO age groups are taking increasing numbers of holidays with BC Travel?",
                    "Which TWO are the main reasons given for the popularity of activity holidays?",
                    "15 How does BC Travel plan to expand the painting holidays?",
                    "16 Why are BC Travel\u2019s cooking holidays unusual?",
                    "17 What does the speaker say about the photography holidays?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Clothes",
                "questions": [
                    "Where do you buy most of your clothes? [Why?]",
                    "How often do you buy new clothes for yourself? [Why?]",
                    "How do you decide which clothes to buy? [Why?]",
                    "Have the kinds of clothes you like changed in recent years? [Why?/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an interesting discussion you You will have to talk about the",
                "prompts": [
                    "had about how you spend your money. topic for one to two minutes.",
                    "You have one minute to think",
                    "who you had the discussion with You can make some notes to",
                    "why you discussed this topic help you if you wish.",
                    "what the result of the discussion was",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why do some parents give their children money to spend each week?",
                    "Do you agree that schools should teach children how to manage money?",
                    "Do you think it is a good idea for students to earn money while studying?",
                    "Do you think it is true that in today\u2019s society money cannot buy happiness?",
                    "Do you think richer countries have a responsibility to help poorer countries?",
                    "Which is the most rapidly-growing group of residents in the Sheepmarket area?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Art",
                "questions": [
                    "Did you enjoy doing art lessons when you were a child? [Why?/Why not?]",
                    "Do you ever draw or paint pictures now? [Why?/Why not?]",
                    "\u00ab When was the last time you went to an art gallery or exhibition? [Why?]",
                    "What kind of pictures do you like having in your home? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you visited a friend You will have to talk about the",
                "prompts": [
                    "or family member at their workplace. topic for one to two minutes.",
                    "You have one minute to think",
                    "who you visited You can make some notes to",
                    "where this person worked help you if you wish.",
                    "why you visited this person\u2019s",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What things make an office comfortable to work in?",
                    "Why do some people prefer to work outdoors?",
                    "What would life be like if people didn\u2019t have to work?",
                    "Are all jobs of equal importance?",
                    "Why do some people become workaholics?",
                    "Hi. Can | help you?",
                    "Sure. How about taking your family for a cruise? We have a steamship that Example",
                    "That sounds interesting. How long is the trip?",
                    "OK. And | assume there\u2019s a caf\u00e9 or something on board?",
                    "Sure. How old are your children?",
                    "Do you think he\u2019d manage it? He hasn\u2019t done that before.",
                    "OK. Well that all sounds good. And can we get lunch there? Q4",
                    "So is there anything else to do over on that side of the lake?",
                    "What's the trail like in terms of difficulty?",
                    "lll just make a note of that \u2014 er, how do you spell it?",
                    "VISITOR: Yeah. So what sort of prices are we looking at here?",
                    "altogether. Oh, wait a minute, how old did you say your daughter was?",
                    "understand that none of you\u2019ve had any previous experience as kitchen assistants? Well,",
                    "two of you here who are under 18 \u2014 that\u2019s Emma and Jake, isn\u2019t it? Right, so for you two, the",
                    "thought of an angle yet?",
                    "sTewaRT: Right. Well, shall we just brainstorm a few ideas, to get started?",
                    "copyright, aren\u2019t they? And copyright in this country lasts for 70 years after the",
                ]
            }
        },
    },

    "Cambridge 13": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Television programmes",
                "questions": [
                    "+ Where do you usually watch TV programmes/shows? [Why?/Why not?]",
                    "+ What's your favourite TV programme/show? [Why?]",
                    "+ Are there any programmes/shows you don't like watching? [Why?/Why not?]",
                    "Do you think you will watch more TV or fewer TV programmes/shows in the future?",
                    "[Why?/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe someone you know who has started a You will have to talk",
                "prompts": [
                    "business. about the topic for one",
                    "to two minutes. You",
                    "who this person is think about what you",
                    "what work this person does are going to say. You",
                    "why this person decided to start a business can make some notes",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of jobs do young people not want to do in your country?",
                    "Who is best at advising young people about choosing a job: teachers or parents?",
                    "Is money always the most important thing when choosing a job?",
                    "take less holiday?",
                    "What is the impact on society of people having a poor work-life balance?",
                    "ensure people have a good work-life balance? -",
                    "How much time for volunteering does the company allow per employee?",
                    "75 Where will the Digital Inclusion Day be held?",
                    "6 What should staff do if they want to take part in the Digital Inclusion Day?",
                    "What TWO things are mentioned about the participants on the last Digital Inclusion Day?",
                    "What TWO activities on the last Digital Inclusion Day did participants describe as useful?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Age",
                "questions": [
                    "~ Are you happy to be the age you are now? [Why/Why not?]",
                    "= When you were a child, did you think a lot about your future? [Why/Why not?]",
                    "= Do you think you have changed as you have got older? [Why/Why not?]",
                    "\u00bb~ What will be different about your life in the future? [Why]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you started using a new You will have to talk",
                "prompts": [
                    "technological device (e.g. a new computer or phone). about the topic for one",
                    "to two minutes. You",
                    "what device you started using think about what you",
                    "why you started using this device are going to say. You",
                    "how easy or difficult it was to use can make some notes",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What is the best age for children to start computer lessons?",
                    "Do you think that schools should use more technology to help children learn?",
                    "Do you agree or disagree that computers will replace teachers one day?",
                    "How much has technology improved how we communicate with each other?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Television programmes",
                "questions": [
                    "Where do you usually watch TV programmes/shows? [Why?/Why not?]",
                    "What's your favourite TV programme/show? [Why?]",
                    "Are there any programmes/shows you don't like watching? [Why?/Why not?]",
                    "Do you think you will watch more TV or fewer TV programmes/shows in the future?",
                    "[Why?/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe someone you know who has started a You will have to talk",
                "prompts": [
                    "business. about the topic for one",
                    "to two minutes. You",
                    "who this person is think about what you",
                    "what work this person does are going to say. You",
                    "why this person decided to start a business can make some notes",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of jobs do young people not want to do in your country?",
                    "Who is best at advising young people about choosing a job: teachers or parents?",
                    "Is money always the most important thing when choosing a job?",
                    "take less holiday?",
                    "What is the impact on society of people having a poor work-life balance?",
                    "ensure people have a good work-life balance? 9",
                    "What TWO things are mentioned about the participants on the last Digital Inclusion Day?",
                    "What TWO activities on the last Digital Inclusion Day did participants describe as useful?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Money",
                "questions": [
                    "_* When you go shopping, do you prefer to pay for things in cash or by card? [Why?]",
                    "+ Do you ever save money to buy special things? [Why/Why not?]",
                    "+ Would you ever take a job which had low pay? [Why/Why not?]",
                    "+ Would winning a lot of money make a big difference to your life? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an interesting discussion you had as part of You will have to talk",
                "prompts": [
                    "your work or studies. about the topic for one",
                    "to two minutes. You",
                    "what the subject of the discussion was think about what you",
                    "who you discussed the subject with are going to say. You",
                    "what opinions were expressed can make some notes",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why is it good to discuss problems with other people?",
                    "Do you think that it's better to talk to friends and not family about problems?",
                    "Is it always a good idea to tell lots of people about a problem?",
                    "with colleagues?",
                    "What are the possible effects of poor written communication skills at work?",
                ]
            }
        },
    },

    "Cambridge 14": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Future",
                "questions": [
                    "What job would you like to have ten years from now? [Why?]",
                    "How useful will English be for your future? [Why/Why not?]",
                    "How much travelling do you hope to do in the future? [Why/Why not?]",
                    "How do you think your life will change in the future? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a book that you enjoyed reading because You will have to talk",
                "prompts": [
                    "you had to think a lot. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular types of children\u2019s books in your country?",
                    "What are the benefits of parents reading books to their children?",
                    "Should parents always let children choose the books they read?",
                    "How popular are electronic books are in your country?",
                    "Will electronic books ever completely replace printed books in the future?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Social media",
                "questions": [
                    "Which social media websites do you use?",
                    "How much time do you spend on social media sites? [Why/Why not?]",
                    "What kind of information about yourself have you put on social media? [Why/Why not?]",
                    "Is there anything you don't like about social media? [Why?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe something you liked very much which You will have to talk",
                "prompts": [
                    "you bought for your home. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why do some people buy lots of things for their home?",
                    "Do you think it is very expensive to make a home look nice?",
                    "Why don\u2019t some people care about how their home looks?",
                    "In what ways is living in a flat/apartment better than living in a house?",
                    "Do you think homes will look different in the future?",
                    "Do you agree that the kinds of homes people prefer change as they get older?",
                    "Which TWO activities that volunteers do are mentioned?",
                    "Which TWO ways that volunteers can benefit from volunteering are mentioned?",
                    "What has each of the following volunteers helped someone to do?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Neighbours",
                "questions": [
                    "How often do you see your neighbours? [Why/Why not?]",
                    "Do you invite your neighbours to your home? [Why/Why not?]",
                    "Do you think you are a good neighbour? [Why/Why not?]",
                    "Has a neighbour ever helped you? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a very difficult task that you succeeded You will have to talk",
                "prompts": [
                    "in doing as part of your work or studies. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most difficult jobs that people do?",
                    "Why do you think some people choose to do difficult jobs?",
                    "Do you agree or disagree that all jobs are difficult sometimes?",
                    "How important is it for everyone to have a goal in their personal life?",
                    "Is it always necessary to work hard in order to achieve career success?",
                    "Do you think that successful people are always happy people?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Your neighbourhood",
                "questions": [
                    "Do you like the neighbourhood you live in? [Why/Why not?]",
                    "What do you do in your neighbourhood in your free time? [Why/Why not?]",
                    "What new things would you like to have in your neighbourhood? [Why/Why not?]",
                    "Would you like to live in another neighbourhood in your town or city? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a website you have bought something from. You will have to talk",
                "prompts": [
                    "about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of things do people in your country often buy from online shops?",
                    "Why has online shopping become so popular in many countries?",
                    "What are some possible disadvantages of buying things from online shops?",
                    "Will large shopping malls continue to be popular, despite the growth of internet shopping?",
                    "online in the future?",
                    "for apprentices?",
                    "Which paragraph contains the following information?",
                    "Do the following statements agree with the claims of the writer in Reading Passage 3?",
                ]
            }
        },
    },

    "Cambridge 15": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Questions 1-4",
                    "Complete the table below.",
                    "Write ONE WORD ONLY for each answer.",
                    "Festival information",
                    "Date Type of event Details",
                    "17th a concert performers from Canada",
                    "18th a ballet company called 1",
                    "19th\u201420th type of play: a comedy called Jemima",
                    "(afternoon) a play has had a good 2",
                    "20th (EVENING) \u2014 | AB assess show is called 4",
                    "Questions 5\u201410",
                    "Complete the notes below.",
                    "Write ONE WORD ONLY for each answer.",
                    "(children only) Making 6",
                    "(adults only) Making toys from 7",
                    "Outdoor activities",
                    "Swimming in the 8",
                    "Walking in the woods, led by an expert on 9",
                    "See the festival organiser\u2019s 10",
                    ">/@ p. 121 p. 101 31",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a hotel that you know. You will have to talk",
                "prompts": [
                    "about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What things are important when people are choosing a hotel?",
                    "Why do some people not like staying in hotels?",
                    "Do you think staying in a luxury hotel is a waste of money?",
                    "Do you think hotel work is a good career for life?",
                    "How does working in a big hotel compare with working in a small hotel?",
                    "What skills are needed to be a successful hotel manager?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "AMBER: Let me write that down \u2014 Becky ...",
                "questions": [
                    "AMBER? Hello William. This is Amber \u2014 you said to phone if | wanted to get more",
                    "information about the job agency you mentioned. Is now a good time?",
                    "WILLIAM: Oh, hi Amber. Yes. Fine. So the agency | was talking about is called Bankside \u2014",
                    "they're based in Docklands \u2014 | can tell you the address now \u2014 497 Eastside.",
                    "AMBER: OK, thanks. So is there anyone in particular | should speak to there?",
                    "WILLIAM: The agent | always deal with is called Becky Jamieson.",
                    "WILLIAM: Jamieson J-A-M-I-E-S-O-N. Qi",
                    "AMBER: Do you have her direct line?",
                    "WILLIAM: Yes, it's in my contacts somewhere \u2014 right, here we are: 078 double 6, 510 triple",
                    "| wouldn\u2019t call her until the afternoon if | were you \u2014 she\u2019s always really busy in Q2",
                    "the morning trying to fill last-minute vacancies. She\u2019s really helpful and friendly so",
                    "I\u2019m sure it would be worth getting in touch with her for an informal chat.",
                    "AMBER: It's mainly clerical and admin jobs they deal with, isn\u2019t it?",
                    "WILLIAM: That\u2019s right. | know you're hoping to find a full-time job in the media eventually \u2014",
                    "but Becky mostly recruits temporary staff for the finance sector \u2014 which will look",
                    "good on your CV \u2014 and generally pays better too.",
                    "AMBER: Yeah \u2014 I'm just a bit worried because | don\u2019t have much office experience.",
                    "WILLIAM: | wouldn't worry. They'll probably start you as a receptionist, or something like",
                    "that. So what's important for that kind of job isn\u2019t so much having business skills",
                    "or knowing lots of different computer systems \u2014 it's communication that really Q3",
                    "matters \u2014 so you'd be fine there. And you'll pick up office skills really quickly on",
                    "the job. It\u2019s not that complicated.",
                    "AMBER: OK good. So how long do people generally need temporary staff for? It would be",
                    "great if | could get something lasting at least a month.",
                    "WILLIAM: That shouldn't be too difficult. But you\u2019re more likely to be offered something for",
                    "a week at first, which might get extended. It's unusual to be sent somewhere for Q4",
                    "just a day or two.",
                    "AMBER: Right. I\u2019ve heard the pay isn\u2019t too bad \u2014 better than working in a shop or a",
                    "restaurant.",
                    "WILLIAM: Oh yes \u2014 definitely. The hourly rate is about \u00a310, 11 if you're lucky. Q5",
                    "AMBER: That's pretty good. | was only expecting to get eight or nine pounds an hour.",
                    "WILLIAM: Do you want me to tell you anything about the registration process?",
                    "AMBER: Yes, please. | know you have to have an interview.",
                    "WILLIAM: The interview usually takes about an hour and you should arrange that about a",
                    "week in advance.",
                    "AMBER: | suppose | should dress smartly if it\u2019s for office work \u2014 | can probably borrow a",
                    "suit from Mum. Q6",
                    "WILLIAM: Good idea. It\u2019s better to look too smart than too casual.",
                    "AMBER: Will | need to bring copies of my exam certificates or anything like that?",
                    "WILLIAM: No \u2014 they don't need to see those, | don\u2019t think.",
                    "AMBER: What about my passport?",
                    "WILLIAM: Oh yes \u2014 they will ask to see that.",
                    "WILLIAM: | wouldn\u2019t get stressed about the interview though. It\u2019s just a chance for them to",
                    "build a relationship with you \u2014 so they can try and match you to a job which you'll",
                    "like. So there are questions about personality that they always ask candidates \u2014",
                    "fairly basic ones. And they probably won't ask anything too difficult like what your",
                    "plans are for the future.",
                    "AMBER: Hope not.",
                    "WILLIAM: Anyway, there are lots of benefits to using an agency \u2014 for example, the interview",
                    "will be useful because they'll give you feedback on your performance so you can",
                    "improve next time.",
                    "AMBER: And they'll have access to jobs which aren't advertised.",
                    "WILLIAM: Exactly \u2014 most temporary jobs aren't advertised.",
                    "AMBER: And | expect finding a temporary job this way takes a lot less time \u2014 it\u2019s much",
                    "asier than ringing up individual companies.",
                    "WILLIAM: Yes indeed. Well | think ...",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an interesting TV programme you watched",
                "prompts": [
                    "about a science topic. Youwill have to talk",
                    "what science topic this TV programme was to two minutes. You",
                    "about have one minute to",
                    "when you saw this TV programme think about what you",
                    "what you learnt from this TV programme are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "RUTH: Ed, how are you getting on with the reading for our presentation next week?",
                    "RUTH: Really? That's funny. There have been hundreds of studies on twins but mostly",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "Bankside Recruitment Agency",
                    "Address of agency: 497 Eastside, Docklands",
                    "Name of agent: Becky 1",
                    "Phone number: 07866 510333",
                    "\u2014_ Best to call her in the 2...",
                    "Typical jobs",
                    "Clerical and admin roles, mainly in the finance industry",
                    "Must have good 3 skills",
                    "Jobs are usually for at least one 4.",
                    "\u2014- Pay is usually 5 \u00a3",
                    "Registration process",
                    "=\u00a9Wear a6...",
                    "Must bring your 7",
                    "to the interview",
                    "to the interview",
                    "They will ask questions about each applicant\u2019s 8",
                    "Advantages of using an agency",
                    "you receive at interview will benefit you",
                    "Will get access to vacancies which are not advertised",
                    "is involved in applying for jobs",
                    "10 >(@ p.119|[B p.96",
                    "Questions 15-20",
                    "Complete the table below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "Timetable for Isle of Man holiday",
                    "Introduction by manager",
                    "Arrive Hotel dining room has view of the",
                    "Tynwald Exhibition and Peel 16 not 979.",
                    "train to Laxey; train to the",
                    "of Snaefell",
                    "Trip to Snaefell",
                    "transport and heritage sites.",
                    "Free time, then coach to Castletown",
                    "\u2014 former 20 has old",
                    "Take the 19",
                    "train from Douglas to Port Erin",
                    "Leave the island by ferry or plane",
                    "12 >(@p.119||8 p.97",
                    "Questions 27 and 28",
                    "Choose the correct letter, A, B or C.",
                    "27 What do the speakers say about the evidence relating to birth order and academic",
                    "A There is conflicting evidence about whether oldest children perform best in",
                    "intelligence tests.",
                    "B_ There is little doubt that birth order has less influence on academic",
                    "achievement than socio-economic status.",
                    "C Some studies have neglected to include important factors such as family size.",
                    "28 What does Ruth think is surprising about the difference in oldest children\u2019s",
                    "academic performance?",
                    "A itis mainly thanks to their roles as teachers for their younger siblings.",
                    "B_ The advantages they have only lead to a slightly higher level of achievement.",
                    "C_ The extra parental attention they receive at a young age makes little",
                    "difference.",
                    "Questions 29 and 30",
                    "Choose TWO letters, A-E.",
                    "Which TWO experiences of sibling rivalry do the speakers agree has been valuable",
                    "learning to share",
                    "learning to stand up for oneself",
                    "learning to be a good loser",
                    "learning to be tolerant",
                    "learning to say sorry",
                    "14 ->|@ p.119||@ p.98",
                    "READING PASSAGE 1",
                    "You should spend about 20 minutes on Questions 1-13, which are based on Reading",
                    "Passage 1 below.",
                    "Nutmeg \u2014 a valuable spice",
                    "The nutmeg tree, Myristica fragrans, is a large evergreen tree native to Southeast Asia. Until the late",
                    "18th century, it only grew in one place in the world: a small group of islands in the Banda Sea, part",
                    "of the Moluccas \u2014 or Spice Islands \u2014 in northeastern Indonesia. The tree is thickly branched with",
                    "dense foliage of tough, dark green oval leaves, and produces small, yellow, bell-shaped flowers and",
                    "pale yellow pear-shaped fruits. The fruit is encased in a fleshy husk. When the fruit is ripe, this husk",
                    "splits into two halves along a ridge running the length of the fruit. Inside is a purple-brown shiny seed,",
                    "2-3.cm long by about 2cm across, surrounded by a lacy red or crimson covering called an \u2018aril\u2019. These",
                    "are the sources of the two spices nutmeg and mace, the former being produced from the dried seed",
                    "and the latter from the aril.",
                    "Nutmeg was a highly prized and costly ingredient in European cuisine in the Middle Ages, and was",
                    "used as a flavouring, medicinal, and preservative agent. Throughout this period, the Arabs were the",
                    "xclusive importers of the spice to Europe. They sold nutmeg for high prices to merchants based in",
                    "Venice, but they never revealed the exact location of the source of this extremely valuable commodity.",
                    "The Arab-Venetian dominance of the trade finally ended in 1512, when the Portuguese reached the",
                    "Banda Islands and began exploiting its precious resources.",
                    "Always in danger of competition from neighbouring Spain, the Portuguese began subcontracting",
                    "their spice distribution to Dutch traders. Profits began to flow into the Netherlands, and the Dutch",
                    "commercial fleet swiftly grew into one of the largest in the world. The Dutch quietly gained control",
                    "of most of the shipping and trading of spices in Northern Europe. Then, in 1580, Portugal fell under",
                    "Spanish rule, and by the end of the 16th century the Dutch found themselves locked out of the market.",
                    "As prices for pepper, nutmeg, and other spices soared across Europe, they decided to fight back.",
                    "In 1602, Dutch merchants founded the VOC, a trading corporation better known as the Dutch East",
                    "India Company. By 1617, the VOC was the richest commercial operation in the world. The company",
                    "had 50,000 employees worldwide, with a private army of 30,000 men and a fleet of 200 ships. At",
                    "the same time, thousands of people across Europe were dying of the plague, a highly contagious and",
                    "deadly disease. Doctors were desperate for a way to stop the spread of this disease, and they decided",
                    "nutmeg held the cure. Everybody wanted nutmeg, and many were willing to spare no expense to",
                    "have it. Nutmeg bought for a few pennies in Indonesia could be sold for 68,000 times its original cost",
                    "on the streets of London. The only problem was the short supply. And that\u2019s where the Dutch found",
                    "their opportunity.",
                    "Questions 1-4",
                    "Complete the notes below.",
                    "Choose ONE WORD ONLY from the passage for each answer.",
                    "Write your answers in boxes 1\u20144 on your answer sheet.",
                    "The nutmeg tree and fruit",
                    "the leaves of the tree are 1 in shape",
                    "... Surrounds the fruit and breaks open when the fruit",
                    "\u2014 the covering known as the aril is used to produce 4",
                    "is used to produce the spice nutmeg",
                    "the tree has yellow flowers and fruit",
                    "Questions 5-7",
                    "Do the following statements agree with the information given in Reading Passage 1?",
                    "In boxes 5-7 on your answer sheet, write",
                    "TRUE if the statement agrees with the information",
                    "FALSE if the statement contradicts the information",
                    "NOT GIVEN if there is no information on this",
                    "5 In the Middle Ages, most Europeans knew where nutmeg was grown.",
                    "6 The VOC was the world\u2019s first major trading company.",
                    "7 Following the Treaty of Breda, the Dutch had control of all the islands where",
                    "nutmeg grew.",
                    "READING PASSAGE 2",
                    "You should spend about 20 minutes on Questions 14-26, which are based on Reading",
                    "Passage 2 below.",
                    "Driverless cars",
                    "The automotive sector is well used to adapting to automation in manufacturing.",
                    "The implementation of robotic car manufacture from the 1970s onwards led to",
                    "significant cost savings and improvements in the reliability and flexibility of vehicle",
                    "mass production. A new challenge to vehicle production is now on the horizon",
                    "and, again, it comes from automation. However, this time it is not to do with the",
                    "manufacturing process, but with the vehicles themselves.",
                    "Research projects on vehicle automation are not new. Vehicles with limited self-",
                    "driving capabilities have been around for more than 50 years, resulting in significant",
                    "contributions towards driver assistance systems. But since Google announced in",
                    "2010 that it had been trialling self-driving cars on the streets of California, progress",
                    "in this field has quickly gathered pace.",
                    "There are many reasons why technology is advancing so fast. One frequently cited",
                    "motive is safety; indeed, research at the UK\u2019s Transport Research Laboratory has",
                    "demonstrated that more than 90 percent of road collisions involve human error as a",
                    "contributory factor, and it is the primary cause in the vast majority. Automation may",
                    "help to reduce the incidence of this.",
                    "Another aim is to free the time people spend driving for other purposes. If the",
                    "vehicle can do some or all of the driving, it may be possible to be productive, to",
                    "socialise or simply to relax while automation systems have responsibility for safe",
                    "control of the vehicle. If the vehicle can do the driving, those who are challenged",
                    "by existing mobility models \u2014 such as older or disabled travellers \u2014 may be able to",
                    "njoy significantly greater travel autonomy.",
                    "Beyond these direct benefits, we can consider the wider implications for transport",
                    "and society, and how manufacturing processes might need to respond as a",
                    "result. At present, the average car spends more than 90 percent of its life parked.",
                    "Automation means that initiatives for car-sharing become much more viable,",
                    "particularly in urban areas with significant travel demand. If a significant proportion",
                    "of the population choose to use shared automated vehicles, mobility demand can",
                    "be met by far fewer vehicles.",
                    "The Massachusetts Institute of Technology investigated automated mobility in",
                    "Singapore, finding that fewer than 30 percent of the vehicles currently used would",
                    "be required if fully automated car sharing could be implemented. If this is the case,",
                    "it might mean that we need to manufacture far fewer vehicles to meet demand.",
                    "Questions 14-18",
                    "Reading Passage 2 has seven sections, A-G.",
                    "Which section contains the following information?",
                    "Write the correct letter, A-G, in boxes 14-18 on your answer sheet.",
                    "14 reference to the amount of time when a car is not in use",
                    "15 mention of several advantages of driverless vehicles for individual road-users",
                    "16 reference to the opportunity of choosing the most appropriate vehicle for each trip",
                    "17 an estimate of how long it will take to overcome a number of problems",
                    "18 asuggestion that the use of driverless cars may have no effect on the number of",
                    "vehicles manufactured",
                    "Questions 19-22",
                    "Complete the summary below.",
                    "Choose NO MORE THAN TWO WORDS from the passage for each answer.",
                    "Write your answers in boxes 19-22 on your answer sheet.",
                    "The impact of driverless cars",
                    "Figures from the Transport Research Laboratory indicate that most motor accidents",
                    "are partly due to 19 , So the introduction of driverless vehicles",
                    "will result in greater safety. In addition to the direct benefits of automation, it may bring",
                    "will be more",
                    "other advantages. For example, schemes for 20........",
                    "workable, especially in towns and cities, resulting in fewer cars on the road.",
                    "According to the University of Michigan Transportation Research Institute, there could",
                    "of cars. However, this would mean",
                    "... of each car would, on average, be twice as",
                    "be a 43 percent drop in 21",
                    "that the yearly 22",
                    "high as it currently is. This would lead to a higher turnover of vehicles, and therefore no",
                    "reduction in automotive manufacturing.",
                    "READING PASSAGE 3",
                    "You should spend about 20 minutes on Questions 27-40, which are based on Reading",
                    "Passage 3 below.",
                    "What is exploration?",
                    "We are all explorers. Our desire to discover, and then share that new-found knowledge, is part",
                    "of what makes us human \u2014 indeed, this has played an important part in our success as a species.",
                    "Long before the first caveman slumped down beside the fire and grunted news that there were",
                    "plenty of wildebeest over yonder, our ancestors had learnt the value of sending out scouts to",
                    "investigate the unknown. This questing nature of ours undoubtedly helped our species spread",
                    "around the globe, just as it nowadays no doubt helps the last nomadic Penan maintain their",
                    "xistence in the depleted forests of Borneo, and a visitor negotiate the subways of New York.",
                    "Over the years, we\u2019ve come to think of explorers as a peculiar breed \u2014 different from the rest of",
                    "us, different from those of us who are merely \u2018well travelled\u2019, even; and perhaps there is a type of",
                    "person more suited to seeking out the new, a type of caveman more inclined to risk venturing out.",
                    "That, however, doesn\u2019t take away from the fact that we all have this enquiring instinct, even today;",
                    "and that in all sorts of professions \u2014 whether artist, marine biologist or astronomer \u2014 borders of",
                    "the unknown are being tested each day.",
                    "Thomas Hardy set some of his novels in Egdon Heath, a fictional area of uncultivated land, and",
                    "used the landscape to suggest the desires and fears of his characters. He is delving into matters",
                    "we all recognise because they are common to humanity. This is surely an act of exploration, and",
                    "into a world as remote as the author chooses. Explorer and travel writer Peter Fleming talks of",
                    "the moment when the explorer returns to the existence he has left behind with his loved ones. The",
                    "traveller \u2018who has for weeks or months seen himself only as a puny and irrelevant alien crawling",
                    "laboriously over a country in which he has no roots and no background, suddenly encounters his",
                    "other self, a relatively solid figure, with a place in the minds of certain people\u2019.",
                    "In this book about the exploration of the earth\u2019s surface, I have confined myself to those whose",
                    "travels were real and who also aimed at more than personal discovery. But that still left me with",
                    "another problem: the word \u2018explorer\u2019 has become associated with a past era. We think back to a",
                    "golden age, as if exploration peaked somehow in the 19th century \u2014 as if the process of discovery",
                    "is now on the decline, though the truth is that we have named only one and a half million of this",
                    "planet\u2019s species, and there may be more than 10 million \u2014 and that\u2019s not including bacteria. We",
                    "have studied only 5 per cent of the species we know. We have scarcely mapped the ocean floors,",
                    "and know even less about ourselves; we fully understand the workings of only 10 per cent of our",
                    "Questions 27-32",
                    "Choose the correct letter, A, B, C or D.",
                    "Write the correct letter in boxes 27-32 on your answer sheet.",
                    "27 The writer refers to visitors to New York to illustrate the point that",
                    "A __ exploration is an intrinsic element of being human.",
                    "B_ most people are enthusiastic about exploring.",
                    "C exploration can lead to surprising results.",
                    "D__ most people find exploration daunting.",
                    "28 According to the second paragraph, what is the writer\u2019s view of explorers?",
                    "A Their discoveries have brought both benefits and disadvantages.",
                    "B_ Their main value is in teaching others.",
                    "C_ They act on an urge that is common to everyone.",
                    "D They tend to be more attracted to certain professions than to others.",
                    "29 The writer refers to a description of Egdon Heath to suggest that",
                    "A Hardy was writing about his own experience of exploration.",
                    "B_ Hardy was mistaken about the nature of exploration.",
                    "C_Hardy\u2019s aim was to investigate people\u2019s emotional states.",
                    "D Hardy's aim was to show the attraction of isolation.",
                    "30 In the fourth paragraph, the writer refers to \u2018a golden age\u2019 to suggest that",
                    "A __ the amount of useful information produced by exploration has decreased.",
                    "B__ fewer people are interested in exploring than in the 19th century.",
                    "C recent developments have made exploration less exciting.",
                    "D_ we are wrong to think that exploration is no longer necessary.",
                    "31 In the sixth paragraph, when discussing the definition of exploration, the writer",
                    "argues that",
                    "A people tend to relate exploration to their own professional interests.",
                    "B certain people are likely to misunderstand the nature of exploration.",
                    "C__ the generally accepted definition has changed over time.",
                    "D historians and scientists have more valid definitions than the general public.",
                    "32 In the last paragraph, the writer explains that he is interested in",
                    "how someone\u2019s personality is reflected in their choice of places to visit.",
                    "the human ability to cast new light on places that may be familiar.",
                    "how travel writing has evolved to meet changing demands.",
                    "the feelings that writers develop about the places that they explore.",
                    "WRITING TASK 1",
                    "You should spend about 20 minutes on this task.",
                    "The chart below shows the results of a survey about people\u2019s coffee and tea",
                    "buying and drinking habits in five Australian cities.",
                    "Summarise the information by selecting and reporting the main features, and",
                    "make comparisons where relevant.",
                    "Write at least 150 words.",
                    "Coffee and tea buying and drinking habits in five cities in Australia",
                    "Percentage of city residents",
                    "Sydney Melbourne Brisbane Adelaide Hobart",
                    "IB Bought fresh coffee in last 4 weeks",
                    "ieee Bought instant coffee in last 4 weeks",
                    "[BB Went to a caf\u00e9 for coffee or tea in last 4 weeks",
                    "28 = >|N p. 127",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an interesting TV programme you watched",
                "prompts": [
                    "about a science topic. Youwill have to talk",
                    "what science topic this TV programme was to two minutes. You",
                    "about have one minute to",
                    "when you saw this TV programme think about what you",
                    "what you learnt from this TV programme are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "How interested are most people in your country in science?",
                    "Why do you think children today might be better at science than their parents?",
                    "How do you suggest the public can learn more about scientific developments?",
                    "What do you think are the most important scientific discoveries in the last 100 years?",
                    "Do you agree or disagree that there are no more major scientific discoveries left to make?",
                    "Who should pay for scientific research \u2014 governments or private companies? 95",
                    "What does it mean?",
                    "Why are they unique?",
                    "WHAT IS THE TEST FORMAT?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Festival information",
                    "Questions 5-10",
                    "Complete the notes below.",
                    "Write ONE WORD ONLY for each answer.",
                    "Making 5....",
                    "\u00a2 Swimming in the 8",
                    "(children only) Making 6.........",
                    "Outdoor activities",
                    "\u2014 Walking in the woods, led",
                    "See the festival organiser\u2019s 10.......",
                    "sissies $OOE",
                    "(adults only) Making toys from 7...",
                    "by an expert on 9",
                    "Date Type of event Details",
                    "17th a concert performers from Canada",
                    "18th a ballet company called 1",
                    "49th-20th type of play: a comedy called Jemima",
                    "(afternoon) a play has had a good 2",
                    "20th (evening) a3... show is called 4.",
                    "mune USING Various tools",
                    "for more information",
                    ">/ p. 121 |[B p. 101",
                    "The same is true in transport engineering, which uses models to predict and shape the",
                    "way people move through the city. Again, these models are necessary, but they are built",
                    "on specific world views in which certain forms of efficiency and safety are considered",
                    "and other experiences of the city ignored. Designs that seem logical in models appear",
                    "counter-intuitive in the actual experience of their users. The guard rails that will be familiar",
                    "to anyone who has attempted to cross a British road, for example, were an engineering",
                    "solution to pedestrian safety based on models that prioritise the smooth flow of traffic. On",
                    "wide major roads, they often guide pedestrians to specific crossing points and slow down",
                    "their progress across the road by using staggered access points to divide the crossing into",
                    "two \u2014 one for each carriageway. In doing so they make crossings feel longer, introducing",
                    "psychological barriers greatly impacting those that are the least mobile, and encouraging",
                    "others to make dangerous crossings to get around the guard rails. These barriers don\u2019t",
                    "just make it harder to cross the road: they divide communities and decrease opportunities",
                    "for healthy transport. As a result, many are now being removed, causing disruption, cost,",
                    "If their designers had had the tools to think with their bodies \u2014 like dancers \u2014 and imagine",
                    "how these barriers would feel, there might have been a better solution. In order to bring",
                    "about fundamental changes to the ways we use our cities, engineering will need to develop",
                    "aricher understanding of why people move in certain ways, and how this movement affects",
                    "them. Choreography may not seem an obvious choice for tackling this problem. Yet it shares",
                    "with engineering the aim of designing patterns of movement within limitations of space.",
                    "It is an art form developed almost entirely by trying out ideas with the body, and gaining",
                    "instant feedback on how the results feel. Choreographers have deep understanding of the",
                    "psychological, aesthetic, and physical implications of different ways of moving.",
                    "Observing the choreographer Wayne McGregor, cognitive scientist David Kirsh described",
                    "how he \u2018thinks with the body\u2019. Kirsh argues that by using the body to simulate outcomes,",
                    "McGregor is able to imagine solutions that would not be possible using purely abstract",
                    "thought. This kind of physical knowledge is valued in many areas of expertise, but currently",
                    "has no place in formal engineering design processes. A suggested method for transport",
                    "ngineers is to improvise design solutions and get instant feedback about how they",
                    "would work from their own experience of them, or model designs at full scale in the way",
                    "choreographers experiment with groups of dancers. Above all, perhaps, they might learn to",
                    "design for emotional as well as functional effects.",
                    "Shared By Aykhan Quliyev",
                    "Link_Library",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a hotel that you know. You will have to talk",
                "prompts": [
                    "about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "where this hotel is",
                    "what this hotel looks like",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What things are important when people are choosing a hotel?",
                    "Why do some people not like staying in hotels?",
                    "Do you think staying in a luxury hotel is a waste of money?",
                    "Do you think hotel work is a good career for life?",
                    "How does working in a big hotel compare with working in a small hotel?",
                    "What skills are needed to be a successful hotel manager?",
                ]
            }
        },
    },

    "Cambridge 16": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "JUNIOR CYCLE CAMP |",
                    "The course focuses on skills and safety.",
                    "\u00a2 Charlie would be placed in Level 5.",
                    "_ First of all, children at this level are taken to practise in a 1....",
                    "Instructors",
                    "is required and training is given.",
                    "Instructors wear 2...",
                    "The size of the classes is limited.",
                    "\u2014 There are quiet times during the morning for a 4",
                    "Classes are held even if there is 5",
                    "What to bring",
                    "\u2014 achange of clothing",
                    "shoes (not sandals)",
                    "\u00b0  Charlie\u2019s 7",
                    "\u00a2 \u2014 Charlie should arrive at 9.20 am on the first day.",
                    "Before the class, his 8 \u00ab0.0.2.0... will be checked.",
                    "He should then go to the 9 to meet his class instructor.",
                    "\u2014 The course costs 10 $..",
                    ">| p. 125] /8 p.110] 55",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a review you read about a product or You will have to talk",
                "prompts": [
                    "service. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of things do people write online reviews about in your country?",
                    "Why do some people write online reviews?",
                    "Do you think that online reviews are good for both shoppers and companies?",
                    "What do you think it might be like to work in a customer service job?",
                    "Do you agree that customers are more likely to complain nowadays?",
                    "How important is it for companies to take all customer complaints seriously?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "Holiday rental",
                    "Owners\u2019 names: Jack Fitzgerald and Shirley Fitzgerald",
                    "Granary Cottage",
                    "available for week beginning 1.....",
                    "cost for the week: 2 \u00a3",
                    "\u00b0 cost for the week: \u00a3480",
                    "building was originally a 4.",
                    "\u2014 walk through doors from living room into a 5",
                    "several 6 spaces at the front",
                    "bathroom has a shower",
                    "central heating and stove that burns 7 ..",
                    "views of old 8 ..\u00ab from living room",
                    "from the bedroom",
                    "view of hilltop 9",
                    "deposit: \u00a3144",
                    "deadline for final payment: end of 10",
                    "READING PASSAGE 2",
                    "You should spend about 20 minutes on Questions 14-26, which are based on Reading",
                    "Passage 2 below.",
                    "Changes in reading habits",
                    "What are the implications of the way we read today?",
                    "Look around on your next plane trip. The iPad is the new pacifier for babies and toddlers. Younger",
                    "school-aged children read stories on smartphones; older kids don\u2019t read at all, but hunch over",
                    "video games. Parents and other passengers read on tablets or skim a flotilla of email and news",
                    "feeds. Unbeknown to most of us, an invisible, game-changing transformation links everyone",
                    "in this picture: the neuronal circuit that underlies the brain\u2019s ability to read is subtly, rapidly",
                    "changing and this has implications for everyone from the pre-reading toddler to the expert adult.",
                    "As work in neurosciences indicates, the acquisition of literacy necessitated a new circuit in our",
                    "species\u2019 brain more than 6,000 years ago. That circuit evolved from a very simple mechanism",
                    "for decoding basic information, like the number of goats in one\u2019s herd, to the present, highly",
                    "laborated reading brain. My research depicts how the present reading brain enables the",
                    "development of some of our most important intellectual and affective processes: internalized",
                    "knowledge, analogical reasoning, and inference; perspective-taking and empathy; critical analysis",
                    "and the generation of insight. Research surfacing in many parts of the world now cautions that",
                    "ach of these essential \u2018deep reading\u2019 processes may be under threat as we move into digital-",
                    "based modes of reading.",
                    "This is not a simple, binary issue of print versus digital reading and technological innovation. As",
                    "MIT scholar Sherry Turkle has written, we do not err as a society when we innovate but when",
                    "we ignore what we disrupt or diminish while innovating. In this hinge moment between print and",
                    "digital cultures, society needs to confront what is diminishing in the expert reading circuit, what",
                    "our children and older students are not developing, and what we can do about it.",
                    "We know from research that the reading circuit is not given to human beings through a genetic",
                    "blueprint like vision or language; it needs an environment to develop. Further, it will adapt to that",
                    "nvironment\u2019s requirements \u2014 from different writing systems to the characteristics of whatever",
                    "medium is used. If the dominant medium advantages processes that are fast, multi-task oriented",
                    "and well-suited for large volumes of information, like the current digital medium, so will the",
                    "reading circuit. As UCLA psychologist Patricia Greenfield writes, the result is that less attention",
                    "and time will be allocated to slower, time-demanding deep reading processes.",
                    "Increasing reports from educators and from researchers in psychology and the humanities bear",
                    "this out. English literature scholar and teacher Mark Edmundson describes how many college",
                    "students actively avoid the classic literature of the 19th and 20th centuries in favour of something",
                    "simpler as they no longer have the patience to read longer, denser, more difficult texts. We should",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a luxury item you would like to own in",
                "prompts": [
                    "the future.",
                    "what item you would like to own",
                    "what this item looks like",
                    "why you would like to own this item",
                    "explain whether you think you will ever own",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Which expensive items would many young people (in your country) like to buy?",
                    "people want to buy?",
                    "How difficult is it to become very rich in today\u2019s world?",
                    "Do you agree that money does not necessarily bring happiness?",
                    "In what ways might rich people use their money to help society?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": ", Questions 1-10",
                "questions": [
                    "COONOURWNH=",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe some technology (e.g. an app, phone,",
                "prompts": [
                    "software program) that you decided to stop using. You will-hawe to talk",
                    "about the topic for one",
                    "when and where you got this technology have one minute to",
                    "why you started using this technology think about what you",
                    "why you decided to stop using it are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of computer games do people play in your country?",
                    "Why do people enjoy playing computer games?",
                    "Do you think that all computer games should have a minimum age for players?",
                    "In what ways can technology in the classroom be helpful?",
                    "Do you agree that students are often better at using technology than their teachers?",
                    "Do you believe that computers will ever replace human teachers?",
                ]
            }
        },
    },

    "Cambridge 17": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Questions 1-7",
                    "Complete the notes below.",
                    "Write ONE WORD ONLY for each answer.",
                    "Opportunities for voluntary work in Southoe village",
                    "Help with 1 books (times to be arranged)",
                    "Help needed to keep 2 of books up to date",
                    "__ Library is in the 3 Room in the village hall",
                    "\u2014_ Help by providing 4",
                    "\u2014 Help with hobbies such as 5",
                    "Help for individuals needed next week",
                    "\u2014 Taking Mrs Carroll to 6",
                    "Work in the 7",
                    "Questions 8-10",
                    "Complete the table below.",
                    "Write ONE WORD ONLY for each answer.",
                    "Village social events",
                    "Date | Event Location Help needed",
                    "19 Oct |g .. Village hall providing refreshments",
                    "31 Dec | New Year\u2019s Eve party Mountfort Hotel designing the 10",
                    "2/0 p. 121 p. 101",
                    "lt dacebook.com/Goctienganh",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe the neighbourhood you lived in when You will have to talk",
                "prompts": [
                    "you were a child. about the topic for one",
                    "where in your town/city the neighbourhood was lave One C 39",
                    ". F think about what you",
                    "what kind of people lived there are qoina to say. Yo",
                    "what it was like to live in this neighbourhood going Ye TOU",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What sort of things can neighbours do to help each other?",
                    "How well do people generally know their neighbours in your country?",
                    "How important do you think it is to have good neighbours?",
                    "Which facilities are most important to people living in cities?",
                    "How does shopping in small local shops differ from shopping in large city centre shops?",
                    "Do you think that children should always go to the school nearest to where they live?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD AND/OR A NUMBER for each answer.",
                    "Advice on surfing holidays",
                    "Jack\u2019s advice",
                    "Recommends surfing for 1 holidays in the summer",
                    "Need to be quite 2",
                    "lrish surfing locations",
                    "County Clare",
                    "\u2014 Lahinch has some good quality 3 and surf schools",
                    "\u2014 There are famous cliffs nearby",
                    "County Mayo",
                    "\u2014 Good surf school at 4",
                    "\u2014 Surf camp lasts for one 5.......",
                    "\u2014 Can also explore the local 6",
                    "Best month to go: 7",
                    "Average temperature in summer: approx. 8 degrees",
                    "\u2014 Wetsuit and surfboard: 9 ....... euros per day",
                    "\u2014 Also advisable to hire 10 ....... .... for warmth",
                    "(\u00a9 p. 123] |S p. 107 ie,",
                    "lt dacebook.com/Goctienganh",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a big city you would like to visit. You will have to talk",
                "prompts": [
                    "about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most interesting things to do while visiting cities on holiday?",
                    "Why can it be expensive to visit cities on holiday?",
                    "Do you think it is better to visit cities alone or in a group with friends?",
                    "Why have cities increased in size in recent years?",
                    "What are the challenges created by ever-growing cities?",
                    "In what ways do you think cities of the future will be different to cities today?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD for each answer.",
                    "Easy Life Cleaning Services",
                    "Basic cleaning package offered",
                    "Cleaning all surfaces",
                    "Cleaning the 1... throughout the apartment",
                    "\u2014 Cleaning shower, sinks, toilet etc.",
                    "Additional services agreed",
                    "\u2014 Cleaning the 2",
                    "\u2014 Ironing clothes \u2014 3",
                    "Every month",
                    "\u2014 Cleaning all the 4",
                    "\u2014 Washing down the 5",
                    "Other possibilities",
                    "They can organise a plumber or an 6 if necessary.",
                    "\u2014 Aspecial cleaning service is available for customers who are allergic",
                    "Information on the cleaners",
                    "Before being hired, all cleaners have a background check carried out by",
                    "References are required.",
                    "All cleaners are given 9 for two weeks.",
                    "Customers send a 10 after each visit.",
                    ">/@ p. 125) |& p. 113 ens",
                    "lt dacebook.com/Goctienganh",
                    "Usually, each customer has one regular cleaner.",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a monument (e.g., a statue or sculpture) You will have to talk",
                "prompts": [
                    "that you like. about the topic for one",
                    ". to two minutes. You",
                    ". . have one minute to",
                    "what this monument is think about what",
                    "where this monument is are cng tO son ho",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of monuments do tourists in your country enjoy visiting?",
                    "Why do you think there are often statues of famous people in public places?",
                    "Do you agree that old monuments and buildings should always be preserved?",
                    "Why is architecture such a popular university subject?",
                    "In what ways has the design of homes changed in recent years?",
                    "To what extent does the design of buildings affect people\u2019s moods?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "PETER: Yes, I\u2019m Peter. I\u2019m the secretary.",
                "questions": [
                    "PETER: Hello?",
                    "JAN: Oh hello. My name\u2019s Jan. Are you the right person to talk to about the Buckworth",
                    "Conservation Group?",
                    "JAN: Good. I\u2019ve just moved to this area, and I\u2019m interested in getting involved. | was",
                    "in a similar group where | used to live. Could you tell me something about your",
                    "activities, please?",
                    "PETER: Of course. Well, we have a mixture of regular activities and special events. One",
                    "of the regular ones is trying to keep the beach free of litter. A few of us spend a Q1",
                    "couple of hours a month on it, and it\u2019s awful how much there is to clear. | wish",
                    "people would be more responsible and take it home with them.",
                    "JAN: | totally agree. I\u2019d be happy to help with that. Is it OK to take dogs? Q2",
                    "PETER: I\u2019m afraid not, as they\u2019re banned from the beach itself. You can take them along",
                    "the cliffs, though. And children are welcome.",
                    "JAN: Right.",
                    "PETER: We also manage a nature reserve, and there\u2019s a lot to do there all year round.",
                    "For example, because it\u2019s a popular place to visit, we spend a lot of time looking",
                    "after the paths and making sure they're in good condition for walking.",
                    "JAN? | could certainly help with that.",
                    "PETER: Good. And we have a programme of creating new habitats there. We've just",
                    "finished making and installing nesting boxes for birds to use, and next we're",
                    "going to work on encouraging insects \u2014 they're important for the biodiversity of Q3",
                    "the reserve.",
                    "JAN: They certainly are.",
                    "PETER: Oh, and we're also running a project to identify the different species of butterflies Q4",
                    "that visit the reserve. You might be interested in taking part in that.",
                    "JAN: Sure. | was involved in something similar where | used to live, counting all the",
                    "species of moths. I'd enjoy that.",
                    "PETER: Another job we're doing at the reserve is replacing the wall on the southern side, Q5",
                    "between the parking area and our woodshed. It was badly damaged in a storm",
                    "last month.",
                    "PETER Then as | said, we have a programme of events as well, both at the weekend,",
                    "and during the week.",
                    "JAN: Right. | presume you have guided walks? I'd like to get to know the local",
                    "countryside, as I\u2019m new to the area.",
                    "PETER Yes, we do. The next walk is to Ruston Island, a week on Saturday. We'll be",
                    "meeting in the car park at Dunsmore Beach at low tide \u2014 that\u2019s when the sands",
                    "are dry enough for us to walk to the island without getting wet. Q6",
                    "JAN: Sounds good.",
                    "lt dacebook.com/Goctienganh",
                    "PETER: The island\u2019s a great place to explore. It\u2019s quite small, and it\u2019s got a range of",
                    "habitats. It\u2019s also an ideal location for seeing seals just off the coast, or even on",
                    "JAN: OK. And is there anything we should bring, like a picnic, for instance?",
                    "PETER: Yes, do bring one, as it\u2019s a full-day walk. And of course it'll be wet walking across",
                    "and back, so make sure your boots are waterproof. Q7",
                    "JAN: | must buy a new pair \u2014 there\u2019s a hole in one of my current ones! Well, I\u2019d",
                    "definitely like to come on the walk.",
                    "PETER: Great. Then later this month we\u2019re having a one-day woodwork session in",
                    "Hopton Wood.",
                    "JAN: I've never tried that before. Is it OK for beginners to take part? Q8",
                    "PETER: Definitely. There'll be a couple of experts leading the session, and we keep the",
                    "number of participants down, so you'll get as much help as you need.",
                    "JAN: Excellent! I'd love to be able to make chairs.",
                    "PETER: That's probably too ambitious for one day! You'll be starting with wooden spoons, Q9",
                    "and of course learning how to use the tools. And anything you make is yours to",
                    "take home with you.",
                    "JAN: That sounds like fun. When is it?",
                    "PETER: It's on the 17th, from 10 a.m. until 3. There\u2019s a charge of \u00a335, including lunch, or Q10",
                    "\u00a340 if you want to camp in the wood.",
                    "JAN! | should think I'll come home the same day. Well, I'd certainly like to join the",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe an occasion when you had to do",
                "prompts": [
                    "oe You will have to talk",
                    "something in a hurry.",
                    "about the topic for one",
                    "what you had to do have one minute to",
                    "why you had to do this in a hurry think about what you",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "DIANA: On your own?",
                    "TIM: So were they bred for their meat?",
                ]
            }
        },
    },

    "Cambridge 18": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Questions 1-4",
                    "Complete the form below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "Wayside Camera Club",
                    "membership form",
                    "Name: Dan Green",
                    "Email address: dan1068@market.com",
                    "Home address: 52 coeeosttssssstsnrsineeeneene Street, Peacetown",
                    "Heard about us: from a2",
                    "Reasons for joining: to enter competitions",
                    "LOS sscssseiererceseisesvcasscoure",
                    "Type of membership: 4 voecssetnetnennenenennne Membership (\u00a330)",
                    "Questions 5-10",
                    "Complete the table below.",
                    "Write NO MORE THAN TWO WORDS for each answer.",
                    "Photography competitions",
                    "Title of competition Feedback to Dan",
                    ". .... | Ascene in the home The picture\u2019s composition was",
                    "\u2018Beautiful Sunsets\u2019 Scene must show attuuiiuiiunnee WS Wrong.",
                    "SOME 6 a eecrsseesssnssenesenetne",
                    "_.\u2019 | Scene must show The photograph was too",
                    ">/@ p. 123] [HB p. 109] 55",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a tourist attraction in your country that You will have to talk",
                "prompts": [
                    "you would recommend. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular museums and art galleries in ... / where you live?",
                    "Do you believe that all museums and art galleries should be free?",
                    "What kinds of things make a museum or art gallery an interesting place to visit?",
                    "Would you say that large numbers of tourists cause problems for local people?",
                    "What sort of impact can large holiday resorts have on the environment?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "MAN:",
                "questions": [
                    "Excuse me. Would you mind if | asked you some questions? We're doing a",
                    "survey on transport.",
                    "Yes, that\u2019s OK.",
                    "First of all, can | take your name?",
                    "Yes. It's Sadie Jones.",
                    "Thanks very much. And could | have your date of birth \u2014 just the year will do,",
                    "actually. Is that all right?",
                    "Yes, that\u2019s fine. It\u2019s 1991.",
                    "So next your postcode, please.",
                    "It's DW30 7YZ.",
                    "Great. Thanks. Is that in Wells?",
                    "No it\u2019s actually in Harborne \u2014 Wells isn\u2019t far from there, though.",
                    "| really like that area. My grandmother lived there when | was a kid.",
                    "Yes, it is nice.",
                    "Right, so now | want to ask you some questions about how you travelled here",
                    "today. Did you use public transport?",
                    "Yes. | came by bus.",
                    "OK. And that was today. It\u2019s the 24th of April, isn\u2019t it?",
                    "Isn't it the 25th? No, actually, you\u2019re right.",
                    "Ha ha. And what was the reason for your trip today? | can see you\u2019ve got some",
                    "shopping with you.",
                    "Yes. | did some shopping but the main reason | came here was to go to the",
                    "That\u2019s not much fun. Hope it was nothing serious.",
                    "No, it was just a check-up. It\u2019s fine.",
                    "Good. Do you normally travel by bus into the city centre?",
                    "Yes. | stopped driving in ages ago because parking was so difficult to find and it",
                    "costs so much.",
                    "The bus is much more convenient too. It only takes about 30 minutes.",
                    "That\u2019s good. So where did you start your journey?",
                    "At the bus stop on Claxby Street.",
                    "Is that C-L-A-X-B-Y?",
                    "That\u2019s right.",
                    "And how satisfied with the service are you? Do you have any complaints?",
                    "Well, as | said, it's very convenient and quick when it's on time, but this morning it",
                    "was late. Only about 10 minutes, but still.",
                    "Yes, | understand that\u2019s annoying. And what about the timetable? Do you have",
                    "any comments about that?",
                    "Mmm. | suppose | mainly use the bus during the day, but any time I\u2019ve been in",
                    "town in the evening \u2014 for dinner or at the cinema \u2014 I\u2019ve noticed you have to wait a",
                    "long time for a bus \u2014 there aren\u2019t that many.",
                    "Audioscripts",
                    "MAN: OK, thanks. So now I'd like to ask you about your car use.",
                    "SADIE: Well, | have got a car but | don\u2019t use it that often. Mainly just to go to the",
                    "supermarket. But that\u2019s about it really. My husband uses it at the weekends to go",
                    "to the golf club.",
                    "MAN: And what about a bicycle?",
                    "SADIE: | don\u2019t actually have one at the moment.",
                    "MAN: What about the city bikes you can rent? Do you ever use those?",
                    "SADIE: No \u2014 I\u2019m not keen on cycling there because of all the pollution. But | would like to",
                    "get a bike \u2014 it would be good to use it to get to work.",
                    "MAN: So why haven\u2019t you got one now?",
                    "SADIE: Well, | live in a flat \u2014 on the second floor and it doesn\u2019t have any storage \u2014 so",
                    "we'd have to leave it in the hall outside the flat.",
                    "MAN: | see. OK. Well, | think that\u2019s all ...",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you met someone who you",
                "prompts": [
                    "became good friends with.",
                    "who you met",
                    "when and where you met this person",
                    "what you thought about this person when you",
                    "first met",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "HUGO: Hi Chantal. What did you think of the talk, then?",
                    "HUGO: Oh \u2014 were the people beside you chatting or something?",
                    "HUGO: It's hard to see through people's heads. isn\u2019t it?",
                    "HUGO: Mmm. Overall, she had quite a strong message, didn\u2019t she?",
                ]
            }
        },
    },

    "Cambridge 19": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Questions 1-6",
                    "Complete the form below.",
                    "Write ONE WORD AND/OR A NUMBER for each answer.",
                    "Guitar Group",
                    "Coordinator:",
                    "First floor, Room T347",
                    "Time: Thursday morning at 5",
                    "Recommended website: \u2018The perfect 6 son",
                    "@cambridge_library",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a law that was introduced in your country You will have to talk",
                "prompts": [
                    "that you thought was a very good idea. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of rules are common in a school?",
                    "How important is it to have rules in a school?",
                    "What do you recommend should happen if children break school rules?",
                    "Can you suggest why many students decide to study law at university?",
                    "What are the key personal qualities needed to be a successful lawyer?",
                    "Do you agree that working in the legal profession is very stressful?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Questions 1-6",
                    "Complete the notes below.",
                    "Write ONE WORD ANDIOR A NUMBER for each answer.",
                    "Local food shops",
                    "Where to go",
                    "Kite Place \u2014 near the",
                    "Fish market",
                    "\u2014_ cross the 2 ..and turn right",
                    "best to go before 3....... pm, earlier than closing time",
                    "Organic shop",
                    "= called 4 *..",
                    "\u00b0 below a restaurant in the large, grey building",
                    "look for the large 5........",
                    "Supermarket",
                    "= take a... minibus, number 289",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person from your country who has won You will have to talk",
                "prompts": [
                    "a prize, award or medal. about the topic for one",
                    "to two minutes. You",
                    "have one minute to",
                    "think about what you",
                    "are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What types of school prizes do children in your country receive?",
                    "What do you think are the advantages of rewarding schoolchildren for good work?",
                    "than from teachers?",
                    "Do you think that some sportspeople (e.g., top footballers) are paid too much money?",
                    "Should everyone on a team get the same prize money when they win?",
                    "Do you agree with the view that, in sport, taking part is more important than winning?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": ", Questions 1-10",
                "questions": [
                    "11 / eleven (am)",
                    "SOCONOMAWN=",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a place you visited that has",
                "prompts": [
                    "beautiful views. You will have to talk",
                    "about the topic for one",
                    "where this place is have one minute to",
                    "when and why you visited it think about what you",
                    "what views you can see from this place are going to say. You",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "COLIN: You're making a vegan alternative to eggs, aren't you? Something that doesn't",
                    "use animal products?",
                    "MARIE: But you were using 3-D printing, weren't you, to make the paste into biscuits?",
                    "COLIN: Interesting. So just solid food?",
                    "However, archaeologists believe that this way of life at C\u00e9ide ceased abruptly. Why was this?",
                ]
            }
        },
    },

    "Cambridge 20": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "",
                "questions": [
                    "What do you think your best personal qualities are? [Why?]",
                    "Do you have the same personal qualities as your parents? [Why/Why not?)",
                    "What personal qualities are important to you in a friend? [Why?]",
                    "Do you think you have the personal qualities to be a good/successful leader? [Why/Why not?]",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a play or a film you have seen that you would like to see again with friends.",
                "prompts": [
                    "what play or film you\u2019d like to go to see again",
                    "who you would go with",
                    "what other people have said about this play or film",
                    "explain why you would like to see this play or film again with friends.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular kinds of plays or shows at theatres in your country?",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "",
                "questions": [
                    "What's your favourite fruit?",
                    "Are there any kinds of fruit that you don\u2019t like eating?",
                    "Do you like eating cooked food that has fruit in it?",
                    "Where\u2019s the best place to buy fruit where you live?",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you changed a plan you had made.",
                "prompts": [
                    "what your original plan was",
                    "why you changed it",
                    "what new plan you made",
                    "explain how you felt about changing your plan.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What kinds of plans do friends make together?",
                    "Do you think it\u2019s better to discuss future plans with friends or with family?",
                    "When making plans for the future, is it important not to copy friends?",
                    "Whyis it a good idea to get some work experience before deciding on a future career?",
                    "How easy do you think it is for people to change from one career to another?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": "",
                "questions": [
                    "Did you enjoy going to museums when you were a child?",
                    "Are there any interesting museums near where you live now?",
                    "Do you think it is best to go to museums by yourself or with friends?",
                    "4, When you visit another city or country, do you think it\u2019s important to go to a museum there?",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a piece of work you did for your job or your studies that you felt very satisfied with.",
                "prompts": [
                    "what this piece of work was",
                    "why you did this piece of work",
                    "who or what helped you to do this work",
                    "explain why you felt so satisfied with this piece of work.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are some aspects of people's lives that they can often be dissatisfied with?",
                    "Would you say that having ambitions in life is always a positive thing?",
                    "What do you believe the most important components are of a satisfying life?",
                    "What makes a job more satisfying: a high salary or having good colleagues?",
                    "Do you think people need to change jobs regularly if they want to stay satisfied at work?",
                    "Is it possible to find job satisfaction in all types of work?",
                    "Why did | feel satisfied? Well, it was partly because all the hard work paid off. | ended up getting a pretty good",
                ]
            },
        },
        "Test 4": {
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you had a long discussion about a news story.",
                "prompts": [
                    "what the news story was about",
                    "who you discussed this news story with",
                    "what people's opinions were",
                    "explain why you had such a long discussion about this news story.",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
        },
    },

    "Cambridge 21": {
        "Test 1": {
            "Part 1 - Introduction & Interview": {
                "topic": "WOMAN:",
                "questions": [
                    "Hello, Oyster Bay Sailing Club. How can | help you?",
                    "Oh hi. I'd like to find out about sailing courses for beginners.",
                    "No problem. Is it for yourself?",
                    "Yes. | had a look online but I\u2019m not sure which course would be best.",
                    "OK. Well you might be interested in our Taster Days?",
                    "So these are for people who've never sailed before - it's basically an",
                    "introduction to sailing to find out whether you enjoy it and want to carry on",
                    "And how much is that?",
                    "It's \u00a3120 for the day \u2014 but it's reduced to \u00a3110 each if there are two of you.",
                    "No, it would just be me.",
                    "Oh that's fine. You'd be in a small group, usually about eight people but no",
                    "more than ten \u2014 and everyone's always very friendly.",
                    "Uh huh. And are there any other suitable courses?",
                    "The other option is the Level 1 course. These are two-day weekend courses and",
                    "we run those all year round.",
                    "OK. And what do you learn on that course?",
                    "This is a mix of theory and practical skills. So you learn about things like the",
                    "weather, which is obviously really important and also the tides, as well as",
                    "learning basic sailing skills. You go out into the harbour in special training",
                    "dinghies for beginners, two people in each dinghy and an instructor. He or she",
                    "will make sure you understand everything you need to know about safety.",
                    "It sounds like hard work!",
                    "Yes, but you'll have a lot of fun too.",
                    "And the cost of that one is...?",
                    "\u00a3200. But it\u2019s a bit cheaper if you decide to join the club. There's a discount for",
                    "Well, I'm not sure about that yet.",
                    "You've got plenty of time to decide.",
                    "And does the cost include everything?",
                    "Yes, everything's included and you also get a really good dictionary explaining",
                    "all the sailing terminology. A lot of people struggle with this at first. It\u2019s got",
                    "lots of pictures, so I\u2019m sure you'd find it really helpful. And on completion of",
                    "the course you get a certificate. Then you're ready to move on to the Level 2",
                    "Sounds good.",
                    "| think that's all the info you need for now. Just a couple of general things.",
                    "For example, it's really important that you know how to swim.",
                    "Yes, I\u2019m pretty confident in the water.",
                    "Audioscripts",
                    "WOMAN: Great. The other thing | should tell you is that we provide wetsuits and life",
                    "jackets but you need to bring swimming trunks and some old trainers.",
                    "MAN: And a towel?",
                    "WOMAN: Yes definitely. And you might want to bring your own toiletries, things like shampoo.",
                    "MAN: OK. What about food and drink? Do | need to bring that or is there a caf\u00e9 at the",
                    "WOMAN: Yes, you can get sandwiches, cakes and snacks there. The food's pretty reasonable.",
                    "MAN: OK good. Well | think I\u2019m interested in the Level 1 course. But | know absolutely",
                    "nothing about sailing so is there anything | can do to prepare myself a bit?",
                    "WOMAN: | recommend you watch some videos we use for training. They're available",
                    "online. | can send you the link. They'll give you an idea of what to expect.",
                    "MAN: Perfect, thanks. That would be very helpful. Oh and just one other thing - I'll",
                    "be cycling to the club and will need somewhere to put valuables. I\u2019m just",
                    "wondering if there are lockers for people to use?",
                    "WOMAN: Yes, there are plenty in the changing rooms.",
                    "MAN: Great. OK well could you book me onto...",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe 2 person you know who is very You will have to talk",
                "prompts": [
                    "petitive. .",
                    "about the topic for 1 to",
                    "You should Say: . 2 minutes. You have",
                    "who this person is 1 minute to think about",
                    "what this person is competitive about what you are going to",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "That lecture from the visiting speaker yesterday was good, wasn\u2019t it?",
                    "The research project she described was impressive, wasn\u2019t it? I'd have thought",
                ]
            },
        },
        "Test 2": {
            "Part 1 - Introduction & Interview": {
                "topic": "Questions 1-10",
                "questions": [
                    "Complete the notes below.",
                    "Write ONE WORD AND/OR A NUMBER for each answer.",
                    "Ferry to Shetland Islands",
                    "Name of ferry company: . Ferries",
                    "Ferries depart seven times per . in summer",
                    "\u2014 Cost for four people with car: a little less than 3 \u00a3",
                    "Cancellation policy: receive a4 sen",
                    "(if cancelled a month in advance)",
                    "book one with a 5",
                    "luxury cabins have a TV",
                    "\u2014 Bring snacks and 6... for the children",
                    "is required for the dog kennels",
                    "Try to see 8... in the morning",
                    "If time, visit 9...",
                    ".. restaurant in a nearby village is recommended",
                    "54 = => |@ p. 121] | p. 107",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you read or heard something",
                "prompts": [
                    "that you thought was not true. You will have to talk",
                    "about the topic for 1 to",
                    "where you read/heard this 1 minute to think about",
                    "what you read/heard what you are going to",
                    "why you thought it was not true say. You can make some",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Do you think children are more honest than adults?",
                    "Why do adults tell children it\u2019s important to be honest?",
                    "Do you think there are sometimes good reasons for adults not to tell children the truth?",
                    "Are there any claims in advertisements that are sometimes not true?",
                    "completely accurate?",
                    "Do you think advertisements that are dishonest should be banned?",
                ]
            },
        },
        "Test 3": {
            "Part 1 - Introduction & Interview": {
                "topic": ", Questions 1-10",
                "questions": [
                    "hairdresser",
                    "CVONAOUAWN =",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a person you know who is very You will have to talk",
                "prompts": [
                    "ive to",
                    "competitive.",
                    "petitive: about the topic for 1 to",
                    "who this person is 1 minute to think about",
                    "what this person is competitive about what you are going to",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "Why are they unique?",
                ]
            },
        },
        "Test 4": {
            "Part 1 - Introduction & Interview": {
                "topic": "Hairstyles",
                "questions": [
                    "\u00a9 Where do you go to get a haircut?",
                    "\u00a9 Have you changed your hairstyle recently?",
                    "\u00a9 Would you ever change the colour of your hair?",
                    "\u00a9 Do you enjoy going to the hairdresser/barber?",
                ]
            },
            "Part 2 - Individual Long Turn": {
                "cue_card": "Describe a time when you used information for",
                "prompts": [
                    "tourists, for example from a guidebook or online. You will have to talk",
                    "about the topic for 1 to",
                    "where you got this information 1 minute to think about",
                    "what place this information was about what you are going to",
                    "what information you got say. You can make some",
                ],
                "follow_up": "You should speak for 1-2 minutes."
            },
            "Part 3 - Discussion": {
                "topic": "",
                "questions": [
                    "What are the most popular kinds of holidays for people from your country to go on?",
                    "Why do some people want to do absolutely nothing when they go away on holiday?",
                    "What are the kinds of tourist attraction that visitors to your country like to see?",
                    "Do you think tourist attractions such as museums should be free for local people to visit?",
                    "What can make a tourist attraction disappointing for visitors?",
                ]
            }
        },
    },

}

def get_all_topics():
    topics = []
    for book, tests in IELTS_SPEAKING_QUESTIONS.items():
        for test_name, parts in tests.items():
            for part_name, data in parts.items():
                if "topic" in data:
                    topics.append(data["topic"])
    return list(set(topics))

def get_test(book_name, test_name):
    if book_name in IELTS_SPEAKING_QUESTIONS:
        if test_name in IELTS_SPEAKING_QUESTIONS[book_name]:
            return IELTS_SPEAKING_QUESTIONS[book_name][test_name]
    return None

_custom_loaded = False

def _init_custom():
    global _custom_loaded, IELTS_SPEAKING_QUESTIONS
    if _custom_loaded:
        return
    _custom_loaded = True
    try:
        cfg = os.path.join(os.path.dirname(__file__), "custom_questions.json")
        if os.path.exists(cfg):
            with open(cfg, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data:
                IELTS_SPEAKING_QUESTIONS["Custom Questions"] = data
    except Exception:
        pass

def add_custom_test_set(test_name, part1_data=None, part2_data=None, part3_data=None, questions_data=None):
    global IELTS_SPEAKING_QUESTIONS
    _init_custom()
    if "Custom Questions" not in IELTS_SPEAKING_QUESTIONS:
        IELTS_SPEAKING_QUESTIONS["Custom Questions"] = {}
    entry = {}
    if part1_data:
        entry["Part 1 - Introduction & Interview"] = part1_data
    if part2_data:
        entry["Part 2 - Individual Long Turn"] = part2_data
    if part3_data:
        entry["Part 3 - Discussion"] = part3_data
    IELTS_SPEAKING_QUESTIONS["Custom Questions"][test_name] = entry
    _save_custom()

def delete_custom_test_set(test_name):
    global IELTS_SPEAKING_QUESTIONS
    _init_custom()
    if "Custom Questions" in IELTS_SPEAKING_QUESTIONS and test_name in IELTS_SPEAKING_QUESTIONS["Custom Questions"]:
        del IELTS_SPEAKING_QUESTIONS["Custom Questions"][test_name]
        _save_custom()

def get_custom_test_names():
    _init_custom()
    if "Custom Questions" in IELTS_SPEAKING_QUESTIONS:
        return list(IELTS_SPEAKING_QUESTIONS["Custom Questions"].keys())
    return []

def _save_custom():
    try:
        cfg = os.path.join(os.path.dirname(__file__), "custom_questions.json")
        if "Custom Questions" in IELTS_SPEAKING_QUESTIONS:
            with open(cfg, "w", encoding="utf-8") as f:
                json.dump(IELTS_SPEAKING_QUESTIONS["Custom Questions"], f, ensure_ascii=False, indent=2)
    except Exception:
        pass

_init_custom()
