attributes = {}


class Context:
    def set(self, raw_key, value):
        # String key !
        key = str(raw_key)
        if key is None or value is None:
            # Check if key and value was given
            return
        # Update or create key-value
        attributes[key] = value

    def get(self, key):
        if key is None:
            # Error
            return
        if key in attributes.keys():
            return attributes[key]
