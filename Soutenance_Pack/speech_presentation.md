# Guide de Présentation de la Soutenance (15 Minutes)

Ce document contient le script détaillé et fluide pour chaque diapositive de votre soutenance PFE, récrit dans un registre de langue courant, naturel et facile à prononcer à l'oral.

## Structure du Temps (15 Minutes Chrono)
*   **Partie 1 : Contexte & Enjeux (Slides 1 à 10) :** ~4 minutes 30s
*   **Partie 2 : Modélisation Deep Learning (Slides 11 à 18) :** ~4 minutes 30s
*   **Partie 3 : Déploiement Cloud & SOC (Slides 19 à 21) :** ~3 minutes (incluant 2 min de démonstration vidéo)
*   **Partie 4 : Validation & Perspectives (Slides 22 à 24) :** ~3 minutes
*   **Total :** 15 minutes.

---

## Script Courant et Fluide par Diapositive

### ⏱️ Partie 1 : Contexte & Enjeux (Slides 1 à 10) - Cible : 4 min 30s

#### Slide 1 : Page de garde (30s)
*   **Speech :** 
    > *"Bonjour Madame la Présidente, bonjour à tous les membres du jury. Je suis très heureux de vous présenter aujourd'hui mon projet de fin d'études pour l'obtention de mon diplôme d'Ingénieur d'État. Mon travail porte sur le développement d'un système de détection d'intrusions réseau, basé sur le Deep Learning. J'ai réalisé ce projet au sein du service R&D de 3D Smart Factory à Mohammedia, sous l'encadrement de Mme Saida HAIDRAR pour l'école HESTIM, et de M. Hamza MOUNCIF, mon maître de stage."*
*   **Cues visuels :** Posture droite, regardez l'ensemble du jury.
*   **Transition :** *"Pour cette présentation, voici le plan que nous allons suivre."*

#### Slide 2 : Plan de la présentation (20s)
*   **Speech :**
    > *"Notre présentation va suivre un plan en six étapes. Nous commencerons par l'introduction et le contexte du projet. Ensuite, nous verrons la partie Deep Learning avec le comparatif de nos 11 modèles. Après cela, je vous présenterai l'architecture cloud sur AWS. Nous verrons ensuite le pipeline technique en détail. Puis, nous passerons à la démonstration et à la validation avec de vraies attaques. Et enfin, nous terminerons par le bilan et les perspectives du projet."*
*   **Cues visuels :** Balayez d'un geste de la main les 6 parties affichées à l'écran.
*   **Transition :** *"Débutons par le contexte général de la sécurité de nos réseaux."*

#### Slide 3 : Introduction Générale (40s)
*   **Speech :**
    > *"Aujourd'hui, avec le cloud et les objets connectés, les réseaux d'entreprises sont plus exposés que jamais à des attaques complexes et discrètes. Pour les surveiller, on utilise des NIDS (des systèmes de détection d'intrusions). Mais les outils actuels ont des limites : ils ratent les nouvelles attaques (les Zero-Days), ils génèrent trop de fausses alertes à cause de règles trop rigides, et ils sont bloqués par le chiffrement du trafic, comme avec TLS 1.3, qui empêche de lire le contenu des paquets."*
*   **Cues visuels :** Pointez la carte gauche (Contexte Cyber) puis la carte droite (Limites du SOC : Zéro-Day, Faux Positifs, TLS 1.3).
*   **Transition :** *"Pour bien comprendre ces limites, étudions un scénario d'attaque type."*

#### Slide 4 : Scénario d'Attaque & Problématique Centrale (45s)
*   **Speech :**
    > *"Prenons un exemple concret : une attaque de force brute lente et distribuée sur SSH, lancée depuis 15 adresses IP différentes, avec seulement une tentative par minute. Les outils classiques comme Fail2ban ne voient rien car l'attaque est trop lente. Et les systèmes à signatures échouent aussi car chaque connexion a l'air normale. Notre approche par Deep Learning permet de régler ce problème : en analysant les statistiques des flux (comme la taille des paquets et le timing), l'IA détecte ce comportement anormal. Notre problématique est donc : comment créer un système de détection par IA qui soit très précis, léger, ultra-rapide (moins d'une milliseconde) et connecté en temps réel sur le cloud ?"*
