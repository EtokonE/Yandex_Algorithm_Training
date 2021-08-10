def read_file(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
        room, cond = data[0].split()
        mode = data[1]
    return room, cond, mode


def conditioner(room, cond, mode):
    def freeze_room(room, cond):
        if room > cond:
            return cond
        else:
            return room

    def heat_room(room, cond):
        if room < cond:
            return cond
        else:
            return room

    def fan_room(room, cond):
        return room

    mode_dict = {
        'freeze': freeze_room,
        'heat': heat_room,
        'fan': fan_room,
    }

    return mode_dict[mode](room, cond)


conditioner(*read_file('input.txt'))
