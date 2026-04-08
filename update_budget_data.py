import re
import json

budgetData = {
    "ailette": {
        "id": "ailette",
        "name": "Lac d'Ailette",
        "totalTTC": 263754.27,
        "totalHT": 219931.06,
        "honorairesHT": 23564.04,
        "categories": {
            "hebergement": 91421.28,
            "reunions": 25855.52,
            "restauration": 36341.79,
            "gestion": 30528.24,
            "accompagnement": 12220.18
        },
        "details": {
            "hebergement": [
                {"desc": "Forfait séminaire résidentiel du 13/10 au matin au 14/10", "price": 70808.09, "subDesc": "315 pax\n1 personne par chambre avec salle de bain individuelle\nInclus : petit-déjeuner, déjeuner, dîner, deux pauses café par jour, salle de réunion plénière avec accès wifi premium, mise à disposition d'un vélo, accès Aqua Mundo"},
                {"desc": "Taxes de séjour", "price": 727.65, "subDesc": "315 pax"},
                {"desc": "Forfait journée d'étude Journée du 14/10", "price": 19885.54, "subDesc": "315 pax\nInclus : déjeuner, deux pauses café par jour, salle de réunion plénière avec accès wifi premium"}
            ],
            "reunions": [
                {"desc": "Salle plénière - inclus", "price": 0.00, "subDesc": "Salle plénière équipée 13/10 - 14/10 (1 écran, 1 paperboard, wifi inclus) - 519 m2"},
                {"desc": "Salle plénière - équipement technique et audiovisuel", "price": 12730.52, "subDesc": "Dispositif audiovisuel complet comprenant : sonorisation professionnelle, éclairage scénique, et dispositif vidéo. Le tout complété par une structure scénique, piloté par une équipe technique dédiée."},
                {"desc": "Privatisation du Centre de convention", "price": 13125.00, "subDesc": "Privatisation du centre de convention 13/10 - 14/10\nInclus : Bar à activités loisirs en libre service, Conciergerie"}
            ],
            "restauration": [
                {"desc": "Pause permanente - boissons chaudes", "price": 1504.91, "subDesc": "315 pax"},
                {"desc": "Déjeuner 13/10 - Cocktail gourmand supplément", "price": 3102.75, "subDesc": "125 pax"},
                {"desc": "Apéritif Dîner 13/10", "price": 3859.85, "subDesc": "315 pax\n1 coupe de Champagne Vranken + 2 pièces cocktail par personne"},
                {"desc": "Dîner 13/10 - supplément Menu Gala", "price": 7818.93, "subDesc": "315 pax\nDîner menu 3 plats, boissons incluses (1/3 vin, eaux minérales, café et thé)"},
                {"desc": "Forfait boissons fin de soirée", "price": 8129.84, "subDesc": "315 pax\nServi pendant 2h (Bière Heineken, vin, alcools forts, soft à discrétion)"},
                {"desc": "Animation soirée J1 Time to quizz", "price": 5239.50, "subDesc": "Plongez vos invités dans une expérience Bingo géant en fil rouge avec notre animateur"},
                {"desc": "Cadeau pour l'équipe gagnante", "price": 100.00, "subDesc": "A définir ensemble"},
                {"desc": "Option 2 Animation soirée Blind test live", "price": 6898.50, "subDesc": "Jeu en équipe et en musique live version groupe. Trophée des vainqueurs offert.\nApplication de réponse par smartphone", "isOption": True},
                {"desc": "Soirée 13/10 - DJ", "price": 1137.50, "subDesc": "Forfait 2h30 (22h30 - 1h00)"},
                {"desc": "Soirée 13/10 - Agents de sécurité", "price": 785.93, "subDesc": "Obligatoire - 1 agent/100 pax. 6h par agent"},
                {"desc": "Déjeuner 14/10 - supplément buffet Finger Food", "price": 1802.59, "subDesc": "Eaux, cafés inclus"},
                {"desc": "Photobooth", "price": 1260.00, "subDesc": "Sur deux jours"},
                {"desc": "Boîte à question - Matériel", "price": 400.00, "subDesc": "Micro type Sennheiser, Paravent Carton, Table haute, Chaise haute, Ordinateur"},
                {"desc": "Boîte à question - Ingénieur son", "price": 1200.00, "subDesc": "1 jour préparation, 1 jour montage"}
            ],
            "gestion": [
                {"desc": "Impression Badges", "price": 1134.00, "subDesc": "315 badges personnalisés Eco-responsable premium"},
                {"desc": "Option 2 Badges", "price": 1323.60, "subDesc": "315 badges personnalisés Eco-responsable premium (Attache cordon)", "isOption": True},
                {"desc": "Photographe", "price": 2300.00, "subDesc": "Camille Hénin Photographie. Le 13 et 14 octobre 2026"},
                {"desc": "Hotesses", "price": 3559.80, "subDesc": "Jour 1: hôtesses d'orientation, émargement, soirée. Jour 2: hôtesses. Inclus frais déplacement et repas"},
                {"desc": "Transfert A-R Roissy", "price": 2788.50, "subDesc": "3 forfaits (Transfert de 48 à 59 places)"},
                {"desc": "Transfert A-R Orly", "price": 3514.50, "subDesc": "3 forfaits (Transfert de 48 à 59 places)"},
                {"desc": "Transfert A-R Gare de Laon et Reims", "price": 4675.00, "subDesc": "5 forfaits (Transfert de 48 à 59 places)"},
                {"desc": "Création fil rouge", "price": 1200.00, "subDesc": "Concept de l'événement, fil rouge autour de l’expérience"},
                {"desc": "Déclinaison kakémono", "price": 90.00},
                {"desc": "Impression Kakémono", "price": 300.00, "subDesc": "2 forfaits"},
                {"desc": "Création invitation", "price": 600.00, "subDesc": "Proposition de 3 pistes graphiques"},
                {"desc": "Création d'invitation digitale", "price": 90.00},
                {"desc": "Déclinaison photocall", "price": 90.00},
                {"desc": "Photocall", "price": 436.80, "subDesc": "Mur 3x3 métres"},
                {"desc": "Déclinaison support digital", "price": 90.00},
                {"desc": "Déclinaison sur badge", "price": 90.00},
                {"desc": "Gestion de l'application", "price": 1800.00, "subDesc": "TEMPS HOMME: Gestion app mobile, inscriptions, relations partenaires"},
                {"desc": "Conception webapp", "price": 1200.00, "subDesc": "Création d'une web app pour jouer au challenge du village partenaire"},
                {"desc": "Masque PPT 10 slides", "price": 1000.00, "subDesc": "Proposition de 3 pistes graphiques", "isOption": True},
                {"desc": "Bilan Carbone", "price": 3000.00, "isOption": True},
                {"desc": "Scénographie Plantes hautes", "price": 360.00, "isOption": True},
                {"desc": "Scénographie lettres", "price": 2172.00, "subDesc": "15 lettres de 50cm de large sur 70cm de haut"},
                {"desc": "Bracelets lumineux", "price": 1937.64},
                {"desc": "Speaker 1 : Cécile Monteil", "price": 7800.00, "subDesc": "Hors VHR", "isOption": True},
                {"desc": "Speaker 2 : Carlos Moreno", "price": 14400.00, "subDesc": "Hors VHR", "isOption": True},
                {"desc": "Speaker 3 : Julie Boureau", "price": 4800.00, "subDesc": "Hors VHR", "isOption": True},
                {"desc": "Don à l'association choisie", "price": 500.00, "subDesc": "A minimum 500€ à verser à une association"},
                {"desc": "Décoration", "price": 600.00, "subDesc": "100 Ballons fluo, 30 ballons confettis fluo, peinture corporelle, table nappe et boite à lettres"},
                {"desc": "Mosaïque Photo", "price": 1000.00, "subDesc": "Solution IA Weevup"}
            ],
            "accompagnement": [
                {"desc": "Forfait Weever", "price": 8000.00, "subDesc": "J-1: 5 weevers, J1: 5 weevers, J2: 5 weevers. 1 WEEVER OFFERT"},
                {"desc": "VHR - Hébergement", "price": 2424.18, "subDesc": "2 nuits x 5 weevers"},
                {"desc": "VHR - Transports", "price": 1296.00, "subDesc": "5 weevers (camion weevup + voiture)"},
                {"desc": "VHR - Restauration", "price": 500.00, "subDesc": "20€ x 5 weevers x 4 repas"},
                {"desc": "Repérage avec 1 Weever", "price": 380.00, "subDesc": "Sur une base d'une demi-journée", "isOption": True}
            ]
        },
        "sideEvent": {
            "totalTTC": 60791.12,
            "totalHT": 50725.24,
            "honorairesHT": 5434.85,
            "categories": {
                "hebergement": 36709.20,
                "reunions": 1203.01,
                "restauration": 0.00,
                "gestion": 3312.00,
                "accompagnement": 4066.18
            },
            "details": {
                "hebergement": [
                    {"desc": "Forfait séminaire résidentiel du 14/10 au matin au 15/10", "price": 26249.85},
                    {"desc": "Taxes de séjour", "price": 346.50},
                    {"desc": "Forfait journée d'étude (15/10)", "price": 10112.85}
                ],
                "reunions": [
                    {"desc": "Salle plénière équipée 15/10", "price": 0.00},
                    {"desc": "Salles de sous-commission (3)", "price": 1203.01}
                ],
                "restauration": [
                    {"desc": "Dîner 14/10, Déjeuner 15/10, Pauses", "price": 0.00, "subDesc": "Inclus"}
                ],
                "gestion": [
                    {"desc": "Transfert > Roissy", "price": 1014.00},
                    {"desc": "Transfert > Orly", "price": 1278.00},
                    {"desc": "Transfert > Gare de Laon et Reims", "price": 1020.00}
                ],
                "accompagnement": [
                    {"desc": "Forfait Weever (J2, J3)", "price": 2700.00},
                    {"desc": "VHR - Hébergement", "price": 727.25},
                    {"desc": "VHR - Axes de séjour", "price": 6.93},
                    {"desc": "VHR - Transports", "price": 432.00},
                    {"desc": "VHR - Restauration", "price": 200.00}
                ]
            }
        }
    },
    "belambra": {
        "id": "belambra",
        "name": "Belambra Presqu'île",
        "totalTTC": 299666.73,
        "totalHT": 249809.63,
        "honorairesHT": 26765.32,
        "categories": {
            "hebergement": 69734.68,
            "reunions": 58274.14,
            "restauration": 58300.19,
            "gestion": 24978.54,
            "accompagnement": 11756.77
        },
        "details": {
            "hebergement": [
                {"desc": "Formule pension complète adulte base Double", "price": 3199.90, "subDesc": "20 pax"},
                {"desc": "Formule pension complète adulte base Single", "price": 66081.18, "subDesc": "295 pax"},
                {"desc": "Taxes de séjour", "price": 453.60, "subDesc": "315 pax"}
            ],
            "reunions": [
                {"desc": "Forfait Business Plus 13.10", "price": 19345.10, "subDesc": "1 salle, 2 pauses, 1 déjeuner. Salle Les 3 Fontaines (320m2)"},
                {"desc": "Salle Les 3 Fontaines - inclus 13.10", "price": 0.00},
                {"desc": "Salles catégorie D journée 13.10 (5 pièces)", "price": 2245.87},
                {"desc": "Salles catégorie C journée 13.10 (3 pièces)", "price": 1897.50},
                {"desc": "Privatisation du rooftop 13.10", "price": 6416.66},
                {"desc": "Salle Soirée de Gala 13.10", "price": 907.50},
                {"desc": "Salle Soirée de Gala - Agent de sécurité", "price": 715.00},
                {"desc": "Salle Les 3 Fontaines - inclus 14.10", "price": 0.00},
                {"desc": "Salles catégorie C journée 14.10 (1 pièce)", "price": 632.50},
                {"desc": "Salles catégorie D journée 14.10 (4 pièces)", "price": 1796.70},
                {"desc": "Privatisation Pinède - Village partenaire", "price": 4583.34},
                {"desc": "Chapiteau Pinède - Village partenaire", "price": 12987.98},
                {"desc": "Chapiteau Pinède - frais de transport", "price": 3880.80},
                {"desc": "Technique Chapiteau", "price": 1806.02},
                {"desc": "Technicien Son & Vidéo obligatoire", "price": 641.67},
                {"desc": "Salle plénière - Agent de sécurité", "price": 357.50},
                {"desc": "Frais de dossier Groupe", "price": 60.00}
            ],
            "restauration": [
                {"desc": "Déjeuner 13.10", "price": 6186.13, "subDesc": "Cocktail déjeunatoire - traiteur Cabiron (125 pax)"},
                {"desc": "Option - Forfait Vin Déjeuner 13.10", "price": 1552.32, "isOption": True},
                {"desc": "Apéritif 13.10", "price": 4331.25, "subDesc": "Apéritif bière et vin + planches au bar (1h)"},
                {"desc": "Dîner 13.10", "price": 10332.63, "subDesc": "Supplément repas \"Signature\" + nappes/serviettes tissus. Dîner menu 3 plats"},
                {"desc": "Forfait boissons fin de soirée", "price": 9816.35, "subDesc": "Open bar soirée sans champagne (22h-1h)"},
                {"desc": "Animation soirée J1 Time to quizz", "price": 5239.50, "subDesc": "Blind test live jeu en équipe et en musique live version groupe (4 musiciens)"},
                {"desc": "Cadeau pour l'équipe gagnante", "price": 100.00},
                {"desc": "Option 2 Animation soirée Blind test", "price": 6930.00, "subDesc": "Blind test live jeu en équipe et en musique live", "isOption": True},
                {"desc": "DJ soirée 13.10", "price": 1466.66, "subDesc": "Soirée dansante avec DJ (22h - 1h)"},
                {"desc": "Déjeuner 14.10", "price": 17307.68, "subDesc": "Cocktail déjeunatoire street food - traiteur Cabiron (315 pax)"},
                {"desc": "Option - Forfait Vin Déjeuner 14.10", "price": 1552.32, "isOption": True},
                {"desc": "Photobooth", "price": 1920.00, "subDesc": "Sur deux jours (2 forfaits)"},
                {"desc": "Boîte à question - Matériel", "price": 400.00},
                {"desc": "Boîte à question - Ingénieur son", "price": 1200.00}
            ],
            "gestion": [
                {"desc": "Impression Badges", "price": 1134.00, "subDesc": "315 badges personnalisés"},
                {"desc": "Option 2 Badges", "price": 1323.60, "isOption": True},
                {"desc": "Photographe", "price": 2520.00, "subDesc": "Studio Cécile Aubry"},
                {"desc": "Hotesses", "price": 3669.60},
                {"desc": "Transfert A-R Aéroport Montpellier", "price": 1699.50},
                {"desc": "Transfert A-R Gare Montpellier St Roch", "price": 1699.50},
                {"desc": "Transfert A-R Gare Montpellier Sud de France", "price": 1699.50},
                {"desc": "Création fil rouge", "price": 1200.00},
                {"desc": "Déclinaison kakémono", "price": 90.00},
                {"desc": "Impression Kakémono", "price": 300.00},
                {"desc": "Création d'invitation", "price": 600.00},
                {"desc": "Déclinaison d'invitation digitale", "price": 90.00},
                {"desc": "Déclinaison photocall", "price": 90.00},
                {"desc": "Photocall", "price": 436.80, "subDesc": "Mur 3x3 mètres"},
                {"desc": "Déclinaison support digital", "price": 90.00},
                {"desc": "Déclinaison sur badge", "price": 90.00},
                {"desc": "Application", "price": 1800.00},
                {"desc": "Conception webapp", "price": 1200.00},
                {"desc": "Masque PPT 10 slides", "price": 1000.00, "isOption": True},
                {"desc": "Bilan Carbone", "price": 3000.00, "isOption": True},
                {"desc": "Scénographie Plantes hautes", "price": 360.00},
                {"desc": "Scénographie lettres", "price": 2172.00},
                {"desc": "Bracelets lumineux", "price": 1937.64},
                {"desc": "Speaker 1 : Cécile Monteil", "price": 7800.00, "isOption": True},
                {"desc": "Speaker 2 : Carlos Moreno", "price": 14400.00, "isOption": True},
                {"desc": "Speaker 3 : Julie Bourreau", "price": 4800.00, "isOption": True},
                {"desc": "Dons à l'association choisie", "price": 500.00},
                {"desc": "Décoration", "price": 600.00},
                {"desc": "Mosaique photo", "price": 1000.00}
            ],
            "accompagnement": [
                {"desc": "Forfait Weever", "price": 8500.00},
                {"desc": "VHR - Hébergement", "price": 1382.37},
                {"desc": "VHR - Taxes de séjour", "price": 14.40},
                {"desc": "VHR - Transports", "price": 1360.00},
                {"desc": "VHR - Restauration", "price": 500.00},
                {"desc": "Repérage avec 1 Weever", "price": 750.00, "isOption": True}
            ]
        },
        "sideEvent": {
            "totalTTC": 63831.98,
            "totalHT": 53234.44,
            "honorairesHT": 5703.69,
            "categories": {
                "hebergement": 40114.65,
                "reunions": 2397.09,
                "restauration": 0.00,
                "gestion": 1699.50,
                "accompagnement": 3319.51
            },
            "details": {
                "hebergement": [
                    {"desc": "Formule pension complète (150 pax)", "price": 39898.65},
                    {"desc": "Taxes de séjour", "price": 216.00}
                ],
                "reunions": [
                    {"desc": "Salle Les 3 Fontaines", "price": 0.00},
                    {"desc": "Salles catégorie C (3)", "price": 1897.50},
                    {"desc": "Technicien Son & Vidéo obligatoire", "price": 320.84},
                    {"desc": "Salle plénière - Agent de sécurité", "price": 178.75}
                ],
                "restauration": [
                    {"desc": "Dîner, Déjeuner, Pause café", "price": 0.00, "subDesc": "Inclus"}
                ],
                "gestion": [
                    {"desc": "Transfert A-R Aéroport Marseille", "price": 566.50},
                    {"desc": "Transfert A-R Avignon TGV", "price": 566.50},
                    {"desc": "Transfert A-R Gare Marseille St Charles", "price": 566.50}
                ],
                "accompagnement": [
                    {"desc": "Forfait Weever (J2, J3)", "price": 1800.00},
                    {"desc": "VHR - Hébergement", "price": 435.19},
                    {"desc": "VHR - Taxes de séjour", "price": 4.32},
                    {"desc": "VHR - Transports", "price": 960.00},
                    {"desc": "VHR - Restauration", "price": 120.00}
                ]
            }
        }
    },
    "pontroyal": {
        "id": "pontroyal",
        "name": "Village Pont Royal",
        "totalTTC": 289621.45,
        "totalHT": 241351.21,
        "honorairesHT": 25859.06,
        "categories": {
            "hebergement": 70779.45,
            "reunions": 49132.92,
            "restauration": 55930.52,
            "gestion": 27743.17,
            "accompagnement": 11906.08
        },
        "details": {
            "hebergement": [
                {"desc": "Forfait Séminaire 1/2 Pension Déjeuner (Single)", "price": 48367.94, "subDesc": "270 pax"},
                {"desc": "Forfait Séminaire 1/2 Pension Déjeuner (Co-single)", "price": 1447.74, "subDesc": "10 pax"},
                {"desc": "Hébergements: 35 appartements (Maeva)", "price": 16232.48, "subDesc": "35 pax"},
                {"desc": "Prestations hébergement (lits, linge, ménage)", "price": 4016.25},
                {"desc": "Taxe de séjour", "price": 715.05, "subDesc": "315 pax"}
            ],
            "reunions": [
                {"desc": "Forfait Journée d'étude", "price": 19467.95, "subDesc": "315 pax"},
                {"desc": "Espace Médicis - Salle plénière", "price": 0.00},
                {"desc": "Espace Médicis - 2 sous-commission le 13/10", "price": 0.00},
                {"desc": "Espace Médicis - Locations sous-com (diverses tailles)", "price": 2006.24},
                {"desc": "Espace Médicis - Forfait prestation technique", "price": 5462.35},
                {"desc": "Espace Médicis - Système de lumière", "price": 858.60, "isOption": True},
                {"desc": "Espace Médicis - Repas techniciens", "price": 124.51},
                {"desc": "Haut du Village - Locations sous-com", "price": 1738.76},
                {"desc": "Haut du Village - Forfait prestation technique Salle Artémisia", "price": 1364.25},
                {"desc": "Haut du Village - Repas technicien", "price": 31.13},
                {"desc": "Chapiteau avec plancher et éclairage", "price": 9947.45},
                {"desc": "25 stands", "price": 1054.49},
                {"desc": "Frais de transport", "price": 7490.00}
            ],
            "restauration": [
                {"desc": "Pauses café", "price": 446.80, "subDesc": "Pour participants Maeva (autres inclus)"},
                {"desc": "Déjeuners & Petit-déjeuners", "price": 1769.80, "subDesc": "Pour participants Maeva (autres inclus)"},
                {"desc": "Cocktail déjeunatoire 13/10 et 14/10", "price": 9452.52},
                {"desc": "Délocalisation restauration sous chapiteau 13/10 et 14/10", "price": 2889.82, "isOption": True},
                {"desc": "Mobilier Guinguette", "price": 1732.50},
                {"desc": "Dîner 13/10 - Dîner Gamme Bistro", "price": 21916.13},
                {"desc": "Dîner 13/10 - Supplément Fromages", "price": 2425.50, "isOption": True},
                {"desc": "Dîner 13/10 - Forfait vin", "price": 1143.45},
                {"desc": "Dîner 13/10 - Apéritif", "price": 3811.50, "isOption": True},
                {"desc": "Dîner 13/10 - Apéritif champagne", "price": 1836.45, "isOption": True},
                {"desc": "Dîner 13/10 - boisson après le repas (soft)", "price": 2875.95},
                {"desc": "Dîner 13/10 - boisson après repas (alcool)", "price": 1074.15},
                {"desc": "Dîner 13/10 - bouteille supplémentaire / fût", "price": 159.26, "isOption": True},
                {"desc": "Dîner 13/10 - Droit de bouchon", "price": 0.00},
                {"desc": "Dîner 13/10 - Forfait transformation", "price": 3208.34},
                {"desc": "Dîner 13/10 - Supplément horaire", "price": 71.50, "isOption": True},
                {"desc": "Dîner 13/10 - Animation DJ", "price": 1485.00},
                {"desc": "Dîner 13/10 - Repas DJ", "price": 32.00},
                {"desc": "Dîner 13/10 - Animation soirée 1 Bingo", "price": 5489.00},
                {"desc": "Dîner 13/10 - Animation soirée 2 Blindtest", "price": 6028.00, "isOption": True},
                {"desc": "Cadeau pour l'équipe gagnante", "price": 100.00},
                {"desc": "Photobooth", "price": 1760.00},
                {"desc": "Boîte à question (matériel + ingé son)", "price": 2000.00}
            ],
            "gestion": [
                {"desc": "Badges", "price": 1181.25},
                {"desc": "Option 2 Badges", "price": 1378.75, "isOption": True},
                {"desc": "Photographe", "price": 2200.00},
                {"desc": "Hôtesses", "price": 3300.00},
                {"desc": "Transfert A-R Aéroport Marseille", "price": 2575.80},
                {"desc": "Transfert A-R Avignon TGV", "price": 2251.80},
                {"desc": "Transfert A-R Gare Marseille St Charles", "price": 2754.00},
                {"desc": "Agent de securité", "price": 996.68},
                {"desc": "Création fil rouge", "price": 1200.00},
                {"desc": "Kakémono (création + impression)", "price": 390.00},
                {"desc": "Création invitation & digitale", "price": 690.00},
                {"desc": "Photocall (déclinaison + mur)", "price": 454.00},
                {"desc": "Déclinaison support digital & badge", "price": 180.00},
                {"desc": "Application & Webapp", "price": 3000.00},
                {"desc": "Masque PPT 10 slides", "price": 1000.00, "isOption": True},
                {"desc": "Bilan Carbone", "price": 3000.00, "isOption": True},
                {"desc": "Scénographie plantes & lettres", "price": 2532.00},
                {"desc": "Bracelets lumineux", "price": 1937.64},
                {"desc": "Speakers (Monteil, Moreno, Bourreau)", "price": 27000.00, "isOption": True},
                {"desc": "Dons à l'association choisie", "price": 500.00},
                {"desc": "Décoration", "price": 600.00},
                {"desc": "Mosaique photo", "price": 1000.00}
            ],
            "accompagnement": [
                {"desc": "Forfait Weever", "price": 8500.00},
                {"desc": "VHR - Hébergement", "price": 1669.08},
                {"desc": "VHR - Train", "price": 325.00},
                {"desc": "VHR - Camion 7m3", "price": 912.00},
                {"desc": "VHR - Restauration", "price": 500.00},
                {"desc": "Repérage avec 1 Weever", "price": 750.00, "isOption": True}
            ]
        },
        "sideEvent": {
            "totalTTC": 58239.00,
            "totalHT": 48532.50,
            "honorairesHT": 5199.91,
            "categories": {
                "hebergement": 34114.26,
                "reunions": 3441.43,
                "restauration": 0.00,
                "gestion": 2574.00,
                "accompagnement": 3202.90
            },
            "details": {
                "hebergement": [
                    {"desc": "Forfait Séminaire Pension complète (150 pax)", "price": 33773.76},
                    {"desc": "Taxe de séjour", "price": 340.50}
                ],
                "reunions": [
                    {"desc": "Espace Médicis - Salle plénière", "price": 0.00},
                    {"desc": "Espace Médicis - Location salles sous commission", "price": 1980.00},
                    {"desc": "Espace Médicis - Forfait prestation technique", "price": 1398.60},
                    {"desc": "Espace Médicis - Repas techniciens", "price": 62.83}
                ],
                "restauration": [
                    {"desc": "Dîner, Déjeuner, Pauses", "price": 0.00, "subDesc": "Inclus"}
                ],
                "gestion": [
                    {"desc": "Transfert A-R Aéroport Marseille", "price": 874.50},
                    {"desc": "Transfert A-R Avignon TGV", "price": 764.50},
                    {"desc": "Transfert A-R Gare Marseille St Charles", "price": 935.00}
                ],
                "accompagnement": [
                    {"desc": "Forfait Weever", "price": 1800.00},
                    {"desc": "VHR - Hébergement", "price": 370.90},
                    {"desc": "VHR - Transport", "price": 912.00},
                    {"desc": "VHR - Restauration", "price": 120.00}
                ]
            }
        }
    }
}

# The category mapping keys are:
categoryLabels = {
    "hebergement": "Hébergement",
    "reunions": "Réunions",
    "restauration": "Restauration & Animation",
    "gestion": "Gestion des participants",
    "accompagnement": "Accompagnement (Weever)"
}

categoryColors = {
    "hebergement": "bg-blue-500",
    "reunions": "bg-purple-500",
    "restauration": "bg-orange-500",
    "gestion": "bg-amber-500",
    "accompagnement": "bg-teal-500"
}

with open("index.html", "r") as f:
    index_html = f.read()

with open("print.html", "r") as f:
    print_html = f.read()

def replace_const(content, const_name, new_value):
    # Matches `const XYZ = { ... };` or similar
    pattern = re.compile(rf'(const\s+{const_name}\s*=\s*)(.*?)(;(?=\s*(?:const|function|\/\/|\/\*)))', re.DOTALL)
    # The regex needs to be more robust for `budgetData` as it's a huge block.
    # Let's find start and find the next 'const ' or 'function'
    pattern = re.compile(rf'(const\s+{const_name}\s*=\s*\{{.*?\}})(?=\s*;\s*const|\s*;\s*\/\/)', re.DOTALL)
    return content

# Better way: Search for `const budgetData = ` and replace everything up to `const categoryLabels = `
def replace_data(html_content):
    start_str = "const budgetData ="
    end_str = "const categoryLabels ="
    
    start_idx = html_content.find(start_str)
    end_idx = html_content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_json = json.dumps(budgetData, indent=4)
        # Javascript boolean requires lowercase true/false, json.dumps does this
        replacement = f"const budgetData = {new_json};\n\n        "
        html_content = html_content[:start_idx] + replacement + html_content[end_idx:]
        
    # Replace categoryLabels
    start_str = "const categoryLabels ="
    end_str = "const categoryColors ="
    start_idx = html_content.find(start_str)
    end_idx = html_content.find(end_str)
    if start_idx != -1 and end_idx != -1:
        new_json = json.dumps(categoryLabels, indent=4)
        replacement = f"const categoryLabels = {new_json};\n\n        "
        html_content = html_content[:start_idx] + replacement + html_content[end_idx:]
        
    # Replace categoryColors
    start_str = "const categoryColors ="
    end_str = "const textColors ="
    start_idx = html_content.find(start_str)
    end_idx = html_content.find(end_str)
    if start_idx != -1 and end_idx != -1:
        new_json = json.dumps(categoryColors, indent=4)
        replacement = f"const categoryColors = {new_json};\n\n        "
        html_content = html_content[:start_idx] + replacement + html_content[end_idx:]
        
    return html_content

# Update React components to render the item conditionally with Option styling
# And render Side Event data

def update_components(html_content):
    # 1. Update the option styling
    # In VenueDetailView, replace:
    # <span className="text-gray-800 font-medium">{item.desc}</span>
    # with
    # <span className={`font-medium ${item.isOption ? 'text-amber-600' : 'text-gray-800'}`}>{item.desc} {item.isOption && <span className="text-xs bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full ml-2 uppercase font-bold tracking-wider">Option</span>}</span>
    
    old_span = '<span className="text-gray-800 font-medium">{item.desc}</span>'
    new_span = '{/* Options in different color */}\n                                                            <span className={`font-medium flex items-center gap-2 ${item.isOption ? "text-amber-600" : "text-gray-800"}`}>\n                                                                {item.desc}\n                                                                {item.isOption && <span className="text-[10px] bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full uppercase font-bold tracking-wider relative top-px">Option</span>}\n                                                            </span>'
    html_content = html_content.replace(old_span, new_span)

    # 2. Add sideEvent rendering in VenueDetailView
    # Find the end of VenueDetailView return block:
    #     </div>
    # </div>
    # );
    
    side_event_block = """
                        </div>
                    </div>
                    {/* --- SIDE EVENT --- */}
                    {venue.sideEvent && (
                        <div className="mt-12">
                            <div className="flex items-center gap-4 mb-6">
                                <h3 className="text-xl font-bold text-gray-900">Side Event (14/10 - 15/10)</h3>
                                <div className="h-px bg-gray-200 flex-1"></div>
                            </div>
                            
                            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
                                <div>
                                    <h4 className="text-lg font-semibold text-gray-900">Budget Side Event</h4>
                                    <p className="text-gray-500">Estimatif pour l'événement secondaire</p>
                                </div>
                                <div className="text-right bg-emerald-50 p-4 rounded-lg border border-emerald-100">
                                    <p className="text-sm font-medium text-emerald-600 uppercase tracking-wider mb-1">Total TTC</p>
                                    <p className="text-3xl font-bold text-emerald-900">{formatEur(venue.sideEvent.totalTTC)}</p>
                                    <p className="text-xs text-emerald-500 mt-1">Total HT: {formatEur(venue.sideEvent.totalHT)}</p>
                                </div>
                            </div>

                            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                                <div className="lg:col-span-2 space-y-4">
                                    {Object.entries(venue.sideEvent.categories).filter(([k,v])=>v>0 || (venue.sideEvent.details[k] && venue.sideEvent.details[k].length>0)).map(([catKey, catValue]) => {
                                        const subHT = venue.sideEvent.totalHT - venue.sideEvent.honorairesHT;
                                        const percentage = ((catValue / subHT) * 100).toFixed(1);
                                        return (
                                            <div key={`side-${catKey}`} className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 flex flex-col gap-4">
                                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                                    <div className="flex items-center gap-3">
                                                        <div className={`min-w-[3.5rem] px-2 h-10 rounded-lg flex items-center justify-center text-white ${categoryColors[catKey] || 'bg-gray-500'}`}>
                                                            <span className="font-bold text-sm">{isNaN(percentage) ? '0.0' : percentage}%</span>
                                                        </div>
                                                        <div>
                                                            <h4 className="font-semibold text-gray-900">{categoryLabels[catKey] || catKey}</h4>
                                                        </div>
                                                    </div>
                                                    <div className="text-right">
                                                        <p className="text-lg font-bold text-gray-900">{formatEur(catValue)}</p>
                                                        <p className="text-xs text-gray-500">HT</p>
                                                    </div>
                                                </div>
                                                {venue.sideEvent.details && venue.sideEvent.details[catKey] && (
                                                    <div className="mt-2 pt-4 border-t border-gray-100 space-y-3">
                                                        {venue.sideEvent.details[catKey].map((item, idx) => (
                                                            <div key={`side-${idx}`} className="flex flex-col text-sm border-b border-gray-50 pb-2 last:border-0 last:pb-0">
                                                                <div className="flex justify-between items-start gap-4">
                                                                    <span className={`font-medium flex items-center gap-2 ${item.isOption ? "text-amber-600" : "text-gray-800"}`}>
                                                                        {item.desc}
                                                                        {item.isOption && <span className="text-[10px] bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full uppercase font-bold tracking-wider relative top-px">Option</span>}
                                                                    </span>
                                                                    <span className="text-gray-900 font-bold whitespace-nowrap">{formatEur(item.price)}</span>
                                                                </div>
                                                                {item.subDesc && (
                                                                    <div className="text-gray-500 text-xs mt-1 italic leading-relaxed whitespace-pre-line pr-16">{item.subDesc}</div>
                                                                )}
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })}
                                    <div className="bg-gray-50 rounded-lg border border-gray-200 p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                        <div>
                                            <h4 className="font-semibold text-gray-900">Honoraires Weever (Side Event)</h4>
                                        </div>
                                        <div className="text-right">
                                            <p className="text-lg font-bold text-gray-900">{formatEur(venue.sideEvent.honorairesHT)}</p>
                                            <p className="text-xs text-gray-500">HT</p>
                                        </div>
                                    </div>
                                </div>
                                <div className="lg:col-span-1">
                                    {/* Additional info or blank space for side event side panel */}
                                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 sticky top-24">
                                        <h3 className="text-lg font-semibold text-gray-900 mb-4 border-b pb-2">Récapitulatif Financier Side Event</h3>
                                        <div className="space-y-3 text-sm">
                                            <div className="flex justify-between text-gray-600">
                                                <span>Sous-total HT</span>
                                                <span>{formatEur(venue.sideEvent.totalHT - venue.sideEvent.honorairesHT)}</span>
                                            </div>
                                            <div className="flex justify-between text-gray-600">
                                                <span>Honoraires HT</span>
                                                <span>{formatEur(venue.sideEvent.honorairesHT)}</span>
                                            </div>
                                            <div className="border-t pt-3 flex justify-between text-gray-500 text-sm">
                                                <span>Total HT</span>
                                                <span>{formatEur(venue.sideEvent.totalHT)}</span>
                                            </div>
                                            <div className="flex justify-between text-gray-500 text-sm mt-1">
                                                <span>TVA estimée</span>
                                                <span>{formatEur(venue.sideEvent.totalTTC - venue.sideEvent.totalHT)}</span>
                                            </div>
                                            <div className="border-t pt-3 mt-2 flex justify-between font-bold text-emerald-600 text-lg">
                                                <span>Total TTC</span>
                                                <span>{formatEur(venue.sideEvent.totalTTC)}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
"""
    
    # We replace the closing tags of the component
    old_end = """                        </div>

                    </div>
                </div>
            );"""
    
    new_end = side_event_block + "\n                </div>\n            );"
    
    html_content = html_content.replace(old_end, new_end)
    return html_content

index_html = replace_data(index_html)
index_html = update_components(index_html)

with open("index.html", "w") as f:
    f.write(index_html)

print_html = replace_data(print_html)
print_html = update_components(print_html)

with open("print.html", "w") as f:
    f.write(print_html)

print("Budget data properly updated!")
