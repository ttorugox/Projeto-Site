#render_template_string#
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site com Flask e Bootstrap</title>

    <!-- Bootstrap 5 CSS via CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            color: #333;
        }
        header h1 {
            color: #004aad;
        }
        section {
            background-color: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="#">Meu Site</a>
        </div>
    </nav>

    <!-- Header -->
    <header class="bg-light py-5 text-center">
        <div class="container">
            <h1 class="display-5 fw-bold">Bem-vindo ao Meu Site</h1>
            <p class="lead">Exemplo com HTML, CSS, JavaScript, Flask e Bootstrap</p>
        </div>
    </header>

    <!-- Formulário -->
    <section class="py-5 my-4">
        <div class="container">
            <h2 class="mb-4">Envie uma mensagem</h2>
            <form action="/enviar" method="POST" class="row g-3">
                <div class="col-12">
                    <label for="nome" class="form-label">Seu nome</label>
                    <input type="text" class="form-control" id="nome" name="nome" required>
                </div>
                <div class="col-12">
                    <label for="mensagem" class="form-label">Mensagem</label>
                    <textarea class="form-control" id="mensagem" name="mensagem" rows="5" required></textarea>
                </div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary">Enviar</button>
                </div>
            </form>
        </div>
    </section>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Script JS -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            console.log("Página carregada com sucesso!");
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    mensagem = request.form['mensagem']
    print(f"Mensagem de {nome}: {mensagem}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
