# defines characters
# characters use their stage outfits
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
    
    hide nene confuse

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
    
    #mmj
    uk "Minori Hanasoto! Uhm, I was assigned the Ultimate Unlucky Student… But, I’m apart of More More Jump! and trying to work past it!"
    "(That’s gotta hurt…)"
    uk "Ah, sorry again, Minori…"
    minn "Don’t worry, Haruka, you weren’t in control of it!"
    ha "Of course, but I still feel bad. Oh, and I’m Haruka Kiritani, the Ultimate Idol and a member of More More Jump!!"
    uk "Airi Momoi! Ultimate Dancer!"
    uk "Shizuku Hinomori! I’m the Ultimate Model, and the older sister of Shiho!"
    "(I looked over and saw Shiho bashfully pouting.)"
    
    






    # This ends the game.
    return
