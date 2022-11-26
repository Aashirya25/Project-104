import cv2
image = cv2.imread("solar-system.png")
#cv2.imshow("output",image)
#cv2.waitKey(0)

comet_image = cv2.imread("comet.png")
comet = comet_image[175:235,40:218]
#comet_image[100:160,60:238] = comet
image[100:160,60:238] = comet


font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_DUPLEX
font3 = cv2.FONT_HERSHEY_COMPLEX
font4 = cv2.FONT_HERSHEY_TRIPLEX
font5 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font6 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(image,"Comet",(80,200),font1,1,(199,17,163),2)
cv2.putText(image,"Sun",(50,480),font2,1,(255,255,255),3)
cv2.putText(image,"Mercury",(200,460),font3,0.8,(173,145,248),2)
cv2.putText(image,"Venus",(270,430),font4,1,(125,184,253),2)
cv2.putText(image,"Earth",(340,385),font5,1,(49,196,206),1)
cv2.putText(image,"Moon",(305,305),font6,0.5,(255,255,255),1)
cv2.putText(image,"Mars",(390,335),font6,0.5,(49,206,140),1)
cv2.putText(image,"Jupiter",(530,305),font1,1,(237,181,177),2)
cv2.putText(image,"Saturn",(680,245),font2,1,(206,59,49),2)
cv2.putText(image,"Uranus",(750,175),font3,1,(236,147,194),2)
cv2.putText(image,"Neptune",(825,125),font4,0.5,(201,180,255),2)
cv2.putText(image,"Pluto",(870,65),font5,0.8,(255,255,255),2)



cv2.imshow("output",image)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithlabel.jpg",image)