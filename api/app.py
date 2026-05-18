import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request  # <-- Ajoutez "request" ici

app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r", encoding="utf-8") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>"]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvee"}), 404
    return jsonify(ligne)
@app.route("/arrets")
def get_all_arrets():
    ensemble_arrets = set()
    
    # Parcourir chaque ligne et ajouter ses arrêts dans le set
    for ligne in lignes:
        for arret in ligne["listeArrets"]:
            ensemble_arrets.add(arret.strip()) # strip() enlève les espaces cachés
            
    # Trier par ordre alphabétique  et convertir en liste
    liste_unique_arrets = sorted(list(ensemble_arrets))
    
    return jsonify(liste_unique_arrets)
@app.route("/stats")
def get_stats():
    nb_total_lignes = len(lignes)
    
    # Somme de la clé "arrets" pour toutes les lignes
    somme_arrets = sum(ligne["arrets"] for ligne in lignes)
    
    # Trouver la ligne qui a le plus d'arrêts
    ligne_max = max(lignes, key=lambda l: l["arrets"])
    
    return jsonify({
        "nombre_total_lignes": nb_total_lignes,
        "nombre_total_arrets": somme_arrets,
        "ligne_plus_longue": {
            "numero": ligne_max["numero"],
            "nb_arrets": ligne_max["arrets"],
            "itineraire": f"{ligne_max['depart']} -> {ligne_max['arrivee']}"
        }
    })
@app.route("/lignes/recherche")
def recherche_lignes():
    # Récupérer le paramètre 'q', s'il n'existe pas, mettre une chaîne vide ""
    query = request.args.get("q", "").strip().lower()
    
    # Si aucun mot-clé n'est fourni, on peut retourner toutes les lignes ou une liste vide
    if not query:
        return jsonify([])
        
    # Filtrer les lignes si le départ ou l'arrivée contient le mot-clé
    resultats = [
        ligne for ligne in lignes 
        if query in ligne["depart"].lower() or query in ligne["arrivee"].lower()
    ]
    
    return jsonify(resultats)
if __name__ == "__main__":
    app.run(debug=True, port=5000)