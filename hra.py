#Proměny, seznamy a knihovny
import random
volba = ""
inventar = ["klíče", "zapalovač", "krabička s léky"]
Wanted_level_SB = 5
#zivoty 0-2
zivoty = 2

#Představení do příběhu
print("Jseš slavný proti vládní autor ve své zemi na přelomu poloviny století. Pro lidi sloužíš jako symbol protestu proti autoritativnímu režimu.") 
print("Už několik let tě pronásledují, ty si ji zatim byl schopný agentům Státní Bezpečnosti unikat. Teď se schovávaš v motelu Levah.")
print(f"U sebe máš {inventar}")

#Definice vybirani moznosti
def vyber_volby(text, moznosti):
    while True:
        try:
            volba = int(input(text + " "))
            if volba in moznosti:
                return volba
            print("Zadej jedno z čísel:", moznosti)
            False
        except ValueError:
            print("Zadej číslo.")

#Definice části hry v motelu
def Motel(Wanted_level_SB, zivoty, inventar):
    print("Je devátá večer, ty naopak od obvykle, kdy si povídáš se ostatními v motelu, sedíš ve svém pokoji. Zrovna děláš na svém dalším dílu které kritizuje současnou vládu")
    print('V tu skrze okno slyšíš bušení na dveře do lobby. "Státní Bezpečnost otevřete!!!" Slyšíš jak postupně postupují směrem k tvému pokoji. Co uděláš?')
    volba = vyber_volby("Zadej 1 jestli se rozhodneš: Utéct oknem. Zadej 2 jestli se rozhodneš: Schovat se ve skříni a situaci přečkat. Zadej 3 jestli se rozhodneš: Utéct hlavními dveřmi", [1, 2, 3])
    if volba == 1:
        strechy(Wanted_level_SB, zivoty, inventar)
        return
    elif volba == 2:
        print("Rychle jsi vlezl do skříně, ve skříni čekáš několik minut a nic. Do bytu ti vejde několik členů Státní Bezpečnosti, ze zdola slyšíš křik tvých přátel")
        volba = vyber_volby("Zadej 1 pokud se budeš dál ve skříni schovávat. Zadej 2 pokud ze skříně vyjdeš", [1, 2])
        if volba == 1:
            print("Držíš se dál ve skříní, přes malou škvíru pozoruješ jak členi státní bezpečnosti procházejí pokoj, už se blíží ke skříni.")
            print("V tu jim něco zazní do vysílačky a odejdou, ty chvíli ještě počkáš ve skříni a cítíš jak se zvyšuje teplo, opět se koukneš přes škvíru ve skříni a vidíš")
            print("jak celý pokoj hoří. Celou budovu podpálila Státní Bezpečnost. Zemřel jsi")
        elif volba == 2:
            print("Rozhodneš se vyjít ze skříně. Jak s Státní Bezpečnosti naložíš?")
            volba = vyber_volby("Zadej 1 pokud s němi rozhodneš bojovat. Zadej 2 pokud se pokusíš s němi komunikovat", [1, 2])
            if volba == 1:
                print("Rychle ze skříně vylezeš a na Státní Bezpečnost zaútočíš")
                print("Na to aby jsi vyhrál souboj, vypočítej příklad")
                cislo_x = random.randint(1, 10)
                cislo_y = random.randint(10,15)
                if int(input(f"Kolik je {cislo_x} * {cislo_y}")) == cislo_x * cislo_y:
                    print("Porazil jsi agenty Státní Bezpečnosti, co uděláš teď?")
                    Wanted_level_SB = Wanted_level_SB + 1
                    volba = vyber_volby("Zadej 1 pokud utečeš oknem. Zadej 2 pokud se pokusíš zachránit lidi zezdola", [1, 2])
                    if volba == 1:
                        print("Rychle běžíš k oknu a vylezeš ním ven")
                        strechy(Wanted_level_SB, zivoty, inventar)
                        return
                    if volba == 2:
                        print("Vyjdeš dveřmi směrem do dolního patra, v tu narazíš na plnou chodbu agentů Státní Bezpečnosti které přivolal hluk z boje.")
                        print("Státní Bezpečnost tě zatkla a převáží do jejich stanice.")
                        stanice(Wanted_level_SB, zivoty, inventar)
                        return
                else:
                    print("Agenti státní bezpečnosti tě porazili a zatkli. Ztratil jsi jeden život")
                    zivoty = zivoty - 1
                    print(f"Máš {zivoty} životy")
                    Wanted_level_SB = Wanted_level_SB + 1
                    if zivoty <= 0:
                        print("Zemřel jsi")
                        return
                    else:
                        print("Teď tě vezou na stanici.")
                        stanice(Wanted_level_SB, zivoty, inventar)
                        return
            elif volba == 2:
                print("Státní Bezpečnost tě nenechala mluvit, dala ti pěstí a zatkla tě. Teď tě odváží na stanici.")
                zivoty = zivoty - 1
                print(f"Ztratil jsi jeden život. Teď máš {zivoty} životy")
                stanice(Wanted_level_SB, zivoty, inventar)
                return
    elif volba == 3:
        print("Běžíš po schodech, zabočíš ke dveřím a najednou naproti tobě jde 10 agentů státní bezpečnosti, hned tě zatknou a odvezou na stanici")
        Wanted_level_SB = Wanted_level_SB - 1
        stanice(Wanted_level_SB, zivoty, inventar)

