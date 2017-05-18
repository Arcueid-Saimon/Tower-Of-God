
image w1 = "healer_shysmile.png"
image w2 = "healer_neutralclosed.png"
image w3 = "healer_neutral.png"
image vous = "militia_neutral.png"
image crea1 = "lucifer.png"

init -1:
    python hide:
        config.developer = True
        config.window_title = "Tower of God"
init 0:
    define A = Character("Alice",color="#c8ffc8")
    define v = Character("Vous",color="#c8ffc8")
    define n = Character("Narrateur",color="#c8c8ff")
    define g = Character("Chef de la Garde",color="#c8c8ff")
    image bg noir = im.Scale("fond_noir.jpg",1280,720)
    image bg auberge = im.Scale("120609.jpg",1280,720)
    image bg chemin = im.Scale("130517.jpg",1280,720)
    image m1 = im.Scale("marquis_concerned.png",375,650)
    image m2 = im.Scale("marquis_smile.png",375,650)
    image m3 = im.Scale("marquis_defensefierce.png",375,650)
    image bg mort = im.Scale("mort_v1.jpg",1280,720)
    
init python in mystore:
    import random

    def lancer_de(lancers):
        global valeur_totale
        d6_roll = 0
        valeur_totale = 0
        i = 1
        for i in range(lancers):
            d6_roll = renpy.random.randint(1,6)
            valeur_totale = valeur_totale + d6_roll
        
        return valeur_totale
        
init python:
    import store.mystore as mystore
            
    
label start:
    python:
        renseignements = False
        mort_par_monstre = False
        player_health = 50
        enemy_health = 20
        max_player_health = 50
        max_enemy_health = 20
    play music "sounds/Black Desert Online Glish.mp3"
    scene bg noir
    v "..."
    v "...Oh..."
    v "... Où...Où suis je?"
      
    scene bg auberge
    show w1 at left
    A "Ah, je vois que tu es enfin réveillé !"
    A "Tu m'as surpris à parler dans ton sommeil."
    hide w1
    show w2 at left
    A "Il m'a semblé t'entendre mentionner une tour."
    A "Justement, il y en a une dans les environs."
    hide w2
    show w3 at left
    A "Mais surtout ne t'avise pas d'y mettre les pieds."
    
    A "Personne n'en est jamais ressorti vivant."
    
    hide w3
    show m1 at left
    g "Hé, là toi !!"
    g "Viens par ici ! Tu es un aventurier à ce que je vois."
    g "Si tu venais à t'approcher de la tour dans les environs, je voudrais d'abord te donner certains renseignements et conseils."
    
    menu:
        "Accepter la proposition du chef de la garde":
            jump garde
            
        "Partir sans entendre ce que le chef de la garde a à vous dire":
            jump depart

label garde:
    $ renseignements = True
    hide m1
    show m2 at left
    
    menu:
        "L'interroger sur les origines de la tour":
            jump origines
        
        "L'interroger sur la dangerosité de la tour":
            jump dangers
        
        "L'interroger sur le bestiaire de la tour":
            jump bestiaire

label origines:
    g "Les anciens du villages racontent que la tour étaient déjà sur pied quand ils ont construits les premières maisons du village."
    g "Certains soutiennent que la tour fut batie par les elfes lorsqu'ils étaient encore la race dominante de ce monde,"
    hide m2
    show m1 at left
    g " D'autres diront que les sciences occultes sont rassemblées dans cette tour mais nul ne sait réellement comment et par qui elle fut construite"
    hide m1
    show m2 at left
    
    menu:
        "Lui demander d'autres informations":
            jump garde
        
        "Le remercier pour ses renseignements et s'en aller vers la tour":
            jump depart
    
