from PIL import Image, ImageDraw

im = Image.open("SEMAFORO_0.jpg")
#im.show()
draw = ImageDraw.Draw(im)

imgWidth,imgHeight = im.size

box=[]

box_Top=0.45734676718711853
box_Left=0.0470198392868042
box_Width=0.1869860738515854
box_Height=0.24286499619483948

left = imgWidth * box_Left
top = imgHeight * box_Top
width = imgWidth * box_Width
height = imgHeight * box_Height
points = (
            (left,top),
            (left + width, top),
            (left + width, top + height),
            (left , top + height),
            (left, top)
)
draw.line(points, fill='#00d400', width=2)
im.show()

print('hola')
print('te quiero')