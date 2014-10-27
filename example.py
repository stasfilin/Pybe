__author__ = 'Stas Filin'
#Github: https://github.com/stasfilin/Pybe
#LinkedIN: https://www.linkedin.com/in/stasfilin
from Pybe.Youtube import Youtube

y = Youtube("useyourname@gmail.com", "useyourpassword") #Use Youtube


if y.login(): #Login to your account
    print "Login"
else:
    print "Not Login"
if y.like("https://www.youtube.com/watch?v=MP7c2dSv2ag"): #Like video
    print "Like"
else:
    print "Error"
y.stop() #Stop web browser