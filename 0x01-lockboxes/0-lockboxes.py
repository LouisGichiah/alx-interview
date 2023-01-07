def canUnlockAll(boxes):
    # Step 1
    unopened = set(range(1, len(boxes)))
    # Step 2
    keys = boxes[0]
    # Step 3
    while keys:
        # Step 3a
        key = keys.pop(0)
        # Step 3b
        if key in unopened:
            unopened.remove(key)
            keys.extend(boxes[key])
    # Step 4
    return not unopened
