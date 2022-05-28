from datetime import datetime
from cgi import print_arguments
from email.mime import image
import linecache
from array import array
from asyncore import read
from curses.ascii import isdigit
from re import X
import sys, pygame ,math
from time import time
import datetime
from PIL import ImageGrab
pygame.init()
clock = pygame.time.Clock()
dt = clock.tick(60)
T0 = 0
screen = Width,Height = 1080,720
window = pygame.display.set_mode((Width,Height),pygame.NOFRAME)
BLACK = (18, 18, 18)
WHITE = '#F9F7F7'
RED = (252, 91, 122)
GREEN = (29, 161, 16)
BLUE = (78, 193, 246)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (90, 110, 183)
Gray = (112, 112, 112)
parameter = True
status = True
Error_check = False
mx = 100
my = 100
Header_font = pygame.font.SysFont("adobedevanagariregular", 21)
base_font = pygame.font.SysFont("adobedevanagariregular", 18)
parameter_font = pygame.font.SysFont("adobedevanagariregular", 16)
Exitprogram = pygame.image.load('Exitprogram.png')
Credit = pygame.image.load('info.png')
class Screen():
    def screen():
        window.fill(WHITE)
        Screen.graph()
        pygame.draw.line(window,Gray,(0,40),(Width,40))
        Text1 = base_font.render("Project simulation",True,Gray)
        Icon = pygame.image.load('UI.png')
        pygame.draw.line(window,Gray,(40+20,560),(60+20,560))
        pygame.draw.line(window,Gray,(40+20,600),(60+20,600))
        pygame.draw.line(window,Gray,(50+20,600),(50+20,560))
        Scale_unit = parameter_font.render(str(projectile1.graph_scale)+"m",True,Gray)
        window.blit(Exitprogram,(1050,8.5))
        window.blit(Icon,(10,7.5))
        window.blit(Credit,(1000,8.5))
        window.blit(Text1,((1080/2)-50,15))
        window.blit(Scale_unit,(60,535))
    def graph():
        for i in range(19): #default i = 23 , j = 14
            for j in range(14):
                pygame.draw.circle(window,Gray,[120+(i*40),(600-(40*j))],2,1)
    def resetcheck():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.draw.rect(window,BLACK,pygame.Rect((935,685),(75,20)),border_radius = 15).collidepoint(event.pos):
                resetdefault()
                projectile1.Error_check = False
                projectile1.imposiblecase = False
                window.fill(WHITE)
                Screen.screen()
            else:
                Textbox.checkreset = False
    #Check Input Value is float
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False  
    #Check start
    def startcheck():
        checktext_K = Screen.isfloat(K_textbox.newtext)
        checktext_theta = Screen.isfloat(theta_textbox.newtext)
        checktext_H = Screen.isfloat(H_textbox.newtext)
        checktext_N = Screen.isfloat(N_textbox.newtext)
        checkfinalx = Screen.isfloat(Xfinal_textbox.newtext)
        checkfianly = Screen.isfloat(Yfinal_textbox.newtext)
        checktext_M = Screen.isfloat(M_textbox.newtext)
        if Textbox.checkreset == True:
            resetdefault()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.draw.rect(window,BLACK,pygame.Rect((935,650),(75,20)),border_radius = 15).collidepoint(event.pos):
                if checktext_K == True and checktext_theta == True and checktext_H == True and checktext_N == True and checkfianly == True and checkfinalx == True and checktext_M == True and float(K_textbox.newtext) >= 0 and float(theta_textbox.newtext) >= 0 and float(H_textbox.newtext) >= 0 and float(N_textbox.newtext) >= 0 and float(Yfinal_textbox.newtext) >= 0 and float(Xfinal_textbox.newtext) >= 0 and float(M_textbox.newtext) >= 0 and float(Xfinal_textbox.newtext) != 0:
                    if float(K_textbox.newtext) == 0 or float(N_textbox.newtext) == 0 or float(Yfinal_textbox.newtext) < 0:
                        projectile1.Error_check = True
                    elif float(theta_textbox.newtext) > 89:
                        projectile1.imposiblecase = True
                    elif float(M_textbox.newtext) <= 0:
                        projectile1.Error_check = True
                    else:
                        T0 = time
                        projectile1.calulate()
                        projectile1.changescale()
                        window.fill(WHITE)
                        Screen.screen()
                else:
                    resetdefault()
                    window.fill(WHITE)
                    projectile1.Error_check = True
                    projectile1.projectilestart = False    