*   **Cues visuels :** Pointez la carte rouge « Bruteforce distribué », puis la verte « Analyse comportementale » et l'encadré « Problématique » en bas.
*   **Transition :** *"Ce projet a été développé en partenariat étroit avec notre structure d'accueil."*

#### Slide 5 : Présentation de l'Entreprise d'Accueil (25s)
*   **Speech :**
    > *"J'ai réalisé mon stage au sein du service R&D de 3D Smart Factory à Mohammedia. C'est une entreprise innovante qui fait le pont entre la recherche et la mise en production de solutions industrielles. Durant ces mois, j'ai pu travailler dans un environnement idéal grâce à trois piliers : un fort encouragement à l'innovation, un encadrement technique au quotidien avec la méthode agile, et un accompagnement pour valoriser et bien dimensionner le projet."*
*   **Cues visuels :** Mentionnez le logo de 3D Smart Factory et les trois icônes (Encouragement, Encadrement, Financement).
*   **Transition :** *"Sur cette base, nous avons délimité le périmètre du projet."*

#### Slide 6 : Cadrage & Périmètre du Projet (35s)
*   **Speech :**
    > *"L'objectif principal a été de passer d'une simple étude théorique sur ordinateur à un vrai système opérationnel en continu sur le cloud AWS. Dans le périmètre du projet, on retrouve : l'équilibrage des données, l'entraînement de 11 modèles d'IA, la capture du trafic avec la sonde NFStream, le déploiement automatique de l'infrastructure et la création du dashboard SOC. À l'inverse, nous ne remplaçons pas les outils de gestion de logs existants et nous ne faisons pas de blocage automatique des attaques. Ce système est destiné aux analystes SOC et aux équipes de sécurité."*
*   **Cues visuels :** Pointez la bannière « Transition », puis les blocs « Dans le Périmètre », « Hors Périmètre » et « Acteurs/Cible ».
*   **Transition :** *"Afin de concevoir le système, nous avons analysé le cahier des charges."*

#### Slide 7 : Besoins Fonctionnels & Non Fonctionnels (35s)
*   **Speech :**
    > *"Pour concevoir notre système, nous avons structuré nos exigences en deux volets en collaboration avec 3D Smart Factory. Côté fonctionnel, nous ciblons 5 points : la détection multi-classes pour classifier 15 types de flux, la capture passive non intrusive, l'alerte temps réel transmise en moins de 5 secondes au SOC, l'archivage persistant des logs, et un dashboard de supervision web. Côté non-fonctionnel, les critères sont très stricts : un F1-score supérieur à 98 %, une inférence ultra-rapide de moins d'une milliseconde par flux sur CPU standard, un modèle de moins de 50 000 paramètres, une reproductibilité complète par IaC Terraform/Ansible, et enfin la sécurité par isolation stricte."*
*   **Cues visuels :** Pointez la colonne de gauche (les 5 besoins fonctionnels) puis la colonne de droite (les 6 exigences non fonctionnelles de performance, compacité et sécurité).
*   **Transition :** *"Voyons à présent comment le Deep Learning permet de lever les verrous technologiques de détection réseau pour satisfaire ces exigences."*

#### Slide 8 : L'avènement du Deep Learning pour le NIDS (35s)
*   **Speech :**
    > *"Le Deep Learning change la donne grâce à trois avantages. Premièrement, l'extraction automatique de caractéristiques : l'IA trouve elle-même les liens invisibles entre les données du réseau, sans qu'un expert ait besoin de concevoir des formules manuellement. Deuxièmement, la capacité de généralisation : le modèle apprend le comportement normal du réseau pour repérer les attaques, même inconnues. Troisièmement, la résistance au chiffrement : plus besoin de lire le contenu des messages, l'IA travaille uniquement sur les statistiques du flux, comme la taille des paquets ou les délais."*
