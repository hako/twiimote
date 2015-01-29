#!/usr/bin/python
#coding: UTF-8
#-------------------------------------------------
#
#       The MIT License (MIT)
#
#       Copyright (c) 2013  Wesley Hill (hakobyte)
#
#       Permission is hereby granted, free of charge, to any person obtaining a copy
#       of this software and associated documentation files (the "Software"), to deal
#       in the Software without restriction, including without limitation the rights
#       to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#       copies of the Software, and to permit persons to whom the Software is
#       furnished to do so, subject to the following conditions:
#       
#       The above copyright notice and this permission notice shall be included in
#       all copies or substantial portions of the Software.
#
#       THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#       IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#       FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#       AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#       LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#       OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#       THE SOFTWARE.
#
#
#
#       ░▀█▀░█░█░▀█▀░▀█▀░█▄█░█▀█░▀█▀░█▀▀
#       ░░█░░█▄█░░█░░░█░░█░█░█░█░░█░░█▀▀
#       ░░▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀
#
#       __INIT__.PY
#
#       Version 1.7.1
#
#       [C] WESLEY HILL 2013
#
#       HTTP://WWW.HAKOBAITO.CO.UK
#
#       HTTP://HAKOB.YT/E/TWIIMOTE
#
#--------------------------------------------------


import base64
import colorama
import cwiid
import sys
import os
import json
import time
import twiimotelogo
import twython
import twiimotesession

colorama.initialise.init()

textcolour = colorama.ansi.Fore

class HashtagStream(twython.streaming.api.TwythonStreamer):

    """twiimote's hashtag tracking/streaming class"""

    def on_success(self, data):
        if (tm.state['buttons'] & cwiid.BTN_HOME):
            self.disconnect()

        if not (tm.state['buttons'] & cwiid.BTN_HOME):
            try:
                if 'text' in data:
                    print textcolour.CYAN + colorama.ansi.Style.NORMAL
                    print textcolour.WHITE + colorama.ansi.Back.BLUE + colorama.ansi.Style.BRIGHT + '@' + data['user']['screen_name'].encode('utf-8') + colorama.ansi.Style.RESET_ALL
                    print data['text'].encode('utf-8')
                    print textcolour.MAGENTA + colorama.ansi.Style.NORMAL + "@" + data['created_at'] + colorama.ansi.Style.RESET_ALL
                    tm.rumble = 1
                    time.sleep(.1)
                    tm.rumble = 0
                    tm.led = 15
                    time.sleep(.1)
                    tm.led = 0

            except twython.TwythonError:
                tm.close()
                print "wiimote disconnected from twitter."

    def on_error(self, status_code, data):
        print "error:"
        print status_code
        self.disconnect()

    def on_timeout(self, data):
        print "timeout."
        print "wiimote disconnected from twitter."
        self.disconnect()

    def on_disconnect(self, data):
        print "wiimote disconnected from twitter."
        self.disconnect()


class Home(twython.streaming.api.TwythonStreamer):

    """twiimote's home timeline streaming class"""

    def on_success(self, data):

        if (tm.state['buttons'] & cwiid.BTN_HOME):
            self.disconnect()

        if not (tm.state['buttons'] & cwiid.BTN_HOME):
            try:
                if 'text' in data:
                    print textcolour.CYAN + colorama.ansi.Style.NORMAL
                    print textcolour.WHITE + colorama.ansi.Back.BLUE + colorama.ansi.Style.BRIGHT + '@' + data['user']['screen_name'].encode('utf-8') + colorama.ansi.Style.RESET_ALL
                    print data['text'].encode('utf-8')

                    print textcolour.MAGENTA + colorama.ansi.Style.NORMAL + "@" + data['created_at'] + colorama.ansi.Style.RESET_ALL
                    tm.rumble = 1
                    time.sleep(.4)
                    tm.rumble = 0
                    tm.led = 15
                    time.sleep(.1)
                    tm.led = 0

            except twython.TwythonError:
                tm.close()
                print "wiimote disconnected from twitter."

        def on_error(self, status_code, data):
            print "error:"
            print status_code
            self.disconnect()

        def on_timeout(self, data):
            print "timeout."
            print "wiimote disconnected from twitter."
            self.disconnect()

        def on_disconnect(self, data):
            print "wiimote disconnected from twitter."
            self.disconnect()


