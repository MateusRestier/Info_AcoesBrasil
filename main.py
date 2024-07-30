# UTILIZANDO VERSAO CHROME 127
# pip install selenium openpyxl

try:  # try/except tenta executar os comandos dentro de 'try' e caso de erro, executa o 'except'
    import os
    from selenium import webdriver  # Importa o módulo webdriver da biblioteca Selenium. O webdriver é usado para controlar navegadores da web através de scripts.
    from selenium.webdriver.common.by import By  # Importa a classe By do módulo selenium.webdriver.common.by. Esta classe é usada para localizar elementos HTML de várias maneiras, como por ID, nome, classe, etc.
    from selenium.webdriver.chrome.service import Service  # A classe Service é usada para iniciar e controlar uma instância do ChromeDriver.
    from selenium.webdriver.chrome.options import Options  # A classe Options é usada para definir várias opções/configurações ao iniciar o ChromeDriver, como abrir o navegador em modo maximizado ou headless.
    from selenium.webdriver.support.ui import WebDriverWait  # A classe WebDriverWait é usada para esperar até que uma condição específica seja satisfeita antes de continuar a execução do script.
    from selenium.webdriver.support import expected_conditions as EC  # Este módulo contém uma série de condições pré-definidas que são comumente usadas para esperar até que um determinado estado ou condição ocorra no navegador.
except Exception as e:  # captura qualquer exceção que ocorra no bloco try. A variável e armazena a exceção levantada.
    print(f"Erro ao importar Bibliotecas. Erro: {e}")  # se ocorrer um erro durante a importação das bibliotecas, uma mensagem de erro será impressa no console, indicando qual foi o erro específico.

def configure_browser():  # define a função q vai ser usada pra configurar e inicalizar o navegador com determinadas opções
    try:
        #Configura o navegador para execução.
        current_dir = os.path.abspath(os.path.dirname(__file__))  # obtém o diretório atual onde o script está localizado. __file__ refere-se ao caminho do arquivo do script. os.path.dirname(__file__) obtém o diretório desse arquivo e os.path.abspath converte esse caminho em um caminho absoluto.
        chrome_options = Options()  # Cria uma instância da classe Options que será usada para definir várias opções/configurações para o ChromeDriver.
        chrome_options.add_argument("--start-maximized")  # Adiciona um argumento para iniciar o navegador maximizado.
        chrome_options.add_argument("--disable-gpu")  # Desabilita a aceleração de GPU, necessária em algumas versões do Windows
        chrome_options.add_argument("--window-size=1270,720")  # Define o tamanho da janela do navegador
        chrome_options.add_argument("--headless") # Inicia o navegador em modo headless
        chrome_options.add_argument("--log-level=3") # Definindo o nível de log para suprimir mensagens indesejadas
        
        # Caminho para o ChromeDriver
        chrome_driver_path = os.path.join(current_dir, 'chromedriver.exe')  # Define o caminho para o ChromeDriver, indicando que esta no diretorio atual, junto com o executavel do chromedriver

        # Inicializando o navegador
        service = Service(chrome_driver_path)  # Cria uma instância da classe Service usando o caminho do ChromeDriver. Isso é usado para iniciar e controlar a instância do ChromeDriver.
        driver = webdriver.Chrome(service=service, options=chrome_options)  # usando webdriver.Chrome, colocou toda a configuração do navegador em uma variável, e iniciou uma instancia do navegador
        return driver  # ao fim da função, retorna a função com toda a configuração do navegador
    except:
        print("Erro ao configurar Navegador.")

def abrir_pagina_acao(acao, driver):
    try:
        url = 'https://investidor10.com.br/acoes/' + acao
        driver.get(url)
    except:
        print("Falha ao abrir a página da ação.")

def pegar_informacoes_acao(driver):
    try:
        # Aguardar até que o elemento com a classe 'value' esteja presente na página
        valor_cotacao_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='value']"))
        )
        # Extrair valor ação
        valor_cotacao = valor_cotacao_element.text
        print("Valor da Cotação:", valor_cotacao)
        # Aguardar até que o elemento com a classe '_card dy' esteja presente na página
        valor_dy_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='_card dy']//div[@class='_card-body']//span"))
        )
        # Extrair valor do DY
        valor_dy = valor_dy_element.text
        print("Valor do DY:", valor_dy)
        # Aguardar até que o elemento com a classe '_card vp' esteja presente na página
        valor_pvp_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='_card vp']//div[@class='_card-body']//span"))
        )
        # Extrair valor do p/vp
        valor_pvp = valor_pvp_element.text
        print("Valor do P/VP:", valor_pvp)
        # Aguardar até que o elemento com a classe '_card pl' esteja presente na página
        valor_pl_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='_card pl']//div[@class='_card-body']//span"))
        )
        # Extrair valor do p/vp
        valor_pl = valor_pl_element.text
        print("Valor do PL:", valor_pl)
    except Exception as e:
        print("Erro ao pegar informações da ação:", e)

def main():
    acao = input("Escreva qual ação você deseja consultar: ")
    driver = configure_browser()
    abrir_pagina_acao(acao, driver)
    pegar_informacoes_acao(driver)
    input("Pressione Enter para sair...")
    driver.quit()

if __name__ == "__main__":
    main()