#Definice části hry na střechách
def strechy(Wanted_level_SB, zivoty, inventar):
    print("Oknem jsi se chytl okapu a vylezl nahoru na Střechy. Běžíš po nich dál až k velké mezeře mezi další ulicí. Tuto cestu ti plánoval kamarád a dal ti tam dlouhý kus prkna.")
    print("Na to aby jsi přešel ale potřebuješ hodně rovnováhy. Jiná cesta není tak se odhodláš a uděláš první krok")
    print("Aby jsi balancoval tak musíš opisovat vypsaná čísla.")
    print("První krok byl bez potíží, jdeš dál, druhý a třetí krok. Pak tě ale vítr sunul do prava")
    terminal = random.randint(300, 1500)
    print(terminal)
    balanc = int(input("Opiš z terminálu"))
    if balanc == terminal:
        print("Chytil jsi balanc a pokračuješ")
    else: 
        zivoty = zivoty - 1
        if zivoty <= 0:
            print("Došli ti životy, zemřel jsi.")
            return
        print("Uklouzl jsi, ztratil jsi život, něco ti vypadlo z kapsy, ale chytil jses")
        inventar.pop(random.randint(0, len(inventar) - 1))
    print("Pokračuješ dál, v tu ti uklouzla noha")
    terminal = random.randint(70000, 50000000)
    print(terminal)
    balanc = int(input("Opiš z terminálu"))
    if balanc == terminal:
        print("Chytil jsi balanc a pokračuješ")
    else:
        zivoty = zivoty - 1
        if zivoty <= 0:
            print("Došli ti životy, zemřel jsi.")
            return
        print("Uklouzl jsi, ztratil jsi život, něco ti vypadlo z kapsy, ale ještě máš energii a chytil jses. Pokračuješ dál.")
        inventar.pop(random.randint(0, len(inventar) - 1))
    print("Už jsi skoro u konce. Ze nadšení že jsi skoro tam jsi uklouznul.")
    terminal = random.randint(100000000000, 900000000000000000)
    print(terminal)
    balanc = int(input("Opiš z terminálu"))
    if balanc == terminal:
        print("Dokázal jsi se chytnout")
    else:
        zivoty = zivoty - 1
        if zivoty <= 0:
            print("Došli ti životy, zemřel jsi.")
            return
        print("Nechytil jsi se, něco ti vypadlo z kapsy, ale s energií co ti zbyla jsi naštěstí spadl na okap jenom o patro níž. Ztratil jsi ale život")
        inventar.pop(random.randint(0, len(inventar) - 1))
    print("Dolezl jsi na druhou stranu.")
    print("Jdeš dál a slezeš po žebříku až do kavárny tvojí blízké kamarádky")
    kavarna(Wanted_level_SB, zivoty, inventar)

#Definice části hry v kavárně
def kavarna(Wanted_level_SB, zivoty, inventar):
    print("Přišel jsi do kavárny kde jsi situaci vysvětlil své kamarádce. Ta tě ukryla do sklepa a předložila ti tvoje další možnosti.")
    print("'Buďto utečeš ze země, nebo se budeš muset dál ukrývat'")
    volba = vyber_volby("Zadej 1 pokud se rozhodneš utéct ze země, ale ztratíš možnost publikovat publiku tvé země. Zadej 2 pokud se budeš dál ukrývat, a bojovat za svobodu", [1, 2])
    if volba == 1:
        print("Sbalil jsis věci a hnedka další den jsi se vydal se skupinou politických imigrantů na cestu. Za týden jsi se dostal ke hranicím kde jsi počkal než se strážní měnili. Pak jsi vyklozl pryč")
        print("Konec hry")
        return
    elif volba == 2:
        print("'skvěle, připravim ti věci do sklepa.")
        print("Další týden se schováváš v kavárně a děláš na svém díle. Pak se tě tvá kamarádka na něco chce zeptat.")
        print("Informuje tě že se připravuje protest před budovou Státní Bezpečnosti, a vypadá to že jeho rozměry budou velké.")
        print("Kdyby se do ní zapojil někdo jako ty, tak by mohla mít rozměry ještě větší.")
        print("Tedy se tě ptá, jestli se zapojíš do organizace")
        volba = vyber_volby("Zadej 1 pokud to odsouhlasíš. Zadej 2 pokud ne", [1, 2])
        if volba == 1:
            print("Začneš vyvěšovat po městě plakáty a mluvit k lidem. Za týden se protest uskuteční, doufáš v to že jsi ho nějak posílil")
            print("Pak přijde den protestu")
            print("Jseš na cestě na protest ale v tu tě chytí záchvat")
            if "krabička s léky" in inventar:
                print("Naštěstí u sebe máš krabičku s léky a nic se ti nestane")
            else:
                print("Vyhmatáš si kapsy a dojde ti že jsi krabičku s léky ztratil. Ztratíš jeden život")
                zivoty = zivoty - 1
                if zivoty <= 0:
                    print("Zemřel jsi")
                    return
            protest()
        elif volba == 2:
            print("Odmítneš, tvá kamarádka se zeptá proč, odpovíš, že už nemáš energii dál bojovat")
            print("Uběhne několik týdnů potom co jsi to vzdal, ležíš v posteli vtom slyšíš stejnou větu jako v motelu.")
            print("Státní bezpečnost přiběhne a zatkne tě. Ty nevzdoruješ, už nemáš energii.")
            print("Pár dní tě drží v cele, ty jim neodpovídáš. Až tě pak dají na popravu.")
            print("Tvá poprava posílí protesty, Státní bezpečnost proti ním tvrdě zasáhne.")
            print("Konec hry")
            return

