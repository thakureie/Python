#Owner : thakur.eie@gmail.com
#Description: This script fetches current value of ipfrag_high_thresh and ipfrag_low_thresh parameter in /etc/sysctl.conf. It also checks Proc value of these 2 parameter .If sysctl.conf and proc is not current it fix both.
###################################################################

HOST=`hostname -s`
ipfrag_high_thresh=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_high'|awk '{print $2,$3}'`
ipfrag_low_thresh=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_low'|awk '{print $2,$3}'`

ipfrag_high_thresh_value=`cat /proc/sys/net/ipv4/ipfrag_high_thresh`
ipfrag_low_thresh_value=`cat /proc/sys/net/ipv4/ipfrag_low_thresh`

# This takes backup of /etc/sysctl.conf if current date has no backup, No time stamp backup!

if [[ ! -f "/etc/sysctl.conf.$(date +%d-%m-%Y)" ]]; then
        cp /etc/sysctl.conf /etc/sysctl.conf.$(date +%d-%m-%Y)
else
S1="/etc/sysctl.conf.$(date +%d-%m-%Y) already exists"

fi

#It Checkes for both parameter value in /etc/sysctl.conf , if no match it updates same

if [[ $(grep net.ipv4.ipfrag_high_thresh"\s*\+"="\s*\+"16777216$ "/etc/sysctl.conf") ]] && [[ $(grep net.ipv4.ipfrag_low_thresh"\s*\+"="\s*\+"15728640$ "/etc/sysctl.conf") ]]; then
RES='SUCCESS'
S2="ED Node having correct value set in systctl file "
ipfrag_high_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_high'|awk '{print $2,$3}'`
ipfrag_low_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_low'|awk '{print $2,$3}'`



else
RES='Modifying'
#status="ISSUE: ipfrag value not set in systctl file "

sed -i "/^net.ipv4.ipfrag_high_thresh/d" /etc/sysctl.conf
sed -i "/^net.ipv4.ipfrag_low_thresh/d" /etc/sysctl.conf
echo "#Adding as per Jira # " >> /etc/sysctl.conf
sed -i "\$anet.ipv4.ipfrag_low_thresh = 15728640" /etc/sysctl.conf
sed -i "\$anet.ipv4.ipfrag_high_thresh = 16777216" /etc/sysctl.conf
#sed -i "s/^net.ipv4.ipfrag_high_thresh/net.ipv4.ipfrag_high_thresh = 16777216/g" /etc/sysctl.conf
#sed -i "s/^net.ipv4.ipfrag_low_thresh/net.ipv4.ipfrag_low_thresh = 15728640/g" /etc/sysctl.conf
#sed -i "\$anet.ipv4.ipfrag_low_thresh = 15728640" /etc/sysctl.conf

if [[ $(grep net.ipv4.ipfrag_high_thresh"\s*\+"="\s*\+"16777216$ "/etc/sysctl.conf") ]] && [[ $(grep net.ipv4.ipfrag_low_thresh"\s*\+"="\s*\+"15728640$ "/etc/sysctl.conf") ]]; then
RES='SUCCESS'
ipfrag_high_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_high'|awk '{print $2,$3}'`
ipfrag_low_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_low'|awk '{print $2,$3}'`
fi
fi

###To check value of /proc/sys/net/ipv4/ipfrag_high_thresh and /proc/sys/net/ipv4/ipfrag_low_thresh file,if no match it updates. ####


if [[ "$ipfrag_high_thresh_value" == "16777216" ]] && [[ "$ipfrag_low_thresh_value" == "15728640" ]]; then
S3="Correct Value in /proc/sys/net/ipv4/ipfrag_high_thresh is already set"

else
echo "16777216" > /proc/sys/net/ipv4/ipfrag_high_thresh
echo "15728640" > /proc/sys/net/ipv4/ipfrag_low_thresh
sleep 2
ipfrag_high_thresh_value1=`cat /proc/sys/net/ipv4/ipfrag_high_thresh`
ipfrag_low_thresh_value1=`cat /proc/sys/net/ipv4/ipfrag_low_thresh`
if [[ "$ipfrag_high_thresh_value1" == "16777216" ]] && [[ "$ipfrag_low_thresh_value1" == "15728640" ]]; then

S4="Updated /proc/sys/net/ipv4/ipfrag_low_high_thresh "
fi
fi

#ipfrag_high_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_high'|awk '{print $2,$3}'`
#ipfrag_low_thresh1=`cat /etc/sysctl.conf |grep 'net.ipv4.ipfrag_low'|awk '{print $2,$3}'`

echo " $S1: $RES: $S2: $HOST : ipfrag_high is: $ipfrag_high_thresh1 and ipfrag_low is: $ipfrag_low_thresh1 :$S3 : $S4   "

