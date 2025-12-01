# routes.py
from flask import request, session, redirect, render_template_string
from app.server import server


@server.route("/", methods=["GET", "POST"])
def login():
        error = None
        if request.method == "POST":
                if request.form.get("user") == "admin" and request.form.get("pwd") == "admin":
                        session["logged"] = True
                        return redirect("/app")
                else:
                        error = "Utilisateur ou mot de passe incorrect."

        return render_template_string("""
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <title>Connexion</title>
    <style>
        :root{--bg:#f6f8fb;--card:#ffffff;--accent:#4f46e5;--muted:#6b7280}
        html,body{height:100%;margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial}
        body{display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#eef2ff 0%,#ffffff 100%);color:#111}
        .card{width:540px;padding:42px;border-radius:18px;background:var(--card);box-shadow:0 9px 45px rgba(15,23,42,0.08);border:1px solid rgba(15,23,42,0.04)}
        h1{margin:0 0 12px;font-size:30px}
        p.lead{margin:0 0 27px;color:var(--muted);font-size:20px}
        label{display:block;font-size:19px;margin:15px 0 9px;color:#374151}
        input[type="text"],input[type="password"]{width:100%;padding:15px 18px;border-radius:12px;border:1px solid #e6e9ee;background:#fbfdff;box-sizing:border-box;font-size:16px}
        button{width:100%;margin-top:24px;padding:15px 18px;border-radius:12px;border:0;background:var(--accent);color:white;font-weight:600;cursor:pointer;font-size:17px}
        .error{background:#ffefef;color:#b91c1c;padding:12px;border-radius:12px;margin-bottom:14px;font-size:16px;border:1px solid #f5c2c2}
        .footer{font-size:16px;color:var(--muted);text-align:center;margin-top:20px}
        @media (max-width:640px){.card{width:92%;padding:28px}}
    </style>
</head>
<body>
    <form method="POST" class="card" autocomplete="off" aria-labelledby="login-title">
        <div style="text-align:center;margin-bottom:12px">
            <img src="app/assets/logo_FH.png" alt="" style="width:84px;height:84px;border-radius:12px;object-fit:cover;filter:grayscale(0.05);">
        </div>
        <h1 id="login-title">Connexion</h1>
        <p class="lead">Connectez-vous pour accéder à l'application.</p>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        <label for="user">Nom d'utilisateur</label>
        <input id="user" name="user" type="text" required autofocus>
        <label for="pwd">Mot de passe</label>
        <input id="pwd" name="pwd" type="password" required>
        <button type="submit">Se connecter</button>
        
    </form>
</body>
</html>
""", error=error)

@server.route("/app")
def protected():
    if not session.get("logged"):
        return redirect("/")

    from app.main import app
    return app.index()