def parameterbox():
    pygame.draw.rect(window,AQUA, pygame.Rect(50,630,1080-50-50,600),border_radius = 15)
    pygame.draw.rect(window,Gray, pygame.Rect(50,630,1080-50-50,600),1,border_radius = 15)
def statusbox():
    pygame.draw.rect(window,AQUA, pygame.Rect(870,80,250,520),border_radius = 15)
    pygame.draw.rect(window,Gray, pygame.Rect(870,80,250,520),1,border_radius = 15)
scale = 200
time = 0.001

#Projectile
class projectile():
    imposiblecase = False
    Error_check = False
    resetvalue = False
    projectilestart = False
    newu = 0
    newt = 0
    newtheta = 0
    newv = 0
    newdeltax = 0
    graph_scale = 0.2
    def __init__(self,scale,time):
        self.scale = scale
        self.time = time
        self.h = 0
        self.thata = 0
        self.x = 0
        self.y = 0
        self.timestep = 0.001
        self.timestep = self.timestep + (self.timestep * (1/self.scale*2))*200
        self.time2 = 0
        self.save = False
        self.plus = True
    def changescale(self):
        self.scale = 200
        while self.x > 1/(self.scale/40)*18 or self.y+self.h > 1/(self.scale/40)*14:
            if self.x > 1/(self.scale/40)*18 or self.y+self.h > 1/(self.scale/40)*14:
                self.scale = self.scale / 2
                self.time = self.time * 1/self.scale
    def drawprojectileline(self):
        projectile1.graph_scale = 1/(self.scale/40)
        #set parameter
        X0 = 120
        Y0 = 600
        #draw shooter image
        #calculate X Y
        if projectile1.newt != self.time2:
            X = projectile1.newu*math.cos(math.radians(self.theta))*self.time2
            Y = projectile1.newu*math.sin(math.radians(self.theta))*self.time2-4.905*self.time2*self.time2
            if self.plus == True:    
                if Y0-Y*self.scale-self.h*self.scale < 600 and self.time2 <= projectile1.newt:
                    self.time2 += 0.025
                    if Y0-Y*self.scale-self.h*self.scale > 75:
                        pygame.draw.circle(window,AQUA,[X0+X*self.scale,Y0-Y*self.scale-self.h*self.scale],2)
        if round(self.time2,4) >= (round(projectile1.newt,4)):
            self.plus = False
            self.time2 = 0
            ct = datetime.datetime.now()
            ts = ct.timestamp()
            pygame.image.save(window,f"Save//"+str(ts)+".jpg")
    def draw(self):
        projectile1.graph_scale = 1/(self.scale/40)
        #set parameter
        X0 = 120
        Y0 = 600
        #draw shooter image
        shooter = pygame.image.load('catapult.png')
        pygame.draw.line(window,Gray,(40+20,560),(60+20,560))
        target = pygame.image.load('target.png')
        
        final_x = projectile1.newu*math.cos(math.radians(self.theta))*projectile1.newt
        final_y = projectile1.newu*math.sin(math.radians(self.theta))*projectile1.newt-4.905*projectile1.newt*projectile1.newt
        #calculate X Y
        if projectile1.newt != self.time:
            if projectile1.newt >= self.time:
                window.fill(WHITE)
                Screen.graph()
                Screen.screen()
                window.blit(shooter,(100,590-(self.h/(1/(self.scale/40)))*40))
            if self.time >= projectile1.newt:
                projectile1.drawprojectileline()
            X = projectile1.newu*math.cos(math.radians(self.theta))*self.time
            Y = projectile1.newu*math.sin(math.radians(self.theta))*self.time-4.905*self.time*self.time
            if Y0-Y*self.scale-self.h*self.scale < 600 and self.time <= projectile1.newt:
                self.time += self.timestep*2
                window.blit(target,[X0-13+final_x*self.scale,Y0-11.5-final_y*self.scale-self.h*self.scale])
                if Y0-Y*self.scale-self.h*self.scale > 75:
                    pygame.draw.circle(window,AQUA,[X0+X*self.scale,Y0-Y*self.scale-self.h*self.scale],5)

    def calulate(self):
        self.time2 = 0
        self.time = 0
        self.plus = True
        self.x = float(Xfinal_textbox.newtext)
        self.y = float(Yfinal_textbox.newtext)
        self.h = float(H_textbox.newtext)
        self.theta = float(theta_textbox.newtext)
        if (self.y-self.h)/self.x <= math.tan(math.radians(self.theta)):
            projectile1.projectilestart = True
            #input value
            k = float(K_textbox.newtext)
            n = float(N_textbox.newtext)
            m = float(M_textbox.newtext)
            sintheta = math.sin(math.radians(self.theta))
            costheta = math.cos(math.radians(self.theta))
            u = ((4.905 * (self.x ** 2) / ((self.x * sintheta * costheta) - ((self.y - self.h) * (costheta ** 2))))) ** 0.5
            projectile1.newu = u
            statustext.u = round(u,2)

            t = self.x / (u * costheta)
            projectile1.newt = t
            statustext.t = round(t,2)
            v = (((u * costheta) ** 2) + ((u * sintheta) - (9.81 * t)) ** 2) ** 0.5
            theta_v = math.degrees(math.atan(((u * sintheta) - (9.81 * t)) / (u * costheta)))
            projectile1.newv = v
            projectile1.newtheta = theta_v
            statustext.v = round(v,2)
            statustext.theta_v = round(theta_v,2)
            afordx = (n * k) / 2   # a for delta x
            bfordx = -(9.81 * m * sintheta)
            cfordx = -(0.5 * m * u * u)
            delta_x = (- bfordx + (((bfordx ** 2) - (4 * afordx * cfordx)) ** 0.5)) / (2 * afordx)
            projectile1.newdeltax = delta_x
            statustext.deltax = round(delta_x,2)
            projectile1.Error_check = False
            projectile1.imposiblecase = False
            Screen.screen()
        else:
            projectile1.projectilestart = False
            projectile1.imposiblecase = True
