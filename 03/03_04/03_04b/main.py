user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}
# Approach -1 by deleting key & value directly ('_' More risk)

def update_preferences(user_pref):
    for key in list(user_pref.keys()):
        if user_pref[key] is None:
            user_pref.pop(key)
    return user_pref

# Approach -2 by creating Another dict ('_' No risk, but we need to create new dict)

def update_preferences(user_pref):
    update_preferences = {}
    for key, value in user_pref.items():
        if value is not None:
            update_preferences[key] = value
    return update_preferences

# Approach -3 by Short-hand method or comprehend method

def update_preferences(user_pref):
    return {key:value for key, value in user_pref.items() if value is not None }

# def update_preferences(user_pref):
#     for key, value in user_preferences.items():
#         if value is None:
#          user_preferences.pop(key)
#     return user_pref


print(update_preferences(user_preferences))
