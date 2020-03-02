from flask import Flask,request,render_template , redirect
import pytesseract as tess
from PIL import Image
import pytesseract
import cv2
import os


app=Flask(__name__)

@app.route('/')

def index():
    return render_template('image_in.html')

app.config["IMAGE_UPLOADS"] ="/home/iiitk/Desktop/flask_practice/Pic_string/static/img"
app.config["ALLOWED_IMAGE_EXTENSIONS"]=["PNG","JPG","JPEG","GIF"]

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True

    else:
        return False

@app.route('/Image_input', methods=['GET','POST'])

def main():
    imag_file=[]
    path="/home/iiitk/Desktop/flask_practice/Pic_string"
    if request.method=='POST':

        if request.files:
            image = request.files["image"]
            if image.filename=="":
                print("image must be uploded")
                return redirect(request.url)

            if not allowed_image(image.filename):
                print("the image extension is not allowed")
                return redirect(request.url)


           
            image.save(os.path.join(path,image.filename))
            imag_file.append(image.filename)
            print(imag_file)
            print("image saved")
            #return redirect(request.url)
    img1=""
    all_word="No image so No word"
    if len(imag_file)!=0:
        img=Image.open(imag_file[0])
        img1=cv2.imread(imag_file[0])
        all_word=tess.image_to_string(img,timeout=5)

  
           
  
   
    return render_template('after_up.html' ,all_word=all_word,img1=img1)

if __name__ == "__main__":
    app.run(debug=True)

