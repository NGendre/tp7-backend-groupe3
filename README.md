# tp7-backend-groupe3
Développement d'une application web Backend 

## Requirements
Pour faire fonctionner l'application, veuillez verifier que vous possedez une version de python 3.11
Installez les dépendances avec cette commande: 
````bash
pip install -r requirements.txt
````

## Environement
L'application a des dépendances d'environnement.
Pour fonctionner, créez un fichier `.env` à la racine et tapez ces variables dans le fichier :
```txt
DATABASE_URL=votre_url #exemple: localhost
DATABASE_USER=root #exemple: root
DATABASE_PASSWORD=votre_password #exemple: TotoTutu123
DATABASE_NAME=votre_nom_de_BDD #exemple: fromagerie_com
```

## Lancer l'application
Pour démarrer l'app tapez la commande suivante:
```bash
uvicorn main:app
```

## Documentation 
### Code source
La documentation est générée avec `pdoc`. Tapez la commande suivante et cela vous créera un dossier de documentation `/html` à la racine.
````bash
pdoc --html src
````

### API
Une fois l'application lancée, vous pouvez accéder à la documentation des points d'entrée de l'API sur cette [URL](http://localhost:8000/docs)
```txt
http://localhost:8000/docs
```
