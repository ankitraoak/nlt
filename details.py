import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

# Split the AUTH_USERS string and convert each part to an integer
auth_users_str = os.environ.get("AUTH_USERS")
auth_users_list = auth_users_str.split(', ')
auth_users = [int(user) for user in auth_users_list]

sudo_user = int(os.environ.get("SUDO_USERS"))
log_channel = int(os.environ.get("GROUPS"))

# Now you can use the 'auth_users' list as needed
print(f"API ID: {api_id}")
print(f"API Hash: {api_hash}")
print(f"Bot Token: {bot_token}")
print(f"Authorized Users: {auth_users}")
print(f"Sudo User: {sudo_user}")
print(f"Log Channel: {log_channel}")
