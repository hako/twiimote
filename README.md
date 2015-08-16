![](https://pbs.twimg.com/media/BBCxQoPCAAE7gSW.gif)

#twiimote


a wiimote to twitter thingy.
by Wesley Hill (@hakobyte)

twiimote is a small toy program that **'connects your wiimote to twitter'.**
it's as simple as that.

Real reason: **I wrote this application just for fun because I was bored due to A Level revision/exams :/**

![](http://www.hakobaito.co.uk/content/twiimote_1376196174_sd.png)

![](http://www.hakobaito.co.uk/content/vHD3l6WvgOHtXUYho0S7t0ixzGMYzU9owcbuTY8EiAtDO1bWFu5GpPpBcLnekwL.gif)

Media:
===============
asciicast:
https://asciinema.org/a/4572

youtube:
http://www.youtube.com/watch?v=KMEmvo1dbgg

#Requirements

You're gonna need some stuff in order to get
twiimote up and running:

+ **Bluetooth/adapter**

+ **A Nintendo Wiimote RVL-CNT-01**

	+ _The motionplus version of the wiimote (Nintendo RVL-CNT-01-TR) reportedly works through the 'sync' button. But it's not been tested._

+ **Linux or a VM.** [Virtualbox](https://www.virtualbox.org) (for windows and mac users)


Install
===============

twiimote requires ```python-cwiid``` and ```python-bluez``` ```bluez``` & obviously ```pip```

    sudo apt-get install python-cwiid python-bluez bluez

then:

    sudo pip install twiimote

**keep in mind twiimote only works on GNU/Linux.**

**not mac or windows.**

Usage
===============
open a terminal and launch:

	twiimote 

that's it!

<br />

When inside twiimote press these buttons to navigate.
                                                                          
Home = Home Timeline - press Home to exit  

1 = List @Mentions 
          
2 = List DM's    
                 
A = ?????        

B = Hashtag tracking. - press Home to exit.

Minus = Exit 

Problem?
===============
twiimote not behaving itself?

contact me on [twitter](https://twitter.com/hakobyte) or by [e-mail](hakobyte@gmail.com) here.

or fork this repo and contribute! :D


Credits
===============
twython by [@ryanmcgrath](https://twitter.com/ryanmcgrath) - _for the awesome twitter api wrapper in python._

colorama by Jonathan Hartley - _for pwetty terminal colours._

[Nintendo](https://nintendo.com) - for the wiimote _duh._


License
===============
twiimote is **free** software.

twiimote is licensed under the [MIT license](http://opensource.org/licenses/MIT)

=[],

 > _munchi says thanks, for using this software, knowing that you will do **good** with it._	

[http://hakobaito.co.uk](http://hakobaito.co.uk)


[http://hakob.yt/e/twiimote](http://hakob.yt/e/twiimote)
