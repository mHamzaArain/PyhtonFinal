# SMTP -> Simnple Mail Transfer Protocol

import smtplib
import imapclient

# ##########smtplib
# s = smtplib.SMTP_SSL()                            # To connect to specified protocol
# server.ehlo()                                              # (status: 200+ sign of success, byte for connection)         
# server.starttls()                                          # Create encryption for password
# server.login(email, pass)                           # To login into account
# server.sendmail(me, to, sub)                    # To send mail
# server.quit()                                              # To disxonnect connection

# ##########imapclient
# conn = imapclient.IMAPClient(<mail>, ssl=True)        # open emial using ssl encryption
# conn.login(email, password)
# selctInfo = conn.select_folder('INBOX', readonly=True)
# selectInfo[b'EXISTS']   # 956 no. of msgs
# m = conn.search(['FROM', 'a@g.com'])     # mail protocol [856]
# len(m)                                                                            # Total msg                                    
# conn.search('(SINCE "01-Jan-2019")')                          # form date
# conn.fetch(936, 'BODY[HEADER]')                               # fetch body of mail
# # #####################To Send Email
# server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
# type(server)      # <class 'smtplib.SMTP'>

# server.ehlo()     # (250, b'smtp.gmail.com at your service, [27.255.50.155]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# server.starttls()   #(220, b'2.0.0 Ready to start TLS')

# server.login('blackymartial@gmail.com', 'martial123!@#')     # (235, b'2.7.0 Accepted')

# me = 'blackymartial@gmail.com'
# to = 'hamzaarain1999@gmail.com'
# sub = 'Automation'

# server.sendmail(me, to, sub)       # {}
# server.quit()       # (221, b'2.0.0 closing connection t125sm14152573pfc.80 - gsmtp')

# ################Receive email
# conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# conn.login('blackymartial@gmail.com', 'martial123!@#')    # b'blackymartial@gmail.com authenticated (Success)'


# conn.select_folder('INBOX', readonly=True)    # {b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 956, b'RECENT': 0, b'UIDNEXT': 984, b'HIGHESTMODSEQ': 92480, b'READ-ONLY': [b'']}
# selectInfo = conn.select_folder('INBOX', readonly=True)
# selectInfo[b'EXISTS']   # 956 no. of msgs
# conn.search(['FROM', 'hamzaarain1999@gmail.com'])   # [] no mail
# m = conn.search(['FROM', 'bushraarain15dec@gmail.com'])     # mail protocol [856]
# print("totat msg: " + len(m))
# len(m)        # 1
# conn.search('(SINCE "01-Jan-2019")')        # [936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 975, 976, 977, 978, 979, 980, 981, 982, 983]
# conn.fetch(936, 'BODY[HEADER]')