*   **Cues visuels :** Soulignez les 3 concepts clés (Extraction de Caractéristiques, Généralisation, Anti-chiffrement TLS 1.3).
*   **Transition :** *"Afin de concevoir et réaliser ce système en 20 semaines, nous avons planifié nos sprints selon une méthodologie rigoureuse."*

#### Slide 9 : Méthodologie de Travail & Planning (25s)
*   **Speech :**
    > *"Pour ce projet, j'ai suivi la méthode agile SCRUM. Cela a permis de faire des tests réguliers et d'éviter l'effet tunnel. Sur les 20 semaines de travail, le planning s'est découpé ainsi : le cadrage en février, la préparation et l'équilibrage des données en mars, le comparatif des modèles d'IA en avril, le développement de l'infrastructure en mai, le déploiement sur AWS et la création de l'interface SOC en juin, et enfin les tests de validation."*
*   **Cues visuels :** Faites un balayage rapide du diagramme de Gantt (de février à juin).
*   **Transition :** *"Pour entraîner et valider nos architectures dans le cadre de ce planning, nous avons exploité un jeu de données de référence."*

---

### ⏱️ Partie 2 : Modélisation Deep Learning (Slides 11 à 18) - Cible : 4 min 30s

#### Slide 10 : Le Dataset de Référence : CICIDS2017 (35s)
*   **Speech :**
    > *"Pour entraîner nos modèles, nous avons utilisé le jeu de données de référence CICIDS2017. Il contient plus de 2,8 millions de flux réseau, chacun décrit par 77 variables statistiques. Il regroupe 15 classes différentes : du trafic normal et 14 types d'attaques moderne, allant des attaques web aux dénis de service, en passant par les infiltrations de réseau."*
*   **Cues visuels :** Pointez les grands chiffres (2.8M de flux, 77 variables, 15 classes) et la taxonomie des menaces.
*   **Transition :** *"Pour mieux comprendre ces flux réseau, analysons les variables caractéristiques."*

#### Slide 11 : Variables Caractéristiques (45s)
*   **Speech :**
    > *"Pour chaque flux réseau, on commence par analyser les informations classiques d'identification, comme les adresses IP et les ports, ainsi que les drapeaux TCP pour repérer les scans. Mais la vraie force de notre modèle réside dans les statistiques comportementales du trafic. Par exemple, on surveille la **Durée du Flux** (ou *Flow Duration*), qui s'effondre sous la seconde lors d'un DDoS, et le **Temps Inter-Arrivée** (ou *Fwd IAT Total*), qui mesure l'espacement temporel entre les paquets reçus. Côté volumétrie, on observe le **Volume des Paquets Retour** (ou *Total Length Bwd*), qui correspond à la taille totale des paquets de retour et qui explose en cas d'exfiltration, ainsi que le **Débit de Paquets Aller** (ou *Fwd Packets/s*). Enfin, la **Fenêtre TCP Initiale** (ou *Init Win Fwd*), qui indique la taille de la fenêtre réseau à l'aller, nous permet de repérer instantanément des outils de scan comme Nmap grâce à leur signature réseau spécifique."*
*   **Cues visuels :** Pointez le Quintuplet Standard, les drapeaux TCP à gauche, puis détaillez le contraste Sain (Vert) vs Attaque (Orange) sur les jauges temporelles et de débits à droite.
*   **Transition :** *"Ces variables brutes doivent passer par un pipeline de prétraitement rigoureux."*

#### Slide 12 : Pipeline de Prétraitement & Équilibrage des Données (45s)
*   **Speech :**
    > *"Avant d'entraîner l'IA, les données passent par un nettoyage en 4 étapes. Première étape : on supprime les valeurs infinies et on remplace les valeurs manquantes par la médiane de l'ensemble d'entraînement pour éviter les fuites de données. Deuxième étape : on utilise la méthode IQR à 1,5 pour réduire l'effet des valeurs aberrantes sans perdre les signatures d'attaques. Troisième étape : on applique une normalisation Z-score sur nos 77 variables. Enfin, quatrième étape : on équilibre le jeu de données en réduisant le trafic normal à 50 000 lignes et en utilisant la méthode SMOTE pour générer de faux exemples des attaques rares, ce qui stabilise l'apprentissage."*
