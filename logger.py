def log_user_action(user, action, details=""):
    with open("user_logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{user.id}] {user.first_name} {user.last_name or ''} - {action}: {details}\n")
