def make_username(email: str):
    email_parts = email.split("@")
    name = email_parts[0]
    domain = email_parts[1]
    domain_parts = domain.split(".")
    domain = "".join(domain_parts[:-1])
    return f"{name}_{domain}".lower()
