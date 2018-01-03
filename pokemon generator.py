import pygame,random,time
pygame.init()
black=(0,0,0)
white=(255,255,255)
dw=400
dh=400
screen=pygame.display.set_mode([400,400])
pygame.display.set_caption("Random Pokemon Generator")
clock=pygame.time.Clock()
class spritesheet:
    def __init__(self,file,col,row):
        self.image=pygame.image.load(file)
        self.rect=self.image.get_rect()
        self.col=col
        self.row=row
        self.tot=col*row
        w=self.w=int(self.rect.width/col)
        h=self.h=int(self.rect.height/row)
        self.cells=list([i%col*w,int(i/col)*h,w,h] for i in range(self.tot))
        self.handle=list([(0,0),(-w,0),(int(-w/2),int(-h/2))])
    def draw(self,surface,ci,x,y,handle=0):
        surface.blit(self.image,(x+self.handle[2][0],y+self.handle[2][1]),self.cells[ci])
def message(msg,x,y):
    font=pygame.font.SysFont("comicsansms",20,bold=1)
    txt=font.render(msg,True,black)
    txtrect=txt.get_rect()
    txtrect.x=x
    txtrect.y=y
    screen.blit(txt,txtrect)
s=spritesheet("pokemon.png",16,10)
img=["bulbasaur","ivysaur","venusaur","charmander","charmeleon","charizard","squirtle","wartortle","blastoise",
         "caterpie","metapod","butterfree","weedle","kakuna","beedrill","pidgey","pidgeotto","pidgeot","rattata","raticate",
         "spearow","fearow","ekans","arbok","pikachu","raichu","sanshrew","sanslash","nidoranf","nidorina","nidoqueen","nidoranm",
         "nidorino","nidoking","clefairy","cleffable","vulpix","ninetales","jigglypuff","wigglytuff","zubat","golbat",
         "oddish","gloom","vileplume","paras","parasect","venonat","venomoth","diglet","dugtrio","meowth",
         "persian","psyduck","goldduck","mankey","primeape","growlithe","arcanine","poliwag","poliwhirl",
         "poliwrath","abra","kadabra","alekazam","machop","machoke","machamp","bellsprout","wepinbell",
         "victrebell","tentacool","tentacruel","geodude","graveller","golem","ponyta","rapidash","slowpoke",
         "slowbro",",magnemite","magneton","farfetch'd","doduo","dodrio","seel","dewgong","grimer","muk",
         "shelder","cloyster","gastly","haunter","gengar","onix","drowzee","hypno","crabby","kingler","voltorb",
         "electrode","exeggcute","exeggcutor","cubone","marowak","hitmonlee","hitmonchan","lickitung","koffing",
         "weezing","rhyhorn","rhydon","chansey","tangela","kangaskhan","horsea","seadra","goldeen","seaking",
         "staryu","starmie","mr.mime","scyther","jynx","electabuzz","magmar","pinsir","tauros","magikarp",
         "gyarados","lapras","ditto","Eevee","vaporeon","jolteon","flareon","porygon","omanyte","omastar",
         "kabuto","kabutops","aerodactyl","snorlax","articuno","zapdos","moltres","dratini","dragonair","dragonite",
         "mewtwo","mew"]

a=random.choice(img)
index=img.index(a)
while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                a=random.choice(img)
                index=img.index(a)
    screen.fill(white)        
    s.draw(screen,index%s.tot,dw/2,dh/2,0)
    message(img[index],160,50)
    pygame.display.flip()        
