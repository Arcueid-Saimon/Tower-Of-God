
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
    
    define p = Character(" Pharaon ", color="#c8c8ff")
    define r = Character(" Reine",color="#c8c8ff")
    image phar = im.FactorScale("Characters/nefren-ka.png ",2,2)
    image darkphar = im.FactorScale("Characters/nefren-ka2.png ",2,2)
    image queen = im.FactorScale("Characters/nitocris.png ",2,2)
    image darkqueen = im.FactorScale("Characters/nitocris2.png ",2,2)
    
    image bg mort = im.Scale("BG/FIRE.jpg",1280,720)
    image bg crypte = im.Scale("BG/blood_pond.jpg",1280,720)
    image bg tunnel = im.Scale("BG/100420.jpg",1280,720)
    image levia = im.Scale("Mobs/leviathan.png",541,382)
    image behem = im.Scale("Mobs/behemoth.png",541,382)
    image bg city = im.Scale("BG/watery_graveyard.jpg",1280,720)
    image bg blood = im.Scale("BG/blood_marsh.jpg",1280,720)

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

    vpunch = Move((0,10), (0, -10), .10, bounce=True, repeat=True, delay=1.0)
    hpunch = Move((15,10), (15, 10), .10, bounce=True, repeat=True, delay=.275)
    import store.mystore as mystore

    
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)
        
        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.
        
        @parm {int} max_particles:
            The maximum number of particles at once in the screen.
            
        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1
            
        @parm {float} wind:
            The max wind force that'll be applyed to the particles.
            
        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.
            
        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """            
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles
            
            # the particle's speed
            self.speed = speed
            
            # the wind's speed
            self.wind = wind
            
            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder
            
            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depth = kwargs.get("depth", 10)
            
            # initialize the images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for the particle
                depth = random.randint(1, self.depth)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.            
            """
            rv = [ ]
            
            # generate the array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            # the horizontal/vertical positions of this particle            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # verify if the particle went out of the screen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None
                
            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image
    
    
init 1: 
    image snow = Snow("Sprites/bulletLa002.png")
    image satan = Snow("Sprites/bulletBb002.png")
            
    
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
        behem_fuit = False
        behem_mort = False
        levia_rencontrer = False
        behem_rencontrer = False
    play music "sounds/007.(未知Artist) - 青年の気ままな日常.mp3" fadeout 2.0
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
    A "C'est la légendaire Tour de Dieu."
    A "L'un des seuls et derniers contacts que les humains peuvent avoir avec les Dieux et les Démons."
    hide w2
    show w3 at left
    A "Mais surtout ne t'avise pas d'y mettre les pieds..."
    A "De terribles choses s'y sont produites et personnes n'en est jamais ressorti vivant."
    A "Ah, Des clients ! Il faut que j'y aille !"
    A "Si tu as des questions, vas les poser au commandant du Bataillon d'Exploration, il est assez reconnaissable, à son armure !"
    hide w3
    n "Vous avancez, et rejoignez un groupe de personnes armées, parmi elle, un homme se démarque du lot."
    v "... Euh excusez moi ?"
    show m1 at left
    v "Etes vous Erwin? Le commandant du Bataillon d'Exploration?"
    g "Hein ? Oui, qu'y a-t-il ?"
    v "Pourriez-vous me donner quelques informations sur la Tour de Dieu ?"
    g "Ah ! Tu es un aventurier, n'est ce pas?"
    g "Mon dieu ! Pourquoi êtes-vous tous aussi suicidaires ? Cette tour est dangereuse, le savez-vous au moins ?"
    v "Oui, je le sais mais une force inconnue m'attire dans cette tour."
    g "Si tu venais à t'approcher de la tour dans les environs, il faut en effet te donner certains renseignements et conseils."
    
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
    g "A cela se rajoute la légende De Kratos, cet ancien héros qui, par avidité s'est rangé du côté des ténèbres."
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
    g "Ici, nous sommes trop superstitieux pour s'approcher de nouveau de la tour."
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
        scene bg chemin
        n "Après vous être renseigné auprès du garde, vous partez à l'Aventure !"
    else:
        g "Très bien, je comprends que tu ne veuilles pas écouter ce que j'ai à te dire."
        g "Reviens ici après avoir triomphé de la tour, j'ai confiance en toi !"
        g "Et, bonne chance !"
        hide m2
        n "Vous entamez ainsi votre Aventure !"
        
    
