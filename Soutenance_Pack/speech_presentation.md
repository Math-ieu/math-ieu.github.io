# Guide de Présentation de la Soutenance (15 Minutes)

Ce document contient le script détaillé et fidèle pour chaque diapositive de votre soutenance PFE. Il a été rigoureusement réaligné sur le contenu textuel et structurel exact de vos diapositives.

## Structure du Temps (15 Minutes Chrono)
*   **Partie 1 : Contexte & Enjeux (Slides 1 à 9) :** ~3 minutes 30s
*   **Partie 2 : Modélisation Deep Learning (Slides 10 à 18) :** ~5 minutes 30s
*   **Partie 3 : Déploiement Cloud & SOC (Slides 19 à 21) :** ~3 minutes (incluant 2 min de démonstration vidéo)
*   **Partie 4 : Validation & Perspectives (Slides 22 à 24) :** ~3 minutes
*   **Total :** 15 minutes.

---

## Script Fidèle par Diapositive

### ⏱️ Partie 1 : Contexte & Enjeux (Slides 1 à 10) - Cible : 4 min 30s

#### Slide 1 : Page de garde (30s)
*   **Speech :** 
    > *"Madame la Présidente, Mesdames et Messieurs les membres du jury, bonjour. Je vous présente aujourd'hui mon projet de fin d'études en vue de l'obtention du diplôme d'Ingénieur d'État Marocain en Ingénierie Informatique & Intelligence Artificielle, option Intelligence Artificielle & Big Data. Mon travail s'intitule : « Développement d'un système de détection d'intrusions réseau (NIDS) basé sur le Deep Learning ». Ce projet a été mené au sein de la structure de R&D de 3D Smart Factory à Mohammedia, sous le double encadrement de Mme Saida HAIDRAR pour HESTIM, et de M. Hamza MOUNCIF en tant que maître de stage."*
*   **Cues visuels :** Posture droite, regardez l'ensemble du jury.
*   **Transition :** *"Pour structurer cette soutenance, voici le plan que nous allons suivre."*

#### Slide 2 : Plan de la présentation (20s)
*   **Speech :**
    > *"Notre présentation s'articulera autour de six parties majeures. D'abord, l'Introduction et le Contexte cyber. Ensuite, la Modélisation Deep Learning avec le benchmark de nos 11 architectures. Troisièmement, la conception de notre Architecture AWS et de son CyberRange. Quatrièmement, la Cartographie Technologique du pipeline avec NFStream, SQS et DynamoDB. Cinquièmement, la Démonstration et la Validation expérimentale sous scénarios d'attaques réelles. Et enfin, nous conclurons par le Bilan et les Perspectives d'évolution de ce projet."*
*   **Cues visuels :** Balayez d'un geste de la main les 6 parties affichées à l'écran.
*   **Transition :** *"Débutons par le contexte général de la sécurité de nos réseaux."*

#### Slide 3 : Introduction Générale (40s)
*   **Speech :**
    > *"Le contexte cyber actuel est marqué par une hybridation Cloud et IoT qui multiplie la surface d'exposition des entreprises, face à des menaces transverses et furtives comme les scans distribués ou les attaques APT. C'est là que la surveillance passive via un NIDS prend tout son sens. Cependant, nos SOC font face à des limites majeures : les moteurs traditionnels basés sur les signatures sont inefficaces contre les attaques Zero-Day, les seuils statiques inondent les analystes de faux positifs (fatigue des alertes), et le chiffrement global comme TLS 1.3 bloque l'inspection profonde des paquets."*
*   **Cues visuels :** Pointez la carte gauche (Contexte Cyber) puis la carte droite (Limites du SOC : Zéro-Day, Faux Positifs, TLS 1.3).
*   **Transition :** *"Pour bien comprendre ces limites, étudions un scénario d'attaque type."*

