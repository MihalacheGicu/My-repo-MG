from selenium import webdriver
from selenium.webdriver.common.by import By

# Seteaza driverul
driver = webdriver.Chrome()

# # Navigam catre un url
# driver.get('https://formy-project.herokuapp.com/form')
# # Selector by ID
# first_name = driver.find_element(By.ID, 'first-name')
# first_name.send_keys('Andy')
#
# # Navigam catre un url
# driver.get('https://formy-project.herokuapp.com/')
# # Selector by Link Text
# driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
# # Selector by Partial Link Text
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()

# # Navigam catre alta pagina
# driver.get('http://www.seleniumframework.com/Practiceform/')
# # Selector by Name
# driver.find_element(By.NAME, 'country').send_keys('Romania')


# # driver.quit()
# # -------
# Navigam catre alta pagina
driver.get('https://formy-project.herokuapp.com/form')
# Selector by Tag - ia primul tot timpul - se poate folosi doar daca avem element unic
driver.find_element(By.TAG_NAME, 'input').send_keys('Andy')
# Gasim mai multe si le punem in lista
input_list = driver.find_elements(By.TAG_NAME, 'input')
input_list[1].send_keys('Sinpetrean')

# Navigam catre alta pagina
driver.get('https://formy-project.herokuapp.com/form')
# Selector by Class - ia primul tot timpul - este ok sa il folosim doar daca avem clasa unica
driver.find_element(By.CLASS_NAME, 'form-control').send_keys('Andy')
# Gasim mai multe si le punem in lista
driver.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Sinpetrean')

# Navigam catre alta pagina
driver.get('https://formy-project.herokuapp.com/form')
# Selector by CSS - ID
driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('An')
# Selector by CSS - Class - la fel ca mai sus, o ia pe prima
driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('dy')
# Selector by CSS - atribut=valoare
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('S')
# Selector by CSS - atribut=valoare partiala + parinte -> copil
driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('inpetrean')

# Navigam catre alta pagina
driver.get('https://formy-project.herokuapp.com/form')
# Selector by Xpath atribut-valoare
driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')
# Selector by Xpath - * toate elementele care respecta regula
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('n')
# Selector by Xpath navigare in jos trecem prin fiecare element -
driver.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('d')
# Selector by Xpath navigare in jos - skip tags cautam oriunde sub form un input care sa respecte regula
driver.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('y')
# Selector by Xpath selectare element din lista index incepe de la 1
driver.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('S')
# Selector by Xpath - OR primul gasit dintre variante
S = driver.find_element(By.XPATH, '//Input[@id="last-name1"] | //Input[@id="last-name2"] | //Input[@id="last-name"]')
# Stergem valorile din input
S.clear()
S.send_keys('Sinpetrean')

# Selector by Xpath - in functie de textul partial + luam textul de pe el cu proprietatea text
full_text = driver.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
print(full_text)

# Selector by Xpath - in functie de textul vizibil
driver.find_element(By.XPATH, '//a[text()="Submit"]').click()

'''
x y axis navigation
Cu parent in sus
Cu /elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
Cu following-sibling::elem_type - urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type- fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong/following-sibling::input/preceding-sibling::strong
'''


# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul

def formy_input(placeholder_text, input_value):
    web_element_input = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    web_element_input.clear()
    web_element_input.send_keys(input_value)


formy_input('Enter first name', 'ANDY')
formy_input('Enter last name', 'ANDY')
formy_input('Enter your job title', 'QA AUTOMATION ENGINEER')
print("am ajuns la final")
