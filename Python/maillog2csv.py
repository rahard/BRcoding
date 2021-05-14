#! /usr/bin/env python3

# convert Postfix mail.log into CSV
# Budi Rahardjo (@rahard)
# (CC) 2021

LOG = "/var/log/mail.log"

import re

# iterate over LOG
with open(LOG) as log:
   postfix=False
   for line in log:
      # stripped line
      sline = str.split(line.strip())
      # print(sline)
      # parse line
      month = sline[0]
      date = sline[1]
      time = sline[2]
      server = sline[3]
      program = sline[4]
      # check if program is postfix/pickup
      if 'postfix/pickup' in program:
         # found postfix
         id = sline[5]
         xuid= sline[6].split('=')
         uid = xuid[1]
         xuser = sline[7].split('=')
         user = xuser[1]
      if 'postfix/cleanup' in program:
         msgid = sline[6]
      if 'postfix/qmgr' in program:
         if 'from=' in sline[6]:
            xfrm = sline[6].split('=')
            frm = xfrm[1]
         if 'removed' in line:
            print(month,date,time, ",", id, ",", frm, to, relay)
      if 'postfix/smtp' in program:
         if 'to=' in sline[6]:
            xto = sline[6].split('=')
            to = xto[1]
         if 'relay=' in sline[7]:
            xrelay=sline[7].split('=')
            relay = xrelay[1]

