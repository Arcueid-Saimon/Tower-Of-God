
image w1 = "Characters/healer_shysmile.png"
image w2 = "Characters/healer_neutralclosed.png"
image w3 = "Characters/healer_neutral.png"
image vous = "Characters/militia_neutral.png"
image crea1 = "Mobs/lucifer.png"

init -1:
    python hide:
        config.developer = True
        config.window_title = "Tower of God"
init 0:
    define A = Character("Alice",color="#c8ffc8")
    define v = Character("Vous",color="#c8ffc8")
    define n = Character("Narrateur",color="#c8c8ff")
    define g = Character("Chef de la Garde",color="#c8c8ff")
    image bg noir = im.Scale("BG/fond_noir.jpg",1280,720)
    image bg auberge = im.Scale("BG/120609.jpg",1280,720)
    image bg chemin = im.Scale("BG/130517.jpg",1280,720)
    image bg foret1 = im.Scale("BG/110618_.jpg",1280,720)
    image m1 = im.Scale("Characters/marquis_concerned.png",375,650)
    image m2 = im.Scale("Characters/marquis_smile.png",375,650)
    image m3 = im.Scale("Characters/marquis_defensefierce.png",375,650)
    image bg mort = im.Scale("BG/mort_v1.jpg",1280,720)
    image bg crypte = im.Scale("BG/blood_pond.jpg",1280,720)
    image levia = im.Scale("Mobs/leviathan.png",541,382)
    image bg city = im.Scale("BG/watery_graveyard.jpg",1280,720)
    image bg blood = im.Scale("BG/blood_marsh.jpg",1280,720)
    image satan = SnowBlossom("Sprites/bulletCa000.png",count = 10,border = 50,xspeed=(20, 10),yspeed=(100, 200),start=0,horizontal = False)
    
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
        player_health = 100
        enemy_health = 20
        max_player_health = 100
        max_enemy_health = 20
        fuite_faite = False
        levia_fuit = False
        levia_mort = False
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
    hide vous
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
        stop music
        scene bg chemin
        n "Après vous être renseigné auprès du garde, vous partez à l'Aventure !"
    else:
        g "Très bien, je comprends que tu ne veuilles pas écouter ce que j'ai à te dire."
        g "Reviens ici après avoir triomphé de la tour, j'ai confiance en toi !"
        g "Et, bonne chance !"
        hide m2
        scene bg chemin
        n "Vous entamez ainsi votre Aventure !"
        
    
label foret:
    
    
    
    
    
    
    n "Vous atteignez la tour et décidez d'entrer pour tenter votre chance."
    n "La porte s'ouvre dans un long grincement puis vous y pénétrez."
    n "Aussitôt entré, aussitôt enfermé, la porte se referme sur vous."
    n "Il ne vous reste donc plus qu'un seul moyen de sortir d'ici, avancer vers l'inconnu !"
    
    jump entree

label entree:
    show bg city
    n "Ainsi vous commencez votre exploration."
    n "Vous entendez du bruit dans le bâtiment central."
    n "Vous vous approchez donc pour découvrir ce qui fait un bruit pareil."
    
    jump rencontre_levia
    
    
label rencontre_levia:
    stop music
    play music "sounds/David Fenn Titans.mp3" loop
    show levia at truecenter
    n "Vous rencontrez une créature aux airs de serpent, vous vous approchez de lui avec méfiance."
    n "Que décidez-vous de faire?"
    
    menu:
        "Combattre ce léviathan":
            jump combat
        "Tenter de fuir":
            jump fuite
            
label fuite:
    $ fuir = mystore.lancer_de(1)
    if not fuite_faite:
        "Pour fuir, vous devrez obtenir moins de 3."
        $ fuite_faite = True
    if fuir >= 3:
        "Vous obtenez [fuir] au lancer de dé."
        "Vous ne parvenez pas à vous enfuir..."
        jump combat
    else:
        "Vous obtenez [fuir] au lancer de dé"
        "Vous donc parvenez à vous enfuir !"
        if not levia_fuit:
            $ levia_fuit = True
            jump suite_levia
    
label combat:
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
            $enemy_health = max_enemy_health
            if not levia_mort:
                $ levia_mort = True
                jump suite_levia
        else:
            "L'ennemi était trop fort pour vous !"
            $ mort_par_monstre = True
            jump mort
            
label suite_levia:
    show bg crypte
    hide levia
    if levia_mort:
        n "Après avoir occis ce monstrueux dragon, vous arrivez dans une crypte..."
    if levia_fuit:
        n "Après avoir échappé à ce monstrueux dragon en vous faufilant derrière lui, vous arrivez dans une crypte..."
    n "Vous remarquez un tombeau sur votre gauche et un bassin vraisemblalement rempli de sang en face de vous."
    n "Que décidez-vous de faire ?"
    
    menu:
        "S'approcher du bassin et l'observer":
            jump absorbe
            
        "Tenter d'ouvrir le tombeau":
            jump maudit
            
        "Emprunter les escaliers":
            jump ray
            
label absorbe:
    n "Vous vous approchez donc du bassin, vous penchez pour vérifier que le liquide rouge est bien du sang."
    n "Ainsi vous tombez à la renverse et êtes absorbé par le bassin..."
    show bg blood
    n " Vous atterissez sans problème mais déboussolé."
    n "Vous découvrez les terres marécageuses qui se profilent devant vous."
    
    return
    
label maudit:
    n "a faire"
    
    return
    
label ray:
    n "pareil"
    
    return
    
label mort:
    scene bg mort
    show satan
    if mort_par_monstre:
        "Vous avez succombé à vos blessures..."
    else:
        "L'aventure s'arrête ici pour vous ..."
        
    return