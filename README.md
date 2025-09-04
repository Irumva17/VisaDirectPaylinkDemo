# PayLink Demo Project

### Visa Direct Sandbox Integration

Ce projet est une démonstration d’intégration avec Visa Direct (sandbox).
Il illustre deux fonctionnalités principales :

- Push Funds Transaction (PFT)
  → Sert à envoyer de l’argent depuis le compte d’un expéditeur vers le compte d’un bénéficiaire.
    Exemple : un wallet mobile ou une microfinance qui veut créditer le compte d’un client.

- Transaction Query API
  → Permet de suivre l’état d’une transaction (réussie, en attente, échouée).
    Exemple : vérifier si un transfert envoyé par Visa Direct a bien été reçu par le bénéficiaire

### 1. Créer un projet Visa Developer(pour avoir votre propre projet)

- Allez sur le [Visa Developer Center](https://developer.visa.com/).
- Créez un compte si vous n'en avez pas.
- Créez un nouveau projet.
- Ajouter le Nom d'un projet(VISADirectDemo dans mon cas).
- Sélectionnez l'API "Visa Direct" et ajoutez-les à votre projet.
- Cliquez sur "Créer" pour créer votre projet.
- Récupérez vos identifiants API Key(key123....pem)
- clique sur le projet et va a l'onglet Credentials copierUser ID, Password et aussi telecharge le certificat du projet(cert.pem).

Jusqu'à présent vous avez votre projet et vos identifiants.

### 2. voici le structure de votre projet

```
├── data.py
├── helloworld.py
├── main.py
├── keys
│   ├── cert.pem
│   └── votreKey.pem
├── requirements.txt
└── README.md
```

### 3. configurer le projet 

- vous aller creer un dossier keys/ cela que vous aller mettre votre propre cert.pem et key.pem que vous avez deja enregistrer dans votre ordinateur.

- puis creer data.py cela que vous aller mettre vos identifiants 
    `exemple`

    ```
    user_id = "Votre Id"  
    password = "Votre Password" 
    cert = "keys/cert.pem"
    key = "keys/VotreKey.pem"   
    ```

- apres ca vous pouvez lancer le Helloworld.py, tape ce (python helloworld.py) pour la verification de ce que vous avez fait et la reponse devrait etre `200(succees)` et un message qui dit `hello world`


- apres ca vous pouvez lancer enfin le main.py c'est la que j'ai fait une transaction push founds transaction et query api , le push founds c'est pour envoyer un le montant a quelq'un tandisque le query api c'est pour voir la liste de ce que vous avez push founds

- ``` les reponse doit etre 200(succees)```


### 4. lancer le projet

- si tu veux tester que tes identifiants sont bien configure tape ce `helloworld.py`
- si tu veux tester que tes transactions sont bien configure tape ce `main.py`

