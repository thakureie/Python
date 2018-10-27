def is_valid_uuid(uuid):
     return bool(re.search(r"^[a-f\d{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}\
     -[a-f\d]{12}$", uuid, re.IGNORECASE))
