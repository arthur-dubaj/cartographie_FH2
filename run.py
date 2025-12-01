from app.server import server

if __name__ == "__main__":
    print(">>> LANCEMENT DE L'APPLICATION")
    server.run(host="0.0.0.0", port=8050, debug=True)