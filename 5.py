
s = raw_input("Please enter your full name: ")
import string
print string.capwords(s)

s = "matt         a             telles"
print string.capwords(s)

sIn = "abcdefghijklmnopqrstuvwxyz"
sOut = "defghijklmnopqrstuvwzyzabc"
sTrans = string.maketrans(sIn, sOut)
print string.translate("This is a test of the emergency broadcast system",
sTrans)

sRevTrans = string.maketrans(sOut, sIn)
s = string.translate("This is a test of the emergency broadcast system",
sTrans)
print string.translate(s, sRevTrans)
print s

sIn = sIn + " "
sOut = sOut + "~"
print string.translate(s, string.maketrans(sIn, sOut) )

