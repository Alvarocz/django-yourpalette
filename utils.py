def hex2rgb(string):
    return (
        int(string[1:3], 16),
        int(string[3:5], 16),
        int(string[5:7], 16)
    )


def rgb2hex(rgb):
    return '#{}{}{}'.format(
        hex(rgb[0])[2:],
        hex(rgb[1])[2:],
        hex(rgb[2])[2:]
    )


def darken(string, amount):
    rgb = hex2rgb(string)
    new_r = rgb[0] - rgb[0]*(amount/100)
    new_g = rgb[1] - rgb[1]*(amount/100)
    new_b = rgb[2] - rgb[2]*(amount/100)
    
    if new_r < 0: new_r = 0
    if new_g < 0: new_g = 0
    if new_b < 0: new_b = 0
    return rgb2hex((new_r, new_g, new_b))


def lighten(string, amount):
    rgb = hex2rgb(string)
    new_r = rgb[0] + rgb[0]*(amount/100)
    new_g = rgb[1] + rgb[1]*(amount/100)
    new_b = rgb[2] + rgb[2]*(amount/100)
    
    if new_r > 255: new_r = 255
    if new_g > 255: new_g = 255
    if new_b > 255: new_b = 255
    return rgb2hex((new_r, new_g, new_b))

