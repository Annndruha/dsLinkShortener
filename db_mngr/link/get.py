
links = []

links.append({
    'id': 1,
    'alias': 'vk',
    'link': 'https://vk.com/dyakovri',
    'creator_id': 1,
    'visits': 0
})


def Get(alias):
    if links[0]['alias'] == alias:
        return links[0]
    else:
        return None