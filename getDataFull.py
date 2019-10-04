import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path = './chromedriver')
url = "https://www.syscom.mx/principal/listadoproductosazul/Bala-65776.html?ordenar=Precio_de_Menor_a_Mayor&pag=1"
driver.get(url)
driver.maximize_window()
#Para dar clic en login
main = driver.find_elements_by_css_selector("nav.navbar")
containerPrevious = main[1].find_element_by_css_selector("div.container")

container = containerPrevious.find_element_by_css_selector("div.navbar-collapse")
containerLog = container.find_element_by_css_selector("ul.navbar-right")
loginA = containerLog.find_element_by_css_selector("li")
loginI = loginA.find_element_by_css_selector("a")
login = loginI.find_element_by_css_selector("i")
containerLog.click()


main = driver.find_element_by_css_selector("main.main_layout")
containerFluid = main.find_element_by_css_selector("div.container-fluid")
row = containerFluid.find_element_by_css_selector("div.row")
listado = row.find_element_by_css_selector("div.col-md-6")
form = listado.find_element_by_xpath("//form")
formGroup = form.find_element_by_xpath("//div[@class='form-group']")
#formGroupButton = form.find_element_by_xpath("//div[@id='block_user']")
boton = form.find_element_by_xpath("//button[@id='login_btn']")
email = formGroup.find_element_by_xpath("//input[@id='email']")
password = formGroup.find_element_by_xpath("//input[@id='password']")
time.sleep(2)
email.send_keys("")
password.send_keys("")
boton.click()
time.sleep(3)
# Comienza extraccion de datos de camaras bala

titles_element = driver.find_element_by_css_selector("main.main_layout")
block = titles_element.find_element_by_css_selector("div.container-fluid")
row = block.find_element_by_css_selector("div.row")
listado = row.find_element_by_css_selector("div.col-sm-9")
time.sleep(3)
listaElementos = listado.find_element_by_id('listado_bloque_productos')
titulosElementos = listaElementos.find_elements_by_xpath('.//div[@class="col-xs-6 col-sm-4 col-md-3 col-lg-2 no_padding "]')
print(len(titulosElementos))
nombres = {}
id = 1
for i in titulosElementos:
    #i = titulosElementos[2]
    # Poner punto para declarar ruta relativa al elemento
    contenedorNombre = i.find_element_by_xpath(".//div[@class='border_gray default_padding_top_bottom altura_bloque']")
    divNombre = contenedorNombre.find_element_by_xpath(".//div[@class='row default_padding_bottom']")
    conNombre = divNombre.find_element_by_class_name("col-xs-12")
    nombre = divNombre.find_element_by_tag_name("h5")
    #contenedorPrecio = i.find_element_by_xpath(".//div[@class='border_gray default_padding_top_bottom altura_bloque']")
    contPrecio = contenedorNombre.find_element_by_xpath(".//div[@class='hidden-xs']")
    precio = contPrecio.find_element_by_xpath(".//div[div/@class='col-xs-12 list-product-price-p3']")

    imagen =  contenedorNombre.find_element_by_xpath(".//div[div/@class='col-xs-12 text-center']")
    imagen =  imagen.find_element_by_xpath(".//a")
    imagen =  imagen.find_element_by_xpath(".//img")
    linkImagen = imagen.get_property('src')
    print("el HTML de imagen: " + linkImagen)
    print(len(linkImagen))
    precioFinal  = precio.text
    precioFinal = precioFinal[4:-9]
    print("El precio:__" + precioFinal +"___")
    nombres[id] = {"nombre":nombre.text,
                        "precio": precioFinal,
                        "imagen": linkImagen

    }
    id += 1
    print(nombre.text)

driver.quit()    


#****INSERT DATA IN DATABASE***
import pymysql
host = "localhost"
user = "admin"
password = "1029"
db = "dataP"
connection  = pymysql.connect(host=host, user=user, password=password,
                             db=db, cursorclass=pymysql.cursors.DictCursor)
id = 1
try:
    cursor = connection.cursor()
    for i in nombres:
        dicActual = nombres[i]
        nombre1 = dicActual["nombre"]
        if len(nombre1)>=99:
            nombre1 = nombre1[:98]
        precio1 = dicActual["precio"]
        urlImagen = dicActual["imagen"]
        primerquery = "INSERT INTO products(categoria,idDescripcion) values('camara bala','"+str(i)+"')"
        segundoquery = "INSERT INTO detallesProductos(Nombre,costo,linkImagen) values('"  +nombre1+"','"+str(precio1)+"','"+urlImagen+"')"
        print(primerquery)
        print(segundoquery)
        cursor.execute(primerquery)
        cursor.execute(segundoquery)
        id += 1
    connection.commit()
finally:
    connection.close()
