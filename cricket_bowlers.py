import random
import math
import numpy as np
import pandas as pd
import copy
import time

t20 = []
for i in range(0, 20):
    t20.append(0)
for i in range(0, 28):
    t20.append(1)
for i in range(0, 17):
    t20.append(2)
for i in range(0, 5):
    t20.append(3)
for i in range(0, 7):
    t20.append(4)
for i in range(0, 4):
    t20.append(5)
for i in range(0, 4):
    t20.append(6)

ODI = []
for i in range(0, 65):
    ODI.append(0)
for i in range(0, 35):
    ODI.append(1)
for i in range(0, 17):
    ODI.append(2)
for i in range(0, 5):
    ODI.append(3)
for i in range(0, 7):
    ODI.append(4)
for i in range(0, 3):
    ODI.append(5)
for i in range(0, 3):
    ODI.append(6)

t20_target = []
for i in range(0, 19):
    t20_target.append(0)
for i in range(0, 23):
    t20_target.append(1)
for i in range(0, 15):
    t20_target.append(2)
for i in range(0, 6):
    t20_target.append(3)
for i in range(0, 5):
    t20_target.append(4)
for i in range(0, 6):
    t20_target.append(5)
for i in range(0, 5):
    t20_target.append(6)

t20_target_2 = []
for i in range(0, 28):
    t20_target_2.append(0)
for i in range(0, 30):
    t20_target_2.append(1)
for i in range(0, 14):
    t20_target_2.append(2)
for i in range(0, 4):
    t20_target_2.append(3)
for i in range(0, 6):
    t20_target_2.append(4)
for i in range(0, 3):
    t20_target_2.append(5)
for i in range(0, 4):
    t20_target_2.append(6)

t20_target_extreme = []
for i in range(0, 15):
    t20_target_extreme.append(0)
for i in range(0, 20):
    t20_target_extreme.append(1)
for i in range(0, 15):
    t20_target_extreme.append(2)
for i in range(0, 4):
    t20_target_extreme.append(3)
for i in range(0, 7):
    t20_target_extreme.append(4)
for i in range(0, 9):
    t20_target_extreme.append(5)
for i in range(0, 8):
    t20_target_extreme.append(6)

ODI_target = []
for i in range(0, 56):
    ODI_target.append(0)
for i in range(0, 50):
    ODI_target.append(1)
for i in range(0, 16):
    ODI_target.append(2)
for i in range(0, 5):
    ODI_target.append(3)
for i in range(0, 10):
    ODI_target.append(4)
for i in range(0, 7):
    ODI_target.append(5)
for i in range(0, 5):
    ODI_target.append(6)

ODI_target_2 = []
for i in range(0, 90):
    ODI_target_2.append(0)
for i in range(0, 40):
    ODI_target_2.append(1)
for i in range(0, 21):
    ODI_target_2.append(2)
for i in range(0, 5):
    ODI_target_2.append(3)
for i in range(0, 6):
    ODI_target_2.append(4)
for i in range(0, 2):
    ODI_target_2.append(5)
for i in range(0, 2):
    ODI_target_2.append(6)

Tests = []
for i in range(0, 270): #250 #275
    Tests.append(0)
for i in range(0, 36):
    Tests.append(1)
for i in range(0, 16):
    Tests.append(2)
for i in range(0, 5):
    Tests.append(3)
for i in range(0, 7):
    Tests.append(4)
for i in range(0, 4): #5
    Tests.append(5)
Tests.append(6)