label dangers:
    g "Des villageois ont rapporté à la garde avoir entendus des cris atroces provenant de la tour, ainsi que de nombreux bruits inhabituels."
    hide m2
    show m1 at left
    g "Malheureuseument, personne n'est en état de corroborer ces faits..."
    g "Ah ! Je ne devrais pas te parler de ça, je vais te faire fuir."
    hide m1
    show m2 at left
    
    menu:
        "Chercher à en savoir plus":
            jump disparus
        
        "Lui demander d'autres informations":
            jump garde
        
        "Le remercier pour ses renseignements et s'en aller vers la tour":
            jump depart
        
label bestiaire:
    g "Des ombres difformes ont été vues près de la tour et depuis personne au village n'ose s'y aventurer."
    g "Ici, nous sommes trop superstitieux pour s'apporcher de nouveau de la tour."
    hide m2
    show m1 at left
    g "C'est pourquoi seuls de rares aventuriers s'approchent de la tour."
    g "Toutefois, quelqu'un a déjà rapporté avoir aperçu un dragon,"
    hide m1
    show m2 at left
    g "Mais tout le monde sait que les dragons ont disparus de la surface du monde depuis longtemps !"
    
    menu:
        "Lui demander d'autres informations":
            jump garde
        
        "Le remercier pour ses renseignements et s'en aller vers la tour":
            jump depart

label disparus:
    hide m2
    show m3 at left
    g "Je me sens coupable d'avoir envoyé tout ces aventuriers avant toi dans cette tour."
    g " Vois-tu, aucun d'eux n'est ressorti, du moins vivant..."
    g "Es-tu vraiment prêt à affronter ce que renferme cette tour ?"
    hide m3
    show vous at right
    v "Déterminé !"
    hide you
    show m2 at left
    g "Soit, je te laisserai y aller dans ce cas là."
    
    menu:
        "Lui demander d'autres informations":
            jump garde
        
        "Le remercier pour ses renseignements et s'en aller vers la tour":
            jump depart

label depart:
    if renseignements:
        g "Reviens ici après avoir triomphé de la tour, j'ai confiance en toi !"
        g "Et, bonne chance !"
        hide m2
        scene bg chemin
        n "Après vous être renseigné auprès du garde, vous partez à l'Aventure !"
    else:
        g "Très bien, je comprends que tu ne veuilles pas écouter ce que j'ai à te dire."
        g "Reviens ici après avoir triomphé de la tour, j'ai confiance en toi !"
        g "Et, bonne chance !"
        hide m2
        scene bg chemin
        n "Vous entamez ainsi votre Aventure !"
    
    n "Vous atteignez la tour et décidez d'entrer pour tenter votre chance."
    n "La porte s'ouvre dans un long grincement puis vous y pénétrez."
    n "Aussitôt entré, aussitôt enfermé, la porte se referme sur vous."
    n "Il ne vous reste donc plus qu'un seul moyen de sortir d'ici, avancer vers l'inconnu !"
    
    jump combat
    
label combat: # ceci est un test qui marche avec des trucs à régler dessus quand meme
    show crea1 at topleft
    python:
        player_damage = mystore.lancer_de(2)
        enemy_damage = mystore.lancer_de(2)
        player_health = max(player_health - enemy_damage, 0)
        enemy_health = max(enemy_health - player_damage, 0)
    "Vous infligez [player_damage] dégats à l'ennemi. Il lui reste [enemy_health]/[max_enemy_health] points de vie."
    "L'ennemi vous a infligé [enemy_damage] dégats. Il vous reste [player_health]/[max_player_health] points de vie."
    
    if player_health>0 and enemy_health>0:
        jump combat
        
    else:
        if enemy_health == 0:
            "Vous avez triomphé de l'ennemi !"
            
            return
        else:
            "L'ennemi était trop fort pour vous !"
            $ mort_par_monstre = True
            jump mort
            
label mort:
    scene bg mort
    if mort_par_monstre:
        "Vous avez succombé à vos blessures..."
    else:
        "L'aventure s'arrête ici pour vous ..."
        
    return