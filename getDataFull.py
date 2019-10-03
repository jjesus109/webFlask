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
#containerLog = container.find_elements_by_xpath("ul[@class='nav']")


#login = containerLog[0].find_element_by_xpath["//li[a/@href='/login']"]
#login2 = containerLog[0].find_element_by_xpath["//li[a/@href='/login']"]

#login = containerLog.find_element_by_xpath["//li"]

#container2 = main[1].find_elements_by_xpath("//div[@class='collapse']")
# Para rellenar datos de usuario

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
email.send_keys("104590314")
password.send_keys("")
boton.click()
time.sleep(3)


titles_element = driver.find_element_by_css_selector("main.main_layout")
block = titles_element.find_element_by_css_selector("div.container-fluid")
row = block.find_element_by_css_selector("div.row")
listado = row.find_element_by_css_selector("div.col-sm-9")
time.sleep(3)
listaElementos = listado.find_element_by_id('listado_bloque_productos')
titulosElementos = listaElementos.find_elements_by_xpath('//div[@class="col-xs-6 col-sm-4 col-md-3 col-lg-2 no_padding "]')
#titulosElementos = listaElementos.find_elements_by_xpath("//div[@class='col-xs-6 col-sm-4']")
nombres = {}
id = 1
#for i in titulosElementos:
i = titulosElementos[1]
contenedorNombre = i.find_element_by_css_selector("div.border_gray")
contenedorPrecio = i.find_element_by_xpath("//div[@class='row precios-movil visible-xs-block']")
divNombre = contenedorNombre.find_element_by_css_selector("div.default_padding_bottom")
conNombre = divNombre.find_element_by_class_name("col-xs-12")
divImagen = divNombre.find_element_by_class_name("col-xs-12")

contPrecio = contenedorNombre.find_element_by_xpath("//div[@class='hidden-xs']")
rowPrecio = contPrecio.find_element_by_xpath("//div[@class='row']")
precio = rowPrecio.find_element_by_xpath("//div[@class='col-xs-12 list-product-price-p3']")
#precio = precio.find_element_by_tag_name("p")
#print(precio.get_attribute('innerHTML'))
nombre = divNombre.find_element_by_tag_name("h5")
nombres[id] = {"nombre":nombre.text,
                    "Precio": 10.0

}
id += 1
"""
aImagen = divImagen.find_element_by_xpath("//div[@class='row precios-movil visible-xs-block']")
aImagen1 = aImagen.find_element_by_xpath("//div[@class='col-xs-12']")
aImagen2 = aImagen1.find_element_by_xpath("//div[@class='row']")
imagenHTML= aImagen2.find_elements_by_xpath("//img")

aImagen3 = aImagen2.find_element_by_xpath("//div[@class='col-xs-12 list-product-price-p3']")
imagen = aImagen3.find_element_by_tag_name('span')
"""

#imagen = aImagen.find_element_by_class_name('foto_producto_bloque')



driver.quit()    
"""

nombres = []
for i in titulosElementos:
    titulo = i.find_element_by_class_name('border_gray')
    contenedorNombre = titulo.find_element_by_class_name("default_padding_bottom")
    divNombre = Contenedornombre.find_element_by_class_name("col-xs-12")
    nombre = divNombre.find_element_by_tag_name("h5")
    print(nombre.getProperty(data-original-title))
    nombres.append(nombre.getProperty(data-original-title))
print(nombres)
"""
#for i in titulosElementos:
#    print(i.text)

    
'''label_title = driver.find_element_by_class_name("col-sm-9 col-md-10 col-lg-11 area-de-listados")
label_countdown = driver.find_element_by_class_name("col-xs-6 col-sm-4 col-md-3 col-lg-2 no_padding ")
print(label_title.text)
print(label_countdown.text)
'''
#print(titles)

#elements  =bloqueProductos.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-2 no_padding')
#productName = elements.find(class_='list-product-title ellipsis-multiline')
#print(productName)

"""INSERT DATA IN DATABASE"""

"""
print("data Obtain")
print("this is the data")
print(nombres)
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
        if len(nombre1)>=29:
            nombre1 = nombre1[:28]
        precio1 = dicActual["Precio"]
        primerquery = "INSERT INTO products(categoria,idDescripcion) values('camara bala','"+str(i)+"')"
        segundoquery = "INSERT INTO detallesProductos(Nombre,costo) values('"+nombre1+"',"+str(precio1)+")"
        print(primerquery)
        print(segundoquery)
        cursor.execute(primerquery)
        cursor.execute(segundoquery)
        id += 1
    connection.commit()
finally:
    connection.close()

"""