*   **Cues visuels :** Suivez le schéma horizontal de gauche à droite (Étape 1 Nettoyage, Étape 2 IQR, Étape 3 Z-Score, Étape 4 SMOTE).
*   **Transition :** *"C'est sur ces données équilibrées que nous avons entraîné nos architectures."*

#### Slide 13 : Les 11 Architectures de Deep Learning Testées (35s)
*   **Speech :**
    > *"Nous avons testé et comparé 11 modèles de réseaux de neurones, répartis en 4 familles : des modèles standards simples (MLP), des modèles spatiaux (CNN 1D et ResNet 1D), des modèles séquentiels (LSTM, GRU, BiLSTM) et enfin des modèles intégrant des mécanismes d'attention, comme les réseaux TCN et notre modèle final, l'Attention MLP."*
*   **Cues visuels :** Montrez la grille de répartition en 4 blocs.
*   **Transition :** *"Pour entraîner ces réseaux, nous avons appliqué un protocole d'entraînement strict."*

#### Slide 14 : Processus d'Entraînement des Modèles (35s)
*   **Speech :**
    > *"Pour l'entraînement, nous avons configuré le système pour pénaliser plus fortement les erreurs sur les attaques rares grâce à une fonction de perte pondérée. Nous avons utilisé l'optimiseur Adam, avec un taux d'apprentissage de 0,001 qui diminue automatiquement si le modèle stagne. Enfin, l'entraînement est limité à 50 époques, avec un mécanisme d'arrêt précoce (Early Stopping) après 10 époques sans amélioration pour éviter le surapprentissage."*
*   **Cues visuels :** Pointez les 2 blocs théoriques en haut (Cross-Entropy et Adam), puis la ligne des 4 paramètres en bas.
*   **Transition :** *"Voici les résultats quantitatifs de ce benchmark."*

#### Slide 15 : Résultats du Benchmark Quantitatif (45s)
*   **Speech :**
    > *"Ce tableau compare la précision des modèles et leur vitesse. On voit que les modèles très complexes comme le BiLSTM sont trop lents (4,8 ms d'inférence) pour du temps réel sans un GPU coûteux. À l'inverse, le MLP de base est très rapide (0,35 ms) mais moins précis. Notre modèle Attention MLP offre le meilleur compromis : il atteint 98,28 % de précision et un F1-score de 98,29 %, tout en s'exécutant en seulement 0,42 ms. De plus, il est très léger avec moins de 50 000 paramètres."*
*   **Cues visuels :** Soulignez la ligne colorée du tableau (Attention MLP) et comparez-la aux lignes BiLSTM et MLP Standard.
*   **Transition :** *"Détaillons l'architecture interne et le fonctionnement de notre modèle Attention MLP."*

#### Slide 16 : Architecture Interne de l'Attention MLP (40s)
*   **Speech :**
    > *"Voici comment fonctionne notre modèle en interne. Les 77 caractéristiques du flux entrent dans le réseau et se séparent en deux branches. La branche supérieure calcule un score d'attention (entre 0 et 1) pour chaque variable. On multiplie ensuite les données d'entrée par ces scores : c'est le produit de Hadamard. Ce filtrage dynamique permet d'éliminer les informations inutiles ou bruyantes. Le signal filtré passe ensuite dans le classificateur (un MLP à deux couches de 128 et 64 neurones) pour prédire le type d'attaque en seulement 0,42 ms."*
*   **Cues visuels :** Suivez pas à pas le flux sur le diagramme (Entrée -> Branche Attention -> Multiplicateur Hadamard -> Classificateur MLP -> Classification).
*   **Transition :** *"Ce modèle étant finalisé, voyons comment il s'intègre dans notre infrastructure de production."*

---

### ⏱️ Partie 3 : Déploiement Cloud & SOC (Slides 19 à 21) - Cible : 3 min

