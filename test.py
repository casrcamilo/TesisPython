import boto3
from PIL import Image, ImageDraw

def detect_labels(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    im = Image.open(photo)
    imgWidth,imgHeight  = im.size  
    """
    for label in response['Labels']:
         for instance in label['Instances']:
             
                draw = ImageDraw.Draw(im)
                box=instance['BoundingBox']
                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']
                points = (
                            (left,top),
                            (left + width, top),
                            (left + width, top + height),
                            (left , top + height),
                            (left, top)
                )
                draw.line(points, fill='#00d400', width=2)
    im.show()
    """
    for label in response['Labels']:
        if (label['Name'] == 'Car' or label['Name'] == 'Motorcycle' or label['Name'] == 'Truck'  or label['Name'] == 'Bus'  or label['Name'] == 'Taxi'):
            for i in range(0, len(label['Instances'])):
                draw = ImageDraw.Draw(im)
                box=label['Instances'][i]['BoundingBox']
                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']
                points = (
                            (left,top),
                            (left + width, top),
                            (left + width, top + height),
                            (left , top + height),
                            (left, top)
                )
                draw.line(points, fill='#00d400', width=2)
    im.show()

    """
    print('Detected labels for ' + photo) 
    print()   
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])
    """



def main():
    photo='imagen_ws_4.jpeg'
    bucket='imagenes-rekognition'
    label_count=detect_labels(photo, bucket)
    print("Labels detected: " + str(label_count))

if __name__ == "__main__":
    main()