import os
import img2pdf 
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import xlsxwriter
from docx import Document
import csv

class Multiprops: 
    
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    
    def create_folder( self, path: str ) -> bool:
        if( not os.path.exists(path=path) ):
            os.mkdir( path )
            return True
    
    def create_image(self, path: str, exts: str,count_img: int = 1) -> str:
        
        try:
            font = ImageFont.truetype("arial.ttf", 150)

            img = Image.new( mode='RGB', size=(750,750 ),color='white' )

            name_folder = 'IMG-TEST'
            name_image  = f'img-test-{count_img}.{exts}'  
            
            path_folder = Path(path).joinpath(name_folder)
            
            self.create_folder(path_folder)
            path_img = Path(path).joinpath(name_folder).joinpath(name_image)
            # Image-Test <-- este es el nombre de la imagen de prueba

            img.save(path_img) # se creea la imagen 
            # img.save('C:/2024/CRs/AON/Email/Documentation/python-merge-img-to-pdf/Archivos-Test/img1.jpg') # se creea la imagen 

            img  = Image.open(path_img)
            draw =  ImageDraw.Draw(img)

            draw.text((175,300),text='TEST',fill=(0,0,0),font=font)

            img.save(path_img)
            # img.show()
            return path_img;
        except :
            raise Exception('An exception occurred') 
            #print('An exception occurred')
    
    def create_img_to_pdf(self):
     
        # path_img = "C:/2024/CRs/AON/Email/Documentation/archivos-pruebas/" 
        # images = os.listdir(path_img)


        # crear imagen 
        
        exts: str = 'png'
    

        name_folder = Path(self.dir_path).joinpath('PDF-TEST')
     
        name_file_aux = "pdf-test-"

        #images = ['C:/2024/CRs/AON/Email/Documentation/archivos-pruebas/test - Copy (315) - Copy - Copy - Copy.png']


        #print(archivos)
        # print(len(images))
        #print(images)

        res: bool = self.create_folder(name_folder)
        
        # if( not os.path.exists('./Archivos-Test') ):
        #     os.mkdir('./Archivos-Test')

        path_image = self.create_image(self.dir_path,exts)



        count = 2
        
        #path_image = 'c:/2024/CRs/AON/Email/Documentation/python-merge-img-to-pdf/test.png'
    
        files_images = [path_image] * count

        # name_file = Path(name_folder).joinpath(name_file_aux) 
        
        for i in range(1):
            name_file = name_file_aux + str( i + 1) +'.pdf'
            path_file_pdf = Path(Path(name_folder).joinpath(name_file))
            with open(path_file_pdf,"wb") as f:
                f.write(img2pdf.convert( files_images ))


        # file_size = os.path.getsize(name_file)
        # file_size_kb = file_size / 1024
        # print(f"Size of {name_file}: {file_size_kb:.2f} KB")

    def create_file_csv(self, count = 1):
        path_folder= self.build_path_folders('CVS-TEST')
        path_csv = Path(path_folder).joinpath(f'csv-test-{count}.csv') 
        
        with open(path_csv, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Test', 'Test', 'Test'])
    
    def create_file_xlsx(self, count:int=1):
      
        path_folder= self.build_path_folders('XLSX-TEST')
        path_xlsx = Path(path_folder).joinpath(f'xlsx-test-{count}.xlsx') 

        workbook = xlsxwriter.Workbook(path_xlsx)
        worksheet = workbook.add_worksheet()

        ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Y','Z']
        
        for i in range(100):
            for j in ABC:
                worksheet.write(f'{j}{i+1}', '''Test''')
        workbook.close()
    
    def create_file_docx(self, count: int = 1):
        
        path_folder= self.build_path_folders('DOCX-TEST')
        path_docx = Path(path_folder).joinpath(f'docx-test-{count}.docx')
        
        document = Document()
        paragraph = """
            Consequat elit eiusmod sit velit nulla laboris ea irure reprehenderit. Nisi ut ad culpa mollit cillum incididunt. Do cupidatat consectetur pariatur nisi labore exercitation ea. Ea ex deserunt tempor eiusmod eu pariatur laborum laboris incididunt laborum ullamco irure.
            Duis nostrud nulla et labore. Cillum exercitation nostrud cillum esse tempor duis velit commodo. Laborum pariatur ut ut ullamco tempor incididunt quis in eiusmod.
            Dolor exercitation cupidatat aute deserunt voluptate nostrud qui Lorem laborum eu irure anim. Incididunt eiusmod mollit anim est nisi. Duis exercitation voluptate ipsum reprehenderit velit laboris tempor exercitation voluptate quis voluptate. Id excepteur dolor sint sunt excepteur fugiat voluptate ad proident et ipsum mollit labore. Eiusmod elit nisi duis fugiat amet culpa fugiat. Dolor adipisicing veniam et esse ullamco ea adipisicing quis incididunt. Ipsum incididunt ex consectetur nisi nisi amet do ex labore est enim ipsum sint eu.
            Ex cillum incididunt consequat culpa enim occaecat mollit et et sunt cillum id sit voluptate. Aliquip aliqua et ad exercitation aute velit sint excepteur laborum adipisicing do. Aute dolore et consequat qui sint id laboris culpa ullamco reprehenderit sint. Esse elit quis in laboris anim dolor. Mollit minim reprehenderit ex ut. Ad culpa velit nostrud ad incididunt.
        """
        document.add_paragraph(paragraph)
        document.save(path_docx)
    
    
    def build_path_folders(self, name_folder: str) -> str:
        path_folder = Path(self.dir_path).joinpath(name_folder)
        self.create_folder(path=path_folder)
        return path_folder
    # def create_file_tiff(self):
    #     pass

multi = Multiprops()

# test.create_file_csv()

if __name__ == '__main__':
    multi.create_img_to_pdf()
    multi.create_file_csv()
    multi.create_file_xlsx()
    multi.create_file_docx()    
    
    



# import numpy as np

# # create data
# d = np.ndarray(shape=(10,20), dtype=np.float32)
# d[()] = np.arange(200).reshape(10, 20)

# im = Image.fromarray(d, mode='F') # float32
# im.save("test2.tiff", "TIFF")