NewZealandT20 = "Finn Allen,Devon Conway,Kane Williamson(c),Glenn Phillips,Jimmy Neesham,Mark Chapman,Michael Santner,Ish Sodhi,Tim Southee,Lockie Ferguson,Trent Boult"
NZT20Bowl = [0, 0, 0.1, 0.7, 0.7, 0.4, 0.8, 0.9, 0.95, 0.95, 0.95]
NewZealandODI = "Devon Conway,Rachin Ravindra,Kane Williamson(c),Daryl Mitchell,Tom Latham,Glenn Phillips,Mark Chapman,Mitchell Santner,Tim Southee,Trent Boult,Lockie Ferguson"
NZODIBowl = [0, 0.6, 0.1, 0.5, 0, 0.7, 0.4, 0.8, 0.95, 0.95, 0.95]
NewZealandTest = "Tom Latham,Devon Conway,Kane Williamson(c),Rachin Ravindra,Daryl Mitchell,Tom Blundell,Glenn Phillips,Trent Boult,Matt Henry,Tim Southee,Ben Sears"
NZTestBowl = [0,0,0.1,0.6,0.6,0,0.75,0.95,0.95,0.95,0.9]
NewZealandT20Women = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze,Rosemary Mair,Lea Tahuhu,Eden Carson,Fran Jonas"
NZT20WBowl = [0.3,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
NewZealandODIWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze,Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
NZODIWBowl = [0.3,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
NewZealandTestWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze,Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
NZTestWBowl = [0.3,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
AustraliaT20 = "Travis Head,Jake Fraser-McGurk,Mitchell Marsh(c),Glenn Maxwell,Marcus Stoinis,Matthew Wade,Tim David,Ashton Agar,Pat Cummins,Mitchell Starc,Adam Zampa"
AUST20Bowl = [0.3,0,0.75,0.7,0.7,0,0.1,0.8,0.95,0.95,0.95]
AustraliaODI = "Travis Head,Jake Fraser-McGurk,Mitchell Marsh,Steve Smith,Marnus Labuschagne,Glenn Maxwell,Alex Carey,Pat Cummins(c),Mitchell Starc,Adam Zampa,Jason Behrendoff"
AUSODIBowl = [0.3,0,0.75,0.2,0.3,0.7,0,0.95,0.95,0.95,0.9]
AustraliaTest = "Nathan McSweeney,Usman Khawaja,Marnus Labuschagne,Steve Smith,Travis Head,Mitchell Marsh,Alex Carey,Pat Cummins(c),Mitchell Starc,Nathan Lyon,Josh Hazlewood"
AUSTestBowl = [0,0,0.3,0.1,0.2,0.8,0,0.95,0.9,0.8,0.9]
AustraliaT20Women = "Alyssa Healy,Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AUST20WBowl = [0,0,0.1,0.1,0.8,0.05,0.75,0.75,0.8,0.8,0.8]
AustraliaODIWomen = "Alyssa Healy,Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AUSODIWBowl = [0,0,0.1,0.1,0.8,0.05,0.75,0.75,0.8,0.8,0.8]
AustraliaTestWomen = "Beth Mooney,Phoebe Litchfield,Ellyse Perry,Tahlia McGrath,Jess Jonassen,Alyssa Healy(c),Ashleigh Gardner,Annabel Sutherland,Alan King,Kim Garth,Darcie Brown"
AUSTestWBowl = [0,0.05,0.9,0.4,0.5,0,0.75,0.75,0.8,0.8,0.8]
IndiaT20 = "Rohit Sharma(c),Abhishek Sharma,Virat Kohli,SKY,Rishabh Pant,Shivam Dube,Rinku Singh,Avesh Khan,Mayank Yadav,Yuzi Chahal,Jasprit Bumrah"
INDT20Bowl = [0.1,0.23,0.1,0.2,0,0.6,0.2,0.8,0.9,0.9,0.95]
IndiaODI = "Rohit Sharma(c),Shubman Gill,Virat Kohli,Shreyash Iyer,SKY,Rinku Singh,Ravindra Jadeja,Jasprit Bumrah,Mohd Shami,Kuldeep Yadav,Mohd Siraj"
INDODIBowl = [0.1,0.1,0.1,0.3,0.3,0.2,0.78,0.95,0.95,0.9,0.85]
IndiaTest = "Rohit Sharma(c),Yashasvi Jaiswal,Shubman Gill,Virat Kohli,KL Rahul,Nitish Kumar Reddy,Rishabh Pant,Ravindra Jadeja,Mohd Shami,Jasprit Bumrah,Mohd Siraj"
INDTestBowl = [0.01,0,0.007,0.01,0,0.4,0,0.8,0.85,0.99,0.9]
IndiaT20Women = "Shafali Verma,Smriti Mandhana,Jemimah Rodrigues,Harmanpreet Kaur(c),Deepti Sharma,Richa Ghosh,Pooja Vastrakar,Arundhati Reddy,Shreyanka Patil,Radha Yadav,Renuka Singh"
INDT20WBowl = [0,0.1,0.1,0.3,0.6,0.6,0.8,0.78,0.9,0.8,0.88]
IndiaODIWomen = "Shafali Verma,Smriti Mandhana,Dayalan Hemalatha,Harmanpreet Kaur(c),Jemimah Rodrigues,Richa Ghosh,Deepti Sharma,Pooja Vastrakar,Radha Yadav,Asha Sobhana,Renuka Singh"
INDODIWBowl = [0,0.1,0.3,0.4,0.1,0.6,0.7,0.88,0.85,0.85,0.9]
IndiaTestWomen = "Shafali Verma,Smriti Mandhana,Shubha Satheesh,Jemimah Rodrigues,Harmanpreet Kaur(c),Richa Ghosh,Deepti Sharma,Pooja Vastrakar,Shen Rana,Renuka Singh,Rajeshwari Gayakwad"
INDTestWBowl = [0,0.1,0,0.1,0.3,0.6,0.6,0.85,0.85,0.9,0.87]
EnglandODI = "Phil Salt,Zack Crawley,Joe Root,Harry Brook,Jos Buttler(c),Ben Stokes,Sam Curran,Chris Woakes,Jofra Archer,Adil Rashid,Mark Wood"
ENGODIBowl = [0,0,0.4,0,0,0.7,0.75,0.9,0.9,0.9,0.95]
EnglandT20 = "Phil Salt,Jos Buttler(c),Will Jacks,Liam Livingstone,Harry Brook,Ben Stokes,Sam Curran,Chris Woakes,Jofra Archer,Adil Rashid,Mark Wood"
ENGT20Bowl = [0,0,0.3,0.5,0,0.5,0.78,0.85,0.9,0.95,0.95]
EnglandTest = "Zack Crawley,Ben Duckett,Joe Root,Harry Brook,Ben Stokes(c),Jamie Smith,Chris Woakes,Gus Atkinson,Jofra Archer,Ollie Robinson,Jack Leach"
ENGTestBowl = [0,0,0.25,0,0.6,0,0.85,0.8,0.87,0.85,0.83]
EnglandT20Women = "Maia Bouchier,Danni Wyatt-Hodge,Alice Capsey,Nat Sciver-Brunt,Heather Knight(c),Amy Jones,Charlie Dean,Kate Cross,Sophie Ecclestone,Sarah Glenn,Lauren Bell"
ENGT20WBowl = [0,0,0.4,0.8,0.01,0.75,0.8,0.85,0.9,0.87,0.9]
EnglandODIWomen = "Tammy Beaumont,Maia Bouchier,Heather Knight(c),Nat Sciver-Brunt,Danni Wyatt-Hodge,Amy Jones,Alice Capsey,Charlie Dean,Sophie Ecclestone,Kate Cross,Lauren Bell"
ENGODIWBowl = [0,0,0.01,0.8,0,0.75,0.4,0.85,0.9,0.9,0.95]
EnglandTestWomen = "Maia Bouchier,Tammy Beaumont,Heather Knight(c),Nat Sciver-Brunt,Sophia Dunkley,Danni Wyatt-Hodge,Amy Jones,Sophie Ecclestone,Kate Cross,Lauren Filer,Lauren Bell"
ENGTestWBowl = [0,0,0.02,0.8,0.01,0.01,0,0.85,0.9,0.87,0.92]
SouthAfricaT20 = "Reeza Hendricks,QDK,Aiden Markram(c),Tristan Stubbs,Heinrich Klaasen,David Miller,Marco Jansen,Keshav Maharaj,Kagiso Rabada,Anrich Nortje,Tabraiz Shamsi"
SAT20Bowl = [0,0,0,0,0,0,0.9,0.87,0.95,0.95,0.88]
SouthAfricaODI = "QDK,Temba Bavuma(c),Rassie van der Dussen,Aiden Markram,Heinrich Klaasen,David Miller,Marco Jensen,Gerald Coetzee,Keshav Maharaj,Kagiso Rabada,Tabraiz Shamsi"
SAODIBowl = [0,0,0,0,0,0,0.87,0.87,0.85,0.95,0.8]
SouthAfricaTEST = "Aiden Markram,Temba Bavuma(c),Tony de Zorzi,Keegan Petersen,David Bedingham,Kyle Verreynne,Marco Jansen,Gerald Coetzee,Kagiso Rabada,Nandre Burger,Anrich Nortje"
SATestBowl = [0,0,0,0,0,0,0.8,0.9,0.95,0.8,0.9]
SouthAfricaT20Women = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Marizanne Kapp,Nadine de Klerk,Chloe Tryon,Sune Luus,Annerie Dercksen,Sinalo Jafta,Nonkululeko Mlaba,Ayabonga Khaka"
SAT20WBowl = np.sort(np.random.beta(0.01, 0.9, size=11))
SAT20WBowl[8] = 0
SouthAfricaODIWomen = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Sune Luus,Marizanne Kapp,Nadine de Klerk,Nondumiso Shangase,Mieke de Ridder,Masabata Klaas,Nonkululeko Mlaba,Ayabonga Khaka"
SAODIWBowl = np.sort(np.random.beta(0.01, 0.9, size=11))
SAODIWBowl[7] = 0
SouthAfricaTESTWomen = "Laura Wolvaardt(c),Anneke Bosch,Sune Luus,Marizanne Kapp,Delmari Tucker,Nadine de Klerk,Sinalo Jafta,Annerie Dercksen,Tumi Sekhukhune,Masabata Klaas,Nonkululeko Mlaba"
SATestWBowl = np.sort(np.random.beta(0.1, 0.9, size=11))
SATestWBowl[6] = 0
PeanutButter = "Peanut Butter(c),Peanut Sandwich,Peanut Pancake,Peanut Burger,Peanut Lasagne,Peanut Colada,Sergeant Peanut,Peanut Calculus,Square Peanut,Peanut Biryani,Peanut Rice"
PBBowl = np.sort(np.random.beta(0.25, 0.8, size=11))
PBBowl[6] = 0
DahliaXI = "Viral C(c),Harsha V,Akshit S,Ayush S,Bunny,Aryan,Rishit,Joshua L,Nikhil G,Anchit K,Devajya K"
DahliaBowl = [0.8,0.83,0.7,0.8,0,0,0,0.65,0.2,0.95,0.9]
SDS = "Viral C(c),Zehaan Naik,Aditya V,Ishi Jain,Nandini Bhattad,Raghav Govind,Subham Anand,Yash Bihany,Devansh Gupta,P Sarath,Priyanshu Gupta"
SDSBowl = [0.8,0.1,0,0.2,0.2,0.3,0.7,0.8,0.85,0.93,0.9]
Beatles = "Paul McCartney,Ringo Starr,George Harrison,John Lennon(c),George Martin,Brian Epstein,Eleanor Rigby,Billy Shears,Geoff Emerick,Sergeant Pepper,Mr Kite"
BeatlesBowl = [0.5,0.4,0.2,0.5,0.2,0,0.8,0.75,0.9,0.85,0.85]
WomenArtist = "Olivia Rodrigo(c),Sabrina Carpenter,Lana Del Rey,Leah Kate,Dua Lipa,Dasha,Adele,Katy Perry,Avril Lavigne,Linda Ronstadt,Tiffany Stringer"
WABowl = [0.2,0.2,0.3,0,0.6,0.5,0.7,0.75,0.8,0.85,0.85]
ModernFamily = "Phil Dunphy(c),Luke Dunphy,Claire Dunphy,Cam Tucker,Jay Pritchett,Lily Tucker-Pritchett,Manny Delgado,Alex Dunphy,Mitchell Pritchett,Gloria Pritchett,Haley Dunphy"
MFBowl = [0.1,0.8,0,0.4,0.3,0.75,0.6,0.58,0.75,0.8,0.9]
WeatherXI = "Alex Halestone,Weather Knight(c),Chris Gaylestorm,Ebony Rainford-Brent,Ben Sun-strokes,Jonny Bairsnow,David Chilley,Rain Warne,Matthew Foggard,Jimmy Andersun,John Snow"
WeatherBowl = [0,0.1,0.4,0,0.5,0,0.8,0.95,0.76,0.85,0.8]
print("Pre defined Teams - New Zealand, Australia, India, England, South Africa(SA), PeanutButter(PB), DahliaXI, Beatles, WomenArtist(WA), ModernFamily(MF), SDS, WeatherXI")
Teams = [NewZealandT20, NewZealandODI, NewZealandTest, NewZealandT20Women, NewZealandODIWomen, NewZealandTestWomen, AustraliaODI, AustraliaT20, AustraliaTest, AustraliaODIWomen, AustraliaT20Women, AustraliaTestWomen, IndiaODI, IndiaT20, IndiaTest, IndiaODIWomen, IndiaT20Women, IndiaTestWomen, EnglandT20, EnglandODI, EnglandTest, EnglandT20Women, EnglandODIWomen, EnglandTestWomen, SouthAfricaT20, SouthAfricaODI, SouthAfricaTEST, SouthAfricaT20Women, SouthAfricaODIWomen, SouthAfricaTESTWomen, PeanutButter, DahliaXI, Beatles, WomenArtist, ModernFamily, SDS, WeatherXI]
TeamBowl = [NZT20Bowl, NZODIBowl, NZTestBowl, NZT20WBowl, NZODIWBowl, NZTestWBowl, AUSODIBowl, AUST20Bowl, AUSTestBowl, AUSODIWBowl, AUST20WBowl, AUSTestWBowl, INDODIBowl, INDT20Bowl, INDTestBowl, INDODIWBowl, INDT20WBowl, INDTestWBowl, ENGT20Bowl, ENGODIBowl, ENGTestBowl, ENGT20WBowl, ENGODIWBowl, ENGTestWBowl, SAT20Bowl, SAODIBowl, SATestBowl, SAT20WBowl, SAODIWBowl, SATestWBowl, PBBowl, DahliaBowl, BeatlesBowl, WABowl, MFBowl, SDSBowl, WeatherBowl]
t = ["NZT20", "NZODI", "NZTEST", "NZWT20", "NZWODI", "NZWTEST", "AUSODI", "AUST20", "AUSTEST", "AUSWODI", "AUSWT20", "AUSWTEST", "INDODI", "INDT20", "INDTEST", "INDWODI", "INDWT20", "INDWTEST", "ENGT20", "ENGODI", "ENGTEST", "ENGWT20", "ENGWODI", "ENGWTEST", "SAT20", "SAODI", "SATEST", "SAWT20", "SAWODI", "SAWTEST", "PB", "DAHLIAXI", "BEATLES", "WA", "MF", "SDS", "WEATHER"]

def removeCap(s):
    return s.replace("(c)", "")

def isInt(p):
    return type(p) == int

def total(A):
    return sum(A) - 5*A.count(5)

def BallsToOvers(b):
    return str(b//6) + "." + str(b%6)

def Bernoulli(p):
    if random.random() < p:
        return 1
    return 0

def Toss():
    if Bernoulli(0.5) == 1:
        return "H"
    return "T"

# Prints scoreline of series as it is going on.
def seriesGoing(S):
    K = list(S.keys())
    if S[K[0]] > S[K[1]]:
        print(K[0] + " leads the series by " + str(S[K[0]]) + " - " + str(S[K[1]]))
    if S[K[0]] < S[K[1]]:
        print(K[1] + " leads the series by " + str(S[K[1]]) + " - " + str(S[K[0]]))
    if S[K[0]] == S[K[1]]:
        print("Series is level at " + str(S[K[0]]) + " - " + str(S[K[1]]))

# Prints scoreline of finished series.
def seriesOutput(S):
    K = list(S.keys())
    if S[K[0]] > S[K[1]]:
        print(K[0] + " wins the series by " + str(S[K[0]]) + " - " + str(S[K[1]]))
    if S[K[0]] < S[K[1]]:
        print(K[1] + " wins the series by " + str(S[K[1]]) + " - " + str(S[K[0]]))
    if S[K[0]] == S[K[1]]:
        print("Series is drawn at " + str(S[K[0]]) + " - " + str(S[K[1]]))

class Bowler:
    def __init__(self):
        self.Economy = None
        self.Overs = None
        self.Runs = None
        self.Wickets = None
        self.Average = None
        self.Figures = None
    def makeStats(self, B):
        Balls = len(B)
        self.Runs = sum(B) - 5*B.count(5)
        self.Economy = round(self.Runs/Balls * 6, 2)
        self.Overs = str(int(Balls/6)) + "." + str(Balls%6)
        self.Wickets = B.count(5)
        if self.Wickets != 0:
            self.Average = round(self.Runs/self.Wickets, 2)
        else:
#           self.Average = self.Runs
            self.Average = None
        self.Figures = 10000*self.Wickets + 1000 - self.Runs
    def printStats(self):
        print(self.Overs + "-" + str(self.Runs) + "-" + str(self.Wickets) + "-" + str(self.Economy))

class Batter:
    def __init__(self):
        self.runs = 0
        self.strikerate = 0
        self.average = 0
    def makeStats(self, Batting):
        Total = 0
        Wickets = 0
        for i in range(0, len(Batting)):
            if isInt(Batting[i]):
                Total += Batting[i]
            else:
                Wickets += 1
        if Wickets != 0:
            self.average = round(Total/Wickets, 2)
        else:
            self.average = Total
        self.runs = Total
        if len(Batting) != 0:
            self.strikerate = round(Total/len(Batting) * 100, 2)
        else:
            self.strikerate = 0

A_Team = []
A_Bowl = []
B_Team = []
B_Bowl = []
for i in range(0, 11):
    A_Team.append("A" + str(i + 1))
    B_Team.append("B" + str(i + 1))
    if i <= 5:
        A_Bowl.append(0)
        B_Bowl.append(0)
    if i > 5:
        A_Bowl.append(i/10)
        B_Bowl.append(i/10)
B_Bowl[5] = 0.5
B_Bowl[-1] = 0.99
A_Bowl[-1] = 0.99

def DistBowl(Team, Bowl, Overs):
    S = 0
    counter = 0
    D = dict(sorted(dict(zip(Team, Bowl)).items(), key=lambda x: x[1], reverse= True))
    T = list(D.keys())
    B = list(D.values())
    DOut = {}
    MaxPer = int(Overs/5)
    for i in range(0, len(T)):
        DOut[T[i]] = 0
    j = 0
    while S < Overs:
        counter += 1
        ma = min(MaxPer, Overs - S + DOut[T[j]])
        mi = DOut[T[j]]
        K = True
        while K:
            if ma < mi:
                j += 1
                j = j % len(T)
                K = False
                break
            c = Bernoulli(B[j])
            if c == 1:
                ex = DOut[T[j]]
                DOut[T[j]] = ma
                S = S - ex + ma
                j += 1
                j = j % len(T)
                K = False
            else:
                ma -= 1
    return DOut

def DistBowlTest(Team, Bowl, Overs):
     Curr = random.choices(Team, weights = Bowl, k = 1)[0]
     D = {}
     D[Curr] = 1
     Count = 1
     while Count < Overs:
         L = []
         Lw = []
         Count += 1
         for i in range(0, len(Team)):
             if Team[i] != Curr:
                 L.append(Team[i])
                 Lw.append(Bowl[i])
         Curr = random.choices(L, weights = Lw, k = 1)[0]
         try:
             D[Curr] += 1
         except:
             D[Curr] = 1
     return D

def generate_bowling_order(player_overs):
    # Create a list of players with their overs left
    overs_left = [(player, overs) for player, overs in player_overs.items()]
    # Sort players by the number of overs in descending order
    overs_left.sort(key=lambda x: x[1], reverse=True)

    bowling_order = []

    while any(overs > 0 for _, overs in overs_left):
        for i, (player, overs) in enumerate(overs_left):
            if overs > 0 and (not bowling_order or bowling_order[-1] != player):
                # Add the player to the bowling order
                bowling_order.append(player)
                # Decrease the overs for this player
                overs_left[i] = (player, overs - 1)
                break
        # Re-sort the list to prioritize players with the most overs left
        overs_left.sort(key=lambda x: x[1], reverse=True)
    print()
    return bowling_order

# Prob is the array with probability distribution of 1 to 6.
def dice(Prob):
    return Prob[random.randint(0, len(Prob) - 1)]

# Merge D2 to D1
def mergeDict(D1, D2):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x].extend(D2[x])
        except:
            D[x] = D2[x]
    return D

# Merge D2 to D1, with an i to indicate match number
def mergeDict_i(D1, D2, i):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x + "_" + str(i)].extend(D2[x + "_" + str(i)])
        except:
            D[x + "_" + str(i)] = D2[x + "_" + str(i)]
    return D

def addDict(D1, D2):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x] += D2[x]
        except:
            D[x] = D2[x]
    return D

def dict_arrange(d):
    d1 = list(d.values())
    d1.sort()
    de = d1[::-1]
    ar = []
    for i in range(0, len(d1)):
        for j in d:
            if d[j] == de[i]:
                ar.append(j)
    return ar

def showStats(D, cut = None, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(round(V[i], 2)))
    else:
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(round(V[i], 2)))

