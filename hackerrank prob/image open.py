def image(file_name):
    with open(file_name,'r')as img:
        img.seek(163)
        x=img.read(2)
        h=(x[0]<< 8)+x[1]
        x=img.read(2)
        w=(x[0]<< 8)+x[1]
        print("Resolution =",w,"x",h)
image("Updesh.JPG")