class Newbutton():
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#488FB1'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#533E85'
		#text
		self.text_surf = parameter_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(window,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(window,self.top_color, self.top_rect,border_radius = 12)
		window.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#4FD3C4'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#488FB1'
class checkbutton():
    def __init__(self,text,width,height,pos):
        self.text = parameter_font.render(text,True,WHITE)
        self.rect = pygame.Rect(pos,(width,height))
        self.textpos = self.textpos = self.text.get_rect(center = self.rect.center)
    def draw(self):
        pygame.draw.rect(window,WHITE,self.rect)
        window.blit(self.text,self.textpos)
class statustext():
    u = 0
    t = 0
    v = 0
    theta_v = 0
    deltax = 0
    intial_x = 0
    intial_y = 0
    final_x = 0
    final_y = 0
    def __init__(self,text,posx,posy,color):
        self.color = WHITE
        self.posx = posx
        self.posy = posy
        self.text = parameter_font.render(text,True,self.color)
    def draw(self):
        Time_icon = pygame.image.load('wall-clock.png')
        U_icon = pygame.image.load('U_speed.png')
        spring_icon = pygame.image.load('spring.png')
        V_icon = pygame.image.load('golf-ball.png')
        angle_icon = pygame.image.load('angle.png')
        status_u_text = parameter_font.render("Initial Velocity:",True,self.color)
        status_t_text = parameter_font.render("Total time:",True,self.color)
        status_v_text = parameter_font.render("Velocity:",True,self.color)
        status_theta_v_text = parameter_font.render("Theta Velocity:",True,self.color)
        status_deltax_text = parameter_font.render("Spring compression:",True,self.color)
        status_u = parameter_font.render(str(statustext.u)+" m/s",True,self.color)
        status_t = parameter_font.render(str(statustext.t)+" sec",True,self.color)
        status_v = parameter_font.render(str(statustext.v)+" m/s",True,self.color)
        status_theta_v = parameter_font.render(str(statustext.theta_v)+" degree",True,self.color)
        status_deltax = parameter_font.render(str(statustext.deltax)+" m",True,self.color)
        window.blit(U_icon,(960,150))
        window.blit(V_icon,(960,250))
        window.blit(angle_icon,(960,350))
        window.blit(Time_icon,(960,550))
        window.blit(spring_icon,(960,450))
        
        window.blit(status_u_text,(900-10,100))
        window.blit(status_v_text,(900-10,200))
        window.blit(status_theta_v_text,(900-10,300))
        window.blit(status_deltax_text,(900-10,400))
        window.blit(status_t_text,(900-10,500))
        window.blit(status_t,(1000-10,500))
        window.blit(status_u,(1000-10,100))
        window.blit(status_v,(1000-10,200))
        window.blit(status_theta_v,(1000-10,300))
        window.blit(status_deltax,(1000+20,400))

#Parameter
class parametertext():
    Equal = parameter_font.render("",True,Gray)
    def __init__(self,text,posx,posy,color):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.text = parameter_font.render(text,True,self.color)
    def draw(self):
        window.blit(parametertext.Equal,(120+160,self.posy))
        window.blit(self.text,(self.posx,self.posy))
#Erroralret
class ErrorTextbox():
    def __init__(self,posx,posy,color,font,witdh,height):
        self.pos = (posx,posy)
        self.color = color
        self.font = font
        self.rect = pygame.Rect((posx,posy),(witdh,height))
        self.upperrect = pygame.Rect((posx,posy),(witdh,height/4.5))
        self.text = parameter_font.render("invalid Input. Please complet all required fields",True,WHITE)
        self.text2 = parameter_font.render("Imposible case. Please change angle, position ",True,WHITE)
        self.text3 = parameter_font.render("and angle can't be more than 90",True,WHITE)
        self.text4 = parameter_font.render("value can't be zero or less than zero",True,WHITE)
        self.textpos = self.textpos = self.text.get_rect(center = self.rect.center)
        self.time = 0
    def draw(self):
        Error = pygame.image.load('warning.png')
        errorexit = pygame.image.load('shutdown.png')
        pygame.draw.rect(window,self.color,self.rect,border_radius = 15)
        pygame.draw.rect(window,WHITE,self.upperrect)
        pygame.draw.rect(window,Gray,self.rect,1,border_radius = 15)
        window.blit(self.text,self.textpos)
        window.blit(self.text4,(540-90, 338))
        window.blit(Error,(self.pos[0]+140,self.pos[1]+105))
        
        window.blit(errorexit,(self.pos[0]+270,self.pos[1]+5))
    def drawimposible(self):
        Error = pygame.image.load('warning2.png')
        errorexit = pygame.image.load('shutdown.png')
        pygame.draw.rect(window,self.color,self.rect,border_radius = 15)
        pygame.draw.rect(window,WHITE,self.upperrect)
        pygame.draw.rect(window,Gray,self.rect,1,border_radius = 15)
        window.blit(self.text2,self.textpos)
        window.blit(self.text3,(540-80, 338))
        window.blit(Error,(self.pos[0]+145,self.pos[1]+110))
        window.blit(errorexit,(self.pos[0]+270,self.pos[1]+5))
#Textbox Class
class Textbox():
    placeholder = ''
    checkreset = False
    checkstart = False
    def __init__(self,text,width,height,pos,Activate,unit):
        self.normaltext = text
        self.newtext = text
        self.posx = pos[0]
        self.posy = pos[1]
        self.w = width
        self.h = height
        self.color = WHITE
        self.firsttext = text
        self.Activate = False
        self.rect = pygame.Rect(pos,(width,height))
        self.text = parameter_font.render(text,True,WHITE)
        self.textpos = self.text.get_rect(center = self.rect.center)
        self.unit = parameter_font.render(unit,True,WHITE)
        Textbox.placeholder = self.firsttext
        self.text = parameter_font.render(Textbox.placeholder,True,AQUA)
    def draw(self):
        pygame.draw.rect(window,WHITE,self.rect,border_radius = 10)
        pygame.draw.rect(window,self.color,self.rect,2,border_radius = 10)
        window.blit(self.unit,(self.posx+75,self.posy))
        window.blit(self.text,(self.posx+(self.w/2)-15,self.posy))
    def check(self): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.color = BLUE
            Textbox.placeholder = ''
            if Textbox.checkreset == True or projectile1.resetvalue == True:
                projectile1.projectilestart = False
                Textbox.placeholder = self.firsttext
                self.text = parameter_font.render(Textbox.placeholder,True,AQUA)
                self.newtext = self.firsttext
            if pygame.draw.rect(window,BLACK,self.rect,1).collidepoint(event.pos):
                Textbox.placeholder = ''
                self.newtext = ''
                self.color = BLUE
                self.Activate = True
                self.text = parameter_font.render(Textbox.placeholder,True,AQUA)
            else:
                self.color = WHITE
                self.Activate = False
        if self.Activate == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Textbox.placeholder = Textbox.placeholder[:-1]
                    self.newtext = Textbox.placeholder 
                    self.text = parameter_font.render(Textbox.placeholder,True,AQUA)
                else:
                    if len(Textbox.placeholder) < 5:
                        Textbox.placeholder += event.unicode
                        self.newtext = Textbox.placeholder
                        self.text = parameter_font.render(Textbox.placeholder,True,AQUA) 
Homefont = pygame.font.SysFont("microsoftsansserif", 75)
Groupfont = pygame.font.SysFont("microsoftsansserif", 60)
def Home():
    Homeicon = pygame.image.load('Homeicon.png')
    pygame.draw.rect(window,WHITE,pygame.Rect((0,0),(1080,720)))
    HomeText = Homefont.render("Project simulation",True,'#707070')
    GroupName = Groupfont.render("G14",True,'#5A6EB7')
    press = pygame.font.SysFont("microsoftsansserif", 30).render("Click anywhere to start",True,'#B6B6B6')
    window.blit(GroupName,((1080/2)+180,(720/2)+100+50))
    window.blit(HomeText,((1080/2)-300,(720/2)+50))
    window.blit(press,((1080/2)-150,(720/2)+120+50))
    window.blit(Homeicon,(400,50+50))
def resetdefault():
    Textbox.checkreset = True
    projectile1.projectilestart = False
    statustext.u = 0
    statustext.t = 0
    statustext.v = 0
    statustext.theta_v = 0
    statustext.deltax = 0
    projectile1.Error_check = False
    Screen.screen()


Creditfont = pygame.font.SysFont("microsoftsansserif", 21)
class UIHistory():
    def __init__(self,posx,posy,color,text):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.text = Creditfont.render(text,True,self.color)
    def draw(self):
        BG = pygame.image.load('BG.jpg')
        window.blit(BG,(-10,40))
        pygame.draw.rect(window,AQUA,pygame.Rect((1080/2)-300,80,600,600),border_radius = 15)
        pygame.draw.rect(window,WHITE,pygame.Rect((1080/2)-300,100,600,560))
        pygame.draw.rect(window,BLACK,pygame.Rect((1080/2)-300,80,600,600),1,border_radius = 15)
class UICredit():
    def __init__(self,posx,posy,color,text):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.text = Creditfont.render(text,True,self.color)
        self.member = pygame.image.load('user.png')
        self.ID = pygame.image.load('id-card.png')
        self.Head = Creditfont.render("Member G14",True,self.color)
    def drawName(self):
        window.blit(self.text,(self.posx,self.posy))
        window.blit(self.member,(self.posx-30,self.posy))
    def drawID(self):
        window.blit(self.text,(self.posx+20,self.posy))
        window.blit(self.ID,(self.posx-10,self.posy))
    def Developer(self):
        BG = pygame.image.load('BG.jpg')
        Image1 = pygame.image.load('Assem_struct.png')
        window.blit(BG,(-10,40))
        pygame.draw.rect(window,AQUA,pygame.Rect((1080/2)-300,80,600,600),border_radius = 15)
        pygame.draw.rect(window,WHITE,pygame.Rect((1080/2)-300,100,600,560))
        pygame.draw.rect(window,BLACK,pygame.Rect((1080/2)-300,80,600,600),1,border_radius = 15)
        window.blit(self.Head,(500,100))
def writehistory():
    history = open("C:\\Users\Lenovo\Downloads\history.txt","a")
    history.write("K"+(K_textbox.newtext)+"n"+(N_textbox.newtext)+"D"+(theta_textbox.newtext)
    +"H"+(H_textbox.newtext)+"M"+(M_textbox.newtext)+"X"+(Xfinal_textbox.newtext)+"Y"+(Yfinal_textbox.newtext)
    +"U"+str(round(projectile1.newu,2))+"V"+str(round(projectile1.newu,2))+"D"+str(round(projectile1.newv,2))
    +"X"+str(round(projectile1.newdeltax,2))+"T"+str(round(projectile1.newt,2))+"L"+'\n')
    history.close()
    showhistory()
    readhistory()

def showhistory():
    history = open("C:\\Users\Lenovo\Downloads\history.txt","r")
    memory = []
    text = ''
    line = 0
    while history.readline():
        line += 1
    history.close()
    line_numbers = [line-1, line,line-4,line-3,line-2]
    for i in line_numbers:
        x = linecache.getline(r"C:\\Users\Lenovo\Downloads\history.txt", i).strip()
        memory.append(x)

    history = open("C:\\Users\Lenovo\Downloads\showhistory.txt","w")
    for i in range(5):
        text = memory[i]
    text = text
    history.write(text)
    history.close()
def readhistory():
    history = open("C:\\Users\Lenovo\Downloads\showhistory.txt","r")
    value = history.read()
    temp = ''
    arrayvalue = ['']
    finalarray = []
    for i in value:
        if i.isdigit() == True or i == '.':
            temp += i
        else:
            arrayvalue.append(temp)
            temp = ''
    ct = datetime.datetime.now()
    for j in range(len(arrayvalue)):
        if arrayvalue[j] != '':
            finalarray.append(arrayvalue[j])
        try: 
            if arrayvalue[j] == '':
                finalarray.append(ct)
        except:
            print("error")
#Credit
Member1 = UICredit(250+50,150+10,Gray,'นายชยพล  หาญเสน่ห์ลักษณ์')
Member2 = UICredit(250+50,250+10,Gray,'นายอดิศักดิ์  สุจริต')
Member3 = UICredit(250+50,350+10,Gray,'นายปภินวิทย์ รัตนศิริ') 
Member4 = UICredit(250+50,450+10,Gray,'นายปัณณพัฒน์ เกตุแก้ว') 
Member5 = UICredit(250+50,550+10,Gray,'นางสาวหญิงวารีย์ อุรัจนานนท')
IDMember1 = UICredit(550,150+10,Gray,'รหัสนักศึกษา 64340500011')
IDMember2 = UICredit(550,250+10,Gray,'รหัสนักศึกษา 64340500054')
IDMember3 = UICredit(550,350+10,Gray,'รหัสนักศึกษา 64340500065')
IDMember4 = UICredit(550,450+10,Gray,'รหัสนักศึกษา 64340500066')
IDMember5 = UICredit(550,550+10,Gray,'รหัสนักศึกษา 64340500074')
#Text
intialpoint_Text = statustext("Initial Position",720,140,WHITE) #720,140
Position_Text = statustext("Position",900,140,WHITE) #900,140
K_Text = parametertext("Spring Constants (K)",120,640+15,WHITE) #120,140
theta_Text = parametertext("Angle ",400,640+15,WHITE) #120,170
M_text = parametertext("Mass (m)",630,680+15,WHITE) #120,200
H_text = parametertext("Height (h)",400,680+15,WHITE) #120,230
N_Text = parametertext("Spring Amout (n)",120,680+15,WHITE) #120,260
Final_position = parameter_font.render("Final Position",True,WHITE)
Finalx_text = parametertext("X",630+100,640+15,WHITE) #250,300
Finaly_text = parametertext(",Y",640+100,640+15,WHITE) #250,330

#Textbox
K_textbox = Textbox("170",70,17,(120+130,640+15),False,"N/m") #300,140.
theta_textbox = Textbox("45",70,17,(400+70,640+15),False,"degree") #300,170
H_textbox = Textbox("0.3",70,17,(400+70,680+15),False,"m") #300,230
M_textbox = Textbox("0.275",70,17,(710,680+15),False,"kg") #300,200
N_textbox = Textbox("2",70,17,(120+130,680+15),False,"pieces") #300,260
Xfinal_textbox = Textbox("x",70,17,(630+130,640+15),False,"") #300,300
Yfinal_textbox = Textbox("y",70,17,(630+210,640+15),False,"m") #300,330

#Button
resertbutton = checkbutton("Reset",50,20,(950,700)) #327,363
startbutton = checkbutton("Start",50,20,(950,650)) #120,360
button1 = Newbutton('Start',75,20,(930+5,655),5)
button2 = Newbutton('Reset',75,20,(930+5,690),5)

#projectile,Error
projectile1 = projectile(scale,dt/1000)
Error_alert = ErrorTextbox(400,250,AQUA,parameter_font,300,140)
window.fill(WHITE)
#checkexitstatus = pygame.draw.rect(window,BLACK, pygame.Rect(700,105,30,10))
#checkexitparameter = pygame.draw.rect(window,BLACK, pygame.Rect(70,660,30,10))
checkexitscreen = pygame.draw.rect(window,WHITE, pygame.Rect(1050,12,15,15))
checkcredit = pygame.draw.rect(window,WHITE, pygame.Rect(1004,12,15,15))
Exitparameter = pygame.image.load('exit.png')
Exitstatus = pygame.image.load('exit.png')
Screen.screen()
CreditActivate = False
checkexiterror = pygame.draw.rect(window,WHITE, pygame.Rect(670,255,24,24))
Homeopen = True
login = False
while True:
    for event in pygame.event.get():
        Screen.startcheck()
        Screen.resetcheck()
        checkexiterror = pygame.draw.rect(window,WHITE, pygame.Rect(670,255,24,24))
        K_textbox.check()
        theta_textbox.check()
        H_textbox.check()
        M_textbox.check()
        N_textbox.check()
        Xfinal_textbox.check()
        Yfinal_textbox.check()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if login == True:
                if checkexitscreen.collidepoint(event.pos):
                    window.fill(WHITE)
                    Screen.screen()
                    pygame.quit()
                    sys.exit()
                if checkcredit.collidepoint(event.pos):
                    if CreditActivate == True:
                        Screen.screen()
                        CreditActivate = False
                    elif CreditActivate == False:
                        CreditActivate = True
                if checkexiterror.collidepoint(event.pos):
                    projectile1.Error_check = False
                    projectile1.imposiblecase = False
                    window.fill(WHITE)
                    Screen.screen()
    Screen.graph()
    if projectile1.Error_check == True:
        checkexiterror = pygame.draw.rect(window,BLACK, pygame.Rect(400+177,250,19,17))
        Screen.screen()
        Error_alert.draw()
        if Screen.isfloat(K_textbox.newtext) == False or (K_textbox.newtext) <= '0':
            K_textbox.color = RED
        if Screen.isfloat(N_textbox.newtext) == False or (N_textbox.newtext) <= '0':
            N_textbox.color = RED
        if Screen.isfloat(M_textbox.newtext) == False or (M_textbox.newtext) <= '0':
            M_textbox.color = RED
        if Screen.isfloat(theta_textbox.newtext) == False or (theta_textbox.newtext) <= '0':
            theta_textbox.color = RED
        if Screen.isfloat(H_textbox.newtext) == False or (H_textbox.newtext) <= '0':
            H_textbox.color = RED
        if Screen.isfloat(Xfinal_textbox.newtext) == False or (Xfinal_textbox.newtext) <= '0':
            Xfinal_textbox.color = RED
        if Screen.isfloat(Yfinal_textbox.newtext) == False or (Xfinal_textbox.newtext) < '0':
            Yfinal_textbox.color = RED
    if projectile1.projectilestart == True:
        projectile1.draw()
    if projectile1.imposiblecase == True:
        Screen.screen()
        Error_alert.drawimposible()
        theta_textbox.color = RED
        Xfinal_textbox.color = RED
        Yfinal_textbox.color = RED
        if Screen.isfloat(K_textbox.newtext):
            if float(K_textbox.newtext) <= 0:
                K_textbox.color = RED
        if Screen.isfloat(H_textbox.newtext):
            if float(H_textbox.newtext) <= 0:
                H_textbox.color = RED
        if Screen.isfloat(N_textbox.newtext):
            if float(N_textbox.newtext) <= 0:
                N_textbox.color = RED
        if Screen.isfloat(Yfinal_textbox.newtext) == True:
            if float(Yfinal_textbox.newtext) < 0:
                Yfinal_textbox.color = RED
        if Screen.isfloat(Xfinal_textbox.newtext) == True:
            if float(Xfinal_textbox.newtext) == 0:
                Xfinal_textbox.color = RED
    if parameter == True:
        parameterbox()
        K_Text.draw()
        theta_Text.draw()
        H_text.draw()
        N_Text.draw()
        M_text.draw()
        Finalx_text.draw()
        Finaly_text.draw()
        K_textbox.draw()
        M_textbox.draw()
        theta_textbox.draw()
        H_textbox.draw()
        N_textbox.draw()
        Xfinal_textbox.draw()
        Yfinal_textbox.draw()
        button1.draw()
        button2.draw()
        window.blit(Final_position,(630,640+15))
    if status == True:
        statusbox()
        intialpoint_Text.draw()
        Position_Text.draw()
    if CreditActivate == True:
        Screen.screen()
        Member1.Developer()
        Member1.drawName()
        Member2.drawName()
        Member3.drawName()
        Member4.drawName()
        Member5.drawName()
        IDMember1.drawID()
        IDMember2.drawID()
        IDMember3.drawID()
        IDMember4.drawID()
        IDMember5.drawID()
    if login == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
            login = True
            Screen.screen()
            Homeopen = False
        if Homeopen == True:
            Home()
    pygame.display.update()