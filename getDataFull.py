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
password.send_keys("1eec5")
boton.click()
time.sleep(4)


titles_element = driver.find_element_by_css_selector("main.main_layout")
block = titles_element.find_element_by_css_selector("div.container-fluid")
row = block.find_element_by_css_selector("div.row")
listado = row.find_element_by_css_selector("div.col-sm-9")
time.sleep(3)
listaElementos = listado.find_element_by_id('listado_bloque_productos')
titulosElementos = listaElementos.find_elements_by_css_selector('div.col-sm-4')
#titulosElementos = listaElementos.find_elements_by_xpath("//div[@class='col-xs-6 col-sm-4']")
nombres = {}
id = 1
for i in titulosElementos:
    #i = titulosElementos[0]
    contenedorNombre = i.find_element_by_css_selector("div.border_gray")
    contenedorPrecio = i.find_element_by_xpath("//div[@class='row precios-movil visible-xs-block']")
    divNombre = contenedorNombre.find_element_by_css_selector("div.default_padding_bottom")
    divImagen = divNombre.find_element_by_class_name("col-xs-12")
    conNombre = divNombre.find_element_by_class_name("col-xs-12")
    divImagen = divImagen.find_element_by_xpath("//div[div/@class='col-xs-12 list-product-price-p3']")
    aImagen = divImagen.find_element_by_tag_name('span')
    nombre = divNombre.find_element_by_tag_name("h5")
    #imagen = aImagen.find_element_by_class_name('foto_producto_bloque')

    nombres[id] = {"nombre":nombre.text,
                            "Precio": divImagen.text

    }
    id += 1
    #print(nombre.text)

print(nombres)

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
