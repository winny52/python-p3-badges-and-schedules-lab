def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(speakers):
    room_assignments = [f"Hello, {speaker}! You'll be assigned to room {index+1}!" for index, speaker in enumerate(speakers)]
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)

# Test the functions
speakers = ["Arel", "Carol"]
printer(speakers)
