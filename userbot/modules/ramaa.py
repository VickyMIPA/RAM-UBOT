from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.wulan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik❤👿`")
    sleep(2)
    await typew.edit("`Kedua kamu manis😚`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku😣`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.nomercy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Fajar Peler☑️**")
    await typew.edit("**Fajar Peler✅**")
    sleep(1)
    await typew.edit("**Tebe Gilaa☑️**")
    await typew.edit("**Tebe Gilaa✅**")
    sleep(2)
    await typew.edit("**Popoy Depresi☑️**")
    await typew.edit("**Popoy Depresi✅**")
    sleep(2)
    await typew.edit("**Timeh Gajelas☑️**")
    await typew.edit("**Timeh Gajelas✅**")
    sleep(2)
    await typew.edit("**Aca GJM!☑️**")
    await typew.edit("**Aca GJM!✅**")
    sleep(2)
    await typew.edit("**Dare GJB!☑️**")
    await typew.edit("**Dare GJB!✅**")
    sleep(2)
    await typew.edit("**Vio,MengRibet☑️**")
    await typew.edit("**Vio,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA VICKY YANG BENER!😁**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.wulan`\
    \nUsage: hiks\
    \n\n`.punten` ; `.nomercy`\
    \nUsage: misi."
})
