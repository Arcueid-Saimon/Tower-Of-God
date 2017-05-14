image bg auberge = "120612.jpg"
image w1 = "Elena_tease.png"
image bg demon = "demon.jpg"
init -1:
    python hide:
        config.developer = True
        config.window_title = "Tower of God"
        
label start:
    scene bg auberge
    show w1 at left
    
    "Ah, je vois que tu es enfin réveillé !"
    "Tu m'as surpris à parler dans ton sommeil."
    "Il m'a semblé t'entendre mentionner une tour"
    "Justement, il y en a une dans les environs"
    "Mais surtout ne t'avise pas d'y mettre les pieds"
    "Personne n'en est jamais ressorti vivant"
    
    hide w1
    "Intrigué par cette tour vous décidez de partir à sa découverte à vos risques et périls"
    "Vous vous mettez en route de cette tour prestement."
    return

label demon:
    scene bg demon
    
    "Tu oses troubler mon repos !"
    return