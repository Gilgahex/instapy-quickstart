""" Quickstart script for InstaPy usage with NLTK Synonym Generation"""
# imports
from nltk.corpus import wordnet as guru
from itertools import chain
import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = '' # <- enter username here
insta_password = ''  # <- enter password here


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    #Pick seedWords here
    seedWords = ['sky','earth','fire','live','living','flowers','travel','nature','sea','sun','wilderness','wild','spring','summer']
    tags = set()
    for seed in seedWords:
        synonyms = guru.synsets(seed)
        lemmas = set(chain.from_iterable( [word.lemma_names() for word in synonyms] ))
        #Sanitize lemmas before adding to tag set, people don't use ' and _ in hashtags
        for i in lemmas:
            i.replace('_','')
            i.replace("'",'')
        tags.update(lemmas)
    #Take random sample of 10 words in your set of hashtags
    sample = random.choice(tags, 10)
    session.like_by_tags(sample, amount=350)
