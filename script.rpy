# defines characters
# characters use their stage outfits


# deleted later
# in order to create menus (example)
# menu:
#   "AAAAAAAA": 
#       jump variable
#   "ew":
#       jump var2
# label variable
#   blah blah blah
#   jump var3*
# label var2
#   blah blah blah
#   jump var3

#INDENTS:  "{i}---{/i}"

# *this is so you can return back to normal story


define ic = Character("Ichika")
define sa = Character("Saki")
define ho = Character("Honami")
define shh = Character("Shiho")
define minn = Character("Minori")
define ha = Character("Haruka")
define ai = Character("Airi")
define shz = Character("Shizuki")
define ko = Character("Kohane")
define an = Character("An")
define toy = Character("Toya")
define ginger = Character("Akito")
define star = Character("Tsukasa")
define ru = Character("Rui")
define ne = Character("Nene")
define em = Character("Emu")
define ka = Character("Kanade")
define ma = Character("Mafuyu")
define yu = Character("Yuki")
define miz = Character("Mizuki")
define en = Character("Ena")
define mik = Character("Miku Miku OOEO")
define rin = Character("Rin")
define len = Character("Len")
define lu = Character("Luka")
define mei = Character("MEIKO")
define daddy = Character("KAITO")

# general "unknown" character
define uk = Character("???")


