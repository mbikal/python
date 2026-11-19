test_settings = {
    'theme': 'dark',
    'language': 'english',
    'font_size': 'medium',
    'notifications': 'enabled'
}
def add_setting(settings, new_setting):
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: 
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_setting):
    key = new_setting[0].lower()
    value = new_setting[1].lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings: 
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else: 
        return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    else: 
        result = "Current User Settings:\n"
        for key, value in settings.items():
            result += f"{key.capitalize()}: {value}\n"

        return result

print(add_setting(test_settings, ('device','andriod')))
print(update_setting(test_settings, ('device','iOS')))
print(view_settings(test_settings))
print(test_settings)