#### Slide 4 : Scénario d'Attaque & Problématique Centrale (45s)
*   **Speech :**
    > *"Prenons le cas concret d'une attaque de Bruteforce SSH distribué et lent, menée depuis 15 IPs distinctes à raison d'une seule tentative par minute et par machine. Face à cela, les seuils de fréquence de blocage comme Fail2ban sont contournés car l'attaque est trop lente. Les signatures classiques échouent car chaque paquet SSH est techniquement valide. Notre approche par Deep Learning permet de capturer les métadonnées de flux (tailles des paquets, délais inter-arrivées) pour détecter cette anomalie temporelle fine. D'où notre problématique : comment concevoir un NIDS basé sur l'IA qui soit précis, léger (moins de 50 000 paramètres), rapide (inférence en moins d'une milliseconde) et intégré en temps réel sur le Cloud ?"*
*   **Cues visuels :** Pointez la carte rouge « Bruteforce distribué », puis la verte « Analyse comportementale » et l'encadré « Problématique » en bas.
*   **Transition :** *"Ce projet a été développé en partenariat étroit avec notre structure d'accueil."*

#### Slide 5 : Présentation de l'Entreprise d'Accueil (25s)
*   **Speech :**
    > *"Ce stage s'est déroulé au sein de la structure mixte de R&D de 3D Smart Factory, située à Mohammedia. C'est un incubateur d'innovation industrielle qui combine recherche appliquée et mise en production. Durant ce stage, j'ai bénéficié des trois piliers d'accueil de l'entreprise : un encouragement constant à l'innovation, un encadrement technique rapproché basé sur les méthodes agiles, et un soutien sur le dimensionnement et la valorisation du projet."*
*   **Cues visuels :** Mentionnez le logo de 3D Smart Factory et les trois icônes (Encouragement, Encadrement, Financement).
*   **Transition :** *"Sur cette base, nous avons délimité le périmètre du projet."*

#### Slide 6 : Cadrage & Périmètre du Projet (35s)
*   **Speech :**
    > *"La transition majeure de ce projet a été de passer d'un simple benchmark théorique hors-ligne à un pipeline opérationnel continu sur AWS. Dans le périmètre, nous retrouvons l'équilibrage SMOTE, l'entraînement de 11 réseaux profonds, la capture continue par sonde NFStream, l'automatisation de l'infrastructure et le dashboard SOC. Hors périmètre, nous ne remplaçons pas les SIEM applicatifs existants, nous ne faisons pas de mitigation active automatique (SOAR), ni de corrélation de logs système ou d'optimisation multi-région. Nos acteurs cibles restent les analystes SOC et les ingénieurs SecOps."*
*   **Cues visuels :** Pointez la bannière « Transition », puis les blocs « Dans le Périmètre », « Hors Périmètre » et « Acteurs/Cible ».
*   **Transition :** *"Afin de concevoir le système, nous avons analysé le cahier des charges."*

#### Slide 7 : Besoins Fonctionnels & Non Fonctionnels (35s)
*   **Speech :**
    > *"Notre analyse se divise en deux volets. Les besoins fonctionnels suivent un pipeline technique en 4 étapes : la capture et l'ingestion passive du trafic, le prétraitement et l'inférence temps réel sur 15 classes d'attaques, la centralisation des alertes sur le SOC, et enfin la validation via des scénarios d'attaques reproductibles. Les besoins non fonctionnels imposent quant à eux des contraintes strictes : une latence globale de traitement de bout-en-bout inférieure à 2 secondes, une scalabilité face aux pics de trafic, une haute disponibilité par architecture découplée, et une sécurité par capture hors-bande non intrusive."*
*   **Cues visuels :** Suivez la timeline A, B, C, D à gauche, puis les 4 blocs de contraintes à droite (Latence, Scalabilité, Disponibilité, Sécurité).
*   **Transition :** *"Étudions à présent pourquoi les signatures classiques ont atteint leurs limites."*