#### Slide 17 : Architecture Globale du CyberRange Cloud (45s)
*   **Speech :**
    > *"Pour tester notre système, nous avons créé une infrastructure sur AWS. Depuis une machine d'attaque Kali Linux, nous lançons des attaques contre nos serveurs de production. Le trafic de ces serveurs est copié en direct et de manière invisible grâce au service Traffic Mirroring d'AWS, puis envoyé vers notre sonde IDS. Cette sonde extrait les données de flux avec NFStream et utilise notre IA pour détecter les attaques. Si une anomalie est trouvée, l'alerte est envoyée dans une file d'attente SQS, puis traitée par une fonction Lambda pour être enregistrée dans DynamoDB. Enfin, notre serveur de supervision pousse l'alerte instantanément vers le dashboard du SOC via WebSockets."*
*   **Cues visuels :** Pointez la zone d'attaque (gauche), puis le VPC AWS (centre), les subnets (Public, IDS Probe, Supervision), et le pipeline serverless (SQS, Lambda, DynamoDB à droite).
*   **Transition :** *"Pour déployer et piloter cette infrastructure, nous avons utilisé des outils modernes."*

#### Slide 18 : Technologies & Outils par Niveau (20s)
*   **Speech :**
    > *"Pour réaliser ce projet, nous avons utilisé des technologies modernes : Terraform pour déployer automatiquement toute l'infrastructure sur AWS, Ansible pour configurer les machines à distance, Docker pour empaqueter nos microservices, et Python avec PyTorch pour développer et faire tourner notre modèle de Deep Learning."*
*   **Cues visuels :** Pointez les 4 sections d'outils (Provisioning, Configuration, Dev & CI/CD, Deep Learning).
*   **Transition :** *"Voici une démonstration concrète de l'interface SOC lors d'une attaque en temps réel."*

#### Slide 19 : Dashboard du SOC & Démonstration Vidéo (2 min 30s total : 30s Intro + 2 min Vidéo)
*   **Speech (Intro - 30s) :**
    > *"Notre tableau de bord en React permet de superviser la sécurité. Il contient quatre onglets : un résumé global, un flux d'alertes en temps réel, des statistiques et un onglet d'enrichissement qui affiche le nom des machines AWS touchées. Je vous propose de lancer une vidéo de démonstration de 2 minutes pour voir comment le système réagit en direct face à une attaque."*
*   **Action :** Déclenchez la vidéo. Laissez-la tourner durant ses 2 minutes. Vous pouvez faire des commentaires succincts sur les détections d'alertes instantanées qui s'affichent à l'écran.
*   **Transition :** *"Pour aller plus loin, et au cas où la vidéo de démonstration ne puisse pas être jouée, voici un aperçu détaillé des quatre principales vues de ce tableau de bord."*

#### Slide 20 : Supervision SOC — Vues Synthèse & Inférence (20s)
*   **Speech :**
    > *"Cette première diapositive montre les vues globales de l'interface. À gauche, la vue d'ensemble, ou Overview, résume les statistiques globales, le statut des sondes et les parts respectives des attaques détectées. À droite, l'onglet Live Feed affiche le flux d'alertes en continu via WebSockets. Chaque ligne représente un flux d'attaque classifié en temps réel, avec des codes couleur alertant l'opérateur en fonction de la sévérité."*
*   **Cues visuels :** Pointez la vue d'ensemble à gauche, puis le journal des alertes dynamique à droite.
*   **Transition :** *"Voyons à présent les détails et les statistiques de ces alertes."*

#### Slide 21 : Supervision SOC — Métriques & Enrichissement (20s)
*   **Speech :**
    > *"La deuxième diapositive présente les analyses et l'enrichissement. À gauche, l'onglet Statistiques montre l'activité temporelle, le taux de faux positifs et la latence d'inférence en direct sous la milliseconde. À droite, l'onglet de détails permet d'enrichir une alerte avec ses 77 variables NFStream d'origine, le protocole réseau, l'adresse MAC et l'emplacement géographique de la source."*
