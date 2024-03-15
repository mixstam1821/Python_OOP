import random

story_parts = {
    'time': ['A long time ago', 'In the distant future', 'During the Middle Ages', 'At the dawn of civilization', 'In the year 3000'],
    'character': ['a hero', 'a villain', 'a wise sage', 'a fearless adventurer', 'a humble peasant'],
    'name': ['Arthur', 'Eleanor', 'Galahad', 'Isolde', 'Merlin'],
    'location': ['a magical kingdom', 'a distant land', 'a hidden village', 'an enchanted forest', 'a bustling city'],
    'activity': ['sought a legendary artifact', 'defeated a mighty dragon', 'discovered an ancient prophecy', 'befriended a mythical creature', 'unraveled a dark mystery']
}

selected_story_parts = {key: random.choice(value) for key, value in story_parts.items()}

story = f"{selected_story_parts['time']}, {selected_story_parts['character']} named {selected_story_parts['name']} embarked on a journey to {selected_story_parts['location']} where they {selected_story_parts['activity']}"

print(story)