#### Slide 8 : Limites des Approches Traditionnelles (30s)
*   **Speech :**
    > *"Trois verrous majeurs limitent les NIDS traditionnels comme Snort ou Suricata. D'abord, l'impuissance face aux attaques inédites (Zero-Days) car aucun motif n'existe dans la base. Ensuite, le chiffrement généralisé (notamment TLS 1.3) qui rend le contenu des paquets opaque pour le Deep Packet Inspection. Enfin, la saturation des CPU à très haut débit (plus de 10 Gbps) provoquée par la complexité de l'analyse de signatures textuelles, entraînant des pertes de paquets."*
*   **Cues visuels :** Pointez les 3 cartes de limites (Zero-Days, Chiffrement TLS 1.3, Surcharges CPU).
*   **Transition :** *"Voyons à présent comment le Deep Learning permet de lever ces verrous technologiques."*

#### Slide 9 : L'avènement du Deep Learning pour le NIDS (35s)
*   **Speech :**
    > *"Le Deep Learning apporte trois révolutions majeures pour la détection d'intrusions : d'abord, l'auto-apprentissage, qui extrait automatiquement des patterns abstraits sans nécessiter de feature engineering manuel. Ensuite, une capacité de généralisation probabiliste pour modéliser le comportement normal et identifier les attaques inconnues. Enfin, et c'est crucial face au chiffrement TLS 1.3, il s'affranchit de l'inspection de contenu en travaillant uniquement sur les caractéristiques statistiques des flux réseau, comme les volumes d'octets et les durées."*
*   **Cues visuels :** Soulignez les 3 concepts clés (Auto-apprentissage, Généralisation, Anti-chiffrement TLS 1.3).
*   **Transition :** *"Afin de concevoir et réaliser ce système en 20 semaines, nous avons planifié nos sprints selon une méthodologie rigoureuse."*

#### Slide 10 : Méthodologie de Travail & Planning (25s)
*   **Speech :**
    > *"Nous avons opté pour une méthodologie itérative Agile SCRUM pour éviter l'effet tunnel et valider en continu nos modèles IA. Le planning sur 20 semaines s'est découpé ainsi : cadrage en février, prétraitement et équilibrage des données en mars, benchmark des modèles en avril, industrialisation en mai, déploiement sur AWS et interface SOC en juin, pour finir par la validation et la rédaction finale."*
*   **Cues visuels :** Faites un balayage rapide du diagramme de Gantt (de février à juin).
*   **Transition :** *"Pour entraîner et valider nos architectures dans le cadre de ce planning, nous avons exploité un jeu de données de référence."*

---

### ⏱️ Partie 2 : Modélisation Deep Learning (Slides 11 à 18) - Cible : 4 min 30s

#### Slide 11 : Le Dataset de Référence : CICIDS2017 (35s)
*   **Speech :**
    > *"Notre dataset de référence est CICIDS2017. Il est composé de plus de 2,8 millions de flux réseau bidirectionnels, décrits par 77 variables statistiques. Il couvre 15 classes différentes, à savoir un trafic sain et 14 catégories d'attaques modernes réparties selon leur taxonomie, allant des attaques Web aux dénis de service et infiltrations."*
*   **Cues visuels :** Pointez les grands chiffres (2.8M de flux, 77 variables, 15 classes) et la taxonomie des menaces.
*   **Transition :** *"Pour mieux comprendre ces flux réseau, analysons les variables caractéristiques."*