label foret:
    scene bg foret1
    show snow
    play sound "sounds/heavyrainthunder.mp3"
    play music "sounds/021.(未知Artist) - 揺らめく禁忌.mp3" fadein 2.0
    v "Wah.... Quelle forêt, le mouvement des arbres et les rayons du soleil à travers les feuilles."
    v "Quels sont ces lumières? ça ne ressemble pas à de la pluie ni à ne la neige..."
    v" Non, c'est quelque chose de bien plus étrange que ça..."
    v "Je ne saurais dire pourquoi, mais je ressent de la nostalgie et de la tristesse devant cette scène..."
    v "Ah... non, je ne dois pas rester trop longtemps ici, il me faut aller à la tour."
    
    scene bg foret2
    
    
    
    
    
    scene bg chemin
    stop music
    stop sound
    play music "sounds/14 - Tonariawase no Jihen.mp3" fadeout 2.0
    n "Vous atteignez la tour et décidez d'entrer pour tenter votre chance."
    play sound "sounds/door.mp3" fadeout 2.0
    n "La porte s'ouvre dans un long grincement puis vous y pénétrez."
    n "Aussitôt entré, aussitôt enfermé, la porte se referme sur vous."
    n "Il ne vous reste donc plus qu'un seul moyen de sortir d'ici, avancer vers l'inconnu !"
    stop sound
    jump entree

label entree:
    show bg city
    n "Ainsi vous commencez votre exploration."
    n "Vous entendez du bruit dans le bâtiment central."
    n "Vous vous approchez donc pour découvrir ce qui fait un bruit pareil."
    
    jump rencontre_levia
    
    
label rencontre_levia:
    stop music fadeout 1.0
    play music "sounds/08.Kratos.mp3" fadeout 3.0
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
    if fuir > 6:
        "Vous obtenez [fuir] au lancer de dé."
        "Vous ne parvenez pas à vous enfuir..."
        jump combat
    else:
        play sound"sounds/running.mp3"
        "Vous obtenez [fuir] au lancer de dé"
        "Vous donc parvenez à vous enfuir !"
        stop sound
        if not levia_rencontrer:
            if not levia_fuit:
                $ levia_fuit = True
                $ levia_rencontrer = True
                jump suite_levia
        if not behem_rencontrer:
            if not behem_fuit:
                $ behem_fuit = True
                $ behem_rencontrer = True
                jump suite_behem

label combat:
    python:
        player_damage = mystore.lancer_de(2)
        enemy_damage = mystore.lancer_de(2)
        player_health = max(player_health - enemy_damage, 0)
        enemy_health = max(enemy_health - player_damage, 0)
    play sound"sounds/sword.mp3"
    "Vous infligez [player_damage] dégats à l'ennemi. Il lui reste [enemy_health]/[max_enemy_health] points de vie." with vpunch
    "L'ennemi vous a infligé [enemy_damage] dégats. Il vous reste [player_health]/[max_player_health] points de vie." with vpunch
    
    if player_health>0 and enemy_health>0:
            jump combat
    else:
        if enemy_health == 0:
            "Vous avez triomphé de l'ennemi !"
            $enemy_health = max_enemy_health
            if not levia_rencontrer:
                if not levia_mort:
                    $ levia_mort = True
                    $ levia_rencontrer = True
                    jump suite_levia
            if not behem_rencontrer:
                if not behem_mort:
                    $ behem_mort = True
                    $ behem_rencontrer = True
                    jump suite_behem
        else:
            "L'ennemi était trop fort pour vous !"
            $ mort_par_monstre = True
            jump mort
            
