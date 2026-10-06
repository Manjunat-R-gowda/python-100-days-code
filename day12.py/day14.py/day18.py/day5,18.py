import colorgram 
colours=colorgram.extract('image.jpg.zip',6)

for clour in colours:
    first_clour=clour[0]
    rgb=first_clour.rgb
    hsl=first_clour.hsl

red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s