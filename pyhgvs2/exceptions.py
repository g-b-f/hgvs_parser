class InvalidHGVSName(ValueError):
    def __init__(self, name="", part="name", reason=""):
        if name:
            message = f'Invalid HGVS {part} "{name}"'
        else:
            message = f"Invalid HGVS {part}"
        if reason:
            message += ": " + reason
        super(InvalidHGVSName, self).__init__(message)

        self.name = name
        self.part = part
        self.reason = reason
