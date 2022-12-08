from PyPDF2 import PdfReader
import os
# os.makedirs("temp_img")

def pdf(pdf_file):
    file=PdfReader(pdf_file)
    image_in_pdf=[]
    
    for page in file.pages:
        # pdf_images= page.images #Getting all the images from a single page
        for ima in page.images:
            image_file=os.getcwd()+ "/temp_img/"+ ima.name
            print("image file name: ",image_file)
            with open (image_file, 'wb') as f:
                f.write(ima.data)
            image_in_pdf.append(image_file)
    return image_in_pdf
        
# print("current working directory: ",os.getcwd())


pdf("honebi.pdf")