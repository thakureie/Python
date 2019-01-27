#!/usr/bin/env python

setting_map = {
    'net.ipv4.ipfrag_low_thresh': 15728640,
    'net.ipv4.ipfrag_high_thresh': 16777216,
}
found = {setting: False for setting in setting_map}
to_write = []

def good_setting(setting):
    return '{} = {}'.format(setting, setting_map[setting])

with open('sysctl.conf') as f:
    for line in f:
        line = line.rstrip()  # remove newlines

        try:
            setting = line.split('=')[0].strip()  # remove spaces if present
            value = int(line.split('=')[-1].strip())
        except Exception as e:
            # you probably don't want to print, but i put it here for demonstration
            #print('could not parse line "{}"; exception: {}'.format(line, repr(e)))
            # keep it as-is
            to_write.append(line)
            continue

        if setting in setting_map:
            found[setting] = True
            if value != setting_map[setting]:
                print('FOUND "{}" with value "{}"; overwriting with "{}"'.format(
                    setting, value, setting_map[setting]
                ))
                to_write.append(good_setting(setting))
                continue

        to_write.append(line)

# opening as 'w' will wipe the file, but we're re-writing every line
# or you can write to a different file if you'd like
with open('sysctl.conf', 'w') as f:
    f.write('\n'.join(to_write))
    f.write('\n')
    for setting in setting_map:
        if not found[setting]:
            print('ADDING "{}"'.format(good_setting(setting)))
            f.write('{}\n'.format(good_setting(setting)))
