
# instaBot vMehc 1.5

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randrange
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
import datetime

# Usuario y password
user = "xx" # 
password = "xx" # 

# Mensajes pop-up
not_now = "//button[contains(text(), 'Ahora no')]"
guardar = "//button[contains(text(), 'Guardar Información')]" # Guardar información inicio sesión en navegador
limit_exceeded = "//button[contains(text(), 'Avísanos')]" # Mensaje que da cuando te bloquea la actividad
limit_exceeded2 = "//button[contains(text(), 'Informar de un problema')]" # Otro mensaje que también sale al bloquear
like = "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Me gusta']"

# Mensajes
hello = "Iniciando Instabot mejorado por mehc de astropajo.com . . ."
usuario = "Conectando con "
hash_selec = ": Hashtags seleccionados: " 
likes_prev = ": Likes previstos: "
hashtag = ": Hashtag: "
like_num = ": Like número: "
not_like = ", ya tenía like."
exception_limit = ": Límite de actividad excedido, mañana más."
fin = "Fin!, cerrando programa . . ."
cambio_hash = "Esperando para cambio de hashtag . . ."
likes_acum = "Likes dados hasta el momento: "
likes_tot = "Likes dados en total: "
fin_inicio = ": Se inició: "
hash_tot = ": Hashtags procesados: " 
txt_descanso = "Hacemos un breve descanso . . ."

# Variables
num_likes = 25 # Likes por hashtag, tener en cuenta de no sobrepasar el límite diario que supuestamente son 2400.
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") # Guardamos cookies e información
PATH = "I:\Instabot-master\driver\chromedriver.exe" # Testeado en versión 87
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get('https://instagram.com/accounts/logout') # Empezamos con logout porque usamos cookies para que no diga que es siempre la primera vez del navegador
time.sleep(randrange(4, 8)) # esperamos..
driver.get('https://instagram.com/accounts/login') # Ahora login por las cookies y cuentas que tengamos almacenadas
cont = 0
cont_h = 0
f_inicio = datetime.datetime.now()
descanso = 100 # Para hacer un breve descanso cada x likes, por defecto 100.

time.sleep(randrange(3, 7)) # esperamos..

try:
    print(f_inicio.strftime("%Y-%m-%d %H:%M:%S"), hello)  

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]"))
        ) # esperamos 10 segundos si el webdriver encuentra la ID
        element.click()
    except Exception:
       pass # todo ok, seguimos 
    finally:
        search = driver.find_element_by_name("username")
        search.send_keys(user)
        time.sleep(randrange(2, 6)) # esperamos..
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), usuario, user, " . . .")  

        search = driver.find_element_by_name("password")
        search.send_keys(password)
        time.sleep(randrange(3, 7)) # esperamos..

        search.send_keys(Keys.RETURN)

    try:    
        element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, guardar))
        ) 
        element.click()
    except Exception:
       pass # todo ok, seguimos     
    finally:
       time.sleep(randrange(3, 6))

    try:
        element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, not_now))
        ) 
        element.click()
    except Exception:
       pass # todo ok, seguimos 
    finally:
       time.sleep(randrange(3, 6))

    time.sleep(randrange(4, 10))    
    
    # Listado de hashtags
    hashtags = ['#likesforlike', '#likeforlikes', '#likeforfollow', '#love', '#bhfyp', '#WYMTM', '#nofilters', '#Smile', '#together', '#instalike', '#CarpeDiem' # Generic (11)				
               ] 

    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"), hash_selec, len(hashtags))        
    print(now.strftime("%Y-%m-%d %H:%M:%S"), likes_prev, len(hashtags)*num_likes)   

    for index in range(len(hashtags)): # bucle para todos los hashtags

        cont_h = cont_h + 1 
        now = datetime.datetime.now()      		
        print(now.strftime("%Y-%m-%d %H:%M:%S"), hashtag, index+1, " - ", hashtags[index])        
            
        search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys(hashtags[index]) 
        time.sleep(randrange(3, 5))
        search.send_keys(Keys.RETURN)
        time.sleep(randrange(3, 9))
        search.send_keys(Keys.RETURN)
        time.sleep(randrange(10, 15))# La búsqueda se realiza en el campo de búsqueda y el resultado se selecciona confirmando dos veces con retorno

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div"))
        )  # esperamos 10 segundos si el webdriver encuentra la ID
        element.click()  # se seleccionará primer elemento
        time.sleep(randrange(5, 9))

        i = 0        
        while i < num_likes:
            try:
                element = WebDriverWait(driver, 9).until(
                    EC.presence_of_element_located(
                        (By.XPATH, like)) 
                )  
                time.sleep(randrange(4, 8))
                element.click()
                cont = cont + 1
                now = datetime.datetime.now()
                print(now.strftime("%Y-%m-%d %H:%M:%S"), like_num, i+1)
            except Exception:
                now = datetime.datetime.now()
                print(now.strftime("%Y-%m-%d %H:%M:%S"), like_num, i+1, not_like)
                pass            
            finally:
                time.sleep(randrange(2, 6))
                search = driver.find_element_by_tag_name("body")
                search.send_keys(Keys.ARROW_RIGHT)  # siguiente
                time.sleep(randrange(3, 9))
                i = i + 1

                # Reviso si ha saltado el límite excedido
                try:
                    element2 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, limit_exceeded)) 
                    )  
                    element2.click()
                    now = datetime.datetime.now()
                    print(now.strftime("%Y-%m-%d %H:%M:%S"), exception_limit)
                    raise Exception(now.strftime("%Y-%m-%d %H:%M:%S"), exception_limit)   
                except TimeoutException:
                    pass
                finally:
                    time.sleep(randrange(1, 3))

                # Reviso si ha saltado el límite excedido 2
                try:
                    element3 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, limit_exceeded2)) 
                    )  
                    element3.click()
                    now = datetime.datetime.now()
                    print(now.strftime("%Y-%m-%d %H:%M:%S"), exception_limit)
                    raise Exception(now.strftime("%Y-%m-%d %H:%M:%S"), exception_limit)   
                except TimeoutException:
                    pass
                finally:
                    time.sleep(randrange(2, 4))

                if cont == descanso:
                    print(now.strftime("%Y-%m-%d %H:%M:%S"), txt_descanso)
                    descanso = descanso + 100
                    time.sleep(randrange(31, 181))

        # Esperamos para cambiar de hashtag
        search.send_keys(Keys.ESCAPE)
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), cambio_hash)
        print(now.strftime("%Y-%m-%d %H:%M:%S"), likes_acum, cont)
        time.sleep(randrange(61, 361))

finally:
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"), fin)
    print(now.strftime("%Y-%m-%d %H:%M:%S"), fin_inicio, f_inicio.strftime("%Y-%m-%d %H:%M:%S"))
    print(now.strftime("%Y-%m-%d %H:%M:%S"), hash_tot, cont_h)
    print(now.strftime("%Y-%m-%d %H:%M:%S"), likes_tot, cont)
    time.sleep(randrange(5, 15))
    driver.quit()