# The game starts here.
label start:

    # bg
    scene bg classroom
    with dissolve


    # nene wakes up from her sleep
    show nene sleep

    ne ""
    show nene confuse
    ne "..huh?"
    "(I raised my head from a desk I don’t remember sleeping on. My body still felt heavy from sleep.)"
    "(Why was I here? I thought I was just in my room, playing a few games.)"
    
    show nene think
    "(No, wait. My troupe had agreed to meet in our SEKAI for practice so we didn’t have to do it in the snow, and I tapped on The World Hasn’t Even Started Yet. I pressed play and it faded to white as normal, but then my memory cuts out.)"
    "(Looking around, a note caught my eye. It’s right next to my arms, and it was placed, seemingly deliberately, on the desk. It was very obviously addressed to me on the outside.)"
    
    hide nene think

    uk "Good morning, Nene!"
    uk "Welcome to the first day of the rest of our lives, and don’t forget that we have an assembly later! I’m sure you can find the gym easily enough."
    uk "Before I forget, you will need to know one piece of information. For the sake of authenticity, you’re now the Ultimate Diva! Don’t forget to include this when you introduce yourself. It’s not like there will be any consequences, but we prefer it this way."
    uk "We’ll see you soon :)"

    show nene surprise
    ne "Rest of our lives?? What the hell???"

    hide nene surprise

    uk "Yawn... Nene-chan? Where are we?"
    "(I look over to my left to see a familiar friend: Emu Otori. Immediately, I hopped up to head to her. As I did, I noticed that I was in my PXL uniform, and so was Emu.)"

    show nene surprise
    ne "Emu! Are you okay?"

    hide nene surprise
    show emu smile
    em "Yupyup! Oo, I have a letter!!"

    hide emu smile
    "(Ah, seems like she noticed it.. I wonder if her’s is any different from mine.)"
    
    show emu negspiral
    em "WAAH!! WE CAN’T LEAVE???"

    hide emu negspiral
    "(..Apparently not. I’m not sure how to calm her down though—)"

    show emu smile
    em "Oo!! I’m the Ultimate Clown!!!!"

    hide emu smile
    "(That was quick. I don’t know what I expected. Clown, though?)"

    show nene think
    ne "That feels backhanded."

    hide nene think
    show emu smug
    em "Huh?? No!! Clowns make people smile!! And I’m one too!!!"

    hide emu smug
    show nene think
    ne "Heh, that’s fair… I think we should find the gym though. I… don’t want to anger whoever did this."

    hide nene think
    show emu smile
    em "Mhm mhm!! Operation “find-the-gym” is a go!!!"

    # hallway
    scene bg black
    with dissolve

    "(Emu and I went into the hall, and one thing was pretty comforting. Though, this is one example of the cons outweighing the pros. We were in Kamikou, but everything was…off.)"

    scene bg hallway
    with dissolve

    "(Some classrooms were changed from their original purpose, but I’m not sure to what. The windows were all blocked with metal. It felt like a prison.)"

    show nene think
    ne "We’re in Kamiyama. Follow me."

    hide nene think
    show emu smile
    em "Oo!! Hehe, maybe I can find a new way to sneak in~!"

    hide emu smile
    "(I couldn’t help the fact that her scheming made me smile a bit; her joy’s always so contagious.)"

    # gym
    show bg black
    with dissolve

    "(Eventually, we got to the gym. It seems like Emu and I were the last ones to arrive. I think there are 18 others; some that I recognize, and others I don’t. Speaking of which…)"

    show bg gym
    with dissolve

    uk "20. Considering we all are apart of some sort of group, I think that’s the last of new arrivals."
    "(Rui. Not even surpised that he was the one to assume that all of us were here. It looks like both him and Tsukasa are also in their PXL uniforms.)"
    uk "Alright then, how about some introductions? Let’s all get into a circle by group~!"
    "(Ah, Mizuki. I’m glad to see that they’re much more confident now, and much happier too.)"
    "(Everyone moved to sit in a circle on the gym floor, seemingly by group. Just as Mizuki requested.)"
    mi "Black hair, you should start!"
    
    # leo/need
    uk "Ah, alright.. I’m Ichika Hoshino, the Ultimate Guitarist! I’m apart of Leo/Need."
    uk "Saki Tenma! I’m the Ultimate Pianist, and the keyboardist in Leo/Need!!"
    uk "Honami Mochizuki, Ultimate Drummer for Leo/Need!"
    uk "Shiho Hinomori, Ultimate Bass Guitarist."
    
    # mmj
    uk "Minori Hanasoto! Uhm, I was assigned the Ultimate Unlucky Student… But, I’m apart of More More Jump! and trying to work past it!"
    "(That’s gotta hurt…)"
    uk "Ah, sorry again, Minori…"
    minn "Don’t worry, Haruka, you weren’t in control of it!"
    ha "Of course, but I still feel bad. Oh, and I’m Haruka Kiritani, the Ultimate Idol and a member of More More Jump!!"
    uk "Airi Momoi! Ultimate Dancer!"
    uk "Shizuku Hinomori! I’m the Ultimate Model, and the older sister of Shiho!"
    "(I looked over and saw Shiho bashfully pouting.)"
    
    # vbs
    uk "Uhm… K-Kohane Azusawa, the Ultimate Photographer..! I’m apart of Vivid Bad Squad, too."
    uk "An Shiraishi, the Ultimate Singer and also apart of Vivid Bad Squad!"
    uk "Toya Aoyagi, the Ultimate Street Artist. It’s a pleasure to meet all of you."
    uk "Akito Shinonome, Ultimate Beatboxer."
    
    # wxs
    "(Well, now it’s Tsukasa’s turn. My turn’s coming up soon… Wait, I didn’t realize that Rui and Tsukasa were sitting next to each other until now. Huh, weird. I’m just glad that they’re getting close. Don’t want a repeat of middle school…)"
    star "Tsukasa Tenma, the Ultimate Actor and a world future star!! I’m also the lead actor for Wonderlands x Showtime and the greatest brother in the world!"
    "(I still wonder how him and Emu actually make those sparkles and such. I asked Emu, but she only told me that you “have to be wonderhoy enough!”. That was a bit vague for me…)"
    "(It seems that Saki, Toya, and a girl with long, white hair all fondly smiled at his last comment. When did the Tenma family grow again? I don’t remember that girl.)"
    ru "Rui Kamishiro, the Ultimate Inventor! I’m also the director at Wonderlands x Showtime."
    
    show emu smile
    em "Emu Otori, the Ultimate Clown and a proud member of Wonderlands x Showtime! Wan-wan… WONDAHOI!!!"
    hide emu smile
    show nene think
    ne "N-Nene Kusanagi… Ultimate Diva and apart of Wonderlands x Showtime…. Ah, she/they, please."
    hide nene think
    "(It… wasn’t that bad to introduce myself to these 16-ish new people. Everyone showed interest in what I said. Maybe this group wont be too bad to be here with.)"
    
    # ji
    uk "U-uhm… Kanade Yoisaki… Ultimate Composer…"
    "(Ah, so the newest Tenma is Kanade.)"
    mi "K~… Don’t forget that you’re apart of N25!"
    ka "Ah.. yeah, I’m the composer for N25…"
    


    # This ends the game.
    return
