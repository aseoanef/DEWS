import tkinter as ttk
from cell import Cell
from detailWindow import detail_window

class MainWindow():
    def on_button_click(self, cell):
        #abrimos otra pestaña con los datos de cada cell
        zoom_image_window = detail_window(cell.image_tk, cell.title, cell.description)
        zoom_image_window.mainloop()
    def __init__(self,root):
        self.root=root
        root.title("MainWindow")
        #lista de imagenes
        self.cells= [
            Cell("image1",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\unedited\\artic.jpg',"""
The Arctic fox (Vulpes lagopus), also known as the white fox, polar fox,
or snow fox, is a small fox that belongs to the family of Canidae, native to the Arctic regions of the Northern 
Hemisphere and common throughout the Arctic tundra biome.[1][7][8][9] It is well adapted to living in cold environments, 
and is best known for its thick, warm fur that is also used as camouflage. 
It has a large and very fluffy tail. In the wild, most individuals do not live past their first year but some exceptional
ones survive up to 11 years.[10] Its body length ranges from 46 to 68 cm (18 to 27 in), with a generally rounded body shape to minimize the escape of body heat. 
                 """),
            Cell("image2",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\unedited\\fennec.jpg',"""
The fennec fox (Vulpes zerda) is a small crepuscular fox native to the deserts of North Africa, ranging from Western 
Sahara and Mauritania to the Sinai Peninsula.[1] Its most distinctive feature is its unusually large ears, which serve 
to dissipate heat and listen for underground prey. The fennec is the smallest fox species. Its coat, ears, and kidney 
functions have adapted to the desert environment with high temperatures and little water. It mainly eats insects, small
mammals and birds. The fennec has a life span of up to 14 years in captivity and about 10 years in the wild. Its main
predators are the Verreaux's eagle-owl, jackals and other large mammals.                
                """),
            Cell("image3",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\unedited\\grey.jpg',"""
Gray Fox, Null, y Garganta Profunda fueron los nombres en clave de Frank Jaeger o Frank Hunter, agente de FOX y posteriormente
FOXHOUND. Fue el único miembro de FOXHOUND en obtener el nombre en código de Fox, la condecoración más alta de la Unidad
(Roy Campbell, que alcanzó el nombre en código “Fox” no cuenta, pues él no era un agente de campo activo). Gray Fox era 
el mejor amigo de Solid Snake después de la operación Intrude N313, pero su lealtad era hacia Big Boss, forzado a luchar 
contra Snake durante la sublevación Zanzibar Land. 
                """),
            Cell("image4",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\unedited\\marble.jpg',"""
The Canadian Marble Fox, or Arctic Marble Fox, is a unique and beautiful subspecies of the red fox that is found only in
a small area of Canada. It is known for its striking coat of fur that is marbled with white, black, and gray, giving it 
a distinctive and eye-catching appearance.The Canadian Marble Fox is found primarily in the northern regions of Canada, 
in the provinces of British Columbia, Alberta, and the Northwest Territories. It is a highly adaptable animal that can 
thrive in a variety of different habitats, from dense forests to open tundra.
"""),
            Cell("image5",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\unedited\\red.jpg',"""
The red fox (Vulpes vulpes) is the largest of the true foxes and one of the most widely distributed members of the order
Carnivora, being present across the entire Northern Hemisphere including most of North America, Europe and Asia, plus parts 
of North Africa. It is listed as least concern by the IUCN.[1] Its range has increased alongside human expansion, having 
been introduced to Australia, where it is considered harmful to native mammals and bird populations. Due to its presence 
in Australia, it is included on the list of the "world's 100 worst invasive species".
""")
        ]
        for i ,cell in enumerate(self.cells):
            #enseñar cada imagen
            label =ttk.Label(root,image=cell.image_tk,text=cell.title,compound=ttk.BOTTOM)
            label.grid(row=i,column=0)
            #bindear el click
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_click(cell))

if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()