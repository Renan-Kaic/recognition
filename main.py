import telebot
import hashlib
from funcs import obterLista, excluir_site, adicionar_site
from os import system
from time import sleep
system('clear')

CHAVE_API = open('dados/api_key.txt', 'r').read()

bot = telebot.TeleBot(CHAVE_API)

IsAuth = False
USER_ID = 5301767566

@bot.message_handler(commands=['menu'])
def menu(msg):
    menu = """
------------- Menu -------------
/cadastrar site
/listar sites
/excluir site
/admin bloqueio
Clique em uma das opções para continuar
"""
    bot.send_message(USER_ID, menu)

@bot.message_handler(commands=['cadastrar'])
def cadastrar(msg):
    if verificar(msg):
        bot.send_message(USER_ID, 'Informe o site que deseja cadastrar')
        bot.register_next_step_handler(msg, cadastrar_site)
    
def cadastrar_site(msg):
    msg = adicionar_site(msg.text)
    
    bot.send_message(USER_ID, msg)
    
        
@bot.message_handler(commands=['listar'])
def listar_sites(msg):
    if verificar(msg):
        print('Listando sites')
        msg = obterLista()
        bot.send_message(USER_ID, msg)
    
@bot.message_handler(commands=['excluir'])
def excluir(msg):
    if verificar(msg):
        listar_sites(msg)
        bot.send_message(USER_ID,'Digite o número do site que deseja excluir: ')
        bot.register_next_step_handler(msg, excluir_s)


def excluir_s(msg):
   msg = excluir_site(msg.text)
   bot.send_message(USER_ID, msg)
   menu(msg)
    
@bot.message_handler(commands=['iniciar'])
def iniciar(msg):
    ID = msg.from_user.id
    if ID != USER_ID:
        bot.send_message(ID, 'Aparelho não autorizado')
        bot.send_message(USER_ID, f'Um aparelho não autorizado tentou fazer login\nID: {ID}')
        return 
    if IsAuth:
        bot.send_message(USER_ID, 'Usuario ja autenticado')
        return    
    bot.send_message(USER_ID, 'Informe a senha: ')
    bot.register_next_step_handler(msg, auth)
    
def auth(msg):
    global IsAuth
    # Por segurança, apagando a senha do usuário
    msgS = str(msg.text).replace(' ', '')
    hashSenha = hashlib.sha256(msgS.encode('utf-8')).hexdigest()
    passW = open('dados/hash.txt', 'r').read()

    if hashSenha == passW:
        IsAuth = True
        bot.send_message(USER_ID, 'Autenticado com sucesso')
        bot.delete_message(USER_ID, msg.message_id)
        menu(msg)
    else:
        bot.send_message(USER_ID, 'Senha incorreta')

@bot.message_handler(commands=['sair'])
def sair(msg):
    global IsAuth
    
    if verificar(msg):
        IsAuth = False
        bot.send_message(USER_ID, 'Deslogado com sucesso')
    

def verificar(msg):
    ID = msg.from_user.id
    if IsAuth == False: 
        # enviando uma mensagem para o usuário
        bot.send_message(ID, 'E necessario autenticar-se para usar o bot')
        bot.send_message(ID, 'Digite /iniciar para autenticar-se')
        return False
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    ...


bot.polling()

" ONDE HOSPEDAR BOT TELEGRAM "
# n
