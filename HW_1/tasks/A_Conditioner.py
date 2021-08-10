def read_file(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
        room, cond = map(int, data[0].split())
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

    def auto_room(room, cond):
        return cond

    mode_dict = {
        'freeze': freeze_room,
        'heat': heat_room,
        'fan': fan_room,
        'auto' : auto_room
    }

    return mode_dict[mode](room, cond)

def main():
    room, cond = map(int, input().split())
    mode = input()
    t_res = conditioner(room, cond, mode)
    return t_res

if __name__ == '__main__':
    main()
