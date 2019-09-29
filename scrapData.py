import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path = './chromedriver')
driver.get("https://www.syscom.mx/principal/listadoproductosazul/Bala-65776.html?ordenar=Precio_de_Menor_a_Mayor&pag=1")
#time.sleep(5)
titles_element = driver.find_element_by_css_selector("main.main_layout")
block = titles_element.find_element_by_css_selector("div.container-fluid")
row = block.find_element_by_css_selector("div.row")
listado = row.find_element_by_css_selector("div.col-sm-9")
time.sleep(3)
listaElementos = listado.find_element_by_id('listado_bloque_productos')
titulosElementos = listaElementos.find_elements_by_css_selector('div.col-sm-4')
#titulosElementos = listaElementos.find_elements_by_xpath("//div[@class='col-xs-6 col-sm-4']")
nombres = []
for i in titulosElementos:

    contenedorNombre = i.find_element_by_css_selector("div.border_gray")
    divNombre = contenedorNombre.find_element_by_css_selector("div.default_padding_bottom")
    conNombre = divNombre.find_element_by_class_name("col-xs-12")
    nombre = divNombre.find_element_by_tag_name("h5")
    nombres.append(nombre.text)

print(nombre.text)
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