label suite_levia:
    stop music
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
    n "Vous atterissez sans problème mais déboussolé."
    n "Vous découvrez les terres marécageuses qui se profilent devant vous."
    n "Il n'y plus de choix, vous devez avancer, l'odeur nauséabonde vous monte au nez."
    n "Cependant au moment où vous commencez votre marche , vous entendez d'étranges bruits,"
    n "Ressemblant à des pas d'animaux, mais énormes..."
    jump rencontre_behem
    
    
label rencontre_behem:
    show behem at truecenter
    n "C'était bien un monstre, un éléphant Géant, un Béhemoth, une créature sensée avoir disparu en même temps que les dragons..."
    n "Que faites vous?"
    
    menu:
        "Combattre le Béhemoth":
            jump combat
            
        "Tenter de fuir":
            jump fuite
    
    return

label suite_behem:
    hide behem
    show bg tunnel
    n "Vous avez réussi à vous enfuir."
    
    return
    
label maudit:
    show phar at left
    play music"sounds/25 - Dread.mp3" fadeout 2.0
    p " Qui ose troubler mon sommeil ?! "
    p " Cela faisait bien 3 millénaires que je dormais."
    p " J'espère que tu as une bonne raison pour me réveiller !!! "
    v " Je fouillais cette crypte quand j'ai ouvert ce tom... "
    p " Quoi ?! Ma divine reine a disparu ! "
    p " Comment est-ce possible ? "
    p " Je... Je suis confus... "
    p " Pourrais-tu te rendre utile ? "
    p " Sache que je te récompenserais en cas de réussite. "
    p " Si tu venais à croiser ma reine, envoie la ici je t'en serais reconnaissant, tu veux bien ? "
    menu :
        " Accepter sa requête " :
            jump ray

        " Rejeter sa requête ":
            jump tp
    
label ray:
    p " Tu as bien fait d'accepter, je n'aurais pas supporté de refus. "
    n " Vous ne cherchez pas à savoir ce qui aurait pu vous arriver en refusant sa généreuse proposition de retrouver sa reine. "
    n " Vous empruntez donc les escaliers pour continuer votre périple. "
    
    return
    
label tp :
    hide phar
    show darkphar at left
    p " Comment ! Tu t'opposes à ma volonté ? " with vpunch
    p " Grossière erreur que tu viens de commettre. "
    p " Fatale dans ton cas, malheureusement  pour toi. "
    show darkqueen at right
    r " Je n'en serais pas si sûre ! "
    p " Ma reine, vous...vous aviez disparu. "
    r " Il n'y a pas de vous qui tienne. "
    r " Personne ne me dicte ma conduite."
    p " Il en va de soit. "
    r " Il en va aussi de soit que cet aventurier imprudent va disparaître de cette tour. "
    hide darkqueen
    hide darkphar
    show phar at left
    show queen at right
    p " Bien sûr ! Et toi tu ne... "
    n " La salle se met à tourbillonner, le sol disparaît, vous perdez l'équilibre, puis tout devient sombre. " with vpunch
    hide phar
    hide queen
    scene bg foret1
    with dissolve
    show snow
    n " Il semblerait que vous ayez été expulsé de la Tour de Dieu."
    n " Vous tentez de reprendre le chemin en direction de la Tour mais une force invisible vous empêche d'avancer. "
    n " Vous vous résolvez à rebrousser chemin. "
    n " Vous rentrez bredouille au village, sain et sauf mais avec la cruelle impression d'avoir manqué quelque chose dans la Tour. "
    n " Ainsi se termine votre aventure, et un pan de votre histoire. "
    
    return


label mort:
    play music "sounds/10.Standing the Pain.mp3" fadeout 3.0
    scene bg mort
    show satan
    if mort_par_monstre:
        "Vous avez succombé à vos blessures..."
        "Les monstres de la tour sont sortis, et ont tout ravagé sur leur passage..."
        "C'est la fin des temps de paix... Et le début de l'ère des démons et de la mort..."
    else:
        "L'aventure s'arrête ici pour vous ..."
        "Les monstres de la tour sont sortis, et ont tout ravagé sur leur passage..."
        "C'est la fin des temps de paix... Et le début de l'ère des démons et de la mort..."
    stop music
    
    return