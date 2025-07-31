from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/agendar', methods = ['GET','POST'])
def agendar():

    if request.method == 'GET':
        return render_template('agendar.html')

    elif request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        hora = request.form.get('hora')
        data = request.form.get('data')
        serviço = request.form.get('serviço')

        print(f'None: {nome} \nE-mail: {email} \ntelefone: {telefone} \hora: {hora} \nserviço {serviço}')
        # return render_template('agendar.html')
    

        dadosServico = {
            "nome":nome,
            "email":email,
            "telefone":telefone,
            "data":data,
            "hora":hora,
            "servico":serviço
        }

        return render_template('confirmacaoServico.html', dadosServicos = dadosServico)

app.run(debug=True)