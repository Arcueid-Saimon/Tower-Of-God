
image w1 = "Elena_tease.png"
image bg demon = "demon.jpg"
init -1:
    python hide:s
        config.developer = True
        config.window_title = "Tower of God"
init 0:
    define A = Character("Alice",color="#c8ffc8")
    define m = Character("Moi",color="#c8ffc8")
    define n = Character("Narrateur",color="#c8c8ff")
    image bg auberge = im.Scale("120609.jpg",1280,720)
    image bg chemin = im.Scale("130517.jpg",1280,720)
    
label start:
    scene bg auberge
    show w1 at left
    
    A "Ah, je vois que tu es enfin réveillé !"
    A "Tu m'as surpris à parler dans ton sommeil."
    A "Il m'a semblé t'entendre mentionner une tour."
    A "Justement, il y en a une dans les environs."
    A "Mais surtout ne t'avise pas d'y mettre les pieds."
    A "Personne n'en est jamais ressorti vivant."
    
    hide w1
    n "Intrigué par cette tour, vous partez à l'Aventure !"
    
    scene bg chemin
    n "Vous atteignez la tour et décidez d'entrer pour tenter votre chance."
    n "La porte s'ouvre dans un long grincement puis vous y pénétrez."
    n "Aussitôt entré, aussitôt enfermé, la porte venait de se bloquer derrière vous."
    n "Il ne vous reste donc plus qu'un seul moyen de sortir d'ici, avancer !"
       
    return

label demon:
    scene bg demon
    
    "Tu oses troubler mon repos !"
    return