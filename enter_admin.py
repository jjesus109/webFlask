'''import requests
from bs4 import BeautifulSoup
#def dataScrap():
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#page = requests.get('https://www.syscom.mx/principal/listadoproductosazul/camaras-bullet-65776.html?ordenar=Precio_de_Menor_a_Mayor&pag=1')
page = requests.get('https://www.syscom.mx/principal/listadoproductosazul/camaras-bullet-65776.html?ordenar=Precio_de_Menor_a_Mayor&pag=1',headers=headers)
print("este es el code")
print(page.status_code)
if page.status_code == 200:
#print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)
    bloqueProductos = soup.find("div",class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-2 no_padding ")
#bloqueProductos = soup.find(class_ ="col-sm-9 col-md-10 col-lg-11 area-de-listados")
#bloqueProductos = soup.find(class_ ="row default_margin_top")


    print(bloqueProductos)

'''
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
#titulosElementos = listaElementos.find_element_by_class_name('form-control')


driver.quit()    

    