def main():

    print textcolour.CYAN + colorama.ansi.Style.BRIGHT

    Logo = twiimotelogo.Logo()

    print Logo.Show() + colorama.ansi.Style.RESET_ALL

    print "Scanning for wiimotes... (Press 1 + 2)"

    global tm

    try:
        tm = cwiid.Wiimote()
    except:
        print ":("
        sys.exit()

    else:
        print "wiimote found!"

    tm.rpt_mode = cwiid.RPT_BTN
    tm.led = 15
    tm.rumble = 1
    time.sleep(.6)
    tm.rumble = 0
    tm.led = 0

    # Standby until user holds the A button to connect to Twitter.

    wiimote = twiimotesession.Auth()

    twiimote = twiimotesession.TwiimoteCommands()

    print "Hold 'A' to connect to Twitter."

    # check if auth file exists...

    if os.path.exists("~/.tmtappauthsettings"):
        pass

    while not tm.state['buttons'] & cwiid.BTN_A:

        ledsnum = [1, 2, 4, 8]

        for loop in ledsnum:
            tm.led = loop
            time.sleep(.8)

        if (tm.state['buttons'] & cwiid.BTN_A):
            tm.led = 0
            time.sleep(.8)
            break

        if (tm.state['buttons'] & cwiid.BTN_MINUS):
            tm.led = 0
            tm.close()
            print "wiimote disconnected."
            sys.exit()
    try:
        tm.led = 15
        wiimote.user_authentication()  # authenticate user.

    except twython.exceptions.TwythonError:
        print "Failed to authenticate wiimote :("
        sys.exit(1)

    else:
        tm.led = 0
        time.sleep(.2)
        tm.led = 15
        print textcolour.GREEN + colorama.ansi.Style.BRIGHT + "Connected!"
        print colorama.ansi.Style.RESET_ALL

        twiimote.displayUser()  # display users twitter handle

        tm.rumble = 1
        time.sleep(.2)
        tm.rumble = 0

        # Battery level indicators: 
        # >= 50 = Green = High,  
        # <= 49 = Yellow = Moderate,
        # <= 20 = Red = Low/Abort

        if tm.state['battery'] <= 49:
            print "Battery Level:" + textcolour.YELLOW + colorama.ansi.Style.BRIGHT
            print tm.state['battery'], '%'
        elif tm.state['battery'] >= 50:
            print "Battery Level:" + textcolour.GREEN + colorama.ansi.Style.BRIGHT
            print tm.state['battery'], '%'
        elif tm.state['battery'] <= 20:
            print "Battery Level:" + textcolour.RED + colorama.ansi.Style.BRIGHT
            print tm.state['battery'], '%'
            print "/n"
            tm.close()
            sys.exit(
                "WARNING! wiimote battery is too low! cowardly aborting...")

        print colorama.ansi.Style.RESET_ALL

        print "Menu: \n Home: Home Timeline  \n 1: List mentions \n 2. List DM's \n A: Soon...  \n B: Hashtag tracking. \n - : Exit"

        tm.led = 15
        time.sleep(.2)

        tm.led = 15
        time.sleep(.2)

        tm.led = 0
        time.sleep(.2)

    # twiimote event loop.

    while not tm.state['buttons'] & cwiid.BTN_MINUS:

        ledsnum = [8, 4, 2, 1]

        led = 0

        for loop in ledsnum:
            tm.led = loop
            time.sleep(.8)

        if(tm.state['buttons'] & cwiid.BTN_HOME):

            # Home Timeline - (beta)
            # Streams the users timeline
            # twiimote responds with a vibration.

            try:

                tm.led = 0

                CK_USR = base64.b64decode(twiimotesession.C_KEY)
                CKS_USR = base64.b64decode(twiimotesession.C_SECRET)

                saved_tkns = open(twiimotesession.app_settings, "rb")
                config = json.load(saved_tkns)
                saved_tkns.close()
                
                foa_tk = config[0]
                foa_tks = config[1]

                twmt = Home(CK_USR, CKS_USR, foa_tk, foa_tks, timeout=300)

                print "\n" + "-"
                print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "Home Timeline" + colorama.ansi.Style.RESET_ALL

                # quickly get the home timeline first.

                timeline = twython.api.Twython(
                    CK_USR, CKS_USR, foa_tk, foa_tks)

                user_timeline = reversed(timeline.get_home_timeline())

                for user in user_timeline:

                    print textcolour.WHITE + colorama.ansi.Back.BLUE + colorama.ansi.Style.BRIGHT + '@' + user['user']['screen_name'].encode('utf-8') + colorama.ansi.Style.RESET_ALL
                    print user['text'].encode('utf-8')

                    print textcolour.MAGENTA + colorama.ansi.Style.NORMAL + "@" + user['created_at'] + colorama.ansi.Style.RESET_ALL

                    tm.rumble = 1
                    time.sleep(.1)
                    tm.rumble = 0
                    tm.led = 0
                    tm.led = 1
                    tm.led = 2
                    tm.led = 4
                    tm.led = 8

                    print "\n"

                tm.led = 15
                time.sleep(.1)
                tm.led = 0

                twmt.user()

            except twython.TwythonError:
                print "error."
                sys.exit()

            else:
                print "Ended streaming timeline."
                continue

        if (tm.state['buttons'] & cwiid.BTN_B):

            # Hashtag tracking.
            # Streams a given hashtag on display,
            # twiimote responds with a vibration.

            CK_USR = base64.b64decode(twiimotesession.C_KEY)
            CKS_USR = base64.b64decode(twiimotesession.C_SECRET)

            saved_tkns = open(twiimotesession.app_settings, "rb")
            config = json.load(saved_tkns)
            saved_tkns.close()
                
            foa_tk = config[0]
            foa_tks = config[1]

            try:
                tm.led = 0

                print "\n" + "-"
                print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "Hashtag tracking" + colorama.ansi.Style.RESET_ALL

                twmt = HashtagStream(
                    CK_USR,
                    CKS_USR,
                    foa_tk,
                    foa_tks,
                    timeout=300)

                print "Enter the name of the hashtag. ('lol' will become #lol)"

                print "here's some popular examples:"

                popular = twython.api.Twython(CK_USR, CKS_USR, foa_tk, foa_tks)

                trend_number = 0

                place = popular.get_place_trends(id='1')

                for trends in place:
                    while trend_number <= 5:
                        trend_number += 1

                        print textcolour.WHITE + colorama.ansi.Back.MAGENTA + colorama.ansi.Style.BRIGHT + trends['trends'][trend_number]['name'] + colorama.ansi.Style.RESET_ALL

                    query = '#' + raw_input('#')

                    tm.led = 15
                    time.sleep(.3)
                    tm.led = 0

                    print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "tracking: " + query + colorama.ansi.Style.RESET_ALL

                    twmt.statuses.filter(track=query)

            except twython.TwythonError:
                print "error."
                sys.exit()

            else:
                print "Ended hashtag tracking."
                continue

        if (tm.state['buttons'] & cwiid.BTN_1):

            # Mentions! your twiimote will react when a user mentions you.
            # The user can either list or stream their mentions.

            print "\n" + "-"
            print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "@Mentions" + colorama.ansi.Style.RESET_ALL

            tm.led = 0

            # LISTING MENTIONS

            try:
                count = int(raw_input("Enter an amount of mentions to list:"))

                if count <= 0:
                    sys.exit()
            except:
                print "error. input was either not a number or less than 1."
                sys.exit()

            print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "listing @mentions:" + colorama.ansi.Style.RESET_ALL

            CK_USR = base64.b64decode(twiimotesession.C_KEY)
            CKS_USR = base64.b64decode(twiimotesession.C_SECRET)
            saved_tkns = open(twiimotesession.app_settings, "rb")
            config = json.load(saved_tkns)
            saved_tkns.close()
                
            foa_tk = config[0]
            foa_tks = config[1]

            twmt = twython.api.Twython(CK_USR, CKS_USR, foa_tk, foa_tks)

            mentions = twmt.get_mentions_timeline(
                count=count,
                trim_user="false",
                include_entities="true")

            for tweet in mentions:
                print textcolour.WHITE + colorama.ansi.Back.BLUE + colorama.ansi.Style.BRIGHT + "@" + tweet["user"]["screen_name"].encode('utf-8') + ':' + colorama.ansi.Style.RESET_ALL
                print tweet['text']

                tm.rumble = 1
                time.sleep(.1)
                tm.rumble = 0

                # count each incoming tweet in binary.

                if led <= count:
                    led += 1
                    tm.led = led
                    time.sleep(.1)
                print "\n"

            time.sleep(1)

        elif(tm.state['buttons'] & cwiid.BTN_2):

            # DM's - twiimote will list latest direct messages

            print "\n" + "-"
            print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "Direct Messages" + colorama.ansi.Style.RESET_ALL

            tm.led = 0

            CK_USR = base64.b64decode(twiimotesession.C_KEY)
            CKS_USR = base64.b64decode(twiimotesession.C_SECRET)

            saved_tkns = open(twiimotesession.app_settings, "rb")
            config = json.load(saved_tkns)
            saved_tkns.close()
                
            foa_tk = config[0]
            foa_tks = config[1]

            twmt = twython.api.Twython(CK_USR, CKS_USR, foa_tk, foa_tks)

            try:
                count = int(raw_input("Enter an amount of DM's to list:"))

                if count <= 0:
                    sys.exit()
            except:
                print "error. input was either not a number or less than 1."
                sys.exit()

            print textcolour.WHITE + colorama.ansi.Back.CYAN + colorama.ansi.Style.BRIGHT + "listing DM's:" + colorama.ansi.Style.RESET_ALL

            dm = twmt.get_direct_messages(count=count, skip_status='true')

            for message in dm:
                print message['sender']['name'].encode('utf-8') + ' | ' + textcolour.WHITE + colorama.ansi.Back.BLUE + colorama.ansi.Style.BRIGHT + '@' + message['sender']['screen_name'].encode('utf-8') + colorama.ansi.Style.RESET_ALL
                print message['text'].encode('utf-8') + "\n"
                tm.rumble = 1
                time.sleep(.1)
                tm.rumble = 0

                # count each incoming tweet in binary.

                if led <= count:
                    led += 1
                    tm.led = led
                    time.sleep(.1)

        elif (tm.state['buttons'] & cwiid.BTN_MINUS):
            tm.led = 9
            print "Quitting..."

            # Ask to remove auth file when exiting.

            print "Would you also like to remove your session [Y/n]?"

            while True:
                decide = raw_input()
                if decide not in ['Y', 'y', 'N', 'n']:
                    print "Enter 'Y' or 'N'"
                    continue

                if decide == 'Y' or decide == 'y':
		    tm.led = 0
                    tm.led = 9
                    time.sleep(.3)
                    tm.led = 0
                    os.remove(twiimotesession.app_settings)
                    print "Successfully removed session!"
                    print "wiimote disconnected."
                    tm.close()
                    sys.exit()
                    return True

                if decide == 'N' or decide == 'n':
                    tm.led = 0
                    print "wiimote disconnected."
                    tm.close()
                    sys.exit()
                    return False


if __name__ == "__main__":
    main()

