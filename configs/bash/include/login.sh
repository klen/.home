# Login screen
# ============

echo    -e ${yellow}------------------------------ $NC
echo    -e ${CYAN}This is BASH ${RED}${BASH_VERSION%.*}${CYAN} - DISPLAY on ${RED}$DISPLAY${NC}
uname   -a
cat /etc/*release* 2>/dev/null
date
__command cowsay && fortune -s | cowsay -f $DOT_SOURCE/stuff/girl.cow