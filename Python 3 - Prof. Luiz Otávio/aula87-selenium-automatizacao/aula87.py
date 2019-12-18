from selenium import webdriver
from time import sleep

sleep_time = 3
meu_usuario = 'axell-brendow'
minha_senha = ''


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clicar_para_logar(self):
        try:
            btn_logar = self.chrome.find_element_by_link_text('Sign in')
            btn_logar.click()

        except Exception as e:
            print('Erro ao clicar no sign in')
            print(e)

    def logar(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys(meu_usuario)
            input_password.send_keys(minha_senha)
            sleep(sleep_time)
            btn_login.click()

        except Exception as e:
            print('Erro ao logar pelo formulário')
            print(e)

    def abrir_dropdown_perfil(self):
        try:
            btn_dropdown = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
            btn_dropdown.click()

        except Exception as e:
            print('Falha ao abrir perfil')
            print(e)

    def clicar_em_logout(self):
        try:
            btn_logout = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            btn_logout.click()

        except Exception as e:
            print('Falha ao fazer logout')
            print(e)

    def verificar_usuario(self, usuario_esperado):
        username = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = username.get_attribute('innerHTML')
        assert usuario_esperado in profile_link_html


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://github.com/')  # Só vai para a linha de baixo quando o site carregar
    sleep(sleep_time)
    chrome.clicar_para_logar()
    sleep(sleep_time)
    chrome.logar()
    sleep(sleep_time)
    chrome.abrir_dropdown_perfil()
    sleep(sleep_time)
    chrome.clicar_em_logout()
    sleep(sleep_time)
    chrome.clicar_para_logar()
    sleep(sleep_time)
    chrome.logar()
    chrome.abrir_dropdown_perfil()
    sleep(sleep_time)
    chrome.verificar_usuario('axell-brendow')
    sleep(sleep_time * 2)
    chrome.sair()