#### Slide 12 : Variables Caractéristiques (45s)
*   **Speech :**
    > *"Pour caractériser chaque flux réseau, nous analysons d'abord son Quintuplet standard d'identification (les adresses IP, ports source et destination, ainsi que le protocole), complété par l'analyse des drapeaux TCP (Flags) comme SYN, ACK or RST pour détecter les scans de ports. Mais le point fort de notre approche réside dans l'analyse comportementale grâce aux variables statistiques de trafic. Nous mettons ici en évidence le contraste direct entre le trafic sain et le trafic d'attaque. Par exemple, la durée moyenne de flux (Flow Duration) est d'environ 15 à 30 secondes en trafic sain, alors qu'elle chute à moins de 1 seconde sous attaque DDoS. De même, le débit de paquets émis par seconde (Fwd Packets/s) passe de moins de 100 paquets en flux normal à plus de 76 000 en cas d'inondation. Enfin, la taille de fenêtre TCP initiale (Init Win Fwd) permet d'identifier la signature de scanners d'attaque comme Nmap qui force des fenêtres de 14.4k octets contre les tailles standards des OS légitimes."*
*   **Cues visuels :** Pointez le Quintuplet Standard (sans badge d'agrégation), les drapeaux TCP à gauche, puis détaillez le contraste Sain (Vert) vs Attaque (Orange) sur les jauges temporelles et de débits à droite.
*   **Transition :** *"Ces variables brutes doivent passer par un pipeline de prétraitement rigoureux."*

#### Slide 13 : Pipeline de Prétraitement & Équilibrage des Données (45s)
*   **Speech :**
    > *"Notre pipeline comprend 4 étapes. Étape 1 : le nettoyage des infinis et l'imputation des valeurs manquantes par la médiane sur l'ensemble d'entraînement pour éviter les fuites de données. Étape 2 : l'écrêtage IQR à un facteur 1,5 pour limiter l'impact des valeurs aberrantes sans supprimer de signatures d'attaques. Étape 3 : la normalisation Z-Score pour centrer et réduire nos 77 caractéristiques. Enfin, l'étape 4 : l'équilibrage hybride, consistant en un sous-échantillonnage aléatoire de la classe saine à 50 000 lignes et un sur-échantillonnage SMOTE des classes d'attaques minoritaires pour stabiliser l'apprentissage."*
*   **Cues visuels :** Suivez le schéma horizontal de gauche à droite (Étape 1 Nettoyage, Étape 2 IQR, Étape 3 Z-Score, Étape 4 SMOTE).
*   **Transition :** *"C'est sur ces données équilibrées que nous avons entraîné nos architectures."*

#### Slide 14 : Les 11 Architectures de Deep Learning Testées (35s)
*   **Speech :**
    > *"Nous avons testé et benchmarké 11 architectures organisées en 4 catégories : des baselines standards (MLP simple et profond), des modèles spatiaux (CNN 1D et réseaux résiduels ResNet 1D), des modèles séquentiels (LSTM, GRU et BiLSTM bidirectionnel) et enfin des modèles à mécanismes d'attention, notamment les réseaux de convolution causale TCN et notre modèle Attention MLP."*
*   **Cues visuels :** Montrez la grille de répartition en 4 blocs.
*   **Transition :** *"Pour entraîner ces réseaux, nous avons appliqué un protocole d'entraînement strict."*

#### Slide 15 : Processus d'Entraînement des Modèles (35s)
*   **Speech :**
    > *"Afin de gérer le déséquilibre persistant, nous avons appliqué une fonction de perte Cross-Entropy pondérée pour pénaliser fortement les erreurs sur les attaques. L'optimisation repose sur l'algorithme Adam avec un ajustement dynamique du taux d'apprentissage (ReduceLROnPlateau) débutant à 0,001. Nous avons configuré une taille de batch de 512, un maximum de 50 époques et une patience d'Early Stopping de 10 époques pour éviter tout sur-apprentissage."*
*   **Cues visuels :** Pointez les 2 blocs théoriques en haut (Cross-Entropy et Adam), puis la ligne des 4 paramètres en bas.
*   **Transition :** *"Voici les résultats quantitatifs de ce benchmark."*

#### Slide 16 : Résultats du Benchmark Quantitatif (45s)
*   **Speech :**
    > *"Ce benchmark compare les performances d'exactitude et le coût de calcul. On constate que les modèles complexes comme le BiLSTM ont un temps d'inférence trop lourd (4,8 ms) pour de la surveillance en temps réel sans carte GPU dédiée. Le MLP Standard est ultra-rapide (0,35 ms) mais manque de précision. Notre modèle Attention MLP s'impose comme le champion indiscutable avec une exactitude de 98,28 %, un F1-score de 98,29 %, un temps d'inférence de seulement 0,42 ms et une grande légèreté avec seulement 49 915 paramètres."*
*   **Cues visuels :** Soulignez la ligne colorée du tableau (Attention MLP) et comparez-la aux lignes BiLSTM et MLP Standard.
*   **Transition :** *"Voyons pourquoi l'Attention MLP offre ce compromis idéal."*

#### Slide 17 : Sélection du Modèle Optimal : Attention MLP (35s)
*   **Speech :**
    > *"L'Attention MLP a été choisi pour trois raisons. D'abord sa sensibilité, avec 98,28% d'exactitude et l'élimination presque totale des faux positifs. Ensuite, sa vitesse sur CPU simple, avec une taille de fichier de seulement 50 Ko pour 0,42 ms d'inférence, ce qui évite les goulots d'étranglement sur la sonde. Enfin, son interprétabilité, car les poids d'attention calculés en direct permettent aux analystes du SOC de comprendre précisément quelles caractéristiques réseau ont déclenché l'alerte."*
*   **Cues visuels :** Pointez les 3 cartes (Sensibilité, Vitesse CPU, Interprétabilité).
*   **Transition :** *"Détaillons l'architecture mathématique interne de ce réseau."*

#### Slide 18 : Architecture Interne de l'Attention MLP (40s)
*   **Speech :**
    > *"L'entrée brute composée des 77 caractéristiques est injectée dans deux branches. La branche du haut calcule un vecteur de poids d'attention alpha compris entre 0 et 1 via des fonctions linéaires et un Softmax. Nous effectuons ensuite un produit de Hadamard, c'est-à-dire une multiplication terme à terme entre l'entrée brute et ces poids. Ce filtrage dynamique élimine les variables redondantes. Le vecteur filtré passe ensuite dans le classificateur MLP composé de couches denses de 128 et 64 neurones, avec Dropout et BatchNorm, pour produire nos 15 logits de classification en 0,42 ms."*
*   **Cues visuels :** Suivez pas à pas le flux sur le diagramme animé (Entrée -> Branche Attention -> Multiplicateur Hadamard -> Classificateur MLP -> Classification).
*   **Transition :** *"Ce modèle étant finalisé, voyons comment il s'intègre dans notre infrastructure de production."*

---

### ⏱️ Partie 3 : Déploiement Cloud & SOC (Slides 19 à 21) - Cible : 3 min

#### Slide 19 : Architecture Globale du CyberRange Cloud (45s)
*   **Speech :**
    > *"Notre infrastructure est déployée sur AWS. Une machine d'attaque Kali Linux cible nos serveurs web, base de données et FTP situés dans un subnet public. Le trafic de ces cibles est dupliqué de façon transparente via du Traffic Mirroring AWS vers notre instance sonde IDS-Node. Cette sonde utilise NFStream pour extraire les métadonnées et fait tourner notre modèle d'IA pour classifier les flux en moins de 5 ms. Les alertes sont envoyées de manière asynchrone à une file SQS, déclenchant une fonction AWS Lambda qui écrit les alertes dans DynamoDB. Enfin, le serveur SOC-Server pousse ces alertes en temps réel via WebSockets vers le tableau de bord des analystes."*
*   **Cues visuels :** Pointez la zone d'attaque (gauche), puis le VPC AWS (centre), les subnets (Public, IDS Probe, Supervision), et le pipeline serverless (SQS, Lambda, DynamoDB à droite).
*   **Transition :** *"Pour déployer et piloter cette infrastructure, nous avons utilisé des outils modernes."*

#### Slide 20 : Technologies & Outils par Niveau (20s)
*   **Speech :**
    > *"Pour garantir la reproductibilité, l'infrastructure est provisionnée avec Terraform. La configuration des sondes est automatisée avec Ansible. Les microservices sont conteneurisés sous Docker et le cœur de détection IA est développé en Python avec la bibliothèque PyTorch."*
*   **Cues visuels :** Pointez les 4 sections d'outils (Provisioning, Configuration, Dev & CI/CD, Deep Learning).
*   **Transition :** *"Voici une démonstration concrète de l'interface SOC lors d'une attaque en temps réel."*

#### Slide 21 : Dashboard du SOC & Démonstration Vidéo (2 min 30s total : 30s Intro + 2 min Vidéo)
*   **Speech (Intro - 30s) :**
    > *"Notre tableau de bord de supervision SOC en React comporte quatre onglets : un aperçu général, un flux d'alertes temps réel, des graphiques statistiques et un onglet d'enrichissement affichant les tags des instances AWS compromises. Je vous propose de lancer notre vidéo de simulation de 2 minutes pour observer le comportement du système lors d'une attaque."*
*   **Action :** Déclenchez la vidéo. Laissez-la tourner durant ses 2 minutes. Vous pouvez faire des commentaires succincts sur les détections d'alertes instantanées qui s'affichent à l'écran.
*   **Transition :** *"Comme la démonstration le prouve, l'asynchronisme de l'architecture garantit une alerte en moins de 2 secondes. Analysons les résultats globaux de ces attaques."*

---

### ⏱️ Partie 4 : Validation & Perspectives (Slides 22 à 24) - Cible : 3 min

#### Slide 22 : Validation Expérimentale & Attaques (45s)
*   **Speech :**
    > *"La validation a consisté à injecter de réelles attaques réseau (SYN Flood DDoS, PortScan lents, et inondations ICMP) tout en maintenant un trafic sain intensif en arrière-plan. Les résultats sont excellents : nous enregistrons 100 % de détection sur les attaques volumétriques et de reconnaissance, une latence globale d'alerte inférieure à 2 secondes de bout-en-bout, et surtout, un impact CPU de 0,00 % sur les machines cibles de production grâce au Traffic Mirroring passif."*
*   **Cues visuels :** Soulignez le bloc gauche (Attaques Simulées) puis les 3 métriques clés à droite (100% Vrais Positifs, Latence < 2s, Impact CPU de 0,00%).
*   **Transition :** *"Ces validations confirment la réussite de notre projet et ouvrent de nouvelles perspectives."*

#### Slide 23 : Conclusion & Perspectives (45s)
*   **Speech :**
    > *"En conclusion, ce projet PFE a concrétisé la transition d'un modèle d'IA théorique vers une architecture de surveillance passive résiliente et opérationnelle sur AWS. Le modèle Attention MLP s'est avéré idéal grâce à sa compacité (50 Ko) et sa rapidité (0,42 ms). En perspectives, nous souhaitons intégrer un pipeline MLOps pour réentraîner le modèle face aux dérives de trafic, intégrer des méthodes d'IA explicable comme SHAP pour détailler les alertes, et mettre en place une réponse active (SOAR) via la modification automatique des Security Groups AWS."*
*   **Cues visuels :** Pointez la carte gauche (Bilan) puis la carte droite (Perspectives).
*   **Transition :** *"J'arrive au terme de mon exposé."*

#### Slide 24 : Merci pour votre attention (30s)
*   **Speech :**
    > *"Je tiens à remercier les équipes de 3D Smart Factory pour leur encadrement, ainsi que l'école HESTIM. Je vous remercie pour votre attention et je suis ravi d'ouvrir la discussion et de répondre à toutes vos questions."*
*   **Cues visuels :** Regardez les membres du jury, souriez poliment et attendez les questions.