#Definice části hry v budově státní bezpečnosti
def stanice(Wanted_level_SB, zivoty, inventar):
    print("Státní bezpečnost tě odvezla do stanice. Budeš během výslechu spolupracovat?")
    volba = vyber_volby("Zadej 1 pokud spolupracovat budeš. 2 pokud ne.", [1, 2])
    if volba == 1:
        if Wanted_level_SB <= 5:
            print("Státní bezpečnost tě vyslechne. Ty spolupracuješ s tím že doufáš v to že tě pustí. Místo toho tě nadoživotí zavřou do vězení a jediné co ti přichází jsou zprávy o tom jak tvojí přátelé umírají.")
        elif Wanted_level_SB > 5:
            print("Státní bezpečnost tě vyshlechne. Ty spolupracuješ s tím že doufáš v to že tě pustí. Místo toho tě zavřou do vězení a za týden tě čeká veřejná poprava.")
            print("Den veřejné popravy přijde. Ty doufáš že tomu něco zabrání ale Státní Bezpečnost zveřejnila záznam z tvého výslechu. Všichni tvoji podpůrci jsou zklamáni a nikdo tě nepřijde zachránit.")
    elif volba == 2:
        if Wanted_level_SB <= 5:
            print("Statní Bezpečnost tě po neúspěšném výslechu odvede do cely. Za týden tě čeká veřejná poprava.")
            print("Když ale den veřejné popravy přijde tak se shromáždí davy lidí na tvojí podporu a bojují za tebe")
            print("Nějaký z protestujících tě vysvobodí a ukryje. Schováš se dál nebo pujdeš podpořit protest?")
            volba = vyber_volby("Zadej 1 pokud se budeš dál ukrývat. 2 pokud se do protestu zapojíš", [1, 2])
            if volba == 1:
                print("Protest se dál rozvíjí, ty se schováváš a pozoruješ ho z okna kam tě jeden z protestujících zavedl. Z protestu se stane revoluce.")
                print("Revoluce je úspěšná ale tebe si zapamatuje jako spouštěč a respektují tě za tvá díla. Však tě odsuzují za tvojí inaktivitu během revoluce.")
                return
            elif volba == 2:
                protest()
                return
        elif Wanted_level_SB > 5:
            print("Státní Bezpečnost tě na místě zmlátí. Ztratíš život.")
            if zivoty <= 0:
                print("Zemřel jsi")
                return
            print("Zavřou tě do vězení a za týden tě čeká veřejná poprava. Když ale den veřejné popravy přijde tak se shromáždí davy lidí na tvojí podporu a bojují za tebe")
            print("Nějaký z protestujících tě vysvobodí a ukryje. Schováš se dál nebo pujdeš podpořit protest?")
            volba = vyber_volby("Zadej 1 pokud se budeš dál ukrývat. 2 pokud se do protestu zapojíš", [1, 2])
            if volba == 1:
                print("Protest se dál rozvíjí, ty se schováváš a pozoruješ ho z okna kam tě jeden z protestujících zavedl. Z protestu se stane revoluce.")
                print("Revoluce je úspěšná ale tebe si zapamatuje jako spouštěč a respektují tě za tvá díla. Však tě odsuzují za tvojí inaktivitu během revoluce.")
                return
            elif volba == 2:
                protest()
                return
            
#Definice vypsání úspěšného protestu
def protest():
    print("Procházíš se protestem proti kterému Státní Bezpečnost tvrdě zasahuje. Lidé okolo tebe padají do bezvědomí nebo umírají na zranění od Státní Bezpečnosti.")
    print("Vedle tebe spadne protestující na zem zraněn od střely. Ránu m")
    print("Ty doběhneš k skupině lidí která má megafony a dáš proslov.")
    print("Tvůj proslov hne všemi protestujícími a dodá jim motivaci bojovat. Lidi z domů tvůj proslov slyší a jdou bojovat.")
    print("Spolu s protestujícími začnete revoluci. Ten stejný den obsadíte hlavní budovu Státní Bezpečnosti, a po dvou letech neustálých bojů vyhrajete.")
    print("Konec hry")
    return

#Spuštění hry
Motel(Wanted_level_SB, zivoty, inventar)
