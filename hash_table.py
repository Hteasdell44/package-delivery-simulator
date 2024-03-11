class HashTable:
    
    def __init__(self):
        # Initialize the hash table with 20 empty buckets
        self.bucket_list = [[] for _ in range(20)]

    def insert(self, key, item):
        # Calculate the index to determine the bucket for the given key
        index = hash(key) % len(self.bucket_list)
        current_bucket = self.bucket_list[index]

        for entry in current_bucket:
            # If the key already exists, update the corresponding item
            if entry[0] == key:
                entry[1] = item
                return True

        # If the key doesn't exist, add a new entry to the current bucket
        new_entry = [key, item]
        current_bucket.append(new_entry)
        return True

    def lookup(self, key):
        # Calculate the index to determine the bucket for the given key
        index = hash(key) % len(self.bucket_list)
        current_bucket = self.bucket_list[index]

        for entry in current_bucket:
            # If the key is found, return the corresponding item
            if key == entry[0]:
                return entry[1]

        # If the key is not found, return None
        return None

    def remove(self, key):
        # Calculate the index to determine the bucket for the given key
        index = hash(key) % len(self.bucket_list)
        current_bucket = self.bucket_list[index]

        # Check if the key is in the current bucket and remove it if found
        for entry in current_bucket:
            if key == entry[0]:
                current_bucket.remove(entry)
                return True

        # If the key is not found, return True (indicating a successful operation)
        return True
