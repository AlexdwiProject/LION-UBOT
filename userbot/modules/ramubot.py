from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
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


@register(outgoing=True, pattern='^.kamuu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hai..**")
    await typew.edit("**Apa Kabar?**")
    sleep(1)
    await typew.edit("**Aku Kangen**")
    await typew.edit("**Sama Kamu🥺**")
    sleep(2)
    await typew.edit("**Kamu Harus**")
    await typew.edit("**Tau..**")
    sleep(2)
    await typew.edit("**Kalo Aku...**")
    await typew.edit("**Cinta Kamu❤️**")
    sleep(2)
    await typew.edit("**Jadi**")
    await typew.edit("**Kamu,**")
    sleep(2)
    await typew.edit("**Jangan Tinggalin**")
    await typew.edit("**Aku☹️☺️**")
    sleep(2)
    await typew.edit("**Tetep**")
    await typew.edit("**Disini Yah🥺✨**")
    sleep(2)
    await typew.edit("**Jangan**")
    await typew.edit("**Pergi🥺**")
    sleep(3)
    await typew.edit("**I Love You❤️❤️**")


@register(outgoing=True, pattern='^.lah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lah, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru ngentod!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "bot":
    "`.bot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.kamuu \
    \nUsage: misi."
})