def convertToFig(N):
    Wickets = N//10000 - 1
    Runs = 10000 * (Wickets + 1) + 1000 - N
    return str(Wickets) + "/" + str(Runs)

def showFigures(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if len(K[0].split("_")) == 2:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]))
    else:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))

def showFiguresTournament(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3])

    else:
        for i in range(cut):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3])


def showFiguresTournamentTest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))
    else:
        for i in range(min(cut, len(K))):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))

def showHighest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if len(K[0].split("_")) == 2:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]))
    else:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))

def showHighestTournament(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + str(A[2]) + " vs " + str(A[3]))
    else:
        for i in range(cut):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + str(A[2]) + " vs " + str(A[3]))

def showHighestTournamentTest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))
    else:
        for i in range(min(cut, len(K))):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))

def getBalls(Balls, Prob):
    A = []
    count = 0
    for i in range(0, Balls):
        K = dice(Prob)
        A.append(K)
        if K == 5:
            count += 1
        if count == 10:
            return A
    return A

def getBallsTest(Prob):
    A = []
    count = 0
    while count < 10:
        K = dice(Prob)
        A.append(K)
        if K == 5:
            count += 1
        if count == 10:
            return A
    return A

# Here, Balls is the getBalls output, aka array of balls. Order is bowling order
def bowlingStats(Order, Balls):
    D = {}
    for i in range(len(Balls)):
        try:
            D[Order[i//6]].append(Balls[i])
        except:
            D[Order[i//6]] = [Balls[i]]
    bowlers = list(D.keys())
    F = {}
    for i in range(len(D)):
        init = Bowler()
        init.makeStats(D[bowlers[i]])
        F[bowlers[i]] = init
    return F, D

Basic = [0, 1, 2, 3, 4, 5, 6]

#D = bowlingStats(generate_bowling_order(DistBowl(A_Team, A_Bowl, 20)), getBalls(120, Basic))

def BattingOrder(Team, Bowling, Balls):
    Curr = Team[0]
    Curr_i = 0
    Non = Team[1]
    Non_i = 1
    D = {}
    D[Curr] = []
    D[Non] = []
    FOW = {}
    Wicket = 1
    Part = 0
    B = 0
    for i in range(len(Balls)):
        B += 1
        if Balls[i] == 5:
            D[Curr].append(Bowling[int(i/6)])
            Curr_i = max(Curr_i, Non_i) + 1
            FOW[Wicket] = [Curr, Part, B]
            Wicket += 1
            Part = 0
            B = 0
            try:
                Curr = Team[Curr_i]
                D[Curr] = []
            except:
                x = 5
        else:
            D[Curr].append(Balls[i])
            Part += Balls[i]
            if Balls[i] % 2 == 1:
                New = Curr
                New_i = Curr_i
                Curr = Non
                Curr_i = Non_i
                Non = New
                Non_i = New_i
        if (i + 1)%6 == 0:
            New = Curr
            New_i = Curr_i
            Curr = Non
            Curr_i = Non_i
            Non = New
            Non_i = New_i
    return D, FOW

# Balls is getBalls output, which we truncate, and Total is the opponent score
def SecondBalls(Balls, Total):
    if total(Balls) <= Total:
        return Balls
    T = 0
    B = []
    for i in range(0, len(Balls)):
        if T <= Total:
            if Balls[i] != 5:
                T += Balls[i]
            B.append(Balls[i])
        if T > Total:
            return B
    return B

def Combinations(A):
    B = []
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            B.append([A[i], A[j]])
    return random.sample(B, len(B))

def MatchLimitedOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2, Format):
    Batting_Score_1 = {}
    Batting_Score_2 = {}
    Batting_Sheet = {}
    Bowling_Perf = {}
    Prob = t20
    Overs = 20
    if Format.upper() == "T20":
        Overs = 20
        Prob = t20
    if Format.upper() == "ODI":
        Overs = 50
        Prob = ODI
    if Format.upper() == "CUSTOM":
        Prob = ODI
        Overs = int(input("Number of Overs : "))
    t = input(Name_1 + "'s Call : ")
    if t.upper() == Toss():
        T1 = input(Name_1 + " chooses to : ").upper()
        while (T1.upper() not in ["BAT", "BOWL"]):
            T1 = input(Name_1 + " chooses to : ").upper()
        if T1 == "BOWL":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
    else:
        T2 = input(Name_2 + " chooses to : ").upper()
        while (T2.upper() not in ["BAT", "BOWL"]):
            T2 = input(Name_2 + " chooses to : ").upper()
        if T2 == "BAT":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3


    ### First Innings
    # Bowling Team Distribution
    Bowl_Dist = DistBowl(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Batting_Balls = getBalls(6*Overs, Prob)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        try:
            Bowling_Perf[Keys[i]].extend(D[Keys[i]])
        except:
            Bowling_Perf[Keys[i]] = D[Keys[i]]

    print(100*"-")
    print(Name_1)
    print(100*"-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            Batting_Score_1[Team_1[i]] = 0
            Batting_Sheet[Team_1[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A)/float(len(A)))))
            Batting_Score_1[Team_1[i]] = sum(A)
            Batting_Sheet[Team_1[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_1[i] + (25 - len(Team_1[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs/float(Balls))))
            Batting_Score_1[Team_1[i]] = Runs
            Batting_Sheet[Team_1[i]] = A
    print(100 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100*"-")
    T1 = total(Batting_Balls)
    B1 = Overs * 6
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)
    print(pd.DataFrame({"Name" : Name, "Overs" : Over, "Runs" : Runs, "Wickets" : Wickets, "Economy" : Economy}))
    print(" ")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")

    X = input("Continue ? : ")
    print(" ")
    ### Second Innings
    # Bowling Team Distribution
    if Format.upper() == "ODI":
        if T1 > 300:
            Prob = ODI_target
        if T1 < 235:
            Prob = ODI_target_2
    if Format.upper() == "T20":
        if T1 >= 180 and T1 < 220:
            Prob = t20_target
        if T1 >= 220:
            Prob = t20_target_extreme
        if T1 <= 135:
            Prob = t20_target_2
    Bowl_Dist = DistBowl(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Batting_Balls = getBalls(6 * Overs, Prob)
    Batting_Balls = SecondBalls(Batting_Balls, T1)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        try:
            Bowling_Perf[Keys[i]].extend(D[Keys[i]])
        except:
            Bowling_Perf[Keys[i]] = D[Keys[i]]

    print(100 * "-")
    print(Name_2)
    print(100 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            Batting_Score_2[Team_2[i]] = 0
            Batting_Sheet[Team_2[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))))
            Batting_Score_2[Team_2[i]] = sum(A)
            Batting_Sheet[Team_2[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_2[i] + (25 - len(Team_2[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))))
            Batting_Score_2[Team_2[i]] = Runs
            Batting_Sheet[Team_2[i]] = A
    print(100 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100 * "-")
    Total = 0
    Balls = 0
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy}))
    T2 = total(Batting_Balls)
    B2 = len(Batting_Balls)
    print(" ")
    Winner = None
    if T1 > T2:
        print(Name_1 + " wins by " + str(T1 - T2) + " runs.")
        Winner = Name_1
    if T1 == T2:
        print("It's a draw!!!")
        Winner = None
    if T1 < T2:
        print(Name_2 + " wins by " + str(10 - Batting_Balls.count(5)) + " wickets.")
        Winner = Name_2
    print("")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        print(" ")
    NRR_Dict = {}
    NRR_Dict[Name_1] = [T1, B1]
    if Winner == Name_1:
        NRR_Dict[Name_2] = [T2, B1]
    else:
        NRR_Dict[Name_2] = [T2, B2]
    return Winner, Batting_Score_1, Batting_Score_2, Batting_Sheet, Bowling_Perf, NRR_Dict

#Format = input("Format : ").upper()
#MatchLimitedOne("A", A_Team, A_Bowl, "B", B_Team, B_Bowl, Format)

def MatchTestOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2):
    Batting_Score_1 = {}
    Batting_Score_2 = {}
    Batting_Score_3 = {}
    Batting_Score_4 = {}
    Batting_Sheet = {}
#    Bowling_Perf = {}
    Bowling_1 = {}
    Bowling_2 = {}
    Bowling_3 = {}
    Bowling_4 = {}
    Prob = Tests
    t = input(Name_1 + "'s Call : ")
    if t.upper() == Toss():
        T1 = input(Name_1 + " chooses to : ").upper()
        while (T1.upper() not in ["BAT", "BOWL"]):
            T1 = input(Name_1 + " chooses to : ").upper()
        if T1 == "BOWL":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
    else:
        T2 = input(Name_2 + " chooses to : ").upper()
        while (T2.upper() not in ["BAT", "BOWL"]):
            T2 = input(Name_2 + " chooses to : ").upper()
        if T2 == "BAT":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3


    ### First Innings
    # Bowling Team Distribution
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls)//6 + 2
    Bowl_Dist = DistBowlTest(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)
    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_1[Keys[i]] = D[Keys[i]]

    print(100*"-")
    print(Name_1)
    print(100*"-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            Batting_Score_1[Team_1[i]] = 0
            Batting_Sheet[Team_1[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A)/float(len(A)))))
            Batting_Score_1[Team_1[i]] = sum(A)
            Batting_Sheet[Team_1[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_1[i] + (25 - len(Team_1[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs/float(Balls))))
            Batting_Score_1[Team_1[i]] = Runs
            Batting_Sheet[Team_1[i]] = A
    print(100 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100*"-")
    T1 = total(Batting_Balls)
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)

    print(pd.DataFrame({"Name" : Name, "Overs" : Over, "Runs" : Runs, "Wickets" : Wickets, "Economy" : Economy}))
    print(" ")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        print("")
    X = input("Continue ? : ")
    print(" ")

    ### Second Innings
    # Bowling Team Distribution
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls)//6 + 2
    Bowl_Dist = DistBowlTest(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_2[Keys[i]] = D[Keys[i]]
    print(100 * "-")
    print(Name_2)
    print(100 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            Batting_Score_2[Team_2[i]] = 0
            Batting_Sheet[Team_2[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))))
            Batting_Score_2[Team_2[i]] = sum(A)
            Batting_Sheet[Team_2[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_2[i] + (25 - len(Team_2[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))))
            Batting_Score_2[Team_2[i]] = Runs
            Batting_Sheet[Team_2[i]] = A
    print(100 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100 * "-")
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy}))
    T2 = total(Batting_Balls)
    print("")
    if T1 > T2:
        print(Name_1 + " leads by " + str(T1 - T2) + " runs.")
    if T1 < T2:
        print(Name_2 + " leads by " + str(T2 - T1) + " runs.")
    if T1 == T2:
        print("Scores are level.")
    print("")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    Total = 0
    Balls = 0
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
    print(" ")
    X = input("Continue ? : ").upper()
    # Third Innings
    print(" ")
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls) // 6 + 2
    Bowl_Dist = DistBowlTest(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_3[Keys[i]] = D[Keys[i]]

    print(100 * "-")
    print(Name_1)
    print(100 * "-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            try:
                Batting_Sheet[Team_1[i]].extend([])
            except:
                Batting_Sheet[Team_1[i]] = []
            Batting_Score_3[Team_1[i]] = 0
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (49 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))))
            try:
                Batting_Sheet[Team_1[i]].extend(A)
            except:
                Batting_Sheet[Team_1[i]] = A
            Batting_Score_3[Team_1[i]] = sum(A)
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_1[i] + (25 - len(Team_1[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))))
            try:
                Batting_Sheet[Team_1[i]].extend(A)
            except:
                Batting_Sheet[Team_1[i]] = A
            Batting_Score_3[Team_1[i]] = Runs

    print(100 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100 * "-")
    T3 = total(Batting_Balls)
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)
    print(pd.DataFrame({"Name": Name, "Overs": Over, "Runs": Runs, "Wickets": Wickets, "Economy": Economy}))
    print(" ")
    if T1 + T3 < T2:
        print(Name_2 + " wins the match by an innings and " + str(T2 - T1 - T3) + " runs.")
    else:
        print("Target for " + Name_2 + " - " + str(T1 + T3 - T2 + 1) + " runs.")
    if T1 + T3 >= T2:
        print(" ")
        Y = input("Fall of Wickets ? : ").upper()
        print("")
        if Y != "N":
            print(60 * "-")
            print("Fall of Wickets")
            print(60 * "-")
            for i in range(len(FOW)):
               K = FOW[i + 1]
               Total += K[1]
               Balls += K[2]
               S = str(Total) + "/" + str(i + 1)
               print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
            print(60 * "-")
    if T1 + T3 < T2:
        Impact_Points = {}
        for i in range(0, len(Team_1)):
            Impact_Points[Team_1[i]] = 0
            try:
                Impact_Points[Team_1[i]] += Batting_Score_1[Team_1[i]]
                if Batting_Score_1[Team_1[i]] >= 100:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5
            try:
                Impact_Points[Team_1[i]] += Batting_Score_3[Team_1[i]]
                if Batting_Score_3[Team_1[i]] >= 100:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_2[Team_1[i]]
                Impact_Points[Team_1[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5

        for i in range(0, len(Team_2)):
            Impact_Points[Team_2[i]] = 50
            try:
                Impact_Points[Team_2[i]] += Batting_Score_2[Team_2[i]]
                if Batting_Score_2[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                Impact_Points[Team_2[i]] += Batting_Score_4[Team_2[i]]
                if Batting_Score_4[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_1[Team_2[i]]
                Impact_Points[Team_2[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_3[Team_2[i]]
                Impact_Points[Team_2[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        if Impact_Sorted[0] in Team_1:
            print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_1 + ")")
        else:
            print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_2 + ")")
        print("")
        if Impact_Sorted[-1] in Team_1:
            print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
        else:
            print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
        print("")
        Y = input("Fall of Wickets ? : ").upper()
        print("")
        if Y != "N":
            print(60 * "-")
            print("Fall of Wickets")
            print(60 * "-")
            for i in range(len(FOW)):
                K = FOW[i + 1]
                Total += K[1]
                Balls += K[2]
                S = str(Total) + "/" + str(i + 1)
                print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        return Name_2, Batting_Score_1, Batting_Score_2, Batting_Score_3, Batting_Score_4, Batting_Sheet, Bowling_1, Bowling_2, Bowling_3, Bowling_4, {Name_1 : [T1 + T3, 20], Name_2 : [T2, 10]}
    X = input("Continue ? : ")
    print(" ")
    # Fourth Innings
    Batting_Balls = getBallsTest(Prob)
    Batting_Balls = SecondBalls(Batting_Balls, T1 + T3 - T2)
    Overs = len(Batting_Balls) // 6 + 2
    Bowl_Dist = DistBowlTest(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        Bowling_4[Keys[i]] = D[Keys[i]]

    print(100 * "-")
    print(Name_2)
    print(100 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-"))
            try:
                Batting_Sheet[Team_2[i]].extend([])
            except:
                Batting_Sheet[Team_2[i]] = []
            Batting_Score_4[Team_2[i]] = 0
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (49 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))))
            try:
                Batting_Sheet[Team_2[i]].extend(A)
            except:
                Batting_Sheet[Team_2[i]] = A
            Batting_Score_4[Team_2[i]] = sum(A)

        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = A[-1]
            print(Team_2[i] + (25 - len(Team_2[i])) * " " + W + (25 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))))
            try:
                Batting_Sheet[Team_2[i]].extend(A)
            except:
                Batting_Sheet[Team_2[i]] = A
            Batting_Score_4[Team_2[i]] = Runs
    print(100 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(100 * "-")
    Total = 0
    Balls = 0
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy}))
    T4 = total(Batting_Balls)
    print("")
    Winner = None
    if T1 + T3 > T2 + T4:
        print(Name_1 + " wins by " + str(T1 + T3 - T2 - T4) + " runs.")
        Winner = Name_1
    if T1 + T3 < T2 + T4:
        if Batting_Balls.count(5) != 9:
            print(Name_2 + " wins by " + str(10 - Batting_Balls.count(5)) + " wickets.")
            Winner = Name_2
        else:
            print(Name_2 + " wins by 1 wicket.")
            Winner = Name_2
    if T1 + T3 == T2 + T4:
        print("It is a tie!")
        Winner = None

    Impact_Points = {}
    for i in range(0, len(Team_1)):
        if Winner == Name_1:
            Impact_Points[Team_1[i]] = 50
        else:
            Impact_Points[Team_1[i]] = 0
        try:
            Impact_Points[Team_1[i]] += Batting_Score_1[Team_1[i]]
            if Batting_Score_1[Team_1[i]] >= 100:
                Impact_Points[Team_1[i]] += 25
        except:
            x = 5
        try:
            Impact_Points[Team_1[i]] += Batting_Score_3[Team_1[i]]
            if Batting_Score_3[Team_1[i]] >= 100:
                Impact_Points[Team_1[i]] += 25
        except:
            x = 5
        try:
            A = Bowling_2[Team_1[i]]
            Impact_Points[Team_1[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_1[i]] += 5*A.count(5)
        except:
            x = 5
        try:
            A = Bowling_4[Team_1[i]]
            Impact_Points[Team_1[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_1[i]] += 5*A.count(5)
        except:
            x = 5

    for i in range(0, len(Team_2)):
        if Winner == Name_2:
            Impact_Points[Team_2[i]] = 50
        else:
            Impact_Points[Team_2[i]] = 0
        try:
            Impact_Points[Team_2[i]] += Batting_Score_2[Team_2[i]]
            if Batting_Score_2[Team_2[i]] >= 100:
                Impact_Points[Team_2[i]] += 25
        except:
            x = 5
        try:
            Impact_Points[Team_2[i]] += Batting_Score_4[Team_2[i]]
            if Batting_Score_4[Team_2[i]] >= 100:
                Impact_Points[Team_2[i]] += 25
        except:
            x = 5
        try:
            A = Bowling_1[Team_2[i]]
            Impact_Points[Team_2[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_2[i]] += 5*A.count(5)
        except:
            x = 5
        try:
            A = Bowling_3[Team_2[i]]
            Impact_Points[Team_2[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_2[i]] += 5*A.count(5)
        except:
            x = 5
    Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
    Impact_Sorted = list(Impact_Sorted_Dict.keys())
    print("")
    if Impact_Sorted[0] in Team_1:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_1 + ")")
    else:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_2 + ")")
    print("")
    if Impact_Sorted[-1] in Team_1:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
    else:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_2 + ")")

    print("")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
    print(" ")
    return Winner, Batting_Score_1, Batting_Score_2, Batting_Score_3, Batting_Score_4, Batting_Sheet, Bowling_1, Bowling_2, Bowling_3, Bowling_4, {Name_1 : [T1 + T3, 20], Name_2 : [T2 + T4, 10 + Batting_Balls.count(5)]}

#Format = input("Format ? : ").upper()
#MatchLimitedOne("Australia", AustraliaT20.split(","), AUST20Bowl, "Dahlia", DahliaXI.split(","), DahliaBowl, Format)
#MatchTestOne("Australia", AustraliaTest.split(","), AUSTestBowl, "Dahlia", DahliaXI.split(","), DahliaBowl)

def Series():
    P = input("Pre Defined or Custom ? ").upper()
    Name_1 = None
    Team_1 = None
    Bowl_1 = None
    Name_2 = None
    Team_2 = None
    Bowl_2 = None
    if P == "C":
        Name_2 = input("Home Team Name : ").upper()
        Team_2 = input("Home Team : ").split(",")
        Bowl_2 = input("Home Team Bowling : ").split(",")
        for i in range(len(Bowl_2)):
            Bowl_2[i] = float(Bowl_2[i])

        Name_1 = input("Visiting Team Name : ").upper()
        Team_1 = input("Visiting Team : ").split(",")
        Bowl_1 = input("Visiting Team Bowling : ").split(",")
        for i in range(len(Bowl_1)):
            Bowl_1[i] = float(Bowl_1[i])

    if P == "P":
        Name_2 = input("Home Team Name : ").upper()
        pos = t.index(Name_2)
        Team_2 = Teams[pos].split(",")
        Bowl_2 = TeamBowl[pos]

        Name_1 = input("Visiting Team Name : ").upper()
        pos = t.index(Name_1)
        Team_1 = Teams[pos].split(",")
        Bowl_1 = TeamBowl[pos]

    Format = input("Format : ").upper()
    Number = int(input("Number of matches : "))
    Score = {Name_1 : 0, Name_2 : 0}
    BattingSheet = {}
    BattingScores = {}
    BowlingStats = {}
    Figures_Bowl = {}
    if Format == "TEST":
        Impact_Points = {}
        for i in range(len(Team_1)):
            Impact_Points[Team_1[i]] = 0
        for i in range(len(Team_2)):
            Impact_Points[Team_2[i]] = 0
        for i in range(Number - 1):
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2)
            for x in BF1.keys():
                A = BF1[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i + 1) + "_" + str(1)] = Figure
                Impact_Points[x] += 20*A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF2.keys():
                A = BF2[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(2)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF3.keys():
                A = BF3[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(3)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF4.keys():
                A = BF4[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(4)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BSco1.keys():
                A = BSco1[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(1)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                A = BSco2[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(2)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                A = BSco3[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(3)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                A = BSco4[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(4)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            if W != None:
                Score[W] += 1
            print("")
            seriesGoing(Score)
            print(" ")
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
 #           BattingScores = mergeDict_i(BattingScores, BSco, i + 1)
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
        W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2)
        for x in BF1.keys():
            A = BF1[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(1)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF2.keys():
            A = BF2[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(2)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF3.keys():
            A = BF3[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(3)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF4.keys():
            A = BF4[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(4)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BSco1.keys():
            A = BSco1[x]
            BattingScores[x + "_" + str(Number) + "_" + str(1)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco2.keys():
            A = BSco2[x]
            BattingScores[x + "_" + str(Number) + "_" + str(2)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco3.keys():
            A = BSco3[x]
            BattingScores[x + "_" + str(Number) + "_" + str(3)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco4.keys():
            A = BSco4[x]
            BattingScores[x + "_" + str(Number) + "_" + str(4)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        if W != None:
            Score[W] += 1
        if Score[Name_1] > Score[Name_2]:
            for i in range(len(Team_1)):
                Impact_Points[Team_1[i]] += 100
        if Score[Name_2] > Score[Name_1]:
            for i in range(len(Team_2)):
                Impact_Points[Team_2[i]] += 100

        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        if Impact_Sorted[0] in Team_1:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_1 + ")")
        else:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_2 + ")")
        print("")
        if Impact_Sorted[-1] in Team_1:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
        else:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
        print("")
        seriesOutput(Score)
        print(" ")
        BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
        BattingSheet = mergeDict(BattingSheet, BShe)
        BowlingStats = mergeDict(BowlingStats, BF)
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
#        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets >= 1.5 * Number:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print(" ")
        print(40*"*")
        print("BATTERS")
        print(40*"*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighest(BattingScores, cut = 10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print(40*"*")
        print("BOWLERS")
        print(40*"*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse = False)
        print(" ")
        print("Best Figures - ")
        showFigures(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

    else:
        for i in range(Number - 1):
            W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2, Format)
            if W != None:
                Score[W] += 1
            print("")
            seriesGoing(Score)
            print(" ")
            for x in BF.keys():
                A = BF[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5*A.count(5))
                Figures_Bowl[x + "_" + str(i + 1)] = Figure
            for x in BSco_1.keys():
                A = BSco_1[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(1)] = A
            for x in BSco_2.keys():
                A = BSco_2[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(2)] = A
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
        W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(Name_1, Team_1, Bowl_1, Name_2, Team_2, Bowl_2, Format)
        for x in BF.keys():
            A = BF[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number)] = Figure
        for x in BSco_1.keys():
            A = BSco_1[x]
            BattingScores[x + "_" + str(Number) + "_" + str(1)] = A
        for x in BSco_2.keys():
            A = BSco_2[x]
            BattingScores[x + "_" + str(Number) + "_" + str(2)] = A
        if W != None:
            Score[W] += 1
        print("")
        seriesOutput(Score)
        print(" ")
 #       BattingScores = mergeDict_i(BattingScores, BSco, Number)
        BattingSheet = mergeDict(BattingSheet, BShe)
        BowlingStats = mergeDict(BowlingStats, BF)
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
#        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets >= 0.75 * Number:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighest(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFigures(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

#Series()

def Tournament():
    N_Teams = input("Teams playing the Tournament : ").upper().split(",")
    IndexArray = [t.index(N_Teams[i]) for i in range(len(N_Teams))]
    MatchOrder = Combinations(IndexArray)
    Format = input("Format : ").upper()
    PointsTable = pd.DataFrame({"Teams" : N_Teams, "Matches" : np.zeros(len(N_Teams)), "Won" : np.zeros(len(N_Teams)), "Lost" : np.zeros(len(N_Teams)), "Draw" : np.zeros(len(N_Teams)), "Points" : np.zeros(len(N_Teams)), "NRR" : np.zeros(len(N_Teams)), "Runs Scored" : np.zeros(len(N_Teams)), "Runs Conceded" : np.zeros(len(N_Teams)), "Balls Bowled" : np.zeros(len(N_Teams)), "Balls Played" : np.zeros(len(N_Teams)), "Wickets Taken" : np.zeros(len(N_Teams)), "Wickets Lost" : np.zeros(len(N_Teams))})
    PointsTable['Matches'] = PointsTable['Matches'].astype(int)
    PointsTable['Won'] = PointsTable['Won'].astype(int)
    PointsTable['Lost'] = PointsTable['Lost'].astype(int)
    PointsTable['Draw'] = PointsTable['Draw'].astype(int)
    PointsTable['Points'] = PointsTable['Points'].astype(int)
    PointsTable['Wickets Taken'] = PointsTable['Wickets Taken'].astype(int)
    PointsTable['Wickets Lost'] = PointsTable['Wickets Lost'].astype(int)
    BattingSheet = {}
    BattingScores = {}
    BowlingStats = {}
    Figures_Bowl = {}
    print("")
    print("Fixture - ")
    for i in range(len(MatchOrder)):
        A = MatchOrder[i]
        print("Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - " + t[A[0]] + " vs " + t[A[1]])
    print("")
    print("Points Table")
    print(PointsTable.loc[:, "Teams":"NRR"])
    print("")
    if Format.upper() != "TEST":
        for i in range(len(MatchOrder)):
            A = MatchOrder[i]
            print("Next Match" + " - " + "Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - "+ t[A[0]] + " vs " + t[A[1]])
            print("")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, BShe, BF, NRR_Dict = MatchLimitedOne(t[A[0]], Teams[A[0]].split(","), TeamBowl[A[0]], t[A[1]], Teams[A[1]].split(","), TeamBowl[A[1]], Format)
            i1 = np.where(PointsTable["Teams"] == t[A[0]])[0][0]
            i2 = np.where(PointsTable["Teams"] == t[A[1]])[0][0]
            PointsTable.loc[i1, "Runs Scored"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i1, "Runs Conceded"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i1, "Balls Bowled"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i1, "Balls Played"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i1, "NRR"] = 6 * (PointsTable.loc[i1, "Runs Scored"]/PointsTable.loc[i1, "Balls Played"] - PointsTable.loc[i1, "Runs Conceded"]/PointsTable.loc[i1, "Balls Bowled"])
            PointsTable.loc[i1, "Matches"] += 1
            PointsTable.loc[i2, "Runs Scored"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i2, "Runs Conceded"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i2, "Balls Bowled"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i2, "Balls Played"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i2, "NRR"] = 6 * (PointsTable.loc[i2, "Runs Scored"] / PointsTable.loc[i2, "Balls Played"] - PointsTable.loc[i2, "Runs Conceded"] / PointsTable.loc[i2, "Balls Bowled"])
            PointsTable.loc[i2, "Matches"] += 1
            if W == None:
                PointsTable.loc[i1, "Draw"] += 1
                PointsTable.loc[i2, "Draw"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            if W == t[A[0]]:
                PointsTable.loc[i1, "Won"] += 1
                PointsTable.loc[i2, "Lost"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
            if W == t[A[1]]:
                PointsTable.loc[i1, "Lost"] += 1
                PointsTable.loc[i2, "Won"] += 1
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam] = K
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            PointsTable = PointsTable.sort_values(by=['Points', 'NRR'], ascending=[False, False]).reset_index().iloc[:, 1:]
            print("Points Table")
            print(PointsTable.loc[:, "Teams":"NRR"])
            print("")
        if len(N_Teams) < 5:
            FinalNames = list(PointsTable.loc[[0, 1], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam] = K
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the Tournament!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the Tournament")
            print("")
        else:
            FinalNames = list(PointsTable.loc[[0, 1, 2, 3], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("SEMI FINAL 1 - " + FinalNames[0] + " vs " + FinalNames[3])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[3]], Teams[FinalIndexArray[3]].split(","), TeamBowl[FinalIndexArray[3]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam] = K
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W1 = None
            if W != None:
                print(W + " advances to the Finals.")
                W1 = W
            else:
                print(FinalNames[0] + " advances to the Finals.")
                W1 = FinalNames[0]
            print("")
            print(40 * "-")
            print("SEMI FINAL 2 - " + FinalNames[1] + " vs " + FinalNames[2])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], t[FinalIndexArray[2]], Teams[FinalIndexArray[2]].split(","), TeamBowl[FinalIndexArray[2]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam] = K
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W2 = None
            if W != None:
                print(W + " advances to the Finals.")
                W2 = W
            else:
                print(FinalNames[1] + " advances to the Finals.")
                W2 = FinalNames[1]
            print("")
            FinalNames = [W1, W2]
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40 * "-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam] = K
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the Tournament!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the Tournament")
            print("")
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
        #        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighestTournament(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFiguresTournament(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")
    else:
        Impact_Points = {}
        for i in range(len(MatchOrder)):
            A = MatchOrder[i]
            print("Next Match" + " - " + "Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - "+ t[A[0]] + " vs " + t[A[1]])
            print("")
            K = input("Continue ? ")
            print(" ")
            for i in range(len(Teams[A[0]].split(","))):
                try:
                    x = Impact_Points[Teams[A[0]].split(",")[i]]
                except:
                    Impact_Points[Teams[A[0]].split(",")[i]] = 0
            for i in range(len(Teams[A[1]].split(","))):
                try:
                    x = Impact_Points[Teams[A[1]].split(",")[i]]
                except:
                    Impact_Points[Teams[A[1]].split(",")[i]] = 0
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, NRR_Dict = MatchTestOne(t[A[0]], Teams[A[0]].split(","), TeamBowl[A[0]], t[A[1]], Teams[A[1]].split(","), TeamBowl[A[1]])
            i1 = np.where(PointsTable["Teams"] == t[A[0]])[0][0]
            i2 = np.where(PointsTable["Teams"] == t[A[1]])[0][0]
            PointsTable.loc[i1, "Runs Scored"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i1, "Runs Conceded"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i1, "Wickets Taken"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i1, "Wickets Lost"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i1, "NRR"] = 6 * (PointsTable.loc[i1, "Runs Scored"]/PointsTable.loc[i1, "Wickets Lost"] - PointsTable.loc[i1, "Runs Conceded"]/PointsTable.loc[i1, "Wickets Taken"])
            PointsTable.loc[i1, "Matches"] += 1
            PointsTable.loc[i2, "Runs Scored"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i2, "Runs Conceded"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i2, "Wickets Taken"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i2, "Wickets Lost"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i2, "NRR"] = 6 * (PointsTable.loc[i2, "Runs Scored"] / PointsTable.loc[i2, "Wickets Lost"] - PointsTable.loc[i2, "Runs Conceded"] / PointsTable.loc[i2, "Wickets Taken"])
            PointsTable.loc[i2, "Matches"] += 1

            if W == None:
                PointsTable.loc[i1, "Draw"] += 1
                PointsTable.loc[i2, "Draw"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            if W == t[A[0]]:
                PointsTable.loc[i1, "Won"] += 1
                PointsTable.loc[i2, "Lost"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
            if W == t[A[1]]:
                PointsTable.loc[i1, "Lost"] += 1
                PointsTable.loc[i2, "Won"] += 1
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
 #           BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco1[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco2[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco3[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco4[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            PointsTable = PointsTable.sort_values(by=['Points', 'NRR'], ascending=[False, False]).reset_index().iloc[:, 1:]
            print("Points Table")
            print(PointsTable.loc[:, "Teams":"NRR"])
            print("")
        if len(N_Teams) < 5:
            FinalNames = list(PointsTable.loc[[0, 1], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]])
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Finals_"+ HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)

            if W != None:
                print(W + " wins the Tournament!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the Tournament")
            print("")
        else:
            FinalNames = list(PointsTable.loc[[0, 1, 2, 3], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("SEMI FINAL 1 - " + FinalNames[0] + " vs " + FinalNames[3])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[3]], Teams[FinalIndexArray[3]].split(","), TeamBowl[FinalIndexArray[3]])
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W1 = None
            if W != None:
                print(W + " advances to the Finals.")
                W1 = W
            else:
                print(FinalNames[0] + " advances to the Finals.")
                W1 = FinalNames[0]
            print("")
            print(40 * "-")
            print("SEMI FINAL 2 - " + FinalNames[1] + " vs " + FinalNames[2])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], t[FinalIndexArray[2]], Teams[FinalIndexArray[2]].split(","), TeamBowl[FinalIndexArray[2]])
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco1[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco2[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco3[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco4[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W2 = None
            if W != None:
                print(W + " advances to the Finals.")
                W2 = W
            else:
                print(FinalNames[1] + " advances to the Finals.")
                W2 = FinalNames[1]
            print("")
            FinalNames = [W1, W2]
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40 * "-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]])
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the Tournament!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the Tournament")
            print("")
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
        #        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        print("")
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        Team_0 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[0] in Teams[IndexArray[i]].split(","):
                Team_0 = t[IndexArray[i]]
        print("Player of the Tournament - " + Impact_Sorted[0] + " (" + Team_0 + ")")
        print("")

        Team_1 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[-1] in Teams[IndexArray[i]].split(","):
                Team_1 = t[IndexArray[i]]
        print("Flog of the Tournament - " + Impact_Sorted[-1] + " (" + Team_1 + ")")
        print("")

        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print("")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighestTournamentTest(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFiguresTournamentTest(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

def cricket():
    ST = input("Series/Tournament : ").upper()
    while ST not in ["S", "T"]:
        ST = input("Series/Tournament : ").upper()
    if ST == "S":
        Series()
    if ST == "T":
        Tournament()

cricket()
