from flask import Flask, request, render_template

app = Flask(__name__)

# Instrucao para o 'barra'. Isso significa que quando alguem tentar abrir
# http://<ip do rasp>:5000  ele vai cair aqui.
#
@app.route("/")
def index():
    return  "Essa eh a pagina http://<ip do rasp>:5000" 

# Quando alguem tentar acessar http://<ip do rasp>:5000/exemplo_uso_post/
# Ele vai cair aqui
# A variavel chamada 'parametro_post' podera ser passada como parametro
# por quem tentar acessar essa pagina. A vantagem de passar parametros por
# POST, eh que ela nao fica visivel na URL. Ou seja, ela vem "por baixo dos
# panos" :) 
#
@app.route("/exemplo_uso_post/", methods=['GET', 'POST'])
def index_exempo_uso_post():
   param = request.form.get('parametro_post')
   return "Variavel recebida via POST: %s" % param

# Quando alguem tentar acessar http://<ip do rasp>:5000/exemplo_parametro_url/qualquer_coisa/
# ele vai cair aqui. 
# Nesse caso, tudo que vier depois da barra do 'exemplo_parametro_url/' o Flask vai atribuir
# na variavel que eu chamei de 'param'.
# Ou seja:
# Abrindo a url http://<ip do rasp>:5000/exemplo_parametro_url/o_que_quer_que_for
# A pagina resultante sera:
#
# Parametro recebido pela URL: o_que_quer_que_for
#
@app.route("/exemplo_parametro_url/<param>")
def index_exemplo_parametro_url(param=None):
    return "Parametro recebido pela URL: %s" % param

# Usando template pra salvar todo o HTML em um arquivo proprio
# E voce pode passar parametros que seu codigo python gera pra esse
# template. Veja a pasta 'templates' e o arquivo .template que tem
# de exemplo la dentro. 
#
# Assim como os exemplos acima, voce acessa essa parte abrindo no browser:
# http://<ip do rasp>:5000/exemplo_usando_template/
#
@app.route("/exemplo_usando_template/")
def index_exemplo_usando_template():
    return render_template('exemplo_usando_template.template', variavel1 = "var1", variavel2 = "var2") 

if __name__ == "__main__":
    app.run(host='0.0.0.0')

