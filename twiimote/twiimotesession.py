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
#       TWIIMOTESESSION.PY
#
#       Version 1.7
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
import os
import sys
import time
import twython

from twython import Twython, TwythonStreamer, TwythonError, TwythonAuthError
textcolour = colorama.ansi.Fore

# Path of saved token
app_settings = os.path.expanduser('~/.tmtappauthsettings')

# SSL Certificate.
os.environ[
    'REQUESTS_CA_BUNDLE'] = '/usr/local/lib/python2.7/dist-packages/requests/cacert.pem'

C_KEY = "YzRyc0ZUb1FuQW9xOEdxc2VRNFlhZw=="
C_SECRET = "dHE2S3ZpNVpObHlmWkdCb0M4S0VWMXlVMXFaTWZub2VDUGd6bzNzeHc="


class Auth:

    # twiimote's authentication class.
    # only for user_authentication.

    def user_authentication(self):

            # OAuth 1 authentication to twitter.
            # linking user -> twiiter -> wiimote.

        print 'talking to twitter...'

        authbase = base64
        CK_U = authbase.b64decode(C_KEY)
        CKS_U = authbase.b64decode(C_SECRET)

        twitterauth = Twython(CK_U, CKS_U) 
        auth = twitterauth.get_authentication_tokens()

        oa_t = auth['oauth_token']
        oa_ts = auth['oauth_token_secret']

        if not os.path.exists(app_settings):

            try:
                print "Please authenticate twiimote with your twitter account. \n" + textcolour.CYAN + colorama.ansi.Style.BRIGHT + auth['auth_url'] + colorama.ansi.Style.RESET_ALL

                oauth_verifier = raw_input('PIN:')

                veritwitter = Twython(CK_U, CKS_U, oa_t, oa_ts)

                authenticated_tokens = veritwitter.get_authorized_tokens(oauth_verifier)

                FINAL_OA_T = authenticated_tokens['oauth_token']
                FINAL_OA_TS = authenticated_tokens['oauth_token_secret']
            except:
                print 'Authentication error.'
                sys.exit()
                return False

            else:
                saved_tkns = open(app_settings, "wb")
                saved_tkns.writelines(FINAL_OA_T)
                saved_tkns.writelines("\n")
                saved_tkns.writelines(FINAL_OA_TS)
                saved_tkns.closed

                print textcolour.GREEN + colorama.ansi.Style.BRIGHT + 'Authenticated!' + " twiimote is linked with your twitter account!"
                sys.exit(0)
                return True


class TwiimoteCommands:

    # twiimote's command class
    # Tell your twiimote to do things while it's connected to twitter.

    def DisplayUser(self):

        # Displays the connected username, duh.

        CK_USR = base64.b64decode(C_KEY)
        CKS_USR = base64.b64decode(C_SECRET)

        saved_tkns = open(app_settings, "rb")
        foa_tk = saved_tkns.readline().rstrip()
        foa_tks = saved_tkns.readline().rstrip()
        saved_tkns.close

        twmt = Twython(CK_USR, CKS_USR, foa_tk, foa_tks)

        user = twmt.get_account_settings()

        print "Hi, " + textcolour.CYAN + colorama.ansi.Style.BRIGHT + user['screen_name'] + "!"
        print colorama.ansi.Style.RESET_ALL