*   **Cues visuels :** Pointez les graphiques analytiques à gauche, puis la fiche d'enrichissement d'alerte à droite.
*   **Transition :** *"Ces visualisations concrétisent les résultats opérationnels de notre système. Analysons maintenant les performances globales lors des attaques."*

---

### ⏱️ Partie 4 : Validation & Perspectives (Slides 22 à 25) - Cible : 3 min

#### Slide 22 : Validation Expérimentale & Attaques (45s)
*   **Speech :**
    > *"Pour valider le système, nous avons injecter de vraies attaques (DDoS SYN Flood, scans de ports et ICMP Flood) au milieu d'un fort trafic normal. Les résultats sont excellents : l'IA a détecté 100 % des attaques, l'alerte s'affiche sur le dashboard du SOC en moins de 2 secondes de bout-en-bout, et surtout, il y a un impact de 0 % sur les performances des serveurs surveillés grâce à la capture passive du trafic."*
*   **Cues visuels :** Soulignez le bloc gauche (Attaques Simulées) puis les 3 métriques clés à droite (100% Vrais Positifs, Latence < 2s, Impact CPU de 0,00%).
*   **Transition :** *"Ces validations démontrent une efficacité opérationnelle maximale. Mais comment ces résultats réels se positionnent-ils face aux travaux académiques existants ? C'est ce que nous allons voir avec cette validation comparative."*

#### Slide 23 : Validation Comparative — État de l'Art vs Notre Apport (45s)
*   **Speech :**
    > *"Notre solution se distingue des travaux de recherche de l'état de l'art par sa légèreté et son application concrète. La plupart des publications récentes proposent des modèles inadaptés pour des sondes en bordure : par exemple, le Transformer de Ferrag (2023) ou le LSTM de Yin (2021) souffrent d'une complexité excessive avec des millions de paramètres. D'autres, comme le BiLSTM de Yang (2023) ou le double Autoencodeur en cascade d'Andresini (2022), induisent une latence trop importante pour le temps réel. Enfin, des modèles comme le CNN 1D de Zhang (2022) souffrent d'un biais topologique en dépendant de l'ordre arbitraire des colonnes du trafic. À l'inverse, notre Attention MLP ne compte que 49 915 paramètres, s'exécute en 0,42 ms sur un CPU standard, et surtout, nous l'avons validé en conditions réelles sur notre CyberRange AWS, ce qui manque à la quasi-totalité des travaux académiques."*
*   **Cues visuels :** Pointez d'abord la carte horizontale du haut recensant les modèles référencés, puis comparez la carte des limites critiques (bas gauche) à notre apport & avantages (bas droite).
*   **Transition :** *"Ce positionnement unique confirme la viabilité de notre approche et nous amène naturellement au bilan de notre projet."*

#### Slide 24 : Conclusion & Perspectives (45s)
*   **Speech :**
    > *"En conclusion, ce projet a permis de passer d'un modèle d'IA théorique à un système de surveillance concret et opérationnel sur AWS. Le modèle Attention MLP s'est montré idéal grâce à sa petite taille (50 Ko) et sa rapidité. Pour la suite, nous envisageons d'intégrer un pipeline MLOps pour mettre à jour le modèle automatiquement si le trafic change, d'ajouter de l'IA explicable avec la méthode SHAP pour détailler les alertes, et de mettre en place un blocage automatique des attaques en modifiant les règles de sécurité AWS à la volée."*
*   **Cues visuels :** Pointez la carte gauche (Bilan) puis la carte droite (Perspectives).
*   **Transition :** *"J'arrive au terme de mon exposé."*

#### Slide 25 : Merci pour votre attention (30s)
*   **Speech :**
    > *"Pour finir, je tiens à remercier chaleureusement les équipes de 3D Smart Factory pour leur accueil et leur aide, ainsi que l'école HESTIM. Merci beaucoup pour votre attention. Je suis maintenant ravi de répondre à vos questions et d'échanger avec vous."*
*   **Cues visuels :** Regardez les membres du jury, souriez poliment et attendez les questions.
