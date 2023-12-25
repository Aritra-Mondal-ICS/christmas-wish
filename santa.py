# santa_1.py
# This is the code for Day 1 of "12 Days of Python",
# by the authors of "Hello World! Computer Programming for Kids and Other Beginners".
import pygame, sys
pygame.init()
pygame.display.set_caption("12 Days of Python")
screen = pygame.display.set_mode((640,480))
santa = pygame.surface.Surface((640,480))
screen.fill((0,0,0))
#---L ARM DRAW
pygame.draw.polygon(santa,(255,0,0),((274,207),(264,197),(243,182),(226,168),
(215,154),(212,153),(206,158),(192,155),(183,157),
(182,172),(204,190),(219,208),(244,231),(261,245))) #arm n hand
pygame.draw.polygon(santa, (255,255,255),((243,182),(242,176),(231,167),
(226,168),(218,181),(204,190),(204,200),(212,208),
(219,208),(232,197))) #arm fur
#---R ARM DRAW
pygame.draw.polygon(santa,(255,0,0),((358,191),(405,202),(428,207),(448,212),
(457,220),(459,226),(457,232),(444,236),(440,243),(421,237),
(399,233),(389,233),(344,236))) #arm n hand
pygame.draw.polygon(santa,(255,255,255),((428,207),(418,197),(406,197),
(407,204),(400,215),(401,237),(421,238),(421,223))) #arm fur
#---L LEG DRAW
pygame.draw.polygon(santa,(255,0,0),((270,323),(268,345),(266,352),(305,361),
(309,352),(317,326),(319,312),(272,306))) #leg
pygame.draw.polygon(santa,(102,68,34),((301,370),(266,361),(247,356),(231,357),
(224,368),(227,380),(245,388),(272,386),(274,390),(295,391))) #boot
pygame.draw.polygon(santa,(255,255,255), ((301,370),(312,355),(303,352),(293,348),
(279,346),(268,342),(263,343),(266,361))) #fur
#---R LEG DRAW
pygame.draw.polygon(santa,(255,0,0),((322,326),(330,352),(331,359),(372,350),
(369,323),(367,311),(316,314))) #leg
pygame.draw.polygon(santa, (102,68,34),((340,369),(373,361),(396,356),(410,359),
(415,375),(400,387),(366,386),(365,392),(347,393),(340,386))) #boot
pygame.draw.polygon(santa,(255,255,255),((373,361),(340,369),(334,368),(326,353),
(345,348),(359,347),(375,343)))
#---BODY DRAW
pygame.draw.polygon(santa, (255,255,255), ((234,289),(226,299),(230,316),
(281,322),(304,327),(317,326),(333,322),(363,324),
(408,304),(410,287),(402,275),(328,208),(281,207))) #vest fur
pygame.draw.polygon(santa, (255,0,0), ((271,188),(245,231),(236,259),(234,272),
(235,287),(241,295),(294,302),(300,298),(304,285),
(298,217))) #vest 1
pygame.draw.polygon(santa, (255,0,0), ((326,235),(328,286),(330,295),(335,300),
(369,297),(401,277),(389,234),(357,192),(334,197))) #vest 2
pygame.draw.circle(santa,(0,0,0),(315,243),4)
pygame.draw.circle(santa,(0,0,0),(314,257),4)
pygame.draw.circle(santa,(0,0,0),(315,274),4)
pygame.draw.circle(santa,(0,0,0),(317,293),4)
#---HEAD DRAW
pygame.draw.polygon(santa, (255,255,255),((278,153),(272,188),
(281,211),(300,232),(315,238),(326,232),(346,215),(357,191),
(351,151),(278,153))) #beard
pygame.draw.polygon(santa, (255, 218, 185),((282,151),(283,166),(309,178),
(315,179),(321,177),(345,166),(346,152),(335,140),(310,133),
(289,141))) #head
pygame.draw.polygon(santa, (255,0,0),((266,139),(278,123),
(293,112),(315,110),(343,115),(312,85),(260,134))) #hat main
pygame.draw.polygon(santa,(255,255,255),((346,152),(335,140),(310,133),
(289,141),(282,151),(270,150),(261,146),(266,139),(278,123),
(293,112),(315,110),(343,115),(357,132))) #hat rim
pygame.draw.circle(santa,(255,255,255),(255,149),15) #hat ball
pygame.draw.circle(santa,( 50, 50, 50),(307,151),3) #eye
pygame.draw.circle(santa,( 50, 50, 50),(319,151),3) #eye
pygame.draw.polygon(santa,(255,255,255),((310,140),(301,141),(294,145),(294,149),
(303,145),(309,144))) #eyebrow
pygame.draw.polygon(santa,(255,255,255),((315,146),(324,146),(330,150),(331,146),
(326,142),(317,140))) #eyebrow
pygame.draw.polygon(santa,(255,255,255),((283,167),(287,177),(296,182),(311,176),
(305,169),)) #mustachelet
pygame.draw.polygon(santa,(255,255,255),((344,168),(323,166),(319,176),(336,178))) #mustachelet
pygame.draw.lines(santa, (0,0,0), False, ((307,165),(307,169),(310,173),(321,171),(322,164)),2) #nose
screen.blit(santa, (0,0))